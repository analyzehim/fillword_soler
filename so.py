#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
a='Привет'
print a.decode('utf-8')
'''
def create_mat():
    f = open('mat.txt', 'r')
    for s in f:
        size=len(s)-1
        break
    f.close()
    print size
    f = open('mat.txt', 'r')
    A = [[0 for x in range(size)] for x in range(size)]
    i=-1
    j=0
    for s in f:
        i+=1
        j=0
        if s[len(s)-1]=='\n':
            for let in s[0:len(s)-1]:
                A[i][j]=let
                j+=1
        else:
           for let in s:
                A[i][j]=let
                j+=1
    f.close()
    return A
def create_set():
    a=set()
    f = open('text.txt', 'r')
    for s in f:
        #a.add(s[0:len(s)-1])
        if s[len(s)-1]=='\n':
            a.add(s[0:len(s)-1])
        else:
           a.add(s)
    f.close()
    return a

def print_list(A):
    s=''
    for i in range(len(A)):
             s+= str(A[i])+' '
    print s[0:len(s)-1]
def print_mat(A):
    for i in range(len(A[0])):
            print_list(A[i])
def print_set(A):
    for i in A:
        print i

def not_null(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j]!=0:
                return True
    return False
        

def search(s,set_words,A,B,i,j,size):
    s+=(A[i][j])
    if len(s)==size:
        
        if s in set_words:
                print s, j+1,i+1
          # print_mat(B)
                return
                '''
                if len(s)>7:
                    global mask
                    for i in range(len(A)):
                        for j in range(len(A)):
                            mask[i][j]=B[i][j]
                    print_mat(mask)
                '''
        
        return ;
    B[i][j]=1
    if (i<len(A)-1) :
        if  B[i+1][j]==0:
            search(s,set_words,A,B,i+1,j,size)
  
    if (j<len(A)-1):
        if  B[i][1+j]==0:
            search(s,set_words,A,B,i,j+1,size)

    if (i>0):
        if  B[i-1][j]==0:
            search(s,set_words,A,B,i-1,j,size)
           
    if (j>0):
        if  B[i][j-1]==0:
            search(s,set_words,A,B,i,j-1,size)
    B[i][j]=0
   
    return
#mask=[[0 for x in range((7))] for x in range(7)]
def go():
    A = create_mat()
    print_mat(A)
    set_words=create_set()
    B = [[0 for x in range(len(A))] for x in range(len(A))]
    
    s=''
    global mask
    for size in range(5,12):    
        for i in range(len(A)):
            for j in range(len(A)):
                count=1
                #size1=13-size
                search(s,set_words,A,B,i,j,size)
                #print mask

    





go()
