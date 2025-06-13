import streamlit as st
import random

st.title("Math challenge")


ss = st.session_state

if "num1" not in ss:
    ss.num1 = random.randint(1, 10)
    ss.num2 = random.randint(1, 10)
    ss.operators = random.choice(["+", "-", "*"])
    ss.answer = eval(f"{ss.num1} {ss.operators} {ss.num2}")
    ss.result = ""

st.write(f"Solve: **{ss.num1} {ss.operators} {ss.num2}**")


user_input = st.number_input("Your answer:", step=1, key="%d")


if st.button("Check"):
    if user_input == ss.answer:
        reactions = [
            "🔥 Great job!",
            "🌟 Correct!",
            "🎯 Nailed it!",
            "🧠 Big brain!",
            "🏆 Champion!",
        ]
        ss.result = random.choice(reactions)
        st.balloons()
        st.image(
            "https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUyMDQzZTc4NTM2cW1uanNlbWY2a2ZqdmZzd3ZrYXF3dzdyODA0ZGk2cSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/YRuFixSNWFVcXaxpmX/source.gif",
            width=300,
        )
    else:
        ss.result = "Naah bro, Try again"
        st.image(
            "https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif", width=300
        )
        st.snow()
st.write(ss.result)


if st.button("New Challenge"):
    ss.num1 = random.randint(1, 10)
    ss.num2 = random.randint(1, 10)
    ss.operators = random.choice(["+", "-", "*"])
    ss.answer = eval(f"{ss.num1} {ss.operators} {ss.num2}")
    ss.result = ""
    st.rerun()
