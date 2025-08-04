def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))



class Event:
    def __init__(self, date, machine, type, user):
        self.date = date
        self.type = type
        self.machine = machine
        self.user = user

events = [
    Event("2023-07-12 08:23", "Printer-01", "Error", "alice"),
    Event("2023-07-13 09:00", "Server-22", "Login", "bob"),
    Event("2023-07-13 12:15", "Server-22", "Logout", "bob"),
    Event("2023-07-13 14:30", "Server-22", "Login", "bob"),
    Event("2023-07-13 18:45", "Server-22", "Logout", "bob"),
    Event("2023-07-14 11:00", "Router-A1", "Login", "charlie"),
    Event("2023-07-14 13:45", "Router-A1", "Logout", "charlie"),
    Event("2023-07-15 09:22", "Laptop-88", "Login", "diana"),
    Event("2023-07-16 02:30", "Database-X", "Logout", "eve"),
    Event("2023-07-17 17:00", "Monitor-Z9", "Login", "frank")
]


# Execution
users = current_users(events)
print(users)

print(generate_report(users))