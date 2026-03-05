import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
                
    .stApp {
        background: linear-gradient(
            180deg,
            #FFFFFF 0%,
            #F8FAFC 60%,
            #F1F5F9 100%
        );
    }

    .score-card {
        background: white;
        padding: 30px 20px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid rgba(0,0,0,0.04);

        box-shadow:
            0 2px 6px rgba(0,0,0,0.04),
            0 12px 30px rgba(0,0,0,0.06);
    }

    .score-value {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .score-label {
        font-size: 14px;
        color: #6b7280;
        letter-spacing: 0.5px;
    }
                
    .score-card:hover {
        transform: translateY(-5px);
        transition: all 0.25s ease;

        box-shadow:
            0 10px 25px rgba(0,0,0,0.08),
            0 20px 40px rgba(0,0,0,0.06);
    }

                /* Target primary button */
    div[data-testid="stButton"] > button[kind="primary"] {
        background-color: #111827;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.25s ease;
        border: none;
    }

    /* Hover effect */
    div[data-testid="stButton"] > button[kind="primary"]:hover {
        background-color: #1f2937;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    /* Click effect */
    div[data-testid="stButton"] > button[kind="primary"]:active {
        transform: translateY(0px);
        box-shadow: none;
    }
                
    /* Target primary button */
    div[data-testid="stButton"] > button[kind="primary"] {
        background-color: #111827;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.25s ease;
        border: none;
    }

    /* Hover effect primary*/
    div[data-testid="stButton"] > button[kind="primary"]:hover {
        background-color: #1f2937;
        transform: translateY(-1.5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }
                
    /* Hover effect secondary*/
    div[data-testid="stButton"] > button[kind="secondary"]:hover {
        background-color: #DCD6F7;
        transform: translateY(-1.5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }
                
    /* Click effect */
    div[data-testid="stButton"] > button[kind="primary"]:active {
        transform: translateY(0px);
        box-shadow: none;
    }     

    .growth-card {
        background: #ffffff;
        border: 1px solid #E5E7EB;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.04);
    }

    .growth-title {
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .growth-why {
        font-size: 13px;
        color: #6B7280;
        margin-bottom: 8px;
    }

    .growth-fix {
        font-size: 14px;
        font-weight: 500;
    }

    /* Download button styling */
    div[data-testid="stDownloadButton"] > button {
        background-color: #111827;
        color: white;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.25s ease;
        border: none;
    }

    /* Hover lift */
    div[data-testid="stDownloadButton"] > button:hover {
        background-color: #1f2937;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    /* Click effect */
    div[data-testid="stDownloadButton"] > button:active {
        transform: translateY(0px);
        box-shadow: none;
    }
                    
    </style>
    """, unsafe_allow_html=True)

