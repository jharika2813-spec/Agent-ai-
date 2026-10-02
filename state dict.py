def rule_based_agent(temperature, max_iters=10):
    state = {
        "done": False,
        "steps": 0
    }

    for i in range(max_iters):
        state["steps"] += 1

        if temperature > 100:
            state["done"] = True
            return "cool", state

        temperature += 1

    return "failure", state


# Test
temperatures = [80, 100, 101, 120]

for temperature in temperatures:
    result, state = rule_based_agent(temperature, max_iters=10)

    print(f"Temperature: {temperature}")
    print(f"Result: {result}")
    print(f"State: {state}")
    print("-" * 30)