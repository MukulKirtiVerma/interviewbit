# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:41:53 2020

@author: Mukul Kirti Verma
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        a=A
        
        i=0
        if(max(a)<0):
            return []
        while(a[i]<0):
            i+=1
        #ok
        temp=a[i]
        b=[]
        d=[]
        
        b.append(a[i])
        d=b
        mx=a[i]
        i+=1
        while(i<len(a)):
            if(a[i]>=0):
                temp=temp+a[i]
                b.append(a[i])
                if(mx<=temp):
                    mx=temp
                    if(sum(d)==sum(b) and len(d)>len(b)):
                        continue
                    d=b
                i+=1
                
            else:
                temp=0
                b=[]
                i+=1
                
        return d
                
                
                
                
                