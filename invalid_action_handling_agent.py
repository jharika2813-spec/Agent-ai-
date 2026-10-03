def agent(action):
    if action == "start":
        return {"status": "success", "message": "Agent started"}

    elif action == "stop":
        return {"status": "success", "message": "Agent stopped"}

    else:
        return {
            "status": "error",
            "message": "Invalid action",
            "action": action
        }


print(agent("start"))
print(agent("hello"))