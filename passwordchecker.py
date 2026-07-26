import streamlit as st
import re



st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Strength Checker")
st.write("Check whether your password is Strong or Weak.")



password = st.text_input(
    "Enter Password",
    type="password"
)



if st.button("Check Password"):

    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Minimum 8 characters required.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one Uppercase Letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one Lowercase Letter.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one Number.")

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one Special Character.")

    # First character should not be a digit
    if password and password[0].isdigit():
        feedback.append("Password should not start with a Number.")
        score = max(score - 1, 0)

   

    st.progress(score / 5)

  

    if score == 5 and not feedback:
        st.success("🟢 Strong Password")
        st.balloons()

    elif score >= 3:
        st.warning("🟠 Medium Password")

    else:
        st.error("🔴 Weak Password")

  

    if feedback:
        st.subheader("Suggestions")

        for item in feedback:
            st.write(f"• {item}")
