def array_left_rotation(a, n, k):
    res = [0] * n
    for i in range(n):
        e = a[i]
        pos = i-k
        res[pos] = e
    return res
            
        
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')