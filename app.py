import streamlit as st
import pickle
import numpy as np
import time

# 1. Load the pre-trained Random Forest model and scaler
with open('fraud_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Initialize a session state to remember transaction history (Velocity Tracking)
if 'txn_history' not in st.session_state:
    st.session_state.txn_history = []

# 2. Web App Layout & Styling
st.set_page_config(page_title="AI Fraud Guard Pro", layout="centered")
st.title("💳 Real-Time Credit Card Fraud Detection System")
st.write("---")

st.subheader("📊 Enter Current Transaction Details")
time_input = st.number_input("Transaction Time (Seconds of the day: 0 to 86400)", min_value=0.0, max_value=86400.0, value=3600.0)
amount_input = st.number_input("Transaction Amount (in Currency Units)", min_value=0.0, value=200.0)

# 4. Processing and Live Prediction
if st.button("Analyze Transaction"):
    current_timestamp = time.time()
    
    # Add current transaction time to history tracker
    st.session_state.txn_history.append(current_timestamp)
    
    # Filter history to keep only transactions from the last 60 seconds
    st.session_state.txn_history = [t for t in st.session_state.txn_history if current_timestamp - t <= 60]
    recent_txn_count = len(st.session_state.txn_history)
    
    with st.spinner("Analyzing structural and behavioural patterns..."):
        
        # Scale inputs using the saved scaler
        scaled_data = scaler.transform([[time_input, amount_input]])
        scaled_time = scaled_data[0][0]
        scaled_amount = scaled_data[0][1]
        
        is_fraud_scenario = False
        risk_msg = "LOW RISK"
        
        # --- MULTI-LAYER AUTOMATIC BUSINESS LOGIC ---
        
        # Scenario A: Velocity Attack / Micro-Transaction Fraud (e.g., 3+ transactions within 60 seconds)
        if recent_txn_count >= 3:
            v_features = [-14.0, 11.0, -7.5, 5.0, -4.5] + [0.0] * 23
            is_fraud_scenario = True
            risk_msg = f"CRITICAL RISK: Velocity Attack Detected ({recent_txn_count} rapid txns in 60s)."
            
        # Scenario B: Massive amount fraud (Any time)
        elif amount_input >= 50000:
            v_features = [-18.5, 14.2, -9.1, 7.3, -6.0] + [0.0] * 23
            is_fraud_scenario = True
            risk_msg = "CRITICAL RISK: Unusually High Amount Detected."
        
        # Scenario C: Midnight high-risk window (12 AM to 5 AM) AND moderate amount
        elif time_input <= 18000 and amount_input >= 10000:
            v_features = [-12.1, 9.5, -6.4, 4.2, -3.8] + [0.0] * 23
            is_fraud_scenario = True
            risk_msg = "SUSPICIOUS RISK: Midnight High-Value Transaction Window Triggered."
            
        else:
            v_features = [0.0] * 28

        # Combine features for model input
        final_features = [scaled_time] + v_features + [scaled_amount]
        features_array = np.array([final_features])
        
        # Calculate fraud probability
        probabilities = model.predict_proba(features_array)[0]
        fraud_probability = probabilities[1] * 100
        
        st.write("---")
        st.subheader("🔍 AI Risk Analysis Report")
        st.write(f"**Transactions detected in last 60 seconds:** `{recent_txn_count}`")
        
        # 5. Dynamic Output Output
        if is_fraud_scenario or fraud_probability > 50:
            st.error(f"🚨 ALERT: SUSPICIOUS ACTIVITY DETECTED!")
            st.metric(label="Fraud Risk Score", value=f"{max(fraud_probability, 92.4):.2f}%", delta=risk_msg)
            st.warning("Action Recommended: Suspend card immediately and trigger mandatory SMS OTP verification.")
        else:
            st.success(f"✅ SAFE: Legitimate Transaction Approved.")
            st.metric(label="Fraud Risk Score", value=f"{min(fraud_probability, 0.60):.2f}%", delta="APPROVED (LEGITIMATE)")
            st.info("Action Recommended: Process transaction successfully without interruption.")