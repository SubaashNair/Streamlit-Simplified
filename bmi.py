import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
# import matplotlib.pyplot as plt

st.title('Enhanced BMI Calculator')

# Display Image
img = Image.open('bmi.jpg')
st.image(img)

# Conversion from feet and inches or meters to centimeters
st.subheader("Enter your height")
option = st.selectbox('Choose your preferred unit for height', ('Centimeters', 'Meters', 'Feet and Inches'))

if option == 'Centimeters':
    height = st.number_input('Enter your height in cm', step=1.0)
elif option == 'Meters':
    meters = st.number_input('Enter your height in meters', step=0.01)
    height = meters * 100
    st.text(f"Your height in centimeters: {height} cm")
else:
    feet = st.number_input('Feet', step=1)
    inches = st.number_input('Inches', step=1)
    height = (feet * 30.48) + (inches * 2.54)
    st.text(f"Your height in centimeters: {height} cm")

# Input for weight
weight = st.number_input('Enter your weight in kg', step=0.1)

# BMI calculation with error handling
try:
    bmi = weight / ((height/100) ** 2)
    if height <= 0 or weight <= 0:
        raise ValueError("Height and Weight must be greater than zero.")

    # Determine the BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 24.9 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    # Display BMI and Category
    st.success(f'Your BMI is {round(bmi, 2)} and you fall under the category: {category}')

    # General advice based on BMI category
    if category == "Underweight":
        st.info("You are underweight. Consider gaining weight through a balanced diet.")
    elif category == "Normal weight":
        st.info("You have a normal body weight. Keep up your healthy lifestyle!")
    elif category == "Overweight":
        st.warning("You are overweight. Consider a balanced diet and regular exercise.")
    else:
        st.error("You are obese. It's recommended to consult a healthcare provider for guidance.")

    # Define BMI categories and corresponding values for bar chart
    bmi_categories = {
        "Underweight": 18.5,
        "Normal": 24.9,
        "Overweight": 29.9,
        "Obesity": 40,  # Upper limit for Obesity category
        "Your BMI": bmi  # User's BMI
    }


    # Define BMI categories and corresponding values for bar chart
    bmi_categories = {
        "Underweight": 18.5,
        "Normal": 24.9,
        "Overweight": 29.9,
        "Obesity": 40,  # Upper limit for Obesity category
        "Your BMI": bmi  # User's BMI
}

    # Create DataFrame for plotting
    df = pd.DataFrame(list(bmi_categories.items()), columns=['Category', 'Value'])

    # Create the bar chart using Plotly Express
    fig = px.bar(df, x='Category', y='Value', text='Value',
                title="BMI Categories and Your BMI",
                labels={'Value': 'BMI', 'Category': 'Categories'},
                color='Category',
                color_discrete_map={
                    "Underweight": "blue",
                    "Normal": "green",
                    "Overweight": "orange",
                    "Obesity": "red",
                    "Your BMI": "purple"  # Highlight user's BMI
                })

    # Update layout for better readability
    fig.update_layout(showlegend=False)
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig.update_yaxes(range=[0, max(df['Value']) + 5])  # Adjust y-axis limit

    # Show plot
    st.plotly_chart(fig)

except ZeroDivisionError:
    st.error("Height cannot be zero. Please enter a valid height.")
except ValueError as e:
    st.error(str(e))
