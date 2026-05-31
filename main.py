import streamlit as st
import pandas as pd
import time
import json
import os
import random
import uuid
import requests 

SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwQnUVxmbpHwCb3Lpow1afiRErv2rkI1LwdLnlY-6XwN8Xgg2K5tgEmgamGQOi1gOT17g/exec"

# =========================
# Participant ID
# =========================


if "participant_id" not in st.session_state:
    st.session_state.participant_id = f"P{str(uuid.uuid4())[:8].upper()}"

st.write(f"Participant ID: {st.session_state.participant_id}")

# =========================
# Load tasks
# =========================
with open("tasks.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)

# =========================
# Session State
# =========================
if "task_index" not in st.session_state:
    st.session_state.task_index = 0
    st.session_state.condition_list = ["AI"] * 8 + ["NO_AI"] * 7
    random.shuffle(st.session_state.condition_list)

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# =========================
# Results file with correct columns
# =========================
csv_file = "results.csv"

if not os.path.exists(csv_file):
    pd.DataFrame(columns=[
        "participant_id",
        "task_id",
        "condition",
        "ai_recommendation",
        "selected_option",
        "response_time",
        "confidence",
        "trust",
        "autonomy",
        "recommendation_rejection"
    ]).to_csv(csv_file, index=False)

# =========================
# Experiment finished
# =========================
if st.session_state.task_index >= len(tasks):
    st.success("🎉 Experiment completed! Thank you for your participation!")
    st.balloons()
    df = pd.read_csv(csv_file)
    participant_data = df[df['participant_id'] == st.session_state.participant_id]
    st.download_button(
        label="Download my results",
        data=participant_data.to_csv(index=False),
        file_name=f"{st.session_state.participant_id}_results.csv",
        mime="text/csv"
    )
    st.stop()

# =========================
# Current Task
# =========================
task = tasks[st.session_state.task_index]

if f"shuffled_{st.session_state.task_index}" not in st.session_state:
    shuffled_options = task["options"].copy()
    random.shuffle(shuffled_options)
    st.session_state[f"shuffled_{st.session_state.task_index}"] = shuffled_options

task_options = st.session_state[f"shuffled_{st.session_state.task_index}"]
current_condition = st.session_state.condition_list[st.session_state.task_index]

st.subheader(f"Task {st.session_state.task_index + 1} of {len(tasks)}")
st.progress(st.session_state.task_index / len(tasks))

st.write("**" + task["task"] + "**")

# AI Recommendation
ai_rec = None
if current_condition == "AI" and "ai" in task:
    ai_rec = random.choice(task_options)
    st.info(f"🤖 **AI recommends:** {ai_rec}")

# =========================
# User inputs
# =========================
selected_option = st.radio("Your choice:", task_options, key=f"opt_{st.session_state.task_index}")

col1, col2, col3 = st.columns(3)
with col1:
    confidence = st.slider("Confidence in your decision", 1, 10, 7, key=f"conf_{st.session_state.task_index}")
with col2:
    trust = st.slider("Trust in AI", 1, 10, 6, key=f"trust_{st.session_state.task_index}")
with col3:
    autonomy = st.slider("Perceived Autonomy", 1, 10, 7, key=f"auto_{st.session_state.task_index}")

# Recommendation rejection
recommendation_rejection = 1 if (ai_rec and selected_option != ai_rec) else 0

# =========================
# Submit
# =========================
if st.button(
    "Submit Answer",
    type="primary",
    key=f"submit_{st.session_state.participant_id}_{st.session_state.task_index}"
):
    response_time = round(time.time() - st.session_state.start_time, 2)

    new_row = {
        "participant_id": st.session_state.participant_id,
        "task_id": st.session_state.task_index + 1,
        "condition": current_condition,
        "ai_recommendation": ai_rec,
        "selected_option": selected_option,
        "response_time": response_time,
        "confidence": confidence,
        "trust": trust,
        "autonomy": autonomy,
        "recommendation_rejection": recommendation_rejection
    }

    response = requests.post(
        SCRIPT_URL,
        json=new_row
    )

    st.write("STATUS:", response.status_code)
    st.write("RESPONSE:", response.text)

    st.stop()

st.caption("Human-AI Collaborative Decision Making Experiment")
