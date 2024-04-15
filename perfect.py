from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
load_dotenv()  ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro model and get reponses
model=genai.GenerativeModel("gemini-1.5-pro-latest")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input]+input_prompt+[Image.open(BytesIO(image))])
    else:
        response=model.generate_content(Image.open(BytesIO(image)))
    return response.text

# Navbar
st.set_page_config(
    page_title="AI UX Designer.",
    page_icon="🦄",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add the Title
st.markdown(
    "<h1 style='text-align: center; color: black;'>"
    "🚀 AI UXDesigner 🦄"
    "</h1>",
    unsafe_allow_html=True
)

# create a subheader
st.markdown('''
<style>
h3 {
    font-family: 'Open Sans', sans-serif;
    font-size: 16px;
    line-height: 24px;
    margin-top: 0;
    margin-bottom: 24px;
}
</style>
<style>
    h3 {
        text-align: center;
        color: black;
        margin-top: 0;
        margin-bottom: 24px;
    }
</style>
<h3>
    🎨🦄 AI-powered Web Design Generator 🎨🦄<br />
    <span style="font-weight: 300; font-style: italic;">Create your perfect web design, no limits!</span>
</h3>
''', unsafe_allow_html=True)

# Add the instructions how to use this tool
st.markdown('''
<style>
    p {
        text-align: center;
        font-weight: 300;
        color: black;
    }
</style>
<p>
    <h4>Instructions:</h4>
    Step 1: Enter a prompt in the input field below.<br />
    Step 2: Upload a sample design to help the ASSISTANT generate a more accurate web design.<br />
    Step 3: Click the "Submit" button to generate a web design for you!<br />
    <i>(Note: The ASSISTANT will generate a new web design based on the prompt.)</i>
</p>
''', unsafe_allow_html=True)

prompt = st.expander("1.Prompt for User:")
with prompt:
    st.write("""
    Here are the latest wireframes. Could you make a new website based on these wireframes
    """)
    
prompt = st.expander("2.Prompt for User:")
with prompt:
    st.write("""
    Here are the latest wireframes including some notes on your previous work. Could you make a new website based on these wireframes
    """) 
    
    st.write("""
        You are an expert web designer and developer, I would like to recreate the website design that I have provided in the attached image using HTML and CSS and needs to be responsive as well. You should not use the same content. Change the content that aligns to my brand.  Generate the unique and different from the upload and also change the color scheme. Generate the complete code including the html, CSS and JavaScript code separately. Give me code  html, CSS and JavaScript
    """) 

# Add the input prompt
input_text = st.text_area("Input Prompt: ", key="input")

# Add the upload button

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = uploaded_file.read()
else:
    image = None
    
# Prompt

input_prompt = [
   """
   You are an expert web developer who specializes in building working website prototypes from low-fidelity wireframes.
    Your job is to accept low-fidelity wireframes, then create a working prototype using HTML, CSS, and JavaScript, and finally send back the results.
    The results should be a single HTML file.
    Use tailwind to style the website.
    Put any additional CSS styles in a style tag and any JavaScript in a script tag.
    Use unpkg or skypack to import any required dependencies.
    Use Google fonts to pull in any open source fonts you require.
    If you have any images, load them from Unsplash or use solid colored rectangles.

    The wireframes may include flow charts, diagrams, labels, arrows, sticky notes, and other features that should inform your work.
    If there are screenshots or images, use them to inform the colors, fonts, and layout of your website.
    Use your best judgement to determine whether what you see should be part of the user interface, or else is just an annotation.

    Use what you know about applications and user experience to fill in any implicit business logic in the wireframes. Flesh it out, make it real!

    The user may also provide you with the html of a previous design that they want you to iterate from.
    In the wireframe, the previous design's html will appear as a white rectangle.
    Use their notes, together with the previous design, to inform your next result.

    Sometimes it's hard for you to read the writing in the wireframes.
    For this reason, all text from the wireframes will be provided to you as a list of strings, separated by newlines.
    Use the provided list of text from the wireframes as a reference if any text is hard to read.

    You love your designers and want them to be happy. Incorporating their feedback and notes and producing working websites makes them happy.
    
    For getting the Html file: You are an expert tailwind developer. A user will provide you with alow-fidelity wireframe of an application and you will return a single html file that uses tailwind to create the website. Use creative license to make the application more fleshed out.if you need to insert an image, use placehold.co to create a placeholder image. Respond only with the html file.
    
    
    """
]

# Submit button

submit_button = st.button("Submit")

## if submit is clicked

if submit_button:
    # Add the loader
    with st.spinner("Generating..."):
    # Get the response
        response = get_gemini_response(input_text, image)
        st.write(response)

#Add the clear button
clear_button = st.button("Clear")    


# Render profile footer in sidebar at the "bottom"
# Set a background image
def set_background_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/4097159/pexels-photo-4097159.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image()

# Set a background image for the sidebar
sidebar_background_image = '''
<style>
[data-testid="stSidebar"] {
    background-image: url("https://www.pexels.com/photo/abstract-background-with-green-smear-of-paint-6423446/");
    background-size: cover;
}
</style>
'''

st.sidebar.markdown(sidebar_background_image, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS to inject into the Streamlit app
footer_css = """
<style>
.footer {
    position: fixed;
    right: 0;
    bottom: 0;
    width: auto;
    background-color: transparent;
    color: black;
    text-align: right;
    padding-right: 10px;
}
</style>
"""


# HTML for the footer - replace your credit information here
footer_html = f"""
<div class="footer">
    <p style="font-size: 12px; font-style: italic; color: gray; margin-bottom: 0px; opacity: 0.7; line-height: 1.2; text-align: center;">
        <span style="display: block; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 8px; font-family: 'Open Sans', sans-serif;">Developed by::</span>
        <span style="font-size: 20px; font-weight: 800; text-transform: uppercase; font-family: 'Open Sans', sans-serif;">Farhan Akbar</span>
    </p>
    <a href="https://www.linkedin.com/in/farhan-akbar-ai/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a>
    <a href="https://api.whatsapp.com/send?phone=923114202358"><img src="https://img.shields.io/badge/WhatsApp-Chat%20Me-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"/></a>
    <a href="mailto:rasolehri@gmail.com"><img src="https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email" alt="Email"/></a>
</div>
"""

# Combine CSS and HTML for the footer
st.markdown(footer_css, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)    
    







# Prompt of user: 	'Here are the latest wireframes. Could you make a new website based on these wireframes and notes and send back just the html file?'

# Prompt for the previous response: 'Here are the latest wireframes including some notes on your previous work. Could you make a new website based on these wireframes and notes and send back just the html file?'

# For getting the Html file: You are an expert tailwind developer. A user will provide you with alow-fidelity wireframe of an application and you will return a single html file that uses tailwind to create the website. Use creative license to make the application more fleshed out.if you need to insert an image, use placehold.co to create a placeholder image. Respond only with the html file.

# Generate the unique and different from the upload and also change the color scheme. Generate the complete code including the html, CSS and JavaScript code separately. Give me code  html, CSS and JavaScript
