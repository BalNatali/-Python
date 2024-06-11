s = list(map(int, input().split()))
s1 = []
for i in range(len(s)):
    if s[i] not in s1:
        print('NO')
        s1.append (s[i])
    else:
        print('YES')