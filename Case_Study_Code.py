# Campus Resource Management System 
"""
Campus Resource Management System (Syllabus + Minimal Imports)
- Imports: os, sys, time, math
- Covers: algorithms, recursion, searching/sorting, data abstraction, files, debugging, tracing
- Length: ~280+ lines
"""

import os      # file existence and path handling
import sys     # recursion limit adjustments
import time    # performance tracing
import math    # factorial comparison

# -------------------------------
# Global state
# -------------------------------

STUDENTS = []  # list of dicts: {name, roll, dept, year}
DEPT_GRAPH = {
    "CSE": ["AIML", "CYS", "ECE"],
    "ECE": ["EEE", "MECH"],
    "EEE": ["CSE"],
    "MECH": ["CIVIL"],
    "CIVIL": [],
    "AIML": [],
    "CYS": []
}
VALID_DEPTS = set(DEPT_GRAPH.keys())
DATA_FILE = "students_data.txt"

# -------------------------------
# Member 1: Validation & core flow
# -------------------------------

def normalize_roll(roll):
    """Normalize roll number to uppercase and strip spaces."""
    return roll.strip().upper()

def sanitize_text(s):
    """Sanitize text to alphanumeric + space/dash/underscore."""
    return "".join(ch for ch in s if ch.isalnum() or ch in (" ", "-", "_")).strip()

def validate_student(name, roll, dept, year):
    """Validate student fields."""
    if not name or not roll or not dept or not year:
        return "All fields required."
    if not year.isdigit():
        return "Year must be numeric."
    yr = int(year)
    if yr < 1 or yr > 5:
        return "Year must be between 1 and 5."
    if dept not in VALID_DEPTS:
        return "Unknown department. Valid: " + ", ".join(sorted(list(VALID_DEPTS)))
    if len(roll) < 6:
        return "Roll must be at least 6 characters."
    # roll should contain at least one digit
    has_digit = False
    for ch in roll:
        if ch.isdigit():
            has_digit = True
            break
    if not has_digit:
        return "Roll must contain digits."
    return None

def display_menu():
    """Display main menu."""
    print("\n===== Campus Resource Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student (linear/binary)")
    print("4. Sort Students (insertion/merge/bubble)")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Summaries")
    print("8. Recursion & Iterative Demos")
    print("9. Save / Load")
    print("10. Tracing & Performance Demo")
    print("11. Recursion Limit Demo")
    print("12. Exit")

# -------------------------------
# Member 2: Data abstraction & summaries
# -------------------------------

def student_summaries(records):
    """Build summaries using sets, dicts, tuples."""
    dept_set = set()
    year_count = {}
    per_dept = {}
    for s in records:
        dept_set.add(s["dept"])
        year_count[s["year"]] = year_count.get(s["year"], 0) + 1
        per_dept.setdefault(s["dept"], []).append(s["name"])
    return {
        "total": len(records),
        "unique_departments": dept_set,
        "year_count": year_count,
        "per_dept": per_dept,
        "summary_tuple": (len(records), len(dept_set))
    }

def print_summaries(summary):
    """Print summaries in readable format."""
    print("\n--- Summaries ---")
    print("Total:", summary["total"])
    print("Unique departments:", summary["unique_departments"])
    print("Year-wise count:", summary["year_count"])
    print("Students per dept:", summary["per_dept"])
    print("Tuple (Total, UniqueDeptCount):", summary["summary_tuple"])

# -------------------------------
# Member 3: Algorithms (search/sort; recursion + iterative)
# -------------------------------

def linear_search(records, roll):
    """Linear search for roll."""
    roll = normalize_roll(roll)
    for s in records:
        if s["roll"] == roll:
            return s
    return None

def bubble_sort(records, key):
    """Bubble sort in-place."""
    n = len(records)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if compare_key(records[j], records[j + 1], key) > 0:
                records[j], records[j + 1] = records[j + 1], records[j]
                swapped = True
        if not swapped:
            break

def insertion_sort(records, key):
    """Insertion sort in-place."""
    for i in range(1, len(records)):
        key_item = records[i]
        j = i - 1
        while j >= 0 and compare_key(records[j], key_item, key) > 0:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key_item

