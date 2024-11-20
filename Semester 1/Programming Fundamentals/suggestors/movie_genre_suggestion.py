# Author: Nathan Asif | 2024F-BSE-278
print("----- Movie Genre Suggestion -----")
valid_time = ["short", "medium", "long"]
valid_mood = ["happy", "sad", "adventurous", "romantic", "thriller"]
valid_genre = ["action", "comedy", "drama", "fantasy", "horror"]

while True:
    time = input("Do you prefer a short, medium, or long movie? ").lower()
    mood = input("What is your mood today? (happy/sad/adventurous/romantic/thriller) ").lower()
    age_group = input("Is the movie for adults, teens, or children? ").lower()
    genre_preference = input("Do you like action, comedy, drama, fantasy, or horror? ").lower()
    watching_alone = input("Will you be watching alone or with someone? ").lower()
    suggestion_made = False

    if time in valid_time and mood in valid_mood and genre_preference in valid_genre:
        if time == "short" and mood == "happy" and genre_preference == "comedy":
            print("You might enjoy a short comedy like 'Rush Hour'.")
            suggestion_made = True
        elif time == "medium" and mood == "sad" and genre_preference == "drama":
            print("A medium-length drama like 'Manchester by the Sea' could be what you need.")
            suggestion_made = True
        elif time == "long" and mood == "adventurous" and genre_preference == "fantasy":
            print("Settle in for a long fantasy adventure with 'The Lord of the Rings: The Return of the King'.")
            suggestion_made = True
        elif time == "medium" and mood == "romantic" and genre_preference == "romantic":
            print("Enjoy a romantic evening with 'The Notebook'.")
            suggestion_made = True
        elif time == "short" and mood == "thriller" and genre_preference == "thriller" and watching_alone == "alone":
            print("A short thriller like 'Get Out' might be perfect for a solo viewing.")
            suggestion_made = True

    if suggestion_made:
        break
    else:
        print("No matching movie suggestion found, please try again.")