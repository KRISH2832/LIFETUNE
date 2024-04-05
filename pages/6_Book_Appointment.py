import streamlit as st
import time
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import requests
import streamlit.components.v1 as components
import js2py 
import sys
st.set_page_config(page_title="LifeTune", page_icon="💊")
def book_appointment(doctor_name, patient_email, patient_name):
    # Add your booking logic here, e.g., database integration, etc.


    # Send confirmation email to the patient
    send_confirmation_email(patient_email, doctor_name, patient_name)


    # Send appointment email to the doctor
    doctor_email = get_doctor_email(doctor_name)
    send_appointment_email(doctor_email, patient_email, doctor_name, patient_name)


    st.success(f"Appointment booked with {doctor_name}. You will be contacted soon!")


def send_confirmation_email(patient_email, doctor_name,patient_name):
   # Replace 'your_azure_logic_app_url' with the URL of your Azure logic app to send appointment emails
    azure_logic_app_url = st.secrets['azure_logic_app']

    email_data = {
        "to": patient_email,
         "name": patient_name,
        "subject": "Appointment Confirmed at LifeTune",
       
        "content": f"Your appointment with {doctor_name} has been booked successfully. You will be contacted soon.",
    }

    response = requests.post(azure_logic_app_url, json=email_data)
    if response.status_code == 200 or response.status_code == 202:
        st.success("Confirmation email sent to the patient.")
    else:
        st.error("Failed to send confirmation email.")


def send_appointment_email(doctor_email, patient_email, doctor_name, patient_name):
    # Replace 'your_azure_logic_app_url' with the URL of your Azure logic app to send appointment emails
    azure_logic_app_url =st.secrets['azure_logic_app']

    email_data = {
        "to": doctor_email,
        "name": doctor_name,
        "subject": "New Appointment at LifeTune",
        "content": f"A new appointment has been booked with you by {patient_name}. \n More details will be shared soon.",
    }


    response = requests.post(azure_logic_app_url, json=email_data)
    if response.status_code == 200 or response.status_code == 202:
        st.success("Appointment email sent to the doctor.")
    else:
        st.error("Failed to send appointment email.")


def get_doctor_email(doctor_name):
    # Replace this function with a method to retrieve the doctor's email from your database or list
    # In this example, we'll assume the email is stored in the 'contact' field of the doctor's details.
    for doctor in st.session_state.doctor:
        if doctor["name"] == doctor_name:
            return doctor["contact"]


def doctor():
    
    def gradient_text(text, color1, color2):
        gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 42px;
        """
        return f'<span style="{gradient_css}">{text}</span>'

    color1 = "#0d3270"
    color2 = "#0fab7b"
    text = "LifeTune: Decode Your Health"
  
    # left_co, cent_co,last_co = st.columns(3)
    # with cent_co:
    #     st.image("images/logo.png", width=200)

    styled_text = gradient_text(text, color1, color2)
    st.write(f"<div style='text-align: center;'>{styled_text}</div>", unsafe_allow_html=True)
    st.markdown("### Book your appointment with ease")
    if "doctor" not in st.session_state:
        database_endpoint="https://hvbajoria101.kintone.com/k/v1/record.json?"
        database_headers={'X-Cybozu-API-Token':f"{st.secrets['kintone_key']}", 'Content-Type': 'application/json'}

        doctors = []

        # Fetching doctors from database
        for i in range(1,9):
            database_data = {
            'app':1,
            'id':i
            }

            database_response = requests.get(f"{database_endpoint}", headers=database_headers, json=database_data)
    
            doctor={}
            doctor["name"]=database_response.json()["record"]["Text"]["value"]
            doctor["specialization"]=database_response.json()["record"]["Text_0"]["value"]
            doctor["location"]=database_response.json()["record"]["Text_1"]["value"]
            doctor["available_days"]=database_response.json()["record"]["Text_3"]["value"]
            doctor["contact"]=database_response.json()["record"]["Text_2"]["value"]
            doctors.append(doctor)
        st.session_state.doctor = doctors

    if "treatment" in st.session_state:
        st.warning(f"We have detected: {st.session_state.treatment}\n", icon='📑')
    st.write("Select a doctor to view details and book an appointment: :stethoscope:")
    selected_doctor = st.selectbox("Select a doctor", [doctor["name"] for doctor in st.session_state.doctor])


    # Add an input field for the patient's email
    patient_email = st.text_input("Enter your email", "")
    patient_name = st.text_input("Enter your name", "")

    # Render TinyMCE editor using components.html
    st.components.v1.html("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <style>
    .button {
    background-color: #12a69c;
    border: none;
    color: white;
    padding: 10px 12px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 15px;
    margin: 4px 2px;
    border-radius: 12px;
    cursor: pointer;
    }
    </style>
    <script src="https://cdn.tiny.cloud/1/0jihkifpc837tensun96a5r8gkwpqi914vkk9f8in0gtxcve/tinymce/6/tinymce.min.js" referrerpolicy="origin"></script>
</head>
<body>
    <script>
        // Create a global variable to store the downloadFile function
        window.downloadFile = function() {
            let content = tinymce.get('myTextArea').getContent();
            var dict={}
            dict["item"]="message"
            dict["value"]=content
            localStorage.setItem('message', content); 
        };

        tinymce.init({
            selector: 'textarea',
            plugins: 'ai tinycomments mentions anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount checklist mediaembed casechange export formatpainter pageembed permanentpen footnotes advtemplate advtable advcode editimage tableofcontents mergetags powerpaste tinymcespellchecker autocorrect a11ychecker typography inlinecss',
            toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table mergetags | align lineheight | tinycomments | checklist numlist bullist indent outdent | emoticons charmap | removeformat',
            tinycomments_mode: 'embedded',
            tinycomments_author: 'Author name',
            mergetags_list: [
                { value: 'First.Name', title: 'First Name' },
                { value: 'Email', title: 'Email' },
            ],
            ai_request: (request, respondWith) => respondWith.string(() => Promise.reject("See docs to implement AI Assistant")),
        });
    </script>

    <form method="post" action="somepage">
        <textarea id="myTextArea" class="mceEditor">It is under development. It stores the message in local storage</textarea>
    </form>

    <button class="button" onclick="downloadFile()">Save Message</button>
</body>
</html>
    """, height=600)

    # Streamlit button to trigger Selenium script
    if st.button("Book Appointment"):
        if not patient_email or not patient_name:
            st.warning("Please enter both email and name.")
        else:   
            book_appointment(selected_doctor, patient_email, patient_name)


    for doctor in st.session_state.doctor:
        if doctor["name"] == selected_doctor:
            st.subheader(doctor["name"])
            st.write(f"Specialization: {doctor['specialization']}")
            st.write(f"Location: {doctor['location']}")
            st.write(f"Available Days: {doctor['available_days']}")
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
doctor()