import streamlit as st

def render_sidebar():
    # SIDEBAR SECTION
    st.sidebar.markdown("""
    <style>
    .sidebar-title {
        font-size: 32px;
        font-weight: 800;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }
    .sidebar-tagline {
        font-size: 15px;
        color: #6b7280;
        margin-bottom: 25px;
    }
    </style>

    <div class="sidebar-title">VOCALYTICS</div>
    <div class="sidebar-tagline">Speech intelligence, powered by AI.</div>
    """, unsafe_allow_html=True)


    st.sidebar.image("assets/mascot.png")
    st.sidebar.divider()
    st.sidebar.header(("ABOUT"))
    st.sidebar.markdown((
    """Vocalytics analyzes:
- Voice and delivery  
- Visual presence  
- Language structure  

It transforms speech into measurable performance insights.
"""
    ))

    st.sidebar.header(("FEATURES"))
    st.sidebar.markdown((
        """
    <div style="font-size:15px; line-height:1.8">

    <b style="letter-spacing:2px;">V</b> — Voice intelligence analytics  
    <b style="letter-spacing:2px;">O</b> — Objective delivery metrics  
    <b style="letter-spacing:2px;">C</b> — Computer vision tracking  
    <b style="letter-spacing:2px;">A</b> — Advanced speech modeling  
    <b style="letter-spacing:2px;">L</b> — Language structure evaluation  
    <b style="letter-spacing:2px;">Y</b> — Year-over-year progress  
    <b style="letter-spacing:2px;">T</b> — Tone variation insights  
    <b style="letter-spacing:2px;">I</b> — Intelligent feedback engine  
    <b style="letter-spacing:2px;">C</b> — Confidence scoring  
    <b style="letter-spacing:2px;">S</b> — Structured reports 

    </div>
    """
    ), unsafe_allow_html=True)

    st.sidebar.header(("HOW IT WORKS"))
    st.sidebar.markdown("""
    <div style="font-size:15px; line-height:2">

    <b>1.</b> Upload your video<br>
    <b>2.</b> I analyzes speech & visuals<br>
    <b>3.</b> Receive structured feedback

    </div>
    """, unsafe_allow_html=True)


    st.sidebar.divider()
    st.sidebar.text("Version 1.0")
    st.sidebar.text("© 2026 Vocalytics")
