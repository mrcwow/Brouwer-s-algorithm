import time
start_time = time.time()
k = 3
# k = int(input())
d = 2^k
n = 31415
# n = int(input())
q = []
r = []
n_brauer = n
while n_brauer>=d:
    q.append(n_brauer // d)
    r.append(n_brauer % d)
    n_brauer = q[-1]
print(q)
print(r)
answer = []
for i in q:
    if i < d:
        answer.extend(range(1, d))
    i_1 = i
    while i_1 <= d*i:
        answer.append(i_1)
        i_1 = i_1 * 2
answer = sorted(set(answer))
answer.append(answer[-1]+r[0])
print(f"B_k({n}) = {answer}")
print(len(answer) - 1)
print("{} seconds".format(time.time()-start_time))