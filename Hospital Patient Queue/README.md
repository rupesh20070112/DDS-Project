# Hospital Patient Queue
## 📌 Overview

A command-line hospital queue management system to handle emergency and regular patients.
Built as a Data Structures project using priority queue for critical cases and normal queue for regular cases.
Supports patient entry/exit, priority-based treatment, and estimated wait time display for better management.

---
## 🛠 Features
---
- Add patients (emergency or regular)

- Serve next patient (priority for emergencies)

- Display current queue (emergency + regular)

- Show estimated wait time for a patient

- Priority handling for emergency cases
  
---

## 📂 Data Structures Used

- Priority Queue (heapq) → To manage emergency patients by priority

- Normal Queue (deque) → To handle regular patients in FIFO order

- Traversal & Time Calculation → To estimate patient wait times

---

## times

🚀 How to Run
```bash
# Clone repository
git clone https://github.com/your-username/hospital-patient-queue.git
cd hospital-patient-queue/src

# Run the program
python hospital_queue.py
