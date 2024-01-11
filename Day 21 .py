def create_sums(s):

    sums = set([0])
    length = 1
    sums.add(ord(s[0]) - ord('a') + 1)
    
    for i in range(1, len(s)):
        weight = ord(s[i]) - ord('a') + 1
        length = length + 1 if s[i] == s[i - 1] else 1
        sums.add(length * weight)
    
    return sums


def weightedUniformStrings(s, queries):
    # Write your code here
    results = []
    sums = create_sums(s)

    for query in queries:
        if query in sums:
            results.append("Yes")
        else:
            results.append("No")
    
    return results