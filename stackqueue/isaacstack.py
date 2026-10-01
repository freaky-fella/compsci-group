undo_stack = []

# Push items in order
undo_stack.append("Type title")
undo_stack.append("Insert image")
undo_stack.append("Change color")

#Display stack and identify top item
print("Current Stack:", undo_stack)
print("Top Item:", undo_stack[-1])

# Pop one action (Undo)
undone_action = undo_stack.pop()
print("Undone Action:", undone_action)

# Check if empty before another pop
if undo_stack:
    next_undo = undo_stack.pop()
    print("Undone Action:", next_undo)
else:
    print("Stack is empty")

print("Remaining Stack", undo_stack)
