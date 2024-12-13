import requests
import streamlit as st
from streamlit_lottie import st_lottie


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie2 = load_lottieurl('https://lottie.host/99a86671-829e-4be9-88b7-0a8ee9dbb8d9/9zHVM4eGRE.json')

# ---- HEADER SECTION ----
with st.container():
    left_column,right_column = st.columns(2)
    with right_column:
        st_lottie(lottie2,height=200,key='coding1')
    with left_column:
        st.subheader("Hey, I am Shaswat :wave:")
        st.title("A Programmer from India")

# ---- Why i created this web ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('The reason behind this web. =>')
        st.write(
            """
            I made this website to provide people programming services like apps and website for an affording price.
            Despite the cheap pricing i will try my best to provide high quality services. Also the best part is that you can customize your apps and websites by yourself.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# # ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
    


with st.container():
    st.write('---')
    st.header('Get your own project done !')
    st.write('Just send a Hello/Hi/Hey message with a breif description of your app/website to my following Insta page ')
    st.write('[ShriJects](https://www.instagram.com/shrijects_96/)')
    st.write('Or')
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
