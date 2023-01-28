from PIL import Image

import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="DG", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local Css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ----LOAD ASSETS----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_3sUZTc7VSz.json")
img_contact_form = Image.open("images/Assassins Creed Odyssey_contact_form.jpg")
img_lottie_animation = Image.open("images/Assassins Creed Odyssey_lottie_animation.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Priyanshu :wave:")
    st.title("world's best gamer")
    st.write("I Am passionate about playing different types of games")
    st.write("[Learnmore >](https://www.youtube.com/channel/UCD8pWrQ9PyNDKuFVrWpdgCA)")

# -----WHAT I DO-----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do ?")
        st.write("##")
        st.write("""Hello Guys My Name Is Priyanshu. I Am From India. My Passon Is Gaming I Upload Walkthrough Videos Of 
        Various Games On My Channel. So PLease Check Out The Channel For Amazing Gameplays And Walkthrough And Please
        Suggest Us Some Games You Want Me To Play""")

        st.write("[Youtube Channel >](https://www.youtube.com/channel/UCD8pWrQ9PyNDKuFVrWpdgCA)")


    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")




# ----PROJECTS----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Watch Gameplay Videos Of Your Favorate Game Series On Our Channel")
        st.write("Watch The Videos Of Assasins Creed Odyssey On Our Channel "
                 ". You Can Also Suggest The Game You Want Us to Play In Comments")
        st.markdown("[watch video...](https://www.youtube.com/watch?v=w7ObmcP56YU&t=0s)")

# ---CONTACT---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/piyupatelmr7@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your Email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()