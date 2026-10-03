def agent():
    step = 1

    while step <= 5:
        print(f"Step {step} completed")
        step += 1   # Fixed: increment step

    return {"status": "success", "steps": step - 1}


result = agent()
print(result)