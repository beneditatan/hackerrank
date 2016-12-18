def solution(query, string, query_len):
    counter = list()
    for k in range(0, query_len):
        counter.append(0)

    for a in range(len(query)):
        for b in range(len(string)):
            if(query[a] == string[b]):
                counter[a] = counter[a] + 1

    for h in range(0, len(counter)):
        print (counter[h])





str_len = int(input())
s = list()
for i in range(0,str_len):
    s.append(str(input()))

q_len = int(input())
q = list()
for j in range(0, q_len):
    q.append(str(input()))

solution(q,s,q_len)