import streamlit as st

# Title and introduction
st.set_page_config(page_title="Mary and John's Story", page_icon="📖")
st.title("Interactive Story - Mary and John")
st.write("Choose an action for Mary and see John's response.")

# Function to display John's response
def show_response(action):
    responses = {
        "Cook Dinner": "Mary cooks dinner for John... John eats and soon falls asleep without thanking her.",
        "Take Off John's Clothes": "Mary takes off John's clothes, hoping he notices her effort... John doesn't reciprocate, he just enjoys it and soon falls asleep.",
        "Apply Lipstick": "Mary applies lipstick to look good when John wakes up... When he wakes up, he doesn't notice, gets dressed, and leaves without saying 'good night'.",
        "End Story": "Regardless of the choices, Mary realizes that John will never change. She is trapped in a cycle of frustration and disillusionment."
    }
    st.write(responses[action])

# Buttons for Mary's choices
if st.button("Cook Dinner"):
    show_response("Cook Dinner")

if st.button("Take Off John's Clothes"):
    show_response("Take Off John's Clothes")

if st.button("Apply Lipstick"):
    show_response("Apply Lipstick")

if st.button("End Story"):
    show_response("End Story")
