weather_condition = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather_condition == "sunny":
    message = "Wear a t-shirt and sunglasses"
elif weather_condition == "rainy":
    message = "Don't forget your umbrella and a raincoat."
elif weather_condition == "cold":
    message = "Make sure to wear a warm coat and a scarf."
else:
    message = "Sorry, I don't have recommendations for this weather."

print(message)