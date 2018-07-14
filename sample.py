def areFollowingPatterns(strings, patterns):
	found_pattern = {}
    for i,j in zip(strings,patterns):
        if j not in found_pattern:
            found_pattern[j] = i
        else:
            if(found_pattern[j]!=i):
                return False

print areFollowingPatterns(["cat", "dog", "dog"],["a","b","c"])