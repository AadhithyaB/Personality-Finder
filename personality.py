import streamlit as st
import joblib

# Load your trained model
# Make sure your model file (e.g., model.joblib) is in the same folder or give path
loaded_model = joblib.load("Personality_finder.pkl")

# Title
st.title("🧑‍🤝‍🧑 Personality Prediction App")

# Input fields
time_spent_alone = st.number_input("Time spent alone (hours)", min_value=0, max_value=24, value=1)

stage_fear_value = st.radio("Stage Fear", [0, 1], index=0, format_func=lambda x: "Yes" if x == 1 else "No")

social_event_attendance = st.number_input("Social Event Attendance (per month)", min_value=0, value=0)

going_outside = st.number_input("Going outside (times per week)", min_value=0, value=0)

drained_after_socializing_value = st.radio("Drained after Socialising", [0, 1], index=0, format_func=lambda x: "Yes" if x == 1 else "No")

friends_circle_size = st.number_input("Friends Circle Size", min_value=0, value=0)

post_frequency = st.number_input("Post Frequency (posts per month)", min_value=0, value=0)

# Prediction Button
if st.button("Predict"):
    features = [[
        time_spent_alone,
        stage_fear_value,
        social_event_attendance,
        going_outside,
        drained_after_socializing_value,
        friends_circle_size,
        post_frequency
    ]]
    
    prediction = loaded_model.predict(features)

    if prediction[0] == 0:
        st.success("🧑 The Person is Introvert")
    else:
        st.success("🧑 The Person is Extrovert")
