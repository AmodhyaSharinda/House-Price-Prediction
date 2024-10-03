import streamlit as st

# Custom CSS to set background image and center the button
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://images.pexels.com/photos/2187605/pexels-photo-2187605.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"); /* Replace with your image URL */
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.title-container {
    text-align: center;
    color: white;
    padding: 10px;
}

.description-container {
    text-align: center;
    color: white;
    font-size: 18px;
    margin-top: 20px;
    margin-bottom: 40px;
}

.center-button {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 50px;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 15px 32px;
    text-align: center;
    font-size: 16px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}
</style>
'''

# Set up session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Inject custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to show the form

st.title("House Pricing Prediction")
st.write("""
This application helps predict house prices based on various property features. Please fill out the necessary details to get an estimate.
""")

    # Prediction Button
st.write("##")
if st.button("Predict House Price", key="predict_button"):
    st.session_state.page = 'form'