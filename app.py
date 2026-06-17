import streamlit as st
import pandas as pd
import numpy as np
import joblib

import plotly.express as px
import plotly.graph_objects as go

import matplotlib.pyplot as plt
import seaborn as sns

from recommendation import get_recommendation
from report_generator import create_report


# PAGE CONFIG


st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🩺",
    layout="wide"
)


# CUSTOM CSS


st.markdown("""
<style>

.main{
    background-color:#F8FAFC;
}

.title{
    font-size:50px;
    font-weight:bold;
    color:#2563EB;
}

.subtitle{
    font-size:18px;
    color:#64748B;
    margin-bottom:20px;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)


# LOAD MODEL


model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load(
    "models/feature_names.pkl"
)
accuracies = joblib.load(
    "models/accuracies.pkl"
)


# HEADER


st.markdown(
"""
<div class='title'>
🩺 Diabetes Risk Predictor
</div>

<div class='subtitle'>
Machine Learning Based Health Assessment System
</div>
""",
unsafe_allow_html=True
)

st.markdown("---")


# PATIENT DETAILS


name = st.text_input("Patient Name")


# HEALTH INFO


with st.expander("📖 Health Parameter Reference Guide"):

    st.markdown("""
## Glucose (mg/dL)

| Range | Interpretation |
|---------|---------|
| 70 - 99 | Normal |
| 100 - 125 | Prediabetes |
| 126+ | Diabetes Risk |

---

## Blood Pressure (mmHg)

| Range | Interpretation |
|---------|---------|
| 90 - 120 | Normal |
| 121 - 129 | Elevated |
| 130+ | High |

---

## BMI

| Range | Interpretation |
|---------|---------|
| <18.5 | Underweight |
| 18.5 - 24.9 | Normal |
| 25 - 29.9 | Overweight |
| 30+ | Obese |

---

## Pregnancies

Reference Guide

| Pregnancies | Risk Contribution |
|---------|---------|
| 0 - 2 | Lower |
| 3 - 5 | Moderate |
| 6+ | Higher |

---

## Insulin (μU/mL)

| Range | Interpretation |
|---------|---------|
| 16 - 166 | Typical |
| >166 | Elevated |
| <16 | Low |

---

## Skin Thickness (mm)

| Range | Interpretation |
|---------|---------|
| 10 - 20 | Typical |
| 20 - 40 | Above Average |
| >40 | Elevated |

---

## Diabetes Pedigree Function

| Value | Interpretation |
|---------|---------|
| <0.3 | Low Genetic Risk |
| 0.3 - 0.6 | Moderate Risk |
| >0.6 | Higher Genetic Risk |

---

## Age

| Range | Interpretation |
|---------|---------|
| <35 | Lower Risk Group |
| 35 - 50 | Moderate Risk Group |
| >50 | Higher Risk Group |
""")

# INPUTS


col1, col2 = st.columns(2)

with col1:

    preg = st.number_input(
    "Pregnancies",
    min_value=0,
    max_value=20,
    help="0-2 lower risk contribution, 6+ higher statistical risk"
)

    glucose = st.number_input(
        "Glucose (mg/dL)",
        min_value=0,
        max_value=300,
        help="Normal fasting glucose: 70-99 mg/dL"
    )

    bp = st.number_input(
        "Blood Pressure",
        min_value=0,
        max_value=200,
        help="Normal range: 90-120 mmHg"
    )

    skin = st.number_input(
    "Skin Thickness (mm)",
    min_value=0,
    max_value=100,
    help="Typical range: 10-40 mm"
)

with col2:

    insulin = st.number_input(
    "Insulin (μU/mL)",
        min_value=0,
        max_value=900,
        help="Typical range: 16-166 μU/mL"
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        help="Healthy BMI: 18.5 - 24.9"
    )

    pedigree = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    help="Measures hereditary diabetes risk"
)
    

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120
    )


# BMI CATEGORY


if bmi > 0:

    if bmi < 18.5:
        bmi_category = "Underweight"

    elif bmi < 25:
        bmi_category = "Normal"

    elif bmi < 30:
        bmi_category = "Overweight"

    else:
        bmi_category = "Obese"

    st.info(f"Current BMI Category: {bmi_category}")

st.markdown("---")
st.subheader("📋 Live Health Analysis")

# Glucose

if glucose > 0:

    if glucose < 100:
        st.success("✅ Glucose Level: Normal")

    elif glucose < 126:
        st.warning("⚠ Prediabetes Range")

    else:
        st.error("🚨 High Diabetes Risk Glucose Level")


# Blood Pressure

if bp > 0:

    if bp < 120:
        st.success("✅ Blood Pressure: Normal")

    elif bp < 130:
        st.warning("⚠ Elevated Blood Pressure")

    else:
        st.error("🚨 High Blood Pressure")


# Insulin

if insulin > 0:

    if insulin < 16:
        st.warning("⚠ Low Insulin")

    elif insulin <= 166:
        st.success("✅ Normal Insulin Range")

    else:
        st.warning("⚠ Elevated Insulin")


# Diabetes Pedigree

if pedigree > 0:

    if pedigree < 0.3:
        st.success("✅ Low Genetic Risk")

    elif pedigree < 0.6:
        st.warning("⚠ Moderate Genetic Risk")

    else:
        st.error("🚨 High Genetic Risk")

# PREDICTION

if st.button("🔍 Predict Diabetes Risk"):

    features = np.array([[
        preg,
        glucose,
        bp,
        skin,
        insulin,
        bmi,
        pedigree,
        age
    ]])

    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)[0]

    risk = model.predict_proba(features_scaled)[0][1] * 100

    result = "Diabetic" if prediction == 1 else "Non-Diabetic"

    st.markdown("---")

    st.subheader("Prediction Result")

    if risk < 30:
        st.success(f"🟢 Low Risk ({risk:.2f}%)")

    elif risk < 70:
        st.warning(f"🟠 Moderate Risk ({risk:.2f}%)")

    else:
        st.error(f"🔴 High Risk ({risk:.2f}%)")

        st.metric(
        "Prediction",
        result
    )

    
    # Gauge Chart
    
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk,
        title={"text": "Diabetes Risk Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "steps": [
                {"range": [0, 30]},
                {"range": [30, 70]},
                {"range": [70, 100]}
            ]
        }
    ))

    st.plotly_chart(
        fig_gauge,
        use_container_width=True
    )

    
    # Recommendations
    

    st.subheader("📋 Health Recommendations")

    st.info(
        get_recommendation(risk)
    )

   
    # AI Interpretation
    

    st.subheader("🧠 AI Risk Interpretation")

    if risk < 30:

        st.success("""
Patient exhibits low diabetes risk based on the provided health indicators.

Continue maintaining a healthy lifestyle and periodic health monitoring.
""")

    elif risk < 70:

        st.warning("""
Patient exhibits moderate diabetes risk.

Lifestyle improvements, exercise, and routine glucose monitoring are recommended.
""")

    else:

        st.error("""
Patient exhibits high diabetes risk.

Medical consultation and further diagnostic testing are strongly advised.
""")

   
    # PDF REPORT
    

    if st.button("📄 Generate PDF Report"):

        pdf_file = create_report(
            name,
            result,
            risk
        )

        st.success(
            f"Report Generated: {pdf_file}"
        )


# DASHBOARD


st.markdown("---")
st.header("📊 Dataset Analytics Dashboard")
st.subheader("🏆 Model Performance Comparison")
accuracy_df = pd.DataFrame({

    "Model": list(accuracies.keys()),

    "Accuracy": list(accuracies.values())

})

fig_acc = px.bar(

    accuracy_df,

    x="Model",

    y="Accuracy",

    text="Accuracy",

    title="Machine Learning Model Comparison"

)

st.plotly_chart(
    fig_acc,
    use_container_width=True
)

df = pd.read_csv("dataset/diabetes.csv")


# METRICS


m1, m2, m3, m4 = st.columns(4)

m1.metric(
    "Total Records",
    len(df)
)

m2.metric(
    "Average Glucose",
    round(df["Glucose"].mean(), 2)
)

m3.metric(
    "Average BMI",
    round(df["BMI"].mean(), 2)
)

m4.metric(
    "Average Age",
    round(df["Age"].mean(), 2)
)


# PIE CHART


st.subheader("Outcome Distribution")

outcome_count = df["Outcome"].value_counts()

fig_outcome = px.pie(
    values=outcome_count.values,
    names=["Non-Diabetic", "Diabetic"],
    title="Diabetes Distribution"
)

st.plotly_chart(
    fig_outcome,
    use_container_width=True
)


# HISTOGRAMS


colA, colB = st.columns(2)

with colA:

    fig_glucose = px.histogram(
        df,
        x="Glucose",
        nbins=30,
        title="Glucose Distribution"
    )

    st.plotly_chart(
        fig_glucose,
        use_container_width=True
    )

with colB:

    fig_bmi = px.histogram(
        df,
        x="BMI",
        nbins=30,
        title="BMI Distribution"
    )

    st.plotly_chart(
        fig_bmi,
        use_container_width=True
    )


# AGE DISTRIBUTION


fig_age = px.histogram(
    df,
    x="Age",
    nbins=20,
    title="Age Distribution"
)

st.plotly_chart(
    fig_age,
    use_container_width=True
)


# SCATTER PLOT


st.subheader("Glucose vs BMI Analysis")

fig_scatter = px.scatter(
    df,
    x="Glucose",
    y="BMI",
    color="Outcome",
    title="Glucose vs BMI"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)


# HEATMAP


st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(
    figsize=(10, 6)
)

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)


# RISK FACTORS


st.subheader("Most Important Risk Factors")

try:

    if hasattr(model, "coef_"):

        importance = np.abs(
            model.coef_[0]
        )

    elif hasattr(model, "feature_importances_"):

        importance = model.feature_importances_

    else:

        importance = np.ones(
            len(feature_names)
        )

    importance_df = pd.DataFrame({

        "Feature": feature_names,

        "Importance": importance

    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    fig_importance = px.bar(

        importance_df,

        x="Feature",

        y="Importance",

        title="Actual Model Feature Importance"

    )

    st.plotly_chart(
        fig_importance,
        use_container_width=True
    )

except Exception:

    st.warning(
        "Feature importance unavailable."
    )


# DATASET TABLE


st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)


# FOOTER

st.markdown("---")

st.markdown(
"""
<center>
Diabetes Risk Predictor | Machine Learning Internship Project
</center>
""",
unsafe_allow_html=True
)
