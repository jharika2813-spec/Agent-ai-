max_iter = 10

state = {
    "done": False,
    "steps": 0,
    "status": "running"
}

for i in range(1, max_iter + 1):
    state["steps"] = i

    print(f"Step {i}")

    # Your task/logic
    success = False

    if success:
        state["done"] = True
        state["status"] = "success"
        break

if not state["done"]:
    state["status"] = "failure"

print("\nFinal State:")
print(state)