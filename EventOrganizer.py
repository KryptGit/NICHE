import streamlit as st
import json
import os

# Function to load events from a JSON file
def load_events(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Function to save events to a JSON file
def save_events(file_path, events):
    with open(file_path, 'w') as file:
        json.dump(events, file, indent=4)

# Path to the events.json file
events_file = 'events.json'

# Load existing events
events = load_events(events_file)

# Streamlit form
st.title("Event Organizer")

with st.form("event_form"):
    event_name = st.text_input("Event Name")
    event_date = st.date_input("Event Date")
    tags = st.text_input("Tags")
    tags_list = [tag.strip() for tag in tags.split(',')]
    location = st.text_input("Location")
    price = st.number_input("Price")
    details = st.text_area("Details")
    link = st.text_input("Link")
    submitted = st.form_submit_button("Add Event")

    if submitted:
        new_event = {
            "title": event_name,
            "date": event_date.strftime("%Y-%m-%d"),         
            "tags": tags_list,
            "location": location,
            "price": price,
            "details": details,
            "link": None
            
        }
        events.append(new_event)
        save_events(events_file, events)
        st.success("Event added successfully!")
