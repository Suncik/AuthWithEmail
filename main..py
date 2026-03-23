#  find reverse word

def reverseWord(s):  
    # k=s[::-1]  # by slicing
    # return k
    
    l=list(s)
    l.reverse()  # by using function
    # return l  # ['m', 'o', 'l', 'a', 's']
    # return "".join(l) # molas
    return "*".join(l)  # m*o*l*a*s

print(reverseWord('salom'))

#kthSmallestElement

# def kthSmallestElement(arr, k):
#     if len(arr)==1:
#         return arr[0]
    
#     arr.sort()
#     return arr[k-1]

# print(kthSmallestElement([2,1,4,5, 6,7], 3))

# Sort an array of 0s, 1s and 2s

# def sort012(arr, n):
#     cnt0=0
#     cnt1=0
#     cnt2=0
    
#     for i in range(n):
#         if arr[i]==0:
#             cnt0+=1
#         elif arr[i]==1:
#             cnt1+=1
#         elif arr[i]==2:  
#             cnt2+=1
            
#     i=0
#     while(cnt0>0):
#         arr[i]=0
#         i+=1
#         cnt0-=1
#     while(cnt1>0):
#         arr[i]=1
#         i+=1
#         cnt1-=1
#     while(cnt2>0):
#         arr[i]=2
#         i+=1
#         cnt2-=1
#     return arr
# print(sort012([0,1,0,2,1,0,2,1], 8))


# Move all negative numbers to beginning and positive to end with constant extra space

# def move(arr, n):
#     j=0
#     for i in range(0,n):
#         if arr[i]<0:
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp
#             j=j+1   
#     return arr
# print(move([2,-3,4,5,6,-7,8,9], 8))

# def move(arr, n):
#     low,high=0, n-1
#     while(low<high):
#         if arr[low]<0:
#             low+=1
#         elif arr[high]>0: 
#             high-=1
            
#         else:
#             arr[low], arr[high]=arr[high], arr[low]
            
#     return arr

# print(move([1,2,-4,-5,2,-7,3,2,-6,-8,-9,3,2,1], 14))  


# find the Union and intersection of the two sorted arrays




