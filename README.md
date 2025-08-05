# Algorithmic Complexity, Approximate & Randomized Algorithms
**Repo:** `goit-algo2-hw-10`

---

## ⚙️ Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📊 Task 1: QuickSort Variants Benchmark

**File:** `quicksort_benchmark.py`  
**What it does:**  
1. Implements `randomized_quick_sort(arr)` (random pivot) and `deterministic_quick_sort(arr)` (fixed pivot).  
2. Generates arrays of sizes 10 000, 50 000, 100 000, 500 000 with random integers.  
3. Runs each sort 5 times per size, measures average execution time.  
4. Prints a table of results and plots a comparison chart.

**Run:**
```bash
python quicksort_benchmark.py
```
---

## 🗓️ Task 2: Greedy Class Scheduling

**File:** `schedule.py`
**What it does:**
1. Defines a Teacher class (first_name, last_name, age, email, can_teach_subjects).
2. Implements create_schedule(subjects, teachers) using a greedy set-cover approach:
3. At each step, picks the teacher covering the most uncovered subjects (tie → youngest).
4. Prints a table of assigned teachers & their subjects, or an error if full coverage is impossible.

**Run:**

```bash
python schedule.py
```
