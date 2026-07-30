import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import joblib
import os
import base64
from PIL import Image
from datetime import datetime
from report_generator import generate_report
import report_generator


# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="EnerVision AI",
    page_icon="Python_Code/assets/app_icon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ============================================================
# HEADER
# ============================================================

from PIL import Image

logo = Image.open("Python_Code/assets/app_icon.png")

col1, col2 = st.columns([0.8,4.2], vertical_alignment="center")

with col1:
    st.markdown(
        "<div style='margin-left:12px;margin-top:4px'></div>",
        unsafe_allow_html=True
    )
    st.image("Python_Code/assets/app_icon.png", width=165)

with col2:
    st.markdown("""
<h1 style="
margin-top:0;
margin-bottom:4px;
">
EnerVision AI
</h1>
""", unsafe_allow_html=True)
    
st.markdown("""
<div style="
font-size:22px;
font-weight:600;
margin-top:6px;
margin-bottom:8px;
color:#4EA1FF;
">
AI Powered Smart Energy Audit & Sustainability Platform
</div>
""", unsafe_allow_html=True)
st.markdown("""
<p style="font-size:20px;color:#E5E7EB;">
Predict • Analyze • Optimize • Save Energy
</p>
""", unsafe_allow_html=True)
# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "models", "energy_model.pkl")
LOGO_PATH = os.path.join(BASE_DIR, "assets", "logo.png")
BACKGROUND_PATH = os.path.join(BASE_DIR, "assets", "background.png")

# ============================================================
# LOAD MODEL
# ============================================================

try:
    model = joblib.load(MODEL_PATH)
except Exception:
    st.error("❌ AI Model not found. Please place energy_model.pkl inside the models folder.")
    st.stop()

# ============================================================
# SESSION STATE
# ============================================================

if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

if "energy" not in st.session_state:
    st.session_state.energy = 0.0

if "cost" not in st.session_state:
    st.session_state.cost = 0.0

if "co2" not in st.session_state:
    st.session_state.co2 = 0.0

if "health" not in st.session_state:
    st.session_state.health = "Unknown"
# ============================================================
# AI ENERGY EFFICIENCY GRADE
# ============================================================

energy = st.session_state.energy

if energy <= 150:
    grade = "A+"
    stars = "★★★★★"
    grade_color = "green"

elif energy <= 250:
    grade = "A"
    stars = "★★★★☆"
    grade_color = "green"

elif energy <= 350:
    grade = "B"
    stars = "★★★☆☆"
    grade_color = "orange"

elif energy <= 500:
    grade = "C"
    stars = "★★☆☆☆"
    grade_color = "red"

else:
    grade = "D"
    stars = "★☆☆☆☆"
    grade_color = "darkred"

st.session_state.grade = grade
st.session_state.stars = stars
st.session_state.grade_color = grade_color
# ============================================================
# PREMIUM THEME
# ============================================================

