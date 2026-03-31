# Banker's Algorithm Implementation

def calculate_need(maximum, allocation):
    n = len(maximum)
    m = len(maximum[0])
    need = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            need[i][j] = maximum[i][j] - allocation[i][j]
    
    return need


def is_safe(processes, available, maximum, allocation):
    n = len(processes)
    m = len(available)

    need = calculate_need(maximum, allocation)

    finish = [False] * n
    safe_sequence = []

    work = available.copy()

    while len(safe_sequence) < n:
        found = False

        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    
                    # Add allocated resources to work
                    for j in range(m):
                        work[j] += allocation[i][j]

                    safe_sequence.append(processes[i])
                    finish[i] = True
                    found = True

        if not found:
            return False, []

    return True, safe_sequence


# ------------------ INPUT SECTION ------------------

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

processes = [i for i in range(n)]

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    allocation.append(row)

print("\nEnter Maximum Matrix:")
maximum = []
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    maximum.append(row)

print("\nEnter Available Resources:")
available = list(map(int, input().split()))


# ------------------ NEED MATRIX ------------------

need = calculate_need(maximum, allocation)

print("\nNeed Matrix:")
for i in range(n):
    print(f"P{i}: {need[i]}")


# ------------------ SAFETY CHECK ------------------

safe, sequence = is_safe(processes, available, maximum, allocation)

if safe:
    print("\nSystem is in SAFE state")
    print("Safe Sequence:", " -> ".join([f"P{i}" for i in sequence]))
else:
    print("\nSystem is NOT in safe state (Deadlock possible)")