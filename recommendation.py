def get_recommendation(risk):

    if risk < 30:

        return """
🟢 LOW RISK

• Maintain a balanced diet.

• Exercise for at least 30 minutes daily.

• Stay hydrated.

• Get annual health checkups.

• Maintain a healthy body weight.
"""

    elif risk < 70:

        return """
🟠 MODERATE RISK

• Reduce sugar intake.

• Avoid processed foods.

• Increase physical activity.

• Monitor blood glucose regularly.

• Schedule routine medical checkups.
"""

    else:

        return """
🔴 HIGH RISK

• Consult a healthcare professional.

• Follow a diabetic-friendly diet.

• Monitor blood sugar levels frequently.

• Maintain a strict exercise schedule.

• Seek immediate medical guidance.
"""