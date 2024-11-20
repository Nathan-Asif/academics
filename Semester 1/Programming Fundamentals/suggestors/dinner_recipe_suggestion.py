# Author: Nathan Asif | 2024F-BSE-278
print("----- Dinner Recipe Suggestion -----")
valid_type = ["vegetarian", "meat", "vegan"]
valid_time = ["quick", "medium", "slow"]
valid_spice_level = ["mild", "medium", "spicy"]

while True:
    food_type = input("What type of dinner are you in the mood for today? (vegetarian/meat/vegan) ").lower()
    cooking_time = input("How much time do you want to spend cooking? (quick/medium/slow) ").lower()
    spice_level = input("How spicy do you like your food? (mild/medium/spicy) ").lower()
    cooking_skill = input("What's your cooking experience? (beginner/intermediate/advanced) ").lower()
    number_of_people = input("How many people are you cooking for? ").lower()
    suggestion_found = False

    if food_type in valid_type and cooking_time in valid_time and spice_level in valid_spice_level:
        # Suggestions for Pakistani dishes
        if food_type == "meat":
            if cooking_time == "quick" and spice_level == "medium":
                print("How about whipping up a quick Chicken Karahi? It's a vibrant Pakistani favorite that you can make in no time!")
                suggestion_found = True
            elif cooking_time == "medium" and spice_level == "spicy":
                print("Why not treat yourself to a flavorful Chicken Biryani? It's perfect for those who love a good spice kick.")
                suggestion_found = True
            elif cooking_time == "slow" and spice_level == "spicy":
                print("Nihari could be your go-to. It's slow-cooked and savory, ideal for those who love rich, deep flavors.")
                suggestion_found = True

        elif food_type == "vegetarian":
            if cooking_time == "quick" and spice_level == "mild":
                print("A quick Aloo ki Bhujia might be just what you need. It's simple, tasty, and comforting.")
                suggestion_found = True
            elif cooking_time == "medium" and spice_level == "medium":
                print("Chana Masala could be perfect tonight. It's hearty and packed with flavors that satisfy.")
                suggestion_found = True
            elif cooking_time == "slow" and spice_level == "spicy":
                print("Consider Baingan ka Bharta. It's a delicious, spicy mashed eggplant dish that's worth the wait.")
                suggestion_found = True

        elif food_type == "vegan":
            if cooking_time == "quick" and spice_level == "medium":
                print("Dal Tadka is quick, easy, and delightful. It's sure to please any vegan dinner table.")
                suggestion_found = True
            elif cooking_time == "medium" and spice_level == "spicy":
                print("A Sabzi Curry could be great. It's mixed vegetables cooked to spicy perfection.")
                suggestion_found = True
            elif cooking_time == "slow" and spice_level == "mild":
                print("Masoor Dal is a mild yet tasty choice that simmers slowly to develop its full flavor.")
                suggestion_found = True

    if suggestion_found:
        break
    else:
        print("It looks like we couldn't find a perfect recipe. Let's try again!")