
N = int(input())

if N == 0:
    print(1)
else:
    answer = 1
    for i in range(1, N+1):
        # answer = answer * i
        answer *= i
    print(answer)