#!/usr/bin/env python
"""
A Thumbtack customer has just submitted a request for a house painter to paint a one bedroom house in San Francisco. Our job is 
to find Pros who provide this service and whose travel distance preference is ideal for the job. To measure how well the Pro and 
the request match, we calculate their matching score and non-matching score as follows:

if the Pro's distance from the customer's house does not exceed their maximum preferred travel distance, then their matching 
score equals the distance between the pro and the customer;
otherwise we calculate a non-matching score as the difference between the distance from the pro to the customer, and their 
maximum preferred travel distance.
For example, let's say a pro Jane has a maximum travel distance of 10 miles.

If a customer is located 5 miles away, their matching score is 5 miles.
If a customer is located 12 miles away, their "non-matching" score is 2 miles.
To select the top 5 Pros, we sort them so that those who have a matching score are always shown before those who have a 
non-matching score, and both matching scores and non-matching scores are sorted in ascending order. If two or more Pros have 
equal scores, they are sorted by their names in lexicographical order.

You're given a list of pros who match the "house painting" category, their distances from the customer's house, and their 
travelPreferences, which denotes the maximum distance each Pro is willing to travel for a given job. Return the top 5 Pros 
sorted as described above. If there are fewer than 5 Pros, return them all.

Example

For
pros = ["Michael", "Mary", "Ann", "Nick", "Dan", "Mark"],
distances = [12, 10, 19, 15, 5, 20], and
travelPreferences = [12, 8, 25, 10, 3, 10], the output should be
requestMatching(pros, distances, travelPreferences) = ["Michael", "Ann", "Dan", "Mary", "Nick"].
Here's how Pros will be sorted in accordance with their scores:

"Michael": matching score equals 12;
"Ann": matching score equals 19;
"Dan": non-matching score equals 5 - 3 = 2;
"Mary": non-matching score equals 10 - 8 = 2;
"Nick": non-matching score equals 15 - 10 = 5;
"Mark": non-matching score equals 20 - 10 = 10.
For
pros = ["Ann", "Michael", "Mary"],
distances = [5, 5, 5], and
travelPreferences = [3, 10, 7], the output should be
requestMatching(pros, distances, travelPreferences) = ["Mary", "Michael", "Ann"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string pros

A non-empty array of unique Pros' names.

Guaranteed constraints:
1 ≤ pros.length ≤ 10,
1 ≤ pros[i].length ≤ 10.

[input] array.integer distances

Array of positive integers. For each valid i distances[i] denotes the distance from the ith Pro to the customer's house.

Guaranteed constraints:
distance.length = pros.length,
2 ≤ distances[i] ≤ 20.

[input] array.integer travelPreferences

Array of positive integers. For each valid i travelPreferences[i] denotes the maximum preferred travel distance of the ith Pro.

Guaranteed constraints:
travelPreferences.length = pros.length,
1 ≤ travelPreferences[i] ≤ 25.

[output] array.string

Top 5 (or fewer) Pros sorted as described above.
"""


def requestMatching(pros, distances, travelPreferences):
    matching = {}
    nmatching = {}
    for x in range(len(pros)):
        if distances[x] <= travelPreferences[x]:
            matching[pros[x]] = distances[x]
        else:
            nmatching[pros[x]] = distances[x] - travelPreferences[x]

    if len(matching) >= 5:
        return sorted(matching, key=lambda x: (matching[x], x))
    else:
        return sorted(matching, key=lambda x: (matching[x], x)) + sorted(nmatching, key=lambda x: (nmatching[x], x))[:5-len(matching)]


pros = ["Ann",
 "Michael",
 "Mary"]
distances = [5, 5, 5]
travelPreferences = [3, 10, 7]
requestMatching(pros, distances, travelPreferences)
