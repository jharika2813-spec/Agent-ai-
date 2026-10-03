max_iter = 10
state = "start"

for iteration in range(1, max_iter + 1):
    print("Iteration:", iteration)

    # Your logic here
    success = False

    if success:
        state = "done"
        print("State:", state)
        break
else:
    state = "failure"
    print("State:", state)
    print("Maximum iterations exceeded.")