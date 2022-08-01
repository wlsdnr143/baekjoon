sum_Of_Number = int(input())
count = 0

# 30 이 주어지면 30에서 1 2 3 .. 이렇게 하나씩 뺌
# 29 27 24 20 15 9 2
# 이렇게 가다가 2에서 8을 빼야하는데 못빼니까 9를 한번에 뺐어야함
# 29 27 24 20 15 9 0  -> 이런식으로
# 즉 9가 i i+1을 더한 것보다 작으면 바로 9를 빼도록
# 1 2 3 4 5 6 9  : 답 7

for i in range(1, sum_Of_Number+1): # sum_Of_Number 에다 +1 을 한 이유는
    # sum_Of_Number 이 1일때 range(1,1)이 되면서 오류가 나기 때문
    if sum_Of_Number >= i*2+1:
        sum_Of_Number -= i
        count += 1
    else:
        count += 1
        break

print(count)


