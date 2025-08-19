import heapq
from collections import deque

class HospitalQueue:
    def _init_(self, avg_time_per_patient=15):
        self.emergency_queue = []   # Min-heap for priority patients (priority, name)
        self.regular_queue = deque()  # FIFO queue for regular patients
        self.avg_time = avg_time_per_patient

    # Add patient
    def add_patient(self, name, category, priority=0):
        if category == "emergency":
            # Lower number = higher priority
            heapq.heappush(self.emergency_queue, (priority, name))
            print(f"🚨 Emergency patient '{name}' added with priority {priority}.")
        elif category == "regular":
            self.regular_queue.append(name)
            print(f"🧑 Regular patient '{name}' added to queue.")
        else:
            print("❌ Invalid category. Use 'emergency' or 'regular'.")

    # Serve next patient
    def serve_patient(self):
        if self.emergency_queue:
            priority, name = heapq.heappop(self.emergency_queue)
            print(f"✅ Serving EMERGENCY patient: {name} (Priority {priority})")
        elif self.regular_queue:
            name = self.regular_queue.popleft()
            print(f"✅ Serving REGULAR patient: {name}")
        else:
            print("🏥 No patients in queue.")

    # Display current queue
    def display_queue(self):
        print("\n📋 Current Queue Status:")
        if not self.emergency_queue and not self.regular_queue:
            print("No patients waiting.")
            return

        print("🚨 Emergency Queue:")
        for p, name in sorted(self.emergency_queue):
            print(f"   - {name} (Priority {p})")

        print("🧑 Regular Queue:")
        for name in self.regular_queue:
            print(f"   - {name}")

    # Estimated wait time
    def estimate_wait_time(self, patient_name):
        time = 0

        # Check in emergency queue
        for idx, (priority, name) in enumerate(sorted(self.emergency_queue)):
            if name == patient_name:
                time = idx * self.avg_time
                print(f"⏳ Estimated wait time for {name}: {time} minutes")
                return

        # Check in regular queue (after emergency patients)
        for idx, name in enumerate(self.regular_queue):
            if name == patient_name:
                time = (len(self.emergency_queue) + idx) * self.avg_time
                print(f"⏳ Estimated wait time for {name}: {time} minutes")
                return

        print(f"❌ Patient {patient_name} not found in queue.")


# ---------- Driver Code ----------
if _name_ == "_main_":
    hospital = HospitalQueue(avg_time_per_patient=10)  # Each patient = 10 mins

    while True:
        print("\n=== Hospital Patient Queue ===")
        print("1. Add Patient")
        print("2. Serve Next Patient")
        print("3. Display Queue")
        print("4. Estimate Wait Time")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter patient name: ")
            category = input("Enter category (emergency/regular): ").lower()
            if category == "emergency":
                priority = int(input("Enter priority (0 = highest, larger = lower): "))
                hospital.add_patient(name, category, priority)
            else:
                hospital.add_patient(name, category)
        elif choice == "2":
            hospital.serve_patient()
        elif choice == "3":
            hospital.display_queue()
        elif choice == "4":
            name = input("Enter patient name: ")
            hospital.estimate_wait_time(name)
        elif choice == "5":
            print("Exiting Hospital Queue System 👋")
            break
        else:
            print("❌ Invalid choice! Try again.")
