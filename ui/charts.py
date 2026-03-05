import plotly.graph_objects as go

def render_radar_chart(visual, audio, language):

    categories = ['Visual', 'Audio', 'Language']

    fig = go.Figure()

    # --- 1️⃣ Benchmark Layer (Target 75 Score) ---
    fig.add_trace(go.Scatterpolar(
        r=[75, 75, 75],
        theta=categories,
        fill='toself',
        fillcolor='rgba(0,0,0,0.04)',
        line=dict(color='rgba(0,0,0,0.15)', width=1, dash='dot'),
        name="Target Level"
    ))

    # --- 2️⃣ Main Performance Layer ---
    fig.add_trace(go.Scatterpolar(
        r=[visual, audio, language],
        theta=categories,
        fill='toself',
        fillcolor='rgba(37, 99, 235, 0.18)',
        line=dict(color='#424874', width=3),
        name="Your Performance"
    ))

    # --- 3️⃣ Soft Glow Effect (Outer Layer Slightly Bigger Transparent) ---
    fig.add_trace(go.Scatterpolar(
        r=[visual+2, audio+2, language+2],
        theta=categories,
        fill='toself',
        fillcolor='rgba(62, 72, 116, 0.05)',
        line=dict(color='rgba(0,0,0,0)', width=0),
        showlegend=False
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor="#E5E7EB",
                tickfont=dict(size=10),
            ),
            angularaxis=dict(
                tickfont=dict(size=13)
            )
        ),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.05,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=20, r=20, t=30, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white",
        height=420
    )

    return fig


# Bar Chart function
def render_bar_chart(visual, audio, language):

    categories = ['Visual', 'Audio', 'Language']
    scores = [visual, audio, language]

    fig = go.Figure()

    # --- Benchmark Background Bars (Target 75) ---
    fig.add_trace(go.Bar(
        x=categories,
        y=[75, 75, 75],
        marker=dict(color='rgba(0,0,0,0.05)'),
        hoverinfo='skip',
        showlegend=False
    ))

    # --- Main Score Bars ---
    fig.add_trace(go.Bar(
        x=categories,
        y=scores,
        marker=dict(
            color='#DCD6F7',
            line=dict(color='#424874', width=1.5)
        ),
        text=[f"{round(s,1)}" for s in scores],
        textposition='outside',
        name="Your Score"
    ))

    fig.update_layout(
        barmode='overlay',
        yaxis=dict(
            range=[0, 100],
            gridcolor="#E5E7EB",
            zeroline=False
        ),
        xaxis=dict(
            tickfont=dict(size=13)
        ),
        margin=dict(l=20, r=20, t=30, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white",
        height=400,
        showlegend=False
    )

    return fig