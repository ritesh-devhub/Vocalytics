import streamlit as st
import os
from backend.main import run_pipeline

def render_upload():
    container = st.container(border=True)
    with container:
        container.text("Upload your speaking video")
        uploaded_file = container.file_uploader(
            "upload your video",
            type=["mp4"],
            label_visibility="collapsed"
        )
        col1, col2 = st.columns(2)

        with col1:
            analyze_btn = st.button("Analyze Now", use_container_width=True, type="primary")

        with col2:
            sample_btn = st.button("Try Sample", use_container_width=True)
            if sample_btn:
                st.session_state.analysis_result = {
                "overall_score": 74.3,
                "visual_score": 68.4,
                "audio_score": 71.2,
                "nlp_score": 82.5,
                "performance_level": "Strong Presence",

                "feedback": [
                    {
                        "area": "eye_contact_score",
                        "growth_area": "Maintain stronger eye contact",
                        "why_it_matters": "Consistent eye contact builds trust and helps the audience feel connected to what you are saying.",
                        "improvement": "Try speaking directly toward the camera lens and hold your gaze for a few seconds before naturally shifting."
                    },

                    {
                        "area": "wpm_score",
                        "growth_area": "Speaking pace could be smoother",
                        "why_it_matters": "When the pace changes too much, it can affect clarity and reduce the overall impact of your message.",
                        "improvement": "Aim for a steady rhythm around 130–150 words per minute and pause slightly between key ideas."
                    },

                    {
                        "area": "sentence_structure_score",
                        "growth_area": "Improve sentence flow",
                        "why_it_matters": "Clear sentence structure helps your audience follow your ideas more easily.",
                        "improvement": "Try expressing each idea in one clear sentence and use natural pauses before starting the next thought."
                    }
                ]
            }
        #container end


    col1, col2, col3 = st.columns(3)

    with col1:
        sub1, sub2 = st.columns([1,5])
        with sub1:
            st.image("assets/shield.svg", width=25)
        with sub2:
            st.write("Secure Processing")

    with col2:
        sub1, sub2 = st.columns([1,5])
        with sub1:
            st.image("assets/real-time.svg", width=25)
        with sub2:
            st.write("Real-Time Feedback")

    with col3:
        sub1, sub2 = st.columns([1,5])
        with sub1:
            st.image("assets/ai-assistant.svg", width=25)
        with sub2:
            st.write("AI Confidence Metrics")


    if analyze_btn and uploaded_file is not None:

        # Save file
        save_path = os.path.join("uploads", uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        progress_bar = st.progress(0)
        status_text = st.empty()

        def update_progress(value, message):
            progress_bar.progress(value)
            status_text.write(message)

        with st.spinner("Initializing Vocalytics engine…"):
            st.session_state.analysis_result = run_pipeline(uploaded_file.name, update_progress)

        st.success("Your report is ready!")
    
    return st.session_state.analysis_result