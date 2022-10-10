height=sorted([int(input()) for _ in range(9)])

Sum=sum(height)
a,b=0,0

for i in range(len(height)):
    for j in range(i,len(height)):
        if i!=j and Sum-height[i]-height[j]==100:
            a,b=height[i],height[j]
            break

height.remove(a)
height.remove(b)

for i in height:
    print(i)