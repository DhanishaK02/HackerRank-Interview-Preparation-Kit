# Sales by Match

## Problem Statement

There is a large pile of socks, each represented by an integer indicating its color.
Find the maximum number of matching pairs of socks.

---

## Topic

- HashMap (Dictionary)
- Frequency Counting

---

## Key Idea

Count how many times each sock color appears.

Each pair consists of 2 socks, so:

pairs = frequency // 2

The total number of pairs is the sum of pairs for all colors.

---

## Approach

1. Create an empty dictionary.
2. Traverse the array.
3. Count the frequency of each sock color.
4. Traverse all frequencies.
5. Add `frequency // 2` to the answer.
6. Return the total number of pairs.

---

## Dry Run

Input:

10 20 20 10 10 30 50 10 20

Frequency Table:

10 → 4

20 → 3

30 → 1

50 → 1

Pairs:

10 → 4 // 2 = 2

20 → 3 // 2 = 1

30 → 1 // 2 = 0

50 → 1 // 2 = 0

Total Pairs = 3

---

## Algorithm

1. Initialize an empty dictionary.
2. Count the occurrence of each color.
3. Initialize `pairs = 0`.
4. For every frequency:
   - Add `frequency // 2` to `pairs`.
5. Return `pairs`.

---

## Time Complexity

O(n)

---

## Space Complexity

O(k)

where k = number of unique colors.

---

## Interview Tip

Whenever a problem asks to count occurrences, duplicates, or frequencies, think of using a Dictionary (HashMap).
