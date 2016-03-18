# -*- coding: utf-8 -*-
import math
A=[0,1,2,3,4,5,6,7,8,9]
B=[10,11,12,13,14,15,16,17,18,19]
k=10
def findkthsmallest(A,B,k):
    lM=0
    lN=0
    hM=len(A)-1
    hN=len(B)-1
    while True:
        if k==1:
            return min(A[lM],B[lN])
        cM=hM-lM+1
        cN=hN-lN+1
        tmp = cM/float(cM+cN)
        iM=int(math.ceil(tmp*k))
        iN=k-iM
        iM=lM+iM-1
        iN=lN+iN-1
        if A[iM] >= B[iN]:
            if iN == hN or A[iM] < B[iN+1]:
                return A[iM]
            else:
                k = k - (iN-lN+1)
                lN=iN+1
                hM=iM-1
        if B[iN] >= A[iM]:
            if iM == hM or B[iN] < A[iM+1]:
                return B[iN]
            else:
                k = k - (iM-lM+1)
                lM=iM+1
                hN=iN-1
        if hM < lM:
            return B[lN+k-1]
        if hN < lN:
            return A[lM+k-1]

def findkthElement(k, array1, start1,end1, array2, start2, end2):
    if(k==0): return min(array1[start1], array2[start2])
    if start1 == end1: return array2[k]
    if start2 == end2: return array1[k]
    mid = (k//2)
    sub1 = min(mid, end1- start1)
    sub2 = min(mid, end2- start2)
    if (array1[start1 + sub1] < array2[start2 + sub2]):
        return findkthElement(k - mid, array1, start1 + sub1, end1, array2, start2, end2)
    else: return findkthElement(k - mid, array1, start1,end1, array2, start2 + sub2, end2)

print(findkthElement(k,A,0,9,B,0,9))
#print(findkthsmallest(A,B,k))