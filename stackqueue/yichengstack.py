undo_history = []

undo_history.append("Type Title")
undo_history.append("Insert Image")
undo_history.append("Change Color")

print("Current Undo History Stack:", undo_history)
print("Top item (most recent action):", undo_history[-1])

undone_action = undo_history.pop()
print("\nPerformed Undo on:", undone_action)
print("Stack after Undo:", undo_history)

if not undo_history:
    print("\nStack is empty. Cannot pop.")
else:
    print("\nStack is not empty. Ready for next pop operation.")
    next_action = undo_history.pop()
    print("Popped next action:", next_action)