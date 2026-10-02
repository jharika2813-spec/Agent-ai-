def rule_based_agent(temperature, max_iters=10):
    for i in range(max_iters):
        if temperature > 100:
            return "cool"
        
        temperature += 1

    return "failure"


# Test
temperatures = [80, 100, 101, 120]

for temperature in temperatures:
    result = rule_based_agent(temperature, max_iters=10)
    print(f"Temperature: {temperature} -> Action: {result}")
    print("-" * 30)