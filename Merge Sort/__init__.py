# -*- coding: utf-8 -*-
def merge(left, right):
    result = []
    print(left,right)
    while(len(left) > 0) and (len(right) > 0):
        if(left[0] <= right[0]):
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while(len(left) > 0):
            result.append(left[0])
            left = left[1:]
    while(len(right) > 0):
            result.append(right[0])
            right = right[1:]
    return result


def mergeSort(lista):
    if len(lista)<=1:
        return lista
    mid = len(lista)//2
    left = lista[:mid]
    right = lista[mid:]
    return merge(mergeSort(left), mergeSort(right))

def insertInOrder(element,a, first,last):
    print(element,a,first,last)
    if(element >= a[last]):
        a[last+1]= element
    else:
        if(first < last):
            a[last+1] = a[last]
            insertInOrder(element,a,first,last-1)
        else:
            a[last+1] = a[last]
            a[last] = element

def insertionSort(arr,first,last):
    print(arr,first,last)
    if(first < last):
        insertionSort(arr,first,last-1)
        insertInOrder(arr[last],arr,first,last-1)



lista = [4,3,2,1,0]
##print(lista)
insertionSort(lista,0,4)
print(lista)