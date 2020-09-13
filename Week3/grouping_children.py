def group(c):
    c.sort()
    n = len(c)
    val = c[0]
    i = 0
    ans = []
    
    while i < n:
        temp = []
        val = c[i]
        val += 1
        for item in c[i:]:
            if item <= val:
                temp.append(item)
                i = i + 1
            else:
                break
        ans.append(temp)
    return ans