st.markdown("""
<style>

.stApp{
    background:#071321;
    color:white;
}

h1,h2,h3,h4,h5,h6{
    color:white;
    font-family:Segoe UI;
}

section[data-testid="stSidebar"]{
    background:#0C1E36;
}

div[data-testid="stMetric"]{
    background:#122947;
    padding:15px;
    border-radius:15px;
    border:1px solid #1E88E5;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    border:none;
    background:#00B8FF;
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#0099E6;
}

</style>
""", unsafe_allow_html=True)
# ============================================================
# HERO SECTION
# ============================================================
st.markdown(
    "<div style='height:30px;'></div>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="
        background: linear-gradient(135deg,#0F172A,#1E3A8A,#059669);
        padding:35px;
        border-radius:20px;
        color:white;
        box-shadow:0px 8px 25px rgba(0,0,0,0.35);
    ">

    <h1 style="margin-bottom:0;">
        📋 Project Overview
    </h1>

    <h3 style="margin-top:8px;color:#D1FAE5;">
        AI Powered Smart Energy Audit Platform
    </h3>

    <p style="font-size:18px;margin-top:15px;line-height:1.6">

    Helping MSMEs reduce electricity costs,
    improve equipment efficiency,
    and achieve sustainable energy management
    through Artificial Intelligence.

    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.image("Python_Code/assets/home_logo.png", width=120)

with st.sidebar:
    st.markdown(
    """
# ⚙️ Control Center

Configure your factory parameters and launch an AI-powered energy audit.

---
"""
)
    st.info(
    """
🏭 **Designed For**

• MSMEs

• Manufacturing

• Textile

• Food Processing

• Engineering Units

---
🤖 Powered by EnerVision AI
"""
)

    company = st.text_input(
        "🏭 Company Name",
        placeholder="ABC Industries"
    )

    location = st.text_input(
        "📍Location",
        placeholder="Ahmedabad"
    )

    auditor = st.text_input(
        "👨‍💼 Auditor Name",
        placeholder="Your Name"
    )

    st.divider()

    st.markdown("### 🏢 Industry Type")

    industry = st.selectbox(
        "",
        [
            "Manufacturing",
            "Textile",
            "Food Processing",
            "Chemical",
            "Engineering",
            "Plastic",
            "Pharmaceutical",
            "Other"
        ]
    )

    st.divider()

    st.markdown("### ⚡ Electricity Tariff")

    tariff = st.number_input(
        "₹ per kWh",
        value=8.50,
        step=0.50
    )

    st.divider()
    # ============================================================
# DEMO MODE
# ============================================================

st.header("🎬 Demo Mode")

if st.button("🚀 Load Demo Factory"):

    st.session_state["company"] = "ABC Industries"
    st.session_state["auditor"] = "Bhavya Prajapati"

    st.session_state["lights"] = 65
    st.session_state["machines"] = 7
    st.session_state["temperature"] = 24
    st.session_state["humidity"] = 48
    st.session_state["occupancy"] = 80
    st.session_state["working_hours"] = 9
    st.session_state["outdoor_temp"] = 34
    st.session_state["production"] = 82

    st.success("✅ Demo Factory Loaded Successfully")
predict_btn = st.button(
        "🚀 Start Energy Audit"
    )
if st.session_state.energy > 0:
       st.success("🔵 AI Audit Completed Successfully")
else:
       st.info("🟢 Ready for Energy Audit")

# ============================================================
# MSME ENERGY INPUT PANEL
# ============================================================

st.header("🏭 MSME Energy Audit")

st.write("Enter your facility's operational details below.")

col1, col2 = st.columns(2)

with col1:

    lights = st.number_input(
        "💡 Lighting Load (Wh)",
        min_value=0,
        value=50
    )

    temperature = st.number_input(
        "🌡️ Room Temperature (°C)",
        value=22.0
    )

    humidity = st.slider(
        "💧 Humidity (%)",
        0,
        100,
        45
    )

    occupancy = st.slider(
        "👨‍🏭 Occupancy (%)",
        0,
        100,
        70
    )

with col2:

    machines = st.number_input(
        "⚙️ Machines Running",
        min_value=0,
        value=5
    )

    working_hours = st.slider(
        "⏰ Working Hours",
        1,
        24,
        8
    )

    outdoor_temp = st.number_input(
        "🌤️ Outdoor Temperature (°C)",
        value=30.0
    )

    production = st.slider(
        "📦 Production Load (%)",
        0,
        100,
        75
    )

st.divider()

# ============================================================
# EXECUTIVE KPI DASHBOARD
# ============================================================

st.header("📊 Executive Energy Dashboard")

st.caption(
    "AI-generated insights for energy consumption, operational cost, carbon emissions and equipment health."
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#2563EB,#1D4ED8);
    padding:22px;
    border-radius:16px;
    color:white;
    text-align:center;
    box-shadow:0 6px 15px rgba(0,0,0,0.20);
    ">
        <div style="font-size:18px;">⚡ Energy</div>
        <div style="font-size:34px;font-weight:bold;">
            {st.session_state.energy:.1f}
        </div>
        <div>Wh / Day</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#059669,#10B981);
    padding:22px;
    border-radius:16px;
    color:white;
    text-align:center;
    box-shadow:0 6px 15px rgba(0,0,0,0.20);
    ">
        <div style="font-size:18px;">💰 Cost</div>
        <div style="font-size:34px;font-weight:bold;">
            ₹ {st.session_state.cost:.2f}
        </div>
        <div>Per Day</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#16A34A,#22C55E);
    padding:22px;
    border-radius:16px;
    color:white;
    text-align:center;
    box-shadow:0 6px 15px rgba(0,0,0,0.20);
    ">
        <div style="font-size:18px;">🌿 CO₂</div>
        <div style="font-size:34px;font-weight:bold;">
            {st.session_state.co2:.2f}
        </div>
        <div>kg / Day</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#F59E0B,#EA580C);
    padding:22px;
    border-radius:16px;
    color:white;
    text-align:center;
    box-shadow:0 6px 15px rgba(0,0,0,0.20);
    ">
        <div style="font-size:18px;">🏭 Health</div>
        <div style="font-size:30px;font-weight:bold;">
            {st.session_state.health}
        </div>
        <div>Equipment Status</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ============================================================
# AI PREDICTION ENGINE
# ============================================================

if predict_btn:
    
    # -------------------------
    # Prepare Model Input
    # -------------------------

    input_data = np.array([[
        lights,
        temperature,
        humidity,
        occupancy,
        machines,
        working_hours,
        outdoor_temp,
        production
    ]])

    prediction = float(model.predict(input_data)[0])

    # -------------------------
    # Cost
    # -------------------------

    cost = (prediction / 1000) * tariff

    # -------------------------
    # CO₂
    # -------------------------

    co2 = (prediction / 1000) * 0.82

    # -------------------------
    # Health
    # -------------------------

    if prediction < 180:

        health = "Excellent"

    elif prediction < 260:

        health = "Good"

    elif prediction < 350:

        health = "Warning"

    else:

        health = "Critical"

# ============================================================
# AI RECOMMENDATION ENGINE
# ============================================================

    recommendations = []

# Lighting
    if lights > 70:
     recommendations.append(
        "💡 Replace conventional lighting with LED fixtures and install occupancy sensors."
    )

# Temperature
    if temperature > 28:
      recommendations.append(
        "🌡 High temperature detected. Optimize HVAC operation and improve ventilation."
    )

# Humidity
    if humidity > 70:
     recommendations.append(
        "💧 High humidity detected. Reduce unnecessary HVAC load using proper dehumidification."
    )

# Machines
    if machines > 8:
     recommendations.append(
        "🏭 Large number of machines operating simultaneously. Consider staggered scheduling."
    )

# Working Hours
    if working_hours > 10:
     recommendations.append(
        "⏰ Long operating hours detected. Review production scheduling to reduce idle energy."
    )

# Production
    if production < 40:
     recommendations.append(
        "📉 Low production with high energy usage. Improve machine utilization."
    )

# Energy Consumption
    if st.session_state.energy > 350:
     recommendations.append(
        "⚡ Overall energy consumption is high. Perform a detailed energy audit."
    )

# Excellent Condition
    if len(recommendations) == 0:
     recommendations.append(
        "✅ Excellent energy performance detected. Continue current operating practices."
    )
      # ================================
# Save Results
# ================================
    
    st.session_state.energy = prediction
    st.session_state.cost = cost
    st.session_state.co2 = co2
    st.session_state.health = health
    st.session_state.recommendations = recommendations

# ================================
# Save Prediction History
# ================================

    history_item = {
    "Company": company,
    "Energy (Wh)": round(prediction, 2),
    "Cost (₹)": round(cost, 2),
    "CO₂ (kg)": round(co2, 2),
    "Health": health,
    "Time": datetime.now().strftime("%d-%m-%Y %H:%M")
}

    if "history" not in st.session_state:
      st.session_state.history = []

    st.session_state.history.append(history_item)

# Refresh UI
    st.rerun()
     
     
# ============================================================
# AI RECOMMENDATIONS
# ============================================================

if (
    st.session_state.energy > 0
    and "recommendations" in st.session_state
):

    st.header("🧠 AI Recommendations")
    st.caption("Recommendations generated using EnerVision AI analysis.")

    priority = "🟢 LOW"

    if st.session_state.energy > 350:
        priority = "🔴 HIGH"
    elif st.session_state.energy > 250:
        priority = "🟠 MEDIUM"

    for i, rec in enumerate(st.session_state.recommendations, start=1):

        st.markdown(f"""
<div style="
background:linear-gradient(135deg,#1E293B,#0F172A);
padding:22px;
margin-bottom:18px;
border-left:6px solid #2563EB;
border-radius:14px;
box-shadow:0px 5px 12px rgba(0,0,0,0.25);
">

<h4 style="color:white;margin:0;">
📌 Recommendation {i}
</h4>

<p style="
color:#E5E7EB;
font-size:17px;
margin-top:12px;
">
{rec}
</p>

<hr>

<b style="color:#60A5FA;">
Priority :
</b>

<span style="color:white;">
{priority}
</span>

<br><br>

<b style="color:#22C55E;">
Expected Impact :
</b>

⭐⭐⭐⭐☆

</div>
""", unsafe_allow_html=True)

    st.divider()
# ============================================================
# AI ENERGY EFFICIENCY SCORE
# ============================================================

st.header("🏆 AI Energy Efficiency Score")

score = max(0, min(100, int(100 - (st.session_state.energy / 5))))

if score >= 90:
    color = "#22C55E"
    status = "Excellent ⭐⭐⭐⭐⭐"

elif score >= 75:
    color = "#10B981"
    status = "Good ⭐⭐⭐⭐"

elif score >= 50:
    color = "#F59E0B"
    status = "Average ⭐⭐⭐"

else:
    color = "#EF4444"
    status = "Poor ⭐⭐"

st.markdown(f"""
<div style="
background:#111827;
padding:30px;
border-radius:18px;
text-align:center;
box-shadow:0px 6px 18px rgba(0,0,0,0.3);
">

<h1 style="
font-size:70px;
color:{color};
margin-bottom:10px;
">
{score}
</h1>

<h3 style="color:white;">
Energy Efficiency Score
</h3>

<h2 style="color:{color};">
{status}
</h2>

</div>
""", unsafe_allow_html=True)

st.progress(score/100)

st.divider()
# ============================================================
# SUSTAINABILITY SCORE
# ============================================================

if st.session_state.energy > 0:

    st.header("🌍 Sustainability Score")

    score = max(
        0,
        min(
            100,
            int(
                100 - st.session_state.energy / 5
            )
        )
    )

    st.progress(score)

    st.success(f"Overall Sustainability Score : {score}/100")

    st.divider()
st.header("💰 Annual Business Impact")

annual_energy = st.session_state.energy * 365 / 1000      # kWh/year
annual_cost = st.session_state.cost * 365
annual_co2 = st.session_state.co2 * 365

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "⚡ Annual Energy",
        f"{annual_energy:.1f} kWh"
    )

with col2:
    st.metric(
        "💵 Annual Electricity Cost",
        f"₹ {annual_cost:,.0f}"
    )

with col3:
    st.metric(
        "🌿 Annual CO₂ Emissions",
        f"{annual_co2:.1f} kg"
    )

st.divider()
saving_percent = 15

annual_saving = annual_cost * saving_percent / 100

st.success(
    f"💡 AI estimates that implementing the recommended actions can reduce electricity costs by approximately **{saving_percent}%**, saving around **₹ {annual_saving:,.0f} per year.**"
)

# ============================================================
# FACTORY PERFORMANCE SUMMARY
# ============================================================

st.header("📊 Factory Performance Summary")

if st.session_state.energy < 200:
    grade = "A+"
    color = "#22C55E"

elif st.session_state.energy < 300:
    grade = "A"
    color = "#10B981"

elif st.session_state.energy < 400:
    grade = "B"
    color = "#F59E0B"

elif st.session_state.energy < 500:
    grade = "C"
    color = "#F97316"

else:
    grade = "D"
    color = "#EF4444"

st.markdown(f"""
<div style="
background:#111827;
padding:28px;
border-radius:18px;
text-align:center;
box-shadow:0px 5px 16px rgba(0,0,0,0.35);
">

<h1 style="font-size:70px;color:{color};">
{grade}
</h1>

<h3 style="color:white;">
Overall Factory Performance Grade
</h3>

<p style="font-size:18px;color:#D1D5DB;">
Generated using EnerVision AI analysis
</p>

</div>
""", unsafe_allow_html=True)

st.divider()
# ============================================================
# MONTHLY ENERGY ANALYTICS
# ============================================================

st.header("📈 Monthly Energy Analytics")
st.caption("Projected monthly energy consumption based on AI prediction.")

months = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

base = st.session_state.energy

monthly_energy = [
    base*0.92,
    base*0.95,
    base*1.00,
    base*1.03,
    base*1.08,
    base*1.12,
    base*1.15,
    base*1.10,
    base*1.02,
    base*0.98,
    base*0.94,
    base*0.90
]

chart_df = pd.DataFrame({
    "Month": months,
    "Energy (Wh)": monthly_energy
})

st.line_chart(
    chart_df.set_index("Month"),
    use_container_width=True
)

st.divider()
# ============================================================
# LIVE ENERGY TREND
# ============================================================

if st.session_state.energy > 0:

    st.header("📈 Live Energy Consumption Trend")

    st.caption("AI simulated hourly energy consumption throughout the working day.")

    history = pd.DataFrame({

        "Hour":[
            "8 AM","9 AM","10 AM","11 AM",
            "12 PM","1 PM","2 PM","3 PM"
        ],

        "Energy":[
            st.session_state.energy*0.82,
            st.session_state.energy*0.90,
            st.session_state.energy*0.95,
            st.session_state.energy,
            st.session_state.energy*1.08,
            st.session_state.energy*1.02,
            st.session_state.energy*0.96,
            st.session_state.energy*0.91
        ]

    })

    fig = px.area(

        history,

        x="Hour",

        y="Energy",

        line_shape="spline",

        markers=True,

        color_discrete_sequence=["#3B82F6"]

    )

    fig.update_traces(

        line=dict(width=4),

        marker=dict(size=10),

        fillcolor="rgba(59,130,246,0.25)"

    )

    fig.update_layout(

        template="plotly_dark",

        height=460,

        paper_bgcolor="#0B1220",

        plot_bgcolor="#111827",

        font=dict(color="white"),

        hovermode="x unified",

        margin=dict(l=20,r=20,t=20,b=20),

        xaxis_title="Working Hours",

        yaxis_title="Energy (Wh)",

        title=""

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

# ============================================================
# PDF REPORT
# ============================================================

if st.session_state.energy > 0:

    st.header("📄 Energy Audit Report")

    if st.button("📥 Generate Professional PDF Report"):

        report_name = f"Reports/{company.replace(' ','_')}_Audit_Report.pdf"

        estimated_saving = st.session_state.cost * 30 * 0.15

        import os
        os.makedirs("Reports", exist_ok=True)

        generate_report(
            report_name,
            company,
            location,
            auditor,
            industry,
            st.session_state.energy,
            st.session_state.cost,
            st.session_state.co2,
            st.session_state.health,
            estimated_saving,
            st.session_state.recommendations
        )

        st.success("✅ Report Generated Successfully!")

        with open(report_name, "rb") as pdf_file:

            st.download_button(
                "⬇ Download Report",
                pdf_file,
                file_name=os.path.basename(report_name),
                mime="application/pdf"
            )

    st.divider()

# ============================================================
# PREDICTION HISTORY
# ============================================================

if "history" in st.session_state and len(st.session_state.history) > 0:

    st.header("📜 Audit History")

    st.caption("Previous AI energy audit results.")

    history_df = pd.DataFrame(st.session_state.history[::-1])

    def color_health(val):

        if val == "Excellent":
            return "background-color:#16A34A;color:white;font-weight:bold;"

        elif val == "Good":
            return "background-color:#22C55E;color:white;font-weight:bold;"

        elif val == "Warning":
            return "background-color:#F59E0B;color:white;font-weight:bold;"

        elif val == "Critical":
            return "background-color:#DC2626;color:white;font-weight:bold;"

        return ""

    styled_df = history_df.style.map(
    color_health,
    subset=["Health"]
)

    st.dataframe(
        styled_df,
        use_container_width=True,
        hide_index=True
    )
    history_df["Energy (Wh)"] = history_df["Energy (Wh)"].round(2)
    history_df["Cost (₹)"] = history_df["Cost (₹)"].round(2)
    history_df["CO₂ (kg)"] = history_df["CO₂ (kg)"].round(2)

    st.download_button(

        "⬇ Download Audit History (CSV)",

        history_df.to_csv(index=False),

        file_name="EnerVision_Audit_History.csv",

        mime="text/csv"

    )

    st.divider()
# ============================================================
# ENERGY HEALTH GAUGE
# ============================================================

if st.session_state.energy > 0:

    st.header("🎯 Energy Health Score")

    energy = st.session_state.energy

    score = max(0, min(100, int(100 - energy / 5)))

    if score >= 80:
        color = "#22C55E"
        status = "Excellent"
        emoji = "🟢"

    elif score >= 60:
        color = "#F59E0B"
        status = "Good"
        emoji = "🟠"

    else:
        color = "#EF4444"
        status = "Critical"
        emoji = "🔴"

    st.markdown(f"""
<div style="
background:#111827;
padding:30px;
border-radius:18px;
text-align:center;
box-shadow:0px 5px 15px rgba(0,0,0,0.35);
">

<h1 style="
font-size:72px;
color:{color};
margin-bottom:0;
">

{score}

</h1>

<h3 style="color:white;">
Energy Health Score
</h3>

<h2 style="color:{color};">

{emoji} {status}

</h2>

</div>
""",
unsafe_allow_html=True)

    st.progress(score)

    st.divider()
# ============================================================
# SMART ENERGY SAVING ESTIMATOR
# ============================================================

if st.session_state.energy > 0:

    st.header("💰 Estimated Savings")

    monthly_energy = st.session_state.energy * 30

    saving_percent = 0

    if lights > 70:
        saving_percent += 5

    if machines > 8:
        saving_percent += 8

    if working_hours > 10:
        saving_percent += 7

    if humidity > 70:
        saving_percent += 3

    if production < 40:
        saving_percent += 5

    monthly_cost = (monthly_energy / 1000) * tariff

    estimated_saving = monthly_cost * saving_percent / 100

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "📅 Monthly Electricity Cost",
            f"₹ {monthly_cost:.2f}"
        )

    with col2:
        st.metric(
            "💸 Possible Monthly Saving",
            f"₹ {estimated_saving:.2f}"
        )

    st.success(
        f"Following the AI recommendations may reduce your electricity bill by approximately {saving_percent}%."
    )

    st.divider()
# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown("""
<div style="
text-align:center;
padding:25px;
color:#9CA3AF;
font-size:15px;
">

<b style="color:white;font-size:18px;">
⚡ EnerVision AI v1.0
</b>

<br><br>

AI Powered Smart Energy Audit & Sustainability Platform

<br><br>

Developed by

<b style="color:#60A5FA;">
Bhavya Prajapati
</b>

<br>

Electronics & Communication Engineering

<br>

L.D. College of Engineering

<br><br>

© 2026 EnerVision AI | All Rights Reserved

</div>
""", unsafe_allow_html=True)