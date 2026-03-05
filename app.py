import streamlit as st

# UI sections
from ui.hero import render_hero
from ui.upload_section import render_upload
from ui.dashboard import render_dashboard
from ui.sidebar import render_sidebar

# Styles
from styles.css import apply_styles


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Vocalytics"
)


# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None


# -----------------------------
# APPLY GLOBAL STYLES
# -----------------------------
apply_styles()


# -----------------------------
# SIDEBAR
# -----------------------------
render_sidebar()


# -----------------------------
# HERO SECTION
# -----------------------------
render_hero()


# -----------------------------
# UPLOAD SECTION
# Handles:
# - video upload
# - analyze button
# - sample demo
# - pipeline execution
# -----------------------------
result = render_upload()


# -----------------------------
# DASHBOARD
# -----------------------------
if result:
    st.markdown("---")
    render_dashboard(result)