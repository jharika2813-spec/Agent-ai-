max_iter = 10
state = {
    "done": False,
    "steps": 0
}

for i in range(max_iter):
    state["steps"] += 1
    print("Step:", state["steps"])

state["done"] = False

if state["steps"] >= max_iter:
    print("State: failure")
else:
    print("State: success")