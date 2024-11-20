# Author: Nathan Asif | 2024F-BSE-278
print("----- Vacation Destination Suggestion -----")
valid_climate = ["tropical", "cold", "temperate"]
valid_preference = ["beach", "mountain", "city", "countryside", "historical sites"]

while True:
    climate = input("Enter a preferred climate (tropical/cold/temperate): ").lower()
    preference = input("Enter a vacation preference (beach/mountain/city/countryside/historical sites): ").lower()
    duration = input("Do you prefer a short (under a week), medium (a week to two weeks), or long (more than two weeks) vacation? ").lower()
    budget = input("Is your budget low, medium, or high? ").lower()
    companions = input("Are you traveling alone, with family, or with friends? ").lower()
    suggestion_found = False
    
    if climate in valid_climate and preference in valid_preference:
        # Tropical conditions
        if climate == "tropical":
            if preference == "beach":
                if duration == "long" and budget == "high" and companions == "family":
                    print("Consider visiting the Maldives for a luxurious beach vacation with your family!")
                    suggestion_found = True
                elif duration == "short" and budget == "medium" and companions == "alone":
                    print("A quick trip to Cancun might be perfect for a solo traveler!")
                    suggestion_found = True
            elif preference == "city":
                if duration == "medium" and budget == "medium" and companions == "friends":
                    print("Explore the vibrant city life of Singapore with your friends!")
                    suggestion_found = True
        
        # Cold conditions
        elif climate == "cold":
            if preference == "mountain":
                if duration == "long" and budget == "high" and companions == "family":
                    print("A family skiing trip to the Swiss Alps would be unforgettable!")
                    suggestion_found = True
                elif duration == "medium" and budget == "medium" and companions == "alone":
                    print("Consider a solitary retreat to Banff National Park in Canada.")
                    suggestion_found = True
            elif preference == "city":
                if duration == "short" and budget == "low" and companions == "friends":
                    print("A budget-friendly weekend in Prague during the winter is magical.")
                    suggestion_found = True
        
        # Temperate conditions
        elif climate == "temperate":
            if preference == "countryside":
                if duration == "medium" and budget == "medium" and companions == "family":
                    print("Enjoy the serene English countryside in the Cotswolds.")
                    suggestion_found = True
            elif preference == "historical sites":
                if duration == "long" and budget == "high" and companions == "alone":
                    print("Embark on a solo journey through the historical sites of Italy.")
                    suggestion_found = True

    if suggestion_found:
        break
    else:
        print("No matching destination suggestion found, please try again.")