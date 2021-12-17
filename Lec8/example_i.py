# Решение задачи O
n_events = int(input().strip())
events = []

for _ in range(n_events):
    events.append(input().strip())

n_todo = int(input().strip())
for _ in range(n_todo):
    event_id = int(input().strip())
    print(events[event_id - 1])