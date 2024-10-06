import streamlit as st
import requests

st.session_state.page = 'form'

if 'page' not in st.session_state:
    st.session_state.page = 'form'

st.title("House Pricing Prediction")

lot_size = st.number_input("Lot size in square feet", key="lot_size")

masonry_area = st.number_input("Masonry veneer area in square feet", key="masonry_area")

KitchenQual = st.selectbox("Kitchen quality", ["Ex Excellent", "Gd Good", "TA Typical/Average", "Fa Fair", "Po Poor"], key="kitchen_quality")

# Text input for total rooms
total_rooms_input = st.text_input(
    "Total rooms above grade (does not include bathrooms)", 
    key="total_rooms"
)

# Initialize total_rooms variable
total_rooms = 0

# Convert input to integer
if total_rooms_input:
    try:
        total_rooms = int(total_rooms_input)  # Convert to integer
    except ValueError:
        st.error("Please enter a valid integer. Floats are not allowed.")

 # Text input for number of fireplaces
num_fireplaces_input = st.text_input(
    "Number of fireplaces", 
    key="num_fireplaces"
)

# Initialize num_fireplaces variable
num_fireplaces = 0

# Convert input to integer
if num_fireplaces_input:
    try:
        num_fireplaces = int(num_fireplaces_input)  # Convert to integer
    except ValueError:
        st.error("Please enter a valid integer. Floats are not allowed.")       


GarageType = st.selectbox("Garage location", ["2Types More than one type of garage", "Attchd Attached to home", "Basment Basement Garage", "BuiltIn Built In",
                                 "CarPort Car Port", "Detchd Detached from home", "No No Garage"], key="GarageType")

GarageFinish = st.selectbox("Interior finish of the garage", ["Fin Finished", "RFn Rough Finished", "Unf Unfinished", "NA No Garage"], key="GarageFinish")

garage_size = st.number_input("Size of garage in square feet", key="garage_size")


# Set the current year
current_year = 2024  # Update this to the current year

# Number input for year built
year_built = st.number_input(
    "Year Built", 
    key="year_built", 
    min_value=1900,  # Set the minimum valid year (you can adjust this as needed)
    max_value=current_year,  # Set the maximum valid year
    step=1,  # Increment step for years
    format="%d"  # Ensure the input format is an integer
)

# Optional: Display an error message if the input is outside valid range
if year_built < 1900 or year_built > current_year:
    st.error("Please enter a valid year between 1900 and the current year.")


# Number input for year remodeled
year_remodeled = st.number_input(
    "Year Remodeled", 
    key="year_remodeled", 
    min_value=year_built,  # Set minimum value to year_built
    max_value=current_year,  # Set the maximum valid year
    step=1,  # Increment step for years
    format="%d"  # Ensure the input format is an integer
)

# Optional: Display an error message if year_remodeled is less than year_built
if year_remodeled < year_built:
    st.error("Year Remodeled must be greater than or equal to Year Built.")

st.write("")
st.write("Total Area in square feet")
total_above_basement = st.number_input("Total square feet above basement", key="total_above_basement")

total_basement = st.number_input("Total square feet of the basement", key="total_basement")

st.write("")
st.write("Total Square Feet")
first_floor = st.number_input("1st Floor square feet", key="first_floor")

second_floor = st.number_input("2nd Floor square feet", key="second_floor")

basement_floor = st.number_input("Basement square feet", key="basement_floor")

st.write("")
st.write("Total Bathrooms")

# Text input for basement full bathrooms
basement_full_bathrooms_input = st.text_input(
    "Basement full bathrooms", 
    key="basement_full_bathrooms"
)

# Initialize half_bathrooms variable
basement_full_bathrooms = 0

# Convert input to integer
if basement_full_bathrooms_input:
    try:
        basement_full_bathrooms = int(basement_full_bathrooms_input)  # Convert to integer
    except ValueError:
        st.error("Please enter a valid integer. Floats are not allowed.")

# Text input for Basement half bathrooms
basement_half_bathrooms_input = st.text_input(
    "Basement half bathrooms", 
    key="basement_half_bathrooms"
)

# Initialize half_bathrooms variable
basement_half_bathrooms = 0

# Convert input to integer
if basement_half_bathrooms_input:
    try:
        basement_half_bathrooms = int(basement_half_bathrooms_input)  # Convert to integer
    except ValueError:
        st.error("Please enter a valid integer. Floats are not allowed.")




# Text input for full bathrooms
full_bathrooms_input = st.text_input(
    "Full bathrooms", 
    key="full_bathrooms"
)

# Initialize half_bathrooms variable
full_bathrooms = 0

# Convert input to integer
if full_bathrooms_input:
    try:
        full_bathrooms = int(full_bathrooms_input)  # Convert to integer
    except ValueError:
        st.error("Please enter a valid integer. Floats are not allowed.")

# Text input for half bathrooms
half_bathrooms_input = st.text_input(
    "Half bathrooms", 
    key="half_bathrooms"
)

# Initialize half_bathrooms variable
half_bathrooms = 0

# Convert input to integer
if half_bathrooms_input:
    try:
        half_bathrooms = int(half_bathrooms_input)  # Convert to integer
    except ValueError:
        st.error("Please enter a valid integer. Floats are not allowed.")


st.write("")
st.write("Exterior conditions")
ExterQual = st.selectbox("ExterQual: Evaluates the quality of the material on the exterior",
             ["Ex	Excellent",
       "Gd	Good",
       "TA	Average/Typical",
       "Fa	Fair",
       "Po	Poor"], key="exterior1")

