import streamlit as st
from Resources import Event, Listings
import json
# Create an instance of Listings to store all events
events_listings = Listings()

from streamlit_autorefresh import st_autorefresh
hide_streamlit_style = """
                <style>
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }

                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
# after it's been refreshed 100 times.
count = st_autorefresh(interval=200, limit=None, key="fizzbuzzcounter")

# Load the events from the JSON file
with open('events.json', 'r') as f:
    events_data = json.load(f)

# Create Event objects from the loaded data
event_1 = Event(**events_data[0])
event_2 = Event(**events_data[1])
event_3 = Event(**events_data[2])
event_4 = Event(**events_data[3])
# Add 16 more events similarly...




# Define the function to render event cards
def car_show_event_card(event):
    date = event.get_date()
    location = event.get_location()
    details = event.get_details()
    price = event.get_price()
    link = event.get_link()
    tags = event.get_tags()
    title = event.title
    # Retrieve the link from the event object
    # Card layout using HTML & inline CSS
    st.markdown(f"""
        <div style='
            border-radius: 12px;
            background-color: #222;
            color: #fff;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0px 8px 16px rgba(0,0,0,0.3);
            font-family: Arial, sans-serif;
            text-align: left;
            '>
            <div style='display: flex; align-items: center;'>
                <div style='width: 65%; padding-left: 20px;'>
                    <h2 style="color: #E3B130; margin-bottom: 10px;">{title}</h2>
                    <p style="color: #bbb; font-size: 16px; margin: 0;"><b>Date:</b> {date}</p>
                    <p style="color: #bbb; font-size: 16px; margin: 0;"><b>Location:</b> {location}</p>
                    <p style="color: #bbb; font-size: 16px; margin: 0;"><b>Price:</b> {price}</p>
                    <p style="color: #bbb; font-size: 16px; margin: 0;"><b>Tags:</b> {', '.join(map(str, tags))}</p>
                    <p style="color: #ddd; margin-top: 10px; font-size: 15px;">{details}</p>
                    <div style='margin-top: 20px;'>
                        <a href="{link}" style='
                            background-color: #E3B130;
                            color: #fff;
                            padding: 12px 20px;
                            text-decoration: none;
                            font-size: 14px;
                            font-weight: bold;
                            border-radius: 6px;
                            text-align: center;
                            display: inline-block;
                            '>RSVP Now</a>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Create a header for DFW Race Events
st.title("Upcoming Cultural Events in the DFW Area")

# Button to scroll to events
if st.button("See All Upcoming Events"):
    st.markdown("""<a href="#events-section" style='display:block; color: #E3B130; font-size: 18px;'>Scroll to Events</a>""", unsafe_allow_html=True)

st.markdown("<div id='events-section'></div>", unsafe_allow_html=True)


for event_data in events_data:
    event = Event(**event_data)
    events_listings.add_event(event)
# Add the remaining 16 events...
search = None
#add search bar with magnifying glass icon
col1, col2  = st.columns([3,0.2])
with col2:
    st.text("")
    st.text("")
    st.image("https://img.icons8.com/color/2x/search", width=30)
with col1:
    search = st.text_input("Search")


if search:
    # Display all events from the Listings object
    i = 0
    for event in events_listings.get_listings():
        if search.lower() in event.get_searchable_text().lower():
            i += 1
            car_show_event_card(event)
else:
# Display all events from the Listings object
    i = 0
    for event in events_listings.get_listings():
        i += 1
        car_show_event_card(event)