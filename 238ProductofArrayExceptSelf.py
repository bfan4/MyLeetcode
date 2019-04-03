
p = 1
n = 5
output = []
nums = [2,2,3,4,5]
for i in range(0,n):
    output.append(p)
    p = p * nums[i]
print(output)
p = 1
for i in range(n-1,-1,-1):
    output[i] = output[i] * p
    p = p * nums[i]
print(output)