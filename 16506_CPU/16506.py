
ans = [0]*16

def opcode(code):
    if code=='ADD' or code=='ADDC':
        ans[0], ans[1], ans[2], ans[3] = 0, 0, 0, 0
    elif code=='SUB' or code=='SUBC':
        ans[0], ans[1], ans[2], ans[3] = 0, 0, 0, 1
    elif code=='MOV' or code=='MOVC':
        ans[0], ans[1], ans[2], ans[3] = 0, 0, 1, 0
    elif code=='AND' or code=='ANDC':
        ans[0], ans[1], ans[2], ans[3] = 0, 0, 1, 1
    elif code=='OR' or code=='ORC':
        ans[0], ans[1], ans[2], ans[3] = 0, 1, 0, 0
    elif code=='NOT':
        ans[0], ans[1], ans[2], ans[3] = 0, 1, 0, 1
    elif code=='MULT' or code=='MULTC':
        ans[0], ans[1], ans[2], ans[3] = 0, 1, 1, 0
    elif code=='LSFTL' or code=='LSFTLC':
        ans[0], ans[1], ans[2], ans[3] = 0, 1, 1, 1
    elif code=='LSFTR' or code=='LSFTRC':
        ans[0], ans[1], ans[2], ans[3] = 1, 0, 0, 0
    elif code=='ASFTR' or code=='ASFTRC':
        ans[0], ans[1], ans[2], ans[3] = 1, 0, 0, 1
    elif code=='RL' or code=='RLC':
        ans[0], ans[1], ans[2], ans[3] = 1, 0, 1, 0
    elif code=='RR' or code=='RRC':
        ans[0], ans[1], ans[2], ans[3] = 1, 0, 1, 1
for _ in range(int(input())):
    ans = [0]*16
    op = input().split()
    opcode(op[0])
    rD = bin(int(op[1]))[2:].zfill(3)
    for i in range(6, 9, 1):
        ans[i] = rD[i-6]
    rA = bin(int(op[2]))[2:].zfill(3)
    for i in range(9, 12, 1):
        ans[i] = rA[i-9]
    rBC = int(op[3])

    # OpCode의 마지막 글자가 C면 rC이용
    # C가 아니면 rB 이용
    if op[0][-1]=='C':
        ans[4] = 1
        rBC = bin(rBC)[2:].zfill(4)
        for i in range(12, 16, 1):
            ans[i] = rBC[i-12]
    else:
        rBC = bin(rBC)[2:].zfill(3)
        for i in range(12, 15, 1):
            ans[i] = rBC[i-12]
    for i in ans:
        print(i, end='')
    print()

    
