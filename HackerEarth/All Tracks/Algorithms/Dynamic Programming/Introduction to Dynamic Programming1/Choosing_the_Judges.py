'''
QUESTION link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/choosing-the-judges-7/description/

'''

T = int(input())
for j in range(1, T+1):
    N = int(input())
    array_ = list(map(int, input().split()))
    max_array = [0] * N
    marks = 0
    if N == 1:
        marks = array_[0]
    else:
        max_array[0] = array_[0]
        max_array[1] = max(array_[0], array_[1])
        for i in range(2, N):
            max_array[i] = max(max_array[i-1], max_array[i-2]+array_[i] )
        marks = max_array[N-1]
    output = "Case"+" "+str(j)+": "+str(marks)
    print(output)
    
