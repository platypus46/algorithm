def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        #비트연산시 둘 중 하나라도 1이면 1
        num=str(bin(arr1[i]|arr2[i]))[2:]
        if len(num)!=n:
             num=("0" *(n - len(num)) + num)
        res = num.replace('1', '#').replace('0', ' ')
        answer.append(res)
    return answer