ExterCond = st.selectbox("ExterCond: Evaluates the present condition of the material on the exterior",
             ["Ex	Excellent",
       "Gd	Good",
       "TA	Average/Typical",
       "Fa	Fair",
       "Po	Poor"], key="exterior2")

st.write("")
st.write("Basement conditions")
bsmt_quality = st.selectbox("BsmtQual: Evaluates the height of the basement",
             ["Ex	Excellent (100+ inches)",	
              "Gd	Good (90-99 inches)",
              "TA	Typical (80-89 inches)",
              "Fa	Fair (70-79 inches)",
              "Po	Poor (<70 inches)",
              "No Basement"], key="bsmt_quality")

bsmt_condition = st.selectbox("Evaluates the general condition of the basement",
             ["Ex	Excellent",	
              "Gd	Good",
              "TA	Typical - slight dampness allowed",
              "Fa	Fair - dampness or some cracking or settling",
              "Po	Poor - Severe cracking, settling, or wetness",
              "No Basement"], key="bsmt_condition")

st.write("")
st.write("Overall Qualities") 
overall_quality = st.selectbox("OverallQual: Rates the overall material and finish of the house",
             ["10	Very Excellent",
              "9	Excellent",
              "8	Very Good",
              "7	Good",
              "6	Above Average",
              "5	Average",
              "4	Below Average",
              "3	Fair",
              "2	Poor",
              "1	Very Poor"], key="overall_quality")

overall_condition = st.selectbox("OverallCond: Rates the overall condition of the house",
             ["10	Very Excellent",
              "9	Excellent",
              "8	Very Good",
              "7	Good",
              "6	Above Average",
              "5	Average",
              "4	Below Average",
              "3	Fair",
              "2	Poor",
              "1	Very Poor"], key="overall_condition")
       


# Prediction Button
st.write("##")

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def extract_quality_score(value):
    # Extract the first part (before tab or space) and map to a score
    prefix = value.split()[0]
    return prefix

OverallQuality_Condition = overall_quality + overall_condition
ExteriorQuality_Condition = extract_quality_score(ExterQual) + extract_quality_score(ExterCond)
AgeBuilt = 2024 - year_built
AgeRemod = 2024 - year_remodeled
totalsf = first_floor + second_floor + basement_floor
totalarea = total_basement + total_above_basement
totalbaths = basement_full_bathrooms + full_bathrooms + 0.5 * (basement_half_bathrooms + half_bathrooms)
BasementQuality_Condition = extract_quality_score(bsmt_quality) + extract_quality_score(bsmt_condition)
GarageType = extract_quality_score(GarageType)
GarageFinish = extract_quality_score(GarageFinish)
KitchenQual = extract_quality_score(KitchenQual)

def extract_numerical_part(value):
    # Split the string by any non-digit characters (remove tabs and text)
    numeric_values = [int(num) for num in value.split('\t') if num.isdigit()]
    return sum(numeric_values)
# Apply the function to the 'OverallQuality_Condition' column
OverallQuality_Condition = extract_numerical_part(OverallQuality_Condition)

# When user clicks 'Predict Price'
if st.button('Predict Price'):
    # Prepare input data in the same format as used during model training
    # Dictionary to hold keys with their corresponding values

    input_keys_dict = {
        "LotArea": lot_size,
        "MasVnrArea": masonry_area,
        "KitchenQual": KitchenQual,
        "TotRmsAbvGrd": total_rooms,
        "Fireplaces": num_fireplaces,
        "GarageType": GarageType,
        "GarageFinish": GarageFinish,
        "GarageArea": garage_size,
        "AgeBuilt": AgeBuilt,
        "AgeRemod": AgeRemod,
        "totalsf": totalsf,
        "totalarea": totalarea,
        "totalbaths": totalbaths,
        "OverallQuality_Condition": OverallQuality_Condition,
        "ExteriorQuality_Condition": ExteriorQuality_Condition,
        "BasementQuality_Condition": BasementQuality_Condition
    }

    # Print input values before creating the dictionary
    print("Lot Size:", lot_size)
    print("Masonry Area:", masonry_area)
    print("Kitchen Quality:", KitchenQual)
    print("Total Rooms:", total_rooms)
    print("Num Fireplaces:", num_fireplaces)
    print("Garage Location:", GarageType)
    print("Garage Finish:", GarageFinish)
    print("Garage Size:", garage_size)
    print("Age Built:", AgeBuilt)
    print("Age Remod:", AgeRemod)
    print("Total Area:", totalarea)
    print("Total SF:", totalsf)
    print("Total Baths:", totalbaths)
    print("Overall Quality Condition:", OverallQuality_Condition)
    print("Exterior Quality Condition:", ExteriorQuality_Condition)
    print("Basement Quality Condition:", BasementQuality_Condition)


    # Print the dictionary
    # st.write(input_keys_dict)

    # Print the dictionary
    # st.write(input_keys_dict)


    # Send POST request to Flask backend
    response = requests.post('http://127.0.0.1:5000/predict', json=input_keys_dict)
    if response.status_code == 200:
        result = response.json()

        print(f"Predicted House Price: ${result['predicted_price']:.2f}")

        sale_price = np.expm1(result['predicted_price'])

         # Display predicted price
        st.write(f"Predicted House Price: ${sale_price:.2f}")
        print(f"Predicted House Price: ${sale_price:.2f}")
    else:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response content: {response.content}")

   