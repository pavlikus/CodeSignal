#!/usr/bin/env python
"""
During a team hackathon at Datto, you decide to quickly implement file backup history. But to do this you first need to know how many backups of a certain file already exist.

You are given the creationTimes of files in the database, where creationTimes[i] stands for the time the ith file was created. Assume that all files are configured to be backed up every k seconds after their creation time, but this default behavior can be changed manually.

The system administrator can make one of two manual request types:

cancel all future auto-backups for the specified file;
immediately create a backup of the specified file.
Note that manual requests are processed before automatic actions, so if a cancellation request coincides with an auto-backup, the auto-backup doesn't happen. In a given second only 1 backup of a file is possible, so in the case that a manual request coincides with an auto-backup, only one backup is made.

Given a list of backupRequests, your task is to find the number of backups that have been made of each file by the given time t. Events that occurred at exactly t seconds should be included in the answer.

Example

For creationTimes = [461620201, 461620203, 461620207],

backupRequests = [[1, 0, 461620202],
                  [1, 2, 461620208],
                  [0, 2, 461620210],
                  [1, 0, 461620204],
                  [1, 1, 461620209],
                  [1, 1, 461620203]]
k = 3, and t = 461620210, the output should be
backupHistory(creationTimes, backupRequests, k, t) = [4, 3, 1].

Here's how the backups were created:

for file 0: manual backups at 461620202 and 461620204 and automatic ones at 461620207, 461620210 (461620204 is skipped because it was made manually);
for file 1: manual backups at times 461620203 and 461620209 and auto-backup at time 461620206;
for file 2: manual backup at time 461620208 and a cancellation at time 461620210, which canceled the auto-backup at 461620210.
Check out the image below for better understanding:



Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer creationTimes

Array of timestamps of when the files were created, sorted in ascending order.

Guaranteed constraints:
1 ≤ creationTimes.length ≤ 1000,
4 · 108 ≤ creationTimes[i] ≤ 5 · 108.

[input] array.array.integer backupRequests

A list of requests. For each valid i the ith request is given as backupRequests[i] = [type, file, time], where:

type is the type of request, 0 for cancellation and 1 for manual backup;
file is the file number, 0 ≤ file < creationTimes.length;
time is the time the request was made, which is guaranteed to be a positive integer not less than creationTimes[file].
It is guaranteed that no two requests to the same file occur simultaneously.

Guaranteed constraints:
1 ≤ backupRequests.length ≤ 1000,

[input] integer k

A positive integer.

Guaranteed constraints:
2 ≤ k ≤ 10.

[input] integer t

A positive integer.

Guaranteed constraints:
108 ≤ t ≤ 109.

[output] array.integer

Array of the same length as creationTimes, where the ith element is the number of times the ith file was backed up.
"""


def backupHistory(creationTimes, backupRequests, k, t):
    result = {}
    blacklist = {}

    # add manual backup in result and add cancelled backup in blacklist
    for i, key, value in backupRequests:
        if i and value <= t:
            result.setdefault(key, set()).add(value)
        if not i:
            if key in blacklist:
                if value < blacklist[key]:
                    blacklist[key] = value
            else:
                blacklist[key] = value

    # generate auto-backups considering blacklist
    for i, value in enumerate(creationTimes):
        if i in blacklist and blacklist[i] <= t:
            value = set(range(value + k, blacklist[i], k))
            result.setdefault(i, set()).update(value)
        else:
            while value + k <= t:
                value += k
                result.setdefault(i, set()).add(value)
        if i not in result:
            result[i] = set()
    return [len(result[r]) for r in sorted(result)]


creationTimes = [461620242, 461620255, 461620439, 461720700]
backupRequests = [[1, 0, 461620253],
                  [1, 1, 461620255],
                  [0, 3, 461770200],
                  [0, 3, 461815200],
                  [1, 2, 461620783],
                  [1, 0, 461620434],
                  [1, 1, 461620302],
                  [0, 2, 461621253]]
k = 5
t = 461820200
# Expected Output:[39993, 39991, 163, 9899]

# creationTimes = [461620200, 461620206, 461620219, 461620224, 461620244, 461620252, 461620254, 461620273, 461620273, 461620295]
# backupRequests = [[1,9,461620296], 
# [1,8,461620276], 
# [1,2,461620269], 
# [0,0,461620243], 
# [0,0,461620202], 
# [1,1,461620232], 
# [1,5,461620272], 
# [1,7,461620273], 
# [1,2,461620276], 
# [1,4,461620279]]
# k = 3
# t = 461620234
# Expected Output:[0, 10, 5, 3, 0, 0, 0, 0, 0, 0]

# creationTimes = [461620201, 461620203, 461620207]
# backupRequests = [[1,0,461620202], 
# [1,2,461620208], 
# [0,2,461620210], 
# [1,0,461620204], 
# [1,1,461620209], 
# [1,1,461620203]]
# k = 3
# t = 461620210
# Expected Output:[4, 3, 1]

# creationTimes = [461620203, 461620206, 461620207, 461620214]
# backupRequests = [[1,0,461620205],
#                  [1,0,461620206],
#                  [1,0,461620210]]
# k = 2
# t = 461620206
# Expected Output:[2, 0, 0, 0]

backupHistory(creationTimes, backupRequests, k, t)
