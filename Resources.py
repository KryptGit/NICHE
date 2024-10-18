import re

# Define the Event class
class Event:
    def __init__(self, title, date, tags, location, price, details, link=None):
        self.date = date
        self.tags = tags
        self.location = location
        self.price = price
        self.details = details
        self.link = link
        self.title = title
    
    # Edit functions
    def set_date(self, date):
        self.date = date
    def set_tags(self, tags):
        self.tags = tags
    def set_location(self, location):
        self.location = location
    def set_price(self, price):
        self.price = price
    def set_details(self, details):
        self.details = details
    def set_link(self, link):
        self.link = link
    def set_title(self, title):
        self.title = title
    
    # Get functions
    def get_date(self):
        return self.date
    def get_tags(self):
        return self.tags
    def get_location(self):
        return self.location
    def get_price(self):
        return self.price
    def get_details(self):
        return self.details
    def get_link(self):
        return self.link
    def get_searchable_text(self):
        clean_details = re.sub(r'\d+', '', self.details)
        clean_location = re.sub(r'\d+', '', self.location)
        return f"{clean_location} {clean_details} {self.tags} {self.title}"


# Define the Listings class to hold multiple Event objects
class Listings:
    def __init__(self, listings=None):
        if listings is None:
            listings = []
        self.listings = listings
        self.length = len(listings)
    
    def add_event(self, event):
        self.listings.append(event)
        self.length += 1
    
    def remove_event(self, event):
        if event in self.listings:
            self.listings.remove(event)
            self.length -= 1
    
    def get_listings(self):
        return self.listings

    def get_event(self, index):
        if 0 <= index < self.length:
            return self.listings[index]
        else:
            return None