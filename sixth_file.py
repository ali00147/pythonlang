arr= [1,2,3,4,6,8]
target= int(input("Enter a number to find two pairs in the given list that add up to the target number: \n"))
if_not_found= False
for i in range(len(arr)):
   for j in range(i+1,len(arr)):
    if arr[i]+arr[j]==target:
       resuarrt=arr[i]+arr[j]
       print(f'Found two numbers that sum to the target {arr[i]} + {arr[j]} = {resuarrt}')
       if_not_found=True
       break
if not if_not_found:
    print("Couldn't find two numbers that sum to the target.")
