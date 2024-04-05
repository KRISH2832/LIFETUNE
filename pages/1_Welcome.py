import streamlit as st

from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title="LifeTune", page_icon="💊", layout="wide")
st.markdown(
    """
        <style>
            [data-testid="stSidebarNav"] {
                background-repeat: no-repeat;                
            }
            [data-testid="stSidebarNav"]::before {
                content: "LifeTune";
                margin-left: 20px;
                margin-top: 20px;

                font-size: 30px;
                text-align: center;
                position: relative;
            }
        </style>
        """,
    unsafe_allow_html=True,
)

def gradient_text(text, color1, color2):
        gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 54px;
        """
        return f'<span style="{gradient_css}">{text}</span>'
 
color1 = "#0d3270"
color2 = "#0fab7b"
text = "LifeTune: Decode Your Health"
  
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("images/logo.png", width=200)

styled_text = gradient_text(text, color1, color2)
st.write(f"<div style='text-align: center;'>{styled_text}</div>", unsafe_allow_html=True)
    
st.markdown("Embark on a transformative health journey with **LifeTune**, the innovative app designed to utilize advanced scanning technology. Our cutting-edge algorithms empower you with precise identification of various health conditions, providing valuable insights for informed decision-making.")
def gradient_text(text, color1, color2):
        gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 32px;
        """
        return f'<span style="{gradient_css}">{text}</span>'

color1 = "#FF5E33"
color2 = "#FFA233"
text = "Brain Lens: Unveil the Details"
  
# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     st.image("images/logo.png", width=200)

styled_text = gradient_text(text, color1, color2)
st.write(f"<div>{styled_text}</div>", unsafe_allow_html=True)
    
st.markdown(
    """


LifeTune is your ally in identifying three distinct types of brain tumors:

- **Pituitary Tumor:** Uncover abnormalities in the pituitary gland, fostering early intervention and targeted treatment plans.

- **Glioma:** Detect the presence of gliomas, the most prevalent form of brain tumors, for proactive health management.

- **Meningioma:** Recognize meningiomas, enabling timely monitoring and potential intervention for optimal outcomes.""")
aps = st.button("Brain Lens")
if aps:
    switch_page("Brain Lens")

def gradient_text(text, color1, color2):
        gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 32px;
        """
        return f'<span style="{gradient_css}">{text}</span>'

color1 = "#FF5E33"
color2 = "#FFA233"
text = "Lung Lens: Precision in Every Scan"
  
# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     st.image("images/logo.png", width=200)

styled_text = gradient_text(text, color1, color2)
st.write(f"<div>{styled_text}</div>", unsafe_allow_html=True)
st.markdown("""
Navigate the complexities of lung health with LifeTune, distinguishing between three primary types of lung cancer:

- **Adenocarcinoma:** Identify glandular tumors accurately, paving the way for tailored treatment approaches.

- **Large Cell Carcinoma:** Detect large cell carcinomas swiftly, ensuring prompt medical attention and targeted therapies.

- **Squamous Cell Carcinoma:** Recognize squamous cell carcinomas with precision, guiding towards effective treatment strategies.""")
aps = st.button("Lung Lens")
if aps:
    switch_page("Lung Lens")

def gradient_text(text, color1, color2):
        gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 32px;
        """
        return f'<span style="{gradient_css}">{text}</span>'

color1 = "#FF5E33"
color2 = "#FFA233"
text = "Kidney Lens: Delving into Kidney Health"
  
# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     st.image("images/logo.png", width=200)

styled_text = gradient_text(text, color1, color2)
st.write(f"<div>{styled_text}</div>", unsafe_allow_html=True)

st.markdown("""
LifeTune extends its capabilities to renal health, offering insights into three crucial conditions:

- **Cyst:** Pinpoint cysts in the kidneys for monitoring and personalized health management.

- **Tumor:** Identify tumors in the kidneys with precision, facilitating prompt medical attention and care.

- **Stone:** Detect kidney stones accurately, guiding healthcare professionals towards the most effective treatment plans.""")
aps = st.button("Kidney Lens")
if aps:
    switch_page("Kidney Lens")

def gradient_text(text, color1, color2):
        gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 32px;
        """
        return f'<span style="{gradient_css}">{text}</span>'

color1 = "#FF5E33"
color2 = "#FFA233"
text = "Tuberculosis Teller: A Comprehensive Approach"
  
# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     st.image("images/logo.png", width=200)

styled_text = gradient_text(text, color1, color2)
st.write(f"<div>{styled_text}</div>", unsafe_allow_html=True)
st.markdown("""
LifeTune goes beyond expectations by identifying tuberculosis in the lungs through detailed Chest X-ray analysis, allowing for early detection and intervention.""")
aps = st.button("Tuberculosis Teller")
if aps:
    switch_page("Tuberculosis Teller")

def gradient_text(text, color1, color2):
        gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 32px;
        """
        return f'<span style="{gradient_css}">{text}</span>'

color1 = "#FF5E33"
color2 = "#FFA233"
text = "Why Choose LifeTune?"
  
# left_co, cent_co,last_co = st.columns(3)
# with cent_co:
#     st.image("images/logo.png", width=200)

styled_text = gradient_text(text, color1, color2)
st.write(f"<div>{styled_text}</div>", unsafe_allow_html=True)

st.markdown("""
- **Accuracy at its Core:** Our advanced algorithms ensure accurate identification of diverse health conditions.

- **Timely Intervention:** Early detection empowers you and your healthcare provider to take proactive measures for optimal health outcomes.

- **User-Friendly Experience:** Seamlessly upload and analyze scans, making health management intuitive and hassle-free.

- **Privacy First:** Your health data is treated with the utmost confidentiality, secured through state-of-the-art encryption.

Embark on a journey towards personalized healthcare. Download **LifeTune** now and unlock a new era of well-being. Your health, our priority!
"""

)



