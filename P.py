import streamlit as st
import pandas as pd
import numpy as np

# Streamlit app title and description
st.set_page_config(page_title="EA FC OVR RATING", layout="centered")

# Add an image (local or online)
st.image('/Users/ibra47sh/np & pd/PycharmProjects/MP2/EA_SPORTS_FC_25_Reveal_Trailer.jpg', use_column_width=True)
st.title('⚽ EA FC OVR RATING')
st.markdown("""
This tool helps calculate weighted attribute values for different football positions based on key stats like 
**PAC (Pace)**, **SHO (Shooting)**, **PAS (Passing)**, **DRI (Dribbling)**, **DEF (Defense)**, **PHY (Physicality)**, and now **GK Stats**.
Select your role and input the corresponding stats to see the result.
""")

# Sidebar for input fields
st.sidebar.header('Input Player Stats')

# Regular player attributes
pac = st.sidebar.number_input('PAC (Pace)', min_value=0, max_value=100, step=1)
sho = st.sidebar.number_input('SHO (Shooting)', min_value=0, max_value=100, step=1)
pas = st.sidebar.number_input('PAS (Passing)', min_value=0, max_value=100, step=1)
dri = st.sidebar.number_input('DRI (Dribbling)', min_value=0, max_value=100, step=1)
def_ = st.sidebar.number_input('DEF (Defense)', min_value=0, max_value=100, step=1)
phy = st.sidebar.number_input('PHY (Physical)', min_value=0, max_value=100, step=1)

# GK specific attributes
st.sidebar.subheader('Goalkeeper Attributes')
gk_diving = st.sidebar.number_input('GK Diving', min_value=0, max_value=100, step=1)
gk_handling = st.sidebar.number_input('GK Handling', min_value=0, max_value=100, step=1)
gk_kicking = st.sidebar.number_input('GK Kicking', min_value=0, max_value=100, step=1)
gk_positioning = st.sidebar.number_input('GK Positioning', min_value=0, max_value=100, step=1)
gk_reflexes = st.sidebar.number_input('GK Reflexes', min_value=0, max_value=100, step=1)

st.sidebar.subheader('Additional Attributes')
weak_foot = st.sidebar.slider('Weak Foot Rating (out of 5)', min_value=1, max_value=5, step=1)
skill_move = st.sidebar.slider('Skill Move Rating (out of 5)', min_value=1, max_value=5, step=1)


role_weights = pd.DataFrame({
    'Role': ['CB', 'RB/LB', 'CM', 'CDM', 'CAM', 'RW/LW', 'ST', 'GK'],
    'PAC': [0.1, 0.2, 0.166, 0.15, 0.1, 0.35, 0.2, 0],
    'SHO': [0.1, 0.1, 0.166, 0.05, 0.2, 0.2, 0.35, 0],
    'PAS': [0.1, 0.2, 0.166, 0.2, 0.35, 0.15, 0.05, 0],
    'DRI': [0.1, 0.15, 0.166, 0.1, 0.25, 0.2, 0.2, 0],
    'DEF': [0.4, 0.3, 0.166, 0.35, 0.05, 0.05, 0.05, 0],
    'PHY': [0.2, 0.15, 0.166, 0.15, 0.05, 0.05, 0.15, 0],
    'GK Diving': [0, 0, 0, 0, 0, 0, 0, 0.225],
    'GK Handling': [0, 0, 0, 0, 0, 0, 0, 0.225],
    'GK Kicking': [0, 0, 0, 0, 0, 0, 0, 0.1],
    'GK Positioning': [0, 0, 0, 0, 0, 0, 0, 0.225],
    'GK Reflexes': [0, 0, 0, 0, 0, 0, 0, 0.225],
    'Weak Foot': [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0],
    'Skill Move': [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0]
})

# Store input attributes in a numpy array
attributes = np.array([pac, sho, pas, dri, def_, phy, gk_diving, gk_handling, gk_kicking, gk_positioning, gk_reflexes, weak_foot, skill_move])

# Select the role from a dropdown
role = st.selectbox('Select Role', role_weights['Role'], index=2)  # Default to CM

# Get the corresponding row for the selected role
role_row = role_weights[role_weights['Role'] == role].iloc[:, 1:].values.flatten()

# Calculate the weighted value using numpy
weighted_value = np.dot(attributes, role_row)

# Display the weighted result with a styled message
st.markdown(f"""
### Calculated Attribute Value for **{role}**:
#### {weighted_value:.2f}
""")

# Add a note for interpretation
st.info("The weighted value is calculated based on the specific priorities for each role. Adjust the attributes to explore different results.")
