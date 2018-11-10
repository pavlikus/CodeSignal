#/usr/bin/env python
"""
As you might already know, Thumbtack helps Professionals (Pros) grow their business by identifying new customers. Upon 
registering on Thumbtack, Pros must select categories that match the type of services they provide. To make this step easier for 
Pros, Thumbtack would like to provide smart suggestions of categories that usually accompany those the Pro has already selected. 
To do this, Thumbtack engineers analyze historical user requestData and categories in proSelections using a Jaccard index 
statistic.

Your task is to implement the following algorithm that returns a single category recommendation:

for each request from requestData:
calculate the Jaccard index of this request and proSelections;
Assign a score to each category that is present in the request but not in proSelections equal to the value of the Jaccard index;
divide each score by the number of summands it was obtained from;
return the category with the highest positive score. If several categories have the same positive score, return the 
lexicographically smallest one. If there are no categories with positive score, return an empty string instead.
Example

For

requestData = [["Accounting", "Administrative Support", "Advertising", 
                              "Bodyguard", "Auctioneering"],
               ["Accounting", "Administrative Support"],
               ["Advertising", "Auctioneering", "Bodyguard"],
               ["Bodyguard", "Services Business", "Consulting"]]
and proSelections = ["Accounting", "Advertising"], the output should be
categoryRecommendations(requestData, proSelections) = "Administrative Support".

Here's how scores are calculated:
* i = 0: Jaccard index equals 2/5 and should be added to "Administrative Support", "Bodyguard", "Auctioneering";
* i = 1: Jaccard index equals 1/3 and should be added to "Administrative Support";
* i = 2: Jaccard index equals 1/4 and should be added to "Auctioneering", "Bodyguard";
* i = 3: Jaccard index equals 0 and should be added to "Bodyguard", "Services Business", "Consulting";

So the final scores equal:
* "Administrative Support": (2/5 + 1/3) / 2 = 11/30;
* "Auctioneering": (2/5 + 1/4) / 2 = 13/40;
* "Bodyguard": (2/5 + 1/4 + 0) / 3 = 13/60;
* "Consulting": 0/1 = 0;
* "Services Business": 0/1 = 0.

For

requestData = [["Accounting", "Bodyguard"],
               ["Accounting", "Auctioneering"]]
and proSelections = ["Accounting"], the output should be
categoryRecommendations(requestData, proSelections) = "Auctioneering".

"Auctioneering" and "Bodyguard" have the same score, but "Auctioneering" is lexicographically smaller than "Bodyguard".

For requestData = [["Bodyguard"]] and proSelections = ["Bodyguard"], the output should be
categoryRecommendations(requestData, proSelections) = "".

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.string requestData

List of user requests. It is guaranteed that requestData contains at least one element, and that each element is non-empty and 
consists of unique items.

Guaranteed constraints:
1 ≤ requestData.length ≤ 10,
1 ≤ requestData[i].length ≤ 10,
1 ≤ requestData[i][j].length ≤ 25.

[input] array.string proSelections

A non-empty array of unique elements.

Guaranteed constraints:
1 ≤ proSelections.length ≤ 10,
1 ≤ proSelections[i].length ≤ 15.

[output] string

A category suggested by the algorithm described above.
"""


def categoryRecommendations(requestData, proSelections):
    results = {}
    b = set(proSelections)
    for request in requestData:
        a = set(request)
        jac = len(a & b) / len(a | b)
        for k in a - b:
            if k not in results:
                results[k] = []
            results[k].append(jac)
    for i, result in results.items():
        results[i] = sum(result)/len(result)
    m = max(results.values()) if any(results.values()) else 0
    if m:
        for i in sorted(results):
            if results[i] == m:
                return i
    else:
        return ''


requestData = [["Accounting", "Administrative Support", "Advertising", "Bodyguard", "Auctioneering"],
               ["Accounting", "Administrative Support"],
               ["Advertising", "Auctioneering", "Bodyguard"],
               ["Bodyguard", "Services Business", "Consulting"]]

proSelections = ["Accounting", "Advertising"]
categoryRecommendations(requestData, proSelections)
