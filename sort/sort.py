#! /usr/bin/env python2.7
import random

def randdata():
    arr = []
    i, num = 0, 10
    while i < num:
        arr.append(random.randint(0,100))
        i += 1 
    return arr


def bubble_sort(arr):
    if len(arr)<2:
        return arr
    for i in xrange(len(arr)-1):
        for j in xrange(len(arr[i:])-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr

def insert_sort(arr):
    if len(arr)<2:
        return arr
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def select_sort(arr):
    if len(arr)<2:
        return arr
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

def binsearch(arr,value):
    first = 0
    last = len(arr)-1
    while first <= last:
        middle = first + (last - first)//2
        middlevalue = arr[middle]
        if middlevalue < value:
            first = middle + 1
        elif middlevalue > value:
            last = middle -1
        else:
            return middle
    return -1
