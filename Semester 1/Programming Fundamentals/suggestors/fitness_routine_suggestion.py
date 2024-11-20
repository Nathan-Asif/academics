# Author: Nathan Asif | 2024F-BSE-278
print("Fitness Routine Suggestion")
valid_intensity = ["low", "medium", "high"]
valid_preference = ["indoor", "outdoor"]

while True:
    intensity = input("How intense do you want your workout to be today? (low, medium, high) ").lower()
    preference = input("Do you feel like working out indoors or outdoors? ").lower()
    time_of_day = input("What time of day suits you best for a workout? (morning, afternoon, evening) ").lower()
    workout_length = input("How long do you want to exercise? (short: under 30 minutes, medium: 30-60 minutes, long: over an hour) ").lower()
    fitness_goal = input("What’s your main fitness goal? (weight loss, muscle gain, flexibility, endurance) ").lower()
    suggestion_found = False

    if intensity in valid_intensity and preference in valid_preference:
        # Generate suggestions based on the user's inputs
        if intensity == "low" and preference == "indoor":
            print("Yoga or some gentle stretching could be perfect for you, especially if you’re looking to relax and unwind indoors.")
            suggestion_found = True
        elif intensity == "medium" and preference == "outdoor":
            if time_of_day == "morning":
                print("A brisk morning walk or a medium-paced bike ride could be just the thing to start your day off right.")
                suggestion_found = True
            elif time_of_day == "evening":
                print("An evening jog or a session of outdoor calisthenics could be ideal to help you wind down.")
                suggestion_found = True
        elif intensity == "high" and preference == "indoor":
            if workout_length == "short":
                print("How about a high-intensity interval training (HIIT) session? It’s quick, sweaty, and super effective for fitness gains.")
                suggestion_found = True
            elif workout_length == "long":
                print("A longer session of mixed cardio and strength training could be great for endurance building.")
                suggestion_found = True
        elif intensity == "high" and preference == "outdoor":
            if fitness_goal == "endurance":
                print("Outdoor cycling or a long-distance run might be just what you need to boost your endurance.")
                suggestion_found = True
            elif fitness_goal == "weight loss":
                print("Try a boot camp-style workout in the park. It’s great for burning calories and building strength.")
                suggestion_found = True

    if suggestion_found:
        break
    else:
        print("Hmm, let's try some different options to find the perfect workout for you.")