n = int(input())
ppl_list = [ (input().split(), i) for i in range(n) ]
ppl_list = sorted(ppl_list, key=lambda x: [int(x[0][0]), x[1]])

for person in ppl_list:
    print(person[0][0], person[0][1])