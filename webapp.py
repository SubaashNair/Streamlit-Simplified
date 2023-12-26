import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Load Data
df = pd.read_csv('tips.csv')

# Title and dataset overview
st.title('Data Science Web App')
st.write("Overview of the Dataset")
st.dataframe(df.head())

st.header("Data Visualization")
# Select columns for the plot
selected_x_var = st.selectbox('Select X variable', df.columns)
selected_y_var = st.selectbox('Select Y variable', df.columns)

# Create the plot
st.subheader('Scatter Plot')
fig = plt.figure()
sns.scatterplot(x=df[selected_x_var], y=df[selected_y_var])
st.pyplot(fig)

# Statistical Analysis
# Perform a simple correlation analysis:
st.header("Statistical Analysis")
st.subheader('Correlation Matrix')
fig1 = plt.figure()
correlation_matrix = df.corr(numeric_only=True)
st.write(sns.heatmap(correlation_matrix, annot=True))
# plt.show()
st.pyplot(fig1)


# Predictive Modeling
# Build a linear regression model to predict tips:
st.header("Predictive Modeling")
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# Define features and target variable
X = df[['total_bill', 'size']]  # Example features
y = df['tip']  # Target variable

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# # Predicting
y_pred = model.predict(X_test)
# User input for prediction
st.subheader('Predict Your Tip')
total_bill_input = st.number_input('Total Bill ($)', min_value=0.0, format='%.2f')
size_input = st.number_input('Size of the Party', min_value=1, max_value=10, step=1)

# Prediction
if st.button('Predict Tip'):
    prediction = model.predict([[total_bill_input, size_input]])
    st.write(f'Estimated Tip: ${prediction[0]:.2f}')


# Display the model's performance
st.subheader('Model Performance')
st.write('Mean Squared Error:', mean_squared_error(y_test, y_pred))


# # User Feedback
# st.header("Feedback")


# with st.form("feedback_form"):
#     feedback = st.text_area("Share your feedback", help="What did you like? What can be improved?")
#     submit_button = st.form_submit_button("Submit")

#     if submit_button:
#         sender_email = "your_email@example.com"
#         receiver_email = "destination@example.com"
#         password = "yourpassword"  # Consider using environment variables or input prompts for security

#         message = MIMEMultipart()
#         message["Subject"] = "New Feedback Submission"
#         message["From"] = sender_email
#         message["To"] = receiver_email

#         message.attach(MIMEText(feedback, "plain"))

#         with smtplib.SMTP("smtp.example.com", 587) as server:  # Replace with your SMTP server
#             server.starttls()
#             server.login(sender_email, password)
#             server.sendmail(sender_email, receiver_email, message.as_string())
        
#         st.write("Thanks for your feedback!")