def merge_sort(records, key):
    """Merge sort returning new list."""
    if len(records) <= 1:
        return records[:]
    mid = len(records) // 2
    left = merge_sort(records[:mid], key)
    right = merge_sort(records[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    """Merge helper for merge_sort."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if compare_key(left[i], right[j], key) <= 0:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

def compare_key(a, b, key):
    """Compare records by key, numeric compare for 'year'."""
    if key == "year":
        return int(a["year"]) - int(b["year"])
    else:
        if a[key] < b[key]:
            return -1
        elif a[key] > b[key]:
            return 1
        return 0

def binary_search(sorted_records, roll):
    """Binary search for roll in sorted list (sorted by roll)."""
    roll = normalize_roll(roll)
    low, high = 0, len(sorted_records) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_roll = sorted_records[mid]["roll"]
        if mid_roll == roll:
            return sorted_records[mid]
        elif mid_roll < roll:
            low = mid + 1
        else:
            high = mid - 1
    return None

def factorial_recursive(n):
    """Recursive factorial."""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Iterative factorial."""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def dfs_recursive(graph, start, target, visited):
    """Recursive DFS path."""
    if start not in graph or target not in graph:
        return None
    if start == target:
        return [start]
    visited.add(start)
    neighbors = graph.get(start, [])
    idx = 0
    while idx < len(neighbors):
        neighbor = neighbors[idx]
        if neighbor not in visited:
            path = dfs_recursive(graph, neighbor, target, visited)
            if path:
                return [start] + path
        idx += 1
    return None

def dfs_iterative(graph, start, target):
    """Iterative DFS path."""
    if start not in graph or target not in graph:
        return None
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node == target:
            return path
        if node not in visited:
            visited.add(node)
            neighbors = graph.get(node, [])
            idx = 0
            while idx < len(neighbors):
                neighbor = neighbors[idx]
                stack.append((neighbor, path + [neighbor]))
                idx += 1
    return None

# -------------------------------
# Member 4: Files & manual parsing
# -------------------------------

def save_to_file(filename=DATA_FILE):
    """Save students to text file."""
    try:
        f = open(filename, "w", encoding="utf-8")
        i = 0
        while i < len(STUDENTS):
            s = STUDENTS[i]
            name = sanitize_text(s["name"])
            roll = sanitize_text(s["roll"])
            dept = sanitize_text(s["dept"])
            year = sanitize_text(s["year"])
            f.write(name + "," + roll + "," + dept + "," + year + "\n")
            i += 1
        f.close()
        print("Saved", len(STUDENTS), "records.")
    except Exception as e:
        print("Save error:", e)

def load_from_file(filename=DATA_FILE):
    """Load students from text file (manual parsing)."""
    try:
        # Check existence with os
        if not os.path.exists(filename):
            print("No file found. Creating empty file.")
            f = open(filename, "w", encoding="utf-8"); f.close()
            return
        f = open(filename, "r", encoding="utf-8")
        count = 0
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = split_csv_line(line)
            if parts is None or len(parts) != 4:
                continue
            name, roll, dept, year = parts
            roll_norm = normalize_roll(roll)
            dept_up = dept.upper()
            err = validate_student(name, roll_norm, dept_up, year)
            if err is not None:
                continue
            # Dedup by roll
            if find_in_memory_by_roll(roll_norm) is not None:
                continue
            STUDENTS.append({"name": name, "roll": roll_norm, "dept": dept_up, "year": year})
            count += 1
        f.close()
        print("Loaded", count, "records.")
    except Exception as e:
        print("Load error:", e)

def split_csv_line(line):
    """Manual split for CSV-like lines with no quoting."""
    parts = []
    cur = ""
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == ",":
            parts.append(cur)
            cur = ""
        else:
            cur += ch
        i += 1
    parts.append(cur)
    if len(parts) != 4:
        return None
    return parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip()

def find_in_memory_by_roll(roll):
    """Find student in memory by roll."""
    i = 0
    while i < len(STUDENTS):
        if STUDENTS[i]["roll"] == roll:
            return STUDENTS[i]
        i += 1
    return None

# -------------------------------
# Member 5: Tracing & performance
# -------------------------------

def trace_add_two_numbers(a, b):
    """Tracing demo."""
    print("[TRACE] a =", a, "b =", b)
    result = a + b
    print("[TRACE] result =", result)
    return result

def performance_compare_sort(records):
    """Compare sorting performance using time module."""
    # Use merge_sort vs Python's built-in sorted for demonstration
    t0 = time.perf_counter()
    ms_sorted = merge_sort(records, "roll")
    t1 = time.perf_counter()
    py_sorted = sorted(records, key=lambda r: r["roll"])
    t2 = time.perf_counter()
    print("merge_sort time:", round((t1 - t0) * 1000, 3), "ms")
    print("sorted() time:", round((t2 - t1) * 1000, 3), "ms")
    # Show first three for visual
    print("Top 3 merge_sort:", [(r["roll"], r["name"]) for r in ms_sorted[:3]])
    print("Top 3 sorted():", [(r["roll"], r["name"]) for r in py_sorted[:3]])

def recursion_limit_demo():
    """Show and adjust recursion limit using sys."""
    print("Current recursion limit:", sys.getrecursionlimit())
    # Carefully increase for demo; restore at end
    sys.setrecursionlimit(2000)
    print("New recursion limit set to 2000")

def factorial_math_demo(n):
    """Use math library factorial for comparison."""
    try:
        print("math.factorial(", n, ") =", math.factorial(n))
    except Exception as e:
        print("math.factorial error:", e)

# -------------------------------
# CRUD flows
# -------------------------------

def add_student_flow():
    """Add student with validation and dedup."""
    print("\n--- Add Student ---")
    name = sanitize_text(input("Name: "))
    roll = normalize_roll(input("Roll: "))
    dept = sanitize_text(input("Department " + str(sorted(list(VALID_DEPTS))) + ": ")).upper()
    year = input("Year (1-5): ").strip()
    err = validate_student(name, roll, dept, year)
    if err is not None:
        print("Validation error:", err)
        return
    if find_in_memory_by_roll(roll) is not None:
        print("Duplicate roll. Not added.")
        return
    STUDENTS.append({"name": name, "roll": roll, "dept": dept, "year": year})
    print("Student added.")

def view_students_flow():
    """View students sorted by roll."""
    print("\n--- Students ---")
    if len(STUDENTS) == 0:
        print("No records.")
        return
    sorted_records = merge_sort(STUDENTS, "roll")
    i = 0
    while i < len(sorted_records):
        s = sorted_records[i]
        print(str(i + 1) + ". " + s["name"] + " | " + s["roll"] + " | " + s["dept"] + " | Year " + s["year"])
        i += 1

def search_student_flow():
    """Search student by roll using linear or binary search."""
    print("\n--- Search Student ---")
    if len(STUDENTS) == 0:
        print("No records to search.")
        return
    roll = normalize_roll(input("Enter roll: "))
    method = input("Method (linear/binary): ").strip().lower()
    if method == "linear":
        result = linear_search(STUDENTS, roll)
        print("Found:" if result is not None else "Not found.", result)
    elif method == "binary":
        sorted_records = merge_sort(STUDENTS, "roll")
        result = binary_search(sorted_records, roll)
        print("Found:" if result is not None else "Not found.", result)
    else:
        print("Unknown method.")

def sort_students_flow():
    """Sort students by chosen key and algorithm."""
    print("\n--- Sort Students ---")
    if len(STUDENTS) == 0:
        print("No records.")
        return
    key = input("Key (roll/name/year): ").strip().lower()
    if key not in ("roll", "name", "year"):
        print("Invalid key. Using 'roll'.")
        key = "roll"
    algo = input("Algorithm (insertion/merge/bubble): ").strip().lower()
    if algo == "insertion":
        copy = STUDENTS[:]
        insertion_sort(copy, key)
        print_sorted(copy)
    elif algo == "merge":
        sorted_records = merge_sort(STUDENTS, key)
        print_sorted(sorted_records)
    elif algo == "bubble":
        copy = STUDENTS[:]
        bubble_sort(copy, key)
        print_sorted(copy)
    else:
        print("Unknown algorithm.")

def print_sorted(records):
    """Print sorted records."""
    i = 0
    while i < len(records):
        s = records[i]
        print(str(i + 1) + ". " + s["name"] + " | " + s["roll"] + " | " + s["dept"] + " | Year " + s["year"])
        i += 1

def update_student_flow():
    """Update student fields with validation."""
    print("\n--- Update Student ---")
    roll = normalize_roll(input("Existing roll: "))
    existing = find_in_memory_by_roll(roll)
    if existing is None:
        print("No such roll.")
        return
    print("Current:", existing)
    name = sanitize_text(input("New name (blank to keep): "))
    dept = sanitize_text(input("New dept (blank to keep): ")).upper()
    year = input("New year (1-5, blank to keep): ").strip()

    name = existing["name"] if name == "" else name
    dept = existing["dept"] if dept == "" else dept
    year = existing["year"] if year == "" else year

    err = validate_student(name, roll, dept, year)
    if err is not None:
        print("Validation error:", err)
        return

    # Update in place
    i = 0
    while i < len(STUDENTS):
        if STUDENTS[i]["roll"] == roll:
            STUDENTS[i]["name"] = name
            STUDENTS[i]["dept"] = dept
            STUDENTS[i]["year"] = year
            print("Updated.")
            return
        i += 1

def delete_student_flow():
    """Delete student by roll."""
    print("\n--- Delete Student ---")
    roll = normalize_roll(input("Roll to delete: "))
    i = 0
    while i < len(STUDENTS):
        if STUDENTS[i]["roll"] == roll:
            STUDENTS.pop(i)
            print("Deleted.")
            return
        i += 1
    print("No such roll.")

# -------------------------------
# Recursion & iterative demos, save/load, tracing
# -------------------------------

def recursion_iterative_demos_flow():
    """Run recursion vs iterative demos."""
    print("\n--- Recursion & Iterative Demos ---")
    try:
        n = int(input("Enter non-negative integer for factorial: ").strip())
        print("factorial_recursive(", n, ") =", factorial_recursive(n))
        print("factorial_iterative(", n, ") =", factorial_iterative(n))
        factorial_math_demo(n)
    except Exception as e:
        print("Factorial error:", e)

    start = sanitize_text(input("DFS start dept: ")).upper()
    target = sanitize_text(input("DFS target dept: ")).upper()
    path_r = dfs_recursive(DEPT_GRAPH, start, target, set())
    path_i = dfs_iterative(DEPT_GRAPH, start, target)
    print("DFS recursive path:", path_r)
    print("DFS iterative path:", path_i)

def save_load_flow():
    """Choose to save or load data."""
    print("\n--- Save / Load ---")
    opt = input("Choose (save/load): ").strip().lower()
    if opt == "save":
        save_to_file(DATA_FILE)
    elif opt == "load":
        load_from_file(DATA_FILE)
    else:
        print("Unknown option.")

def tracing_performance_flow():
    """Run tracing and performance comparisons."""
    print("\n--- Tracing & Performance Demo ---")
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        res = trace_add_two_numbers(a, b)
        print("Trace result:", res)
    except Exception as e:
        print("Trace error:", e)
    performance_compare_sort(STUDENTS)

def recursion_limit_flow():
    """Show and adjust recursion limit."""
    recursion_limit_demo()

# -------------------------------
# Main loop
# -------------------------------

def seed_demo_data():
    """Seed initial demo data for presentations."""
    STUDENTS.append({"name": "Keerthi", "roll": normalize_roll("21CSE001"), "dept": "CSE", "year": "3"})
    STUDENTS.append({"name": "Rahul", "roll": normalize_roll("21ECE105"), "dept": "ECE", "year": "2"})
    STUDENTS.append({"name": "Divya", "roll": normalize_roll("21EEE210"), "dept": "EEE", "year": "4"})
    STUDENTS.append({"name": "Akhil", "roll": normalize_roll("21CSE155"), "dept": "CSE", "year": "2"})
    STUDENTS.append({"name": "Meera", "roll": normalize_roll("21MECH021"), "dept": "MECH", "year": "3"})

def main():
    if len(STUDENTS) == 0:
        seed_demo_data()

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_student_flow()
        elif choice == "2":
            view_students_flow()
        elif choice == "3":
            search_student_flow()
        elif choice == "4":
            sort_students_flow()
        elif choice == "5":
            update_student_flow()
        elif choice == "6":
            delete_student_flow()
        elif choice == "7":
            summary = student_summaries(STUDENTS)
            print_summaries(summary)
        elif choice == "8":
            recursion_iterative_demos_flow()
        elif choice == "9":
            save_load_flow()
        elif choice == "10":
            tracing_performance_flow()
        elif choice == "11":
            recursion_limit_flow()
        elif choice == "12":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

"""
Campus Resource Management System (Syllabus + Minimal Imports)
- Imports: os, sys, time, math
- Covers: algorithms, recursion, searching/sorting, data abstraction, files, debugging, tracing
- Length: ~280+ lines
"""

import os      # Person 4: File handling (save/load student records)
import sys     # Person 4: Recursion limit demo
import time    # Person 4: Performance tracing
import math    # Person 3: Factorial comparison

# -------------------------------
# Global state
# -------------------------------
STUDENTS = []  # list of dicts: {name, roll, dept, year}
DEPT_GRAPH = { # Person 3: Graph for DFS recursion demo
    "CSE": ["AIML", "CYS", "ECE"],
    "ECE": ["EEE", "MECH"],
    "EEE": ["CSE"],
    "MECH": ["CIVIL"],
    "CIVIL": [],
    "AIML": [],
    "CYS": []
}
VALID_DEPTS = set(DEPT_GRAPH.keys())
DATA_FILE = "students_data.txt"

# -------------------------------
# Person 1: Validation & Core Flow
# -------------------------------

def normalize_roll(roll):
    """Normalize roll number to uppercase and strip spaces."""
    return roll.strip().upper()

def sanitize_text(s):
    """Sanitize text to alphanumeric + space/dash/underscore."""
    return "".join(ch for ch in s if ch.isalnum() or ch in (" ", "-", "_")).strip()

def validate_student(name, roll, dept, year):
    """Validate student fields (sequence, selection, repetition)."""
    if not name or not roll or not dept or not year:
        return "All fields required."
    if not year.isdigit():
        return "Year must be numeric."
    yr = int(year)
    if yr < 1 or yr > 5:
        return "Year must be between 1 and 5."
    if dept not in VALID_DEPTS:
        return "Unknown department."
    if len(roll) < 6:
        return "Roll must be at least 6 characters."
    # ensure at least one digit in roll
    has_digit = False
    for ch in roll:
        if ch.isdigit():
            has_digit = True
            break
    if not has_digit:
        return "Roll must contain digits."
    return None

def display_menu():
    """Menu-driven program (algorithm design)."""
    print("\n===== Campus Resource Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student (linear/binary)")
    print("4. Sort Students (insertion/merge/bubble)")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Summaries")
    print("8. Recursion & Iterative Demos")
    print("9. Save / Load")
    print("10. Tracing & Performance Demo")
    print("11. Recursion Limit Demo")
    print("12. Exit")

# -------------------------------
# Person 2: Data Abstraction & Summaries
# -------------------------------

def student_summaries(records):
    """Use sets, dicts, tuples to summarize data."""
    dept_set = set()
    year_count = {}
    per_dept = {}
    for s in records:
        dept_set.add(s["dept"])
        year_count[s["year"]] = year_count.get(s["year"], 0) + 1
        per_dept.setdefault(s["dept"], []).append(s["name"])
    return {
        "total": len(records),
        "unique_departments": dept_set,
        "year_count": year_count,
        "per_dept": per_dept,
        "summary_tuple": (len(records), len(dept_set))
    }

def print_summaries(summary):
    """Print summaries clearly for presentation."""
    print("\n--- Summaries ---")
    print("Total:", summary["total"])
    print("Unique departments:", summary["unique_departments"])
    print("Year-wise count:", summary["year_count"])
    print("Students per dept:", summary["per_dept"])
    print("Tuple (Total, UniqueDeptCount):", summary["summary_tuple"])

# -------------------------------
# Person 3: Algorithms (Search, Sort, Recursion)
# -------------------------------

def linear_search(records, roll):
    """Linear search (O(n))."""
    roll = normalize_roll(roll)
    for s in records:
        if s["roll"] == roll:
            return s
    return None

def compare_key(a, b, key):
    """Compare by key; numeric compare for 'year'."""
    if key == "year":
        return int(a["year"]) - int(b["year"])
    # string comparison for roll/name/dept
    if a[key] < b[key]:
        return -1
    elif a[key] > b[key]:
        return 1
    return 0

def bubble_sort(records, key):
    """Bubble sort (O(n^2))."""
    n = len(records)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if compare_key(records[j], records[j + 1], key) > 0:
                records[j], records[j + 1] = records[j + 1], records[j]
                swapped = True
        if not swapped:
            break

def insertion_sort(records, key):
    """Insertion sort (O(n^2), good for small/nearly sorted data)."""
    for i in range(1, len(records)):
        key_item = records[i]
        j = i - 1
        while j >= 0 and compare_key(records[j], key_item, key) > 0:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key_item

def merge_sort(records, key):
    """Merge sort (O(n log n))."""
    if len(records) <= 1:
        return records[:]
    mid = len(records) // 2
    left = merge_sort(records[:mid], key)
    right = merge_sort(records[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    """Merge helper for merge_sort."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if compare_key(left[i], right[j], key) <= 0:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

def binary_search(sorted_records, roll):
    """Binary search (O(log n)) for roll on a list sorted by roll."""
    roll = normalize_roll(roll)
    low, high = 0, len(sorted_records) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_roll = sorted_records[mid]["roll"]
        if mid_roll == roll:
            return sorted_records[mid]
        elif mid_roll < roll:
            low = mid + 1
        else:
            high = mid - 1
    return None

def factorial_recursive(n):
    """Recursive factorial (O(n), stack depth)."""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Iterative factorial (O(n), safe)."""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def dfs_recursive(graph, start, target, visited):
    """Recursive DFS pathfinding."""
    if start not in graph or target not in graph:
        return None
    if start == target:
        return [start]
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs_recursive(graph, neighbor, target, visited)
            if path:
                return [start] + path
    return None

def dfs_iterative(graph, start, target):
    """Iterative DFS pathfinding."""
    if start not in graph or target not in graph:
        return None
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node == target:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                stack.append((neighbor, path + [neighbor]))
    return None

# -------------------------------
# Person 4: Files, Tracing & Performance
# -------------------------------

def save_to_file(filename=DATA_FILE):
    """Save students to text file (file I/O)."""
    with open(filename, "w", encoding="utf-8") as f:
        for s in STUDENTS:
            f.write(f"{s['name']},{s['roll']},{s['dept']},{s['year']}\n")
    print("Saved", len(STUDENTS), "records.")

def load_from_file(filename=DATA_FILE):
    """Load students from text file (file I/O)."""
    if not os.path.exists(filename):
        print("No file found.")
        return
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            name, roll, dept, year = parts
            # avoid duplicates by roll
            exists = False
            for s in STUDENTS:
                if s["roll"] == normalize_roll(roll):
                    exists = True
                    break
            if exists:
                continue
            STUDENTS.append({
                "name": name,
                "roll": normalize_roll(roll),
                "dept": dept.upper(),
                "year": year
            })
    print("Loaded", len(STUDENTS), "records.")

def trace_add_two_numbers(a, b):
    """Tracing demo (debugging)."""
    print("[TRACE] a =", a, "b =", b)
    result = a + b
    print("[TRACE] result =", result)
    return result

def performance_compare_sort(records):
    """Performance comparison using time module."""
    # Compare merge_sort vs Python's built-in sorted for 'roll'
    t0 = time.perf_counter()
    ms_sorted = merge_sort(records, "roll")
    t1 = time.perf_counter()
    py_sorted = sorted(records, key=lambda r: r["roll"])
    t2 = time.perf_counter()
    print("merge_sort time:", round((t1 - t0) * 1000, 3), "ms")
    print("sorted() time:", round((t2 - t1) * 1000, 3), "ms")
    print("Top 3 merge_sort:", [(r["roll"], r["name"]) for r in ms_sorted[:3]])
    print("Top 3 sorted():", [(r["roll"], r["name"]) for r in py_sorted[:3]])

def recursion_limit_demo():
    """Show and adjust recursion limit using sys."""
    print("Current recursion limit:", sys.getrecursionlimit())
    # Carefully increase for demo
    sys.setrecursionlimit(2000)
    print("New recursion limit set to 2000")

def factorial_math_demo(n):
    """Use math library factorial for comparison."""
    try:
        print("math.factorial(", n, ") =", math.factorial(n))
    except Exception as e:
        print("math.factorial error:", e)

# -------------------------------
# CRUD flows (used across persons; Person 4 presents usage)
# -------------------------------

def add_student_flow():
    """Add student with validation and dedup."""
    print("\n--- Add Student ---")
    name = sanitize_text(input("Name: "))
    roll = normalize_roll(input("Roll: "))
    dept = sanitize_text(input("Department " + str(sorted(list(VALID_DEPTS))) + ": ")).upper()
    year = input("Year (1-5): ").strip()
    err = validate_student(name, roll, dept, year)
    if err is not None:
        print("Validation error:", err)
        return
    # check duplicate
    for s in STUDENTS:
        if s["roll"] == roll:
            print("Duplicate roll. Not added.")
            return
    STUDENTS.append({"name": name, "roll": roll, "dept": dept, "year": year})
    print("Student added.")

def view_students_flow():
    """View students sorted by roll."""
    print("\n--- Students ---")
    if len(STUDENTS) == 0:
        print("No records.")
        return
    sorted_records = merge_sort(STUDENTS, "roll")
    i = 0
    while i < len(sorted_records):
        s = sorted_records[i]
        print(str(i + 1) + ". " + s["name"] + " | " + s["roll"] + " | " + s["dept"] + " | Year " + s["year"])
        i += 1

def search_student_flow():
    """Search student by roll using linear or binary search."""
    print("\n--- Search Student ---")
    if len(STUDENTS) == 0:
        print("No records to search.")
        return
    roll = normalize_roll(input("Enter roll: "))
    method = input("Method (linear/binary): ").strip().lower()
    if method == "linear":
        result = linear_search(STUDENTS, roll)
        print("Found:" if result is not None else "Not found.", result)
    elif method == "binary":
        sorted_records = merge_sort(STUDENTS, "roll")
        result = binary_search(sorted_records, roll)
        print("Found:" if result is not None else "Not found.", result)
    else:
        print("Unknown method.")

def sort_students_flow():
    """Sort students by chosen key and algorithm."""
    print("\n--- Sort Students ---")
    if len(STUDENTS) == 0:
        print("No records.")
        return
    key = input("Key (roll/name/year): ").strip().lower()
    if key not in ("roll", "name", "year"):
        print("Invalid key. Using 'roll'.")
        key = "roll"
    algo = input("Algorithm (insertion/merge/bubble): ").strip().lower()
    if algo == "insertion":
        copy = STUDENTS[:]
        insertion_sort(copy, key)
        print_sorted(copy)
    elif algo == "merge":
        sorted_records = merge_sort(STUDENTS, key)
        print_sorted(sorted_records)
    elif algo == "bubble":
        copy = STUDENTS[:]
        bubble_sort(copy, key)
        print_sorted(copy)
    else:
        print("Unknown algorithm.")

def print_sorted(records):
    """Print sorted records."""
    i = 0
    while i < len(records):
        s = records[i]
        print(str(i + 1) + ". " + s["name"] + " | " + s["roll"] + " | " + s["dept"] + " | Year " + s["year"])
        i += 1

def update_student_flow():
    """Update student fields with validation."""
    print("\n--- Update Student ---")
    roll = normalize_roll(input("Existing roll: "))
    existing = None
    for s in STUDENTS:
        if s["roll"] == roll:
            existing = s
            break
    if existing is None:
        print("No such roll.")
        return
    print("Current:", existing)
    name = sanitize_text(input("New name (blank to keep): "))
    dept = sanitize_text(input("New dept (blank to keep): ")).upper()
    year = input("New year (1-5, blank to keep): ").strip()

    name = existing["name"] if name == "" else name
    dept = existing["dept"] if dept == "" else dept
    year = existing["year"] if year == "" else year

    err = validate_student(name, roll, dept, year)
    if err is not None:
        print("Validation error:", err)
        return

    # Update in place
    for s in STUDENTS:
        if s["roll"] == roll:
            s["name"] = name
            s["dept"] = dept
            s["year"] = year
            print("Updated.")
            return

def delete_student_flow():
    """Delete student by roll."""
    print("\n--- Delete Student ---")
    roll = normalize_roll(input("Roll to delete: "))
    i = 0
    while i < len(STUDENTS):
        if STUDENTS[i]["roll"] == roll:
            STUDENTS.pop(i)
            print("Deleted.")
            return
        i += 1
    print("No such roll.")

# -------------------------------
# Recursion & iterative demos, save/load, tracing
# -------------------------------

def recursion_iterative_demos_flow():
    """Run recursion vs iterative demos."""
    print("\n--- Recursion & Iterative Demos ---")
    try:
        n = int(input("Enter non-negative integer for factorial: ").strip())
        print("factorial_recursive(", n, ") =", factorial_recursive(n))
        print("factorial_iterative(", n, ") =", factorial_iterative(n))
        factorial_math_demo(n)
    except Exception as e:
        print("Factorial error:", e)

    start = sanitize_text(input("DFS start dept: ")).upper()
    target = sanitize_text(input("DFS target dept: ")).upper()
    path_r = dfs_recursive(DEPT_GRAPH, start, target, set())
    path_i = dfs_iterative(DEPT_GRAPH, start, target)
    print("DFS recursive path:", path_r)
    print("DFS iterative path:", path_i)

def save_load_flow():
    """Choose to save or load data."""
    print("\n--- Save / Load ---")
    opt = input("Choose (save/load): ").strip().lower()
    if opt == "save":
        save_to_file(DATA_FILE)
    elif opt == "load":
        load_from_file(DATA_FILE)
    else:
        print("Unknown option.")

def tracing_performance_flow():
    """Run tracing and performance comparisons."""
    print("\n--- Tracing & Performance Demo ---")
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        res = trace_add_two_numbers(a, b)
        print("Trace result:", res)
    except Exception as e:
        print("Trace error:", e)
    performance_compare_sort(STUDENTS)

def recursion_limit_flow():
    """Show and adjust recursion limit."""
    recursion_limit_demo()

# -------------------------------
# Main loop
# -------------------------------

def seed_demo_data():
    """Seed initial demo data for presentations."""
    STUDENTS.append({"name": "Keerthi", "roll": normalize_roll("21CSE001"), "dept": "CSE", "year": "3"})
    STUDENTS.append({"name": "Rahul", "roll": normalize_roll("21ECE105"), "dept": "ECE", "year": "2"})
    STUDENTS.append({"name": "Divya", "roll": normalize_roll("21EEE210"), "dept": "EEE", "year": "4"})
    STUDENTS.append({"name": "Akhil", "roll": normalize_roll("21CSE155"), "dept": "CSE", "year": "2"})
    STUDENTS.append({"name": "Meera", "roll": normalize_roll("21MECH021"), "dept": "MECH", "year": "3"})

def main():
    """Main loop showing sequence, selection, repetition."""
    if len(STUDENTS) == 0:
        seed_demo_data()

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_student_flow()
        elif choice == "2":
            view_students_flow()
        elif choice == "3":
            search_student_flow()
        elif choice == "4":
            sort_students_flow()
        elif choice == "5":
            update_student_flow()
        elif choice == "6":
            delete_student_flow()
        elif choice == "7":
            summary = student_summaries(STUDENTS)
            print_summaries(summary)
        elif choice == "8":
            recursion_iterative_demos_flow()
        elif choice == "9":
            save_load_flow()
        elif choice == "10":
            tracing_performance_flow()
        elif choice == "11":
            recursion_limit_flow()
        elif choice == "12":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
