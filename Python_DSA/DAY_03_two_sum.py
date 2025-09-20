nums=[2,7,11,15]
target=int(input("Enter the  targetL: "))
haash_map={}
for i,n in enumerate(nums):
    diff=target-n
    if diff in haash_map:
        print([haash_map[diff],i])
    haash_map[n]=i