from collections import deque

def solution(queue1, queue2):
    division = sum(queue1 + queue2)

    if division % 2 != 0:
        return -1

    q1, q2 = deque(queue1), deque(queue2)

    sum1, sum2 = sum(q1), sum(q2)
    cnt = 0

    for i in range(300001):
        if sum1 == sum2:
            return i
        else:
            if sum1 > sum2:
                num = q1.popleft()
                q2.append(num)
                sum1 -= num
                sum2 += num
            else:
                num = q2.popleft()
                q1.append(num)
                sum2 -= num
                sum1 += num
            cnt += 1
    return -1