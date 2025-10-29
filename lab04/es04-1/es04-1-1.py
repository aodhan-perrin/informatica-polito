def inputValue() -> str:
   return input("Insert a whole num (Enter to quit) -> ")


total = 0
userStr = inputValue()
nums, even, odd = [], [], []

while userStr != "":
    total = total + int(userStr)
    print("total: ", total)

    nums.append(int(userStr))
    userStr = inputValue()

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("max: ", max(nums))
print("min: ", min(nums))
print("even nums: ", even)
print("odd nums: ", odd)