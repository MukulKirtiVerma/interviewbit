# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 22:33:47 2020

@author: Mukul Kirti Verma
"""

a=[1, 3, -1]
a=[ 55, -8, 43, 52, 8, 59, -91, -79, -18, -94 ]
a= [ 84, -65, 10, 0, 36, -98, -2, -47, 47, -99 ]
a= [ 2, 2, 2 ]

"""
if(min(a)<0):
    a=[i+(-1*min(a)) for i in a]"""
#c=[i+j for i , j in enumerate(a)]
#d=[j-i for i , j in enumerate(a)]
c=[]
d=[]
#append index sun and sub
for i,j in enumerate(a):
    c.append(i+j)
    d.append(j-i)
mx=d.index(max(d))+1-1
mi=len(a)-d[::-1].index(min(d))-1
aa=(abs(a[mx]-a[mi])+abs(mx-mi))

mx=c.index(max(c))+1-1
mi=len(a)-c[::-1].index(min(c))-1
bb=(abs(a[mx]-a[mi])+abs(mx-mi))
return max(aa,bb)