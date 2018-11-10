#!/usr/bin env python
"""
Datto is designed to perform backups as quickly as possible, which is usually achieved by using multiple threads. In this task, assume that all of your available threads are backing up documents at the same 1Mb/sec speed.

Given an array of documents sizes that you need to back up and the number of available threads, return the minimum amount of time needed to back up all the files (a single thread can only be backing up one document at any given moment).

Example

For threads = 2 and documents = [4, 2, 5],
the output should be concurrentBackups(threads, documents) = 6.

The optimal solution is to send the documents of sizes 4 and 2 to the first thread and the document of size 5 to the second one. This way the first thread will finish its work in 6 seconds, and the second one in 5, so after 6 seconds the backup will be complete.
"""

from math import ceil


def concurrentBackups(threads, documents):
    if not documents:
        return 0
    else:
        size = len(documents)
    return ceil(sum(documents) / threads) if threads < size else max(documents)


threads = 2
documents = [4, 2, 5]

# threads = 2
# documents= [5, 3, 5, 3, 7]
# Expected Output: 12

# threads = 5
# documents = [2, 1, 1, 3, 5, 3, 4, 2, 4, 1]
# Expected Output: 6

# threads = 5
# documents = [2, 1, 1, 3, 5, 3, 4, 2, 3, 1]
# Expected Output: 5

concurrentBackups(threads, documents)
