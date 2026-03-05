import streamlit as st
import json
import time
from ui.charts import render_bar_chart, render_radar_chart


def get_performance_tier(score):

    if score < 40:
        return "Finding Your Voice", "#DC2626"

    elif score < 55:
        return "Growing Confidence", "#F97316"

    elif score < 70:
        return "Clear & Confident", "#FACC15"

    elif score < 85:
        return "Strong Presence", "#2563EB"

    else:
        return "Next Level Confidence", "#16A34A" 



def render_dashboard(result):

    # 1. OVERALL SCORE & PERFORMANCE TIER
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        final_score = int(result['overall_score'])
        score_placeholder = st.empty()
        tier_name, tier_color = get_performance_tier(final_score)

        for i in range(final_score + 1):
            score_placeholder.markdown(f"""
            <div style="text-align: center;">
                <h1 style="font-size:72px; margin-bottom:0; color:{tier_color}">{i}</h1>
                <h6 style="font-size:18px; color:gray;">Overall Score</h6>
                <h3 style="font-weight:600;">{tier_name}</h3>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.02)
        st.balloons()
    st.space(10)


    # 2. SCORE CARDS OF VISUAL, AUDIO, LANGUAGE
    cols1, cols2, cols3 = st.columns(3)

    visual_score = round(float(result["visual_score"]),2)
    audio_score = round(float(result["audio_score"]),2)
    nlp_score = round(float(result["nlp_score"]),2)

    with cols1:
        st.markdown(f"""
        <div class="score-card">
            <div class="score-value" style="color:#57595B;">
                {visual_score}
            </div>
            <div class="score-label">Visual Score</div>
        </div>
        """, unsafe_allow_html=True)

    with cols2:
        st.markdown(f"""
        <div class="score-card">
            <div class="score-value" style="color:#57595B;">
                {audio_score}
            </div>
            <div class="score-label">Audio Score</div>
        </div>
        """, unsafe_allow_html=True)

    with cols3:
        st.markdown(f"""
        <div class="score-card">
            <div class="score-value" style="color:#57595B;">
                {nlp_score}
            </div>
            <div class="score-label">Language Score</div>
        </div>
        """, unsafe_allow_html=True)

    st.space(20)

    # 3. RADAR CHART
    with st.container(border=True):
        st.markdown("""
            <h3 style="font-weight:600;">Performace Overview</h3>
        """, unsafe_allow_html=True
        )
        radar_fig = render_radar_chart(visual_score, audio_score, nlp_score)
        st.plotly_chart(radar_fig, use_container_width=True)

    # 4. BAR CHART
    with st.container(border=True):
        st.markdown("""
            <h3 style="font-weight:600;">Score Breakdown</h3>
        """, unsafe_allow_html=True
        )
        bar_fig = render_bar_chart(
            visual_score,
            audio_score,
            nlp_score
        )
        st.plotly_chart(bar_fig, use_container_width=True)

    st.space(15)
    
    # 5. Growth section
    st.markdown("""
        <h3 style="font-weight:600;">Growth Areas</h3>
    """, unsafe_allow_html=True
    )

    for item in result["feedback"]:

        with st.expander(item['growth_area']):
            st.write(f'▸ {item["why_it_matters"]}')
            st.write(f"▸ {item['improvement']}")

    st.divider()

    # 6. What's Next
    st.markdown("### What Next?", unsafe_allow_html=True)

    st.success("""
    • Record another attempt within 48 hours  
    • Focus only on one improvement area  
    • Track progress and compare results
    """)
    st.space(10)

    #Download report or Reanalyze
    sp1, col1, sp2, col2, sp3 = st.columns([1, 2, 1, 2, 1])
    
    with col1:
        st.download_button(
            label="📥 Download Report",
            data=json.dumps(result, indent=4),
            file_name="vocalytics_report.json",
            mime="application/json",
            key="download_report_button",
            use_container_width=True,
        )
    with col2:
        reanalyze = st.button("Analyze Another Video", key="reanalyze_btn", use_container_width=True)
        if reanalyze:
            st.session_state.analysis_result = None
            st.rerun()

    st.space(30)

    # Future Enhancement
    st.markdown("### Progress Tracking")
    st.write("Coming soon: Track performance across multiple attempts.")
  