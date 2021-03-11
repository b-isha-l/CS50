# class Point():
#     def __init__(self, inp1, inp2):
#         self.x = inp1
#         self.y = inp2

# p = Point(2, 6)
# print(p.x)
# print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people =["Isha", "Shiva", "Shakti", "Narayan"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seat for {person}")