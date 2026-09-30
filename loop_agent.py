# Observe -> Decide -> Act loop
# Weather temperature example

for i in range(3):
    print("\nIteration", i + 1)

    # OBSERVE
    temperature = float(input("Enter temperature in °C: "))
    print("Observed temperature:", temperature, "°C")

    # DECIDE
    if temperature > 35:
        decision = "Very Hot"
    elif temperature >= 25:
        decision = "Normal"
    else:
        decision = "Cold"

    print("Decision:", decision)

    # ACT
    if decision == "Very Hot":
        print("Action: Drink water and stay indoors.")
    elif decision == "Normal":
        print("Action: Normal outdoor activities are okay.")
    else:
        print("Action: Wear warm clothes.")