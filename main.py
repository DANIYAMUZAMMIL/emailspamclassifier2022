import pickle

import streamlit as st



import subprocess









model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))


def main():
    st.title("Email Spam Classification Application")
    st.write("Build with Streamlit & Python")
    activites = ["Classification", "About"]
    choices = st.sidebar.selectbox("Select Activities", activites)
    if choices == "Classification":
        st.subheader("Classification")
        msg = st.text_area("Enter a text")
        if st.button("Predict"):
            print(msg)
            print(type(msg))
            data = [msg]
            print(data)
            vec = cv.transform(data).toarray()
            result = model.predict(vec)
            if result[0] == 0:
                st.success("This is Not A Spam Email")

                subprocess.call(["say","this is not a spam mail"])
            else:

                st.error("This is A Spam Email")

                subprocess.call(["say", "this is a spam mail"])



main()
