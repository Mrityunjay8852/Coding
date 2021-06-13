#Given five positive integers, find the minimum and maximum
#  values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two 
# space-separated long integers.


arr=[1,2,5,6,9]
#arr=[5,5,5,5,5]
maximum=[]
minimum=[]
sum=0
sum2=0
sum3=0
sum1=0

maximum.append(max(arr))
minimum.append(min(arr))

for i in range(len(arr)):
    if arr[i]<max(arr):
        sum=sum+arr[i]
    if arr[i]>min(arr):
        sum1=sum1+arr[i]
    if arr[i]==arr[i-1]:
        sum2=sum2+arr[i]
        sum3=sum3+arr[i]
        sum=sum2-maximum[0]
        sum1=sum3-minimum[0]
print(sum,sum1)

