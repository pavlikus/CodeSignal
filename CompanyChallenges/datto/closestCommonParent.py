#!/usr/bin/env python
"""
You're on a team at Datto tasked with implementing a backup system aimed at minimizing storage space. While exploring potential solutions, you notice something interesting: while performing backups on enterprise client accounts, the system often outputs clusters of files originating from the same source file, but each with slight differences. You come up with an idea to back up the original file and then use incremental differences to generate all the other files as needed.

To implement this feature, you start by finding the closest common parent file (CCPF) of two files. More specifically, if you define the distance between a parent (the original) file and a child (modified) file as the number of intermediate files between them, then their CCPF is the file that has the least total distance to both of the given files among all of the files in the cluster. Assume that the distance between a file and a file itself is 0.

Given a list of files in a cluster, and the files each of them originated from as an array, parents, find the CCPF of file1 and file2.

Example

For files = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
parents = ["-1", "F1", "F1", "F2", "F2", "F4", "F4", "F4"],
file1 = "F5", and file2 = "F8", the output should be
closestCommonParent(files, parents, file1, file2) = "F2".

The CCPF of "F5" and "F8" is "F2", since it's a parent for both "F5" and "F8", and is located below "F1" (which is also a parent to both of the files).
"""


def closestCommonParent(files, parents, file1, file2):
    result = set((file1, file2))
    while True:
        index = []

        def get_value(file):
            if file != '-1':
                i = files.index(file)
                index.append(i)
                return parents[i]
            else:
                return file

        file1, file2 = map(get_value, (file1, file2))
        if index:
            for i in index:
                if parents[i] not in result:
                    result.add(parents[i])
                else:
                    return parents[i]
        else:
            return '-1'


# files = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"]
# parents = ["-1", "F1", "F1", "F2", "F2", "F4", "F4", "F4"]
# file1 = "F5"
# file2 = "F8"

# files = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]
# parents = ["-1", "F1", "F1", "F3", "F3", "F3", "F6", "F6", "F2"]
# file1 = "F7"
# file2 = "F3"
# Expected Output: "F3"

files = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9"]
parents = ["-1", "F1", "F1", "F3", "F3", "F3", "F6", "F6", "F2"]
file1 = "F9"
file2 = "F8"
# Expected Output: "F1"

# files = ["fileone", "filetwo", "alsofile", "couldbeaname", "5", "F6", "FF", "42"]
# parents = ["-1", "fileone", "fileone", "filetwo", "filetwo", "couldbeaname", "couldbeaname", "couldbeaname"]
# file1 = "fileone"
# file2 = "FF"
# Expected Output: "fileone"

# files = ["a", "b", "C", "d", "1", "e", "f", "g", "h", "i"]
# parents = ["b", "C", "d", "1", "-1", "1", "e", "f", "g", "1"]
# file1 = "i"
# file2 = "h"
# Expected Output: "1"

closestCommonParent(files, parents, file1, file2)
