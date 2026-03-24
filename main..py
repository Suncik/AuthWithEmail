#  find reverse word

def reverseWord(s):  
    # k=s[::-1]  # by slicing
    # return k
    
    l=list(s)
    l.reverse()  # by using function
    # return l  # ['m', 'o', 'l', 'a', 's']
    # return "".join(l) # molas
#     return "*".join(l)  # m*o*l*a*s

# print(reverseWord('salom'))

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

# def Union(arr1,arr2):
#     a=set(arr1)
#     b=set(arr2)
#     c=a.union(b) 
#     print(c)
    
# Union([1,2], [2,3])  # {1, 2, 3}

# def Union(a, b, n, m):
#     c=set()
#     for i in range(0, n):
#         c.add(a[i])
#     for i in range(0,m):
#         c.add(b[i])
#     return c

# print(Union([1,2,3], [3,4,5], 3,3))  # {1, 2, 3, 4, 5}

# rotate array by one

# arr=[1,2,3,4]
# print(arr[:-1])  # [1, 2, 3]
# print(arr[-1:])  # [4]
# print(arr[:-2])  # [1, 2]
# arr[starting:ending]
# print(arr[-1:]+arr[:-1]) # [4, 1, 2, 3]

# def rotate(arr, n):
#     a=arr[-1]
#     for i in range(n-1, 0, -1):
#         arr[i]=arr[i-1]  # arr[2]=arr[1] , arr[1]=arr[0]  
        
#     arr[0]=a
#     return arr
# print(rotate([1,2,3], 3))  # [3, 1, 2] 


# find dublicate number
# def dublicate(nums: list[int]):
#     nums.sort()
#     n=len(nums)
#     for i in range(1,n):
#         if nums[i-1]==nums[i]:
#             return nums[i]
          
        
# print(dublicate([1,2,1,3,2]))

# merge(birlshtiring) 2 sorted arrays without using extra space
import math

def merge(arr1, arr2, n, m):
    gap = math.ceil((n + m) / 2)
    
    while gap > 0:
        i = 0
        j = gap
        
        while j < (n + m):
            # arr1 va arr1 ichida
            if i < n and j < n:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
            
            # arr1 va arr2 orasida
            elif i < n and j >= n:
                if arr1[i] > arr2[j - n]:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]
            
            # arr2 va arr2 ichida
            else:
                if arr2[i - n] > arr2[j - n]:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]
            
            i += 1
            j += 1
        
        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)

# Example
arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]

merge(arr1, arr2, len(arr1), len(arr2))

print(arr1)  # [1, 2, 3, 4, 7]
print(arr2)  # [8, 9, 10]
    



        
    




