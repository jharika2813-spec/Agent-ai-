def agent():
    log = []

    for step in range(1, 6):
        message = f"Step {step} completed"
        log.append(message)

    return log


result = agent()

print("Full Log:")
for item in result:
    print(item)