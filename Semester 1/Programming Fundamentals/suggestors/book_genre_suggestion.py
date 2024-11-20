# Author: Nathan Asif | 2024F-BSE-278
print("Book Genre Suggestion")
valid_age_group = ["adult", "teen", "child"]
valid_genre = ["fiction", "non-fiction", "mystery", "science fiction", "fantasy"]

while True:
    age_group = input("Who are you picking a book for—adults, teens, or children? ").lower()
    genre = input("What type of book are you in the mood for—fiction, non-fiction, mystery, science fiction, or fantasy? ").lower()
    reading_pace = input("How quickly do you want to read this book—fast, medium, or slow? ").lower()
    mood = input("What mood are you in today—happy, reflective, adventurous, or scared? ").lower()
    reading_environment = input("Where do you love to read—at home, outdoors, in bed, or maybe at a cafe? ").lower()
    suggestion_found = False

    if age_group in valid_age_group and genre in valid_genre:
        # Simplified and relatable suggestions
        if age_group == "adult" and genre == "fiction":
            if mood == "reflective" and reading_pace == "slow":
                print("‘The Alchemist’ by Paulo Coelho is a thoughtful read that’s perfect for some quiet time.")
                suggestion_found = True
            elif mood == "happy" and reading_pace == "fast":
                print("Check out ‘The Rosie Project’ by Graeme Simsion. It’s fun, quick, and will definitely lift your spirits!")
                suggestion_found = True

        elif age_group == "teen" and genre == "fantasy":
            if mood == "adventurous":
                print("‘Harry Potter and the Sorcerer's Stone’ by J.K. Rowling is a thrilling start to a magical journey.")
                suggestion_found = True
            elif mood == "scared":
                print("‘Coraline’ by Neil Gaiman is wonderfully spooky and just right for a little scare.")
                suggestion_found = True

        elif age_group == "child" and genre == "mystery":
            if reading_environment == "in bed":
                print("‘Nancy Drew: The Secret of the Old Clock’ by Carolyn Keene is great for bedtime mystery-solving.")
                suggestion_found = True
            elif reading_environment == "outdoors":
                print("‘The Secret Seven’ by Enid Blyton will make any day outside even more exciting!")
                suggestion_found = True

        elif age_group == "adult" and genre == "non-fiction":
            if mood == "reflective" and reading_pace == "medium":
                print("‘Quiet: The Power of Introverts in a World That Can't Stop Talking’ by Susan Cain is a must-read for insightful evenings.")
                suggestion_found = True
            elif mood == "happy" and reading_pace == "slow":
                print("‘Eat, Pray, Love’ by Elizabeth Gilbert is uplifting and perfect for a leisurely read.")
                suggestion_found = True

    if suggestion_found:
        break
    else:
        print("Let's see, it looks like we need a different combo. Don't worry, let's try again to find that perfect book!")