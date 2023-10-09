def badge_maker(name):
    return f"Hello, my name is {name}."
badge_maker("Guido")

def batch_badge_creator(names):
    lists = []
    for name in names:
        greeting =f"Hello, my name is {name}."
        lists.append(greeting)
    return lists
batch_badge_creator(["Sam", "Jane", "Sue"])

def assign_rooms(names):
    room_assignments = []  # Create an empty list to store room assignments

    for index, name in enumerate(names, start=1):
        # Use enumerate to get the index (room number) starting from 1
        assignment = f"Hello, {name}! You'll be assigned to room {index}!"
        room_assignments.append(assignment)  # Add the assignment to the list

    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    assignments = assign_rooms(names)
    for assignment in assignments:
        print(assignment)
    return(badges, assignments)

