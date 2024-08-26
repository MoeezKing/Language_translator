from googletrans import Translator, LANGUAGES
import streamlit as st


def translate(text, lang):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    return translation.text


def get_languages():
    languages = [LANGUAGES[l] for l in LANGUAGES]
    return languages


st.image("translator.png")
st.title("Language translator by NexAI")
st.write("Write the text to be translate")
text = st.text_area("Write here ...")
lang = st.selectbox("Select langauge :", get_languages())

if st.button("Translate"):
    if text:
        translation = translate(text, lang)
        st.success("Translated")
        st.balloons()
        st.subheader("Translation is as following :")
        st.text(translation)

    else:
        st.warning("No text in box ")
