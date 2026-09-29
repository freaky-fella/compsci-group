from collections import deque

queue = deque()
queue.append("Render Image")
queue.append("Save Image")
queue.append("Send Notification")
queue.append("Write Draft")
queue.append("Send Email")
queue.append("Load Application")
queue.append("Open File")
queue.append("Edit Image")
queue.append("Save Image As")
queue.append("Close Application")

queueDuplicate = queue
print('queue: ', queue)
print('queue duplicate: ', queueDuplicate)

current_job = queue.popleft()

print('queue: ', queue)
print('queue duplicate: ', queueDuplicate)

#To prevent shared change we can set the second collection to a duplicate of the first collection instead of to the exact same collection as seen below
queueDuplicateTwo = queue.copy()
print('queue: ', queue)
print('queue duplicate two: ', queueDuplicate)

current_job = queue.popleft()

print('queue: ', queue)
print('queue duplicate two: ', queueDuplicate)
