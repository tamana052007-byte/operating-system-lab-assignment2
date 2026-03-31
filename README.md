# 🏦 Banker's Algorithm – Deadlock Avoidance

## 👨‍💻 Student Details

* **Name:** Tamana
* **Roll No:** 2501720007
* **University:** KR Mangalam University
* **Program:** BSc (Hons) Computer Science
* **Course:** Operating System Fundamentals

---

## 📌 Overview

This project implements the **Banker’s Algorithm**, a deadlock avoidance technique in Operating Systems. It checks whether the system is in a **safe state** and finds a **safe sequence** of process execution.

---

## 🎯 Objectives

* Understand deadlock and resource allocation
* Implement Banker’s Algorithm using Python
* Determine safe and unsafe states
* Find safe execution sequence

---

## 🛠️ Technologies Used

* Python 3.x

---

## ⚙️ Working of Algorithm

### Step 1: Input

* Number of processes and resources
* Allocation Matrix
* Maximum Matrix
* Available Resources

### Step 2: Need Calculation

```
Need = Maximum - Allocation
```

### Step 3: Safety Check

* Initialize Work = Available
* Check if Need ≤ Work
* If yes → allocate resources
* Repeat until all processes complete

---

## ▶️ How to Run

```
python bankers_algorithm.py
```

---

## 📊 Output (From Program)

### Need Matrix:

```
P0: [122]
P1: [301]
P2: [-145]
```

### Result:

```
System is in SAFE state
Safe Sequence: P0 -> P1 -> P2
```

---

## 📈 Conclusion

The program successfully determines whether the system is safe.
It ensures deadlock avoidance by finding a safe execution sequence.

---
