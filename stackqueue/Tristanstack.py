# Declare and initialize the stack
undo_history = []

# Push items
undo_history.append("Type Title")
undo_history.append("Insert Image")
undo_history.append("Change Color")

# Display the stack and identify the top item
print("Stack:", undo_history)
print("Top Item:", undo_history[-1])

# Pop one action to simulate Undo
undo_history.pop()
print("After Undo:", undo_history)

# Check whether the stack is empty before another pop
if len(undo_history) > 0:
    undo_history.pop()
    print("After second pop:", undo_history)
else:
    print("Stack is empty!!")
