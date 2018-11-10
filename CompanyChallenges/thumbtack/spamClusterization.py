#/usr/bin/env python
"""
Thumbtack tries to identify spam coming from multiple user accounts by comparing job request descriptions and identifying 
clusters that have high similarity. Their data analysis engineers are testing out a new clusterization algorithm that uses the 
Jaccard index. As a prospective team member, you've been asked to implement this algorithm.

You are given a list of requests and ids of the users who submitted them. Implement the following algorithm to identify possible 
spammers:

first, split each request into a set of words and convert them to lowercase. We formally define a word as a substring consisting 
of English letters, such that characters to the left of the leftmost letter and to the right of the rightmost letter are not 
letters;
next, calculate the Jaccard index of each pair of sets;
divide the sets into clusters so that:
each set belongs to some cluster;
if Jaccard index of two sets A and B is not less than the given threshold (meaning they are too similar), they belong to the 
same cluster. Note that if A and B as well as B and C satisfy this criteria, then A, B and C belong to the same cluster;
for each cluster that has more than one element, return the list of their author IDs in ascending order.
Example

For

requests = ["I need a new window.",
            "I really, really want to replace my window!",
            "Replace my window.",
            "I want a new window.",
            "I want a new carpet, I want a new carpet, I want a new carpet.",
            "Replace my carpet"]
ids = [374, 2845, 83, 1848, 1837, 1500], and
threshold = 0.5, the output should be
spamClusterization(requests, ids, threshold) = [[83, 1500], [374, 1837, 1848]].

The sets of words obtained after the first step are:

{"i", "need", "a", "new", "window"} - 5 elements;
{"i", "really", "want", "to", "replace", "my", "window"} - 7 elements;
{"replace", "my", "window"} - 3 elements;
{"i", "want", "a", "new", "window"} - 5 elements;
{"i", "want", "a", "new", "carpet"} - 5 elements (note that a set consists only of unique elements);
{"replace", "my", "carpet"} - 3 elements.
Here's a table of Jaccard indices for each pair of request (there are 6 requests in total):

1	2	3	4	5	6
1	-	2/10 = 1/5	1/7	4/6 = 2/3	3/7	0/8 = 0
2	1/5	-	3/7	3/9 = 1/3	2/10 = 1/5	2/8 = 1/4
3	1/7	3/7	-	1/7	0/8 = 0	2/4 = 1/2
4	4/6	3/9	1/7	-	4/6 = 2/3	0/8 = 0
5	3/7	1/5	0	2/3	-	1/7
6	0	1/4	1/2	0	1/7	-
Since threshold = 0.5, there are two clusters with more than one element. The first one contains the third and the sixth 
requests, and the second one contains requests number one, four and five (since Jaccard index of the first and fourth requests 
and of the fourth and fifth requests is larger than threshold, they all belong to the same cluster). After sorting their author 
ids, we arrive at the answer.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string requests

A non-empty list of requests. Each request is a non-empty string consisting of English letters, punctuation marks and whitespace 
characters.

Guaranteed constraints:
1 ≤ requests.length ≤ 10,
1 ≤ requests[i].length ≤ 65.

[input] array.integer ids

Array of unique elements of the same size as requests.

Guaranteed constraints:
1 ≤ ids.length ≤ 10,
1 ≤ ids[i] ≤ 3000.

[input] float threshold

Guaranteed constraints:
0.0 ≤ threshold ≤ 1.0.

[output] array.array.integer

Each element of the output should contain ids of users whose requests ended up in the same cluster sorted in ascending order. 
Output array elements should be sorted by the smallest ids they contain.
"""

import re

def find_intersaction(outputs):
    for i, a in enumerate(outputs):
        for j, b in enumerate(outputs[i+1:], i+1):
            if a & b:
                outputs[i] = a.union(outputs.pop(j))
                return find_intersaction(outputs)
    return outputs


def spamClusterization(requests, ids, threshold):
    results = []
    for request in requests:
        request = request.lower().split()
        request = re.sub(r'\W+', ' ', ' '.join(request))
        results.append(set(request.split()))

    outputs = []
    for i in range(len(results)):
        for j in range(i+1, len(results)):
            jac = len(results[i] & results[j]) / len(results[i] | results[j])
            if jac >= threshold:
                outputs.append({ids[i], ids[j]})

    outputs = find_intersaction(outputs)

    return sorted([sorted(list(i)) for i in outputs if i])

requests = ["I need a new window.",
 "I really, really want to replace my window!",
 "Replace my window.",
 "I want a new window.",
 "I want a new carpet, I want a new carpet, I want a new carpet.",
 "Replace my carpet"]
ids = [374, 2845, 83, 1848, 1837, 1500]
threshold = 0.5

spamClusterization(requests, ids, threshold)
