# Smart Parking Lot Management using Linked List in Python

class Node:
    def _init_(self, car_number):
        self.car_number = car_number
        self.next = None


class ParkingLot:
    def _init_(self, capacity):
        self.capacity = capacity  # total slots
        self.size = 0             # current occupied slots
        self.head = None          # linked list head

    # Park a car (entry)
    def park_car(self, car_number):
        if self.size >= self.capacity:
            print(f"🚫 Parking Lot Full! Cannot park car {car_number}.")
            return

        new_node = Node(car_number)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        self.size += 1
        print(f"✅ Car {car_number} parked successfully.")

    # Remove a car (exit)
    def remove_car(self, car_number):
        if not self.head:
            print("🚫 Parking Lot is empty.")
            return

        temp = self.head
        prev = None

        while temp and temp.car_number != car_number:
            prev = temp
            temp = temp.next

        if not temp:
            print(f"🚗 Car {car_number} not found in parking lot.")
            return

        if prev:
            prev.next = temp.next
        else:
            self.head = temp.next

        self.size -= 1
        print(f"✅ Car {car_number} has exited the parking lot.")

    # Display parked cars
    def display_parking(self):
        if not self.head:
            print("🅿 Parking Lot is empty.")
            return

        print(f"\n📋 Cars currently parked ({self.size}/{self.capacity}):")
        temp = self.head
        while temp:
            print(f" - {temp.car_number}")
            temp = temp.next


# Driver code (menu-driven)
if _name_ == "_main_":
    capacity = int(input("Enter parking lot capacity: "))
    lot = ParkingLot(capacity)

    while True:
        print("\n=== Smart Parking Lot Menu ===")
        print("1. Park a Car")
        print("2. Remove a Car")
        print("3. Display Parked Cars")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            car_num = input("Enter car number: ")
            lot.park_car(car_num)
        elif choice == "2":
            car_num = input("Enter car number to remove: ")
            lot.remove_car(car_num)
        elif choice == "3":
            lot.display_parking()
        elif choice == "4":
            print("Exiting Smart Parking Lot system. 👋")
            break
        else:
            print("❌ Invalid choice! Please try again.")
