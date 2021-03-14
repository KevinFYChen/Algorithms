#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:54:58 2020

@author: kevinchen

This program takes 2 n*n square matrices and computes matrix multiplication 
using both the Strassen's algorithm and the ordinary iterative approach. 
This program prints the input matrices and the resulting product matrix 
to standard output along with the number of multiplications computed 
in each method. 
"""
import argparse
import math
import sys
import copy
import numpy as np


#The main function handles the inputs and outputs of this program. It takes in
#a text stating the order of the square matrix followed by matrix A and matrix 
#B and outputs the product of matrix A and B. This program can take in 
#multiple inputs and return the results for each of the inputs. Upon 
#encountering an invalid input, it prints an error message to standard output 
#and terminates the program.

#This main function also handles errors. If it encounters an invalid value in 
#the matrix or in the order, it will handle it appropriately. It also checks 
#whether the order is a power of 2. If it isn't, then it will print out an 
#error message and stop the program

def main(): 
    parser = argparse.ArgumentParser( description="Multiplies 2 square " 
                                     "matrices with an order that is a " 
                                     "power of 2")

    parser.add_argument('-i', '--input_file', type=str, required=True, help=
                        "Path to an input file to be read")
    args = parser.parse_args()
    fh = open( args.input_file, 'r' )
    
    beginning=True
    order=None
    count=0
    numMat=0
    
    for line in fh:
        line=line.strip()
        #taking in the order of the matrices at the beginning of an entry
        if beginning==True:
            if len(line)==0:
                continue
            if len(line.split())!=1:
                print("{0}".format(line))
                print("invalid input: order of matrix must be a single " 
                      "positive integer")
                sys.exit()
            try:
                order=int(line)
            except:
                print("{0}".format(line))
                print("invalid input: the order of the matrix is not "
                      "an integer")
                sys.exit()
            if order<1:
                print("{0}".format(line))
                print("invalid input: the order of the matrix should "
                      "be >=1")
                sys.exit()
            if log2(order)%1 !=0:
                print("{0}".format(line))
                print("order is not a power of 2")
                sys.exit()
            tmp=np.zeros(shape=(order,order))
            beginning=False
            continue
        try:
            l = [int(num) for num in line.split()]
        except:
            print("{0}\n{1}".format(order,line))
            print("invalid input: matrix contains non-integer values")
            sys.exit()
        if len(l)!=order:
            print("{0}\n{1}".format(order,line))
            print("error - order: {0}, number of integers in line: {1}"
                  .format(order, len(l)))
            sys.exit()
        tmp[count]=l
        count+=1
        if count==order:
            #when count==order, a matrix is fully constructed, if we have 
            #contructed 2 matrices at this point then we are done with 
            #construction and can go on to compute matrix multiplication. 
            #If we have only constructed 1 matrix, then we have to finish the 
            #other matrix
            if numMat==0:
                numMat+=1
                A=copy.deepcopy(tmp)
            else:
                B=copy.deepcopy(tmp)
                print("order: {0}\nA:\n {1}\nB:\n{2}".format(order,A,B))
                scount,C=strassen(A,B)
                ocount,C_2=ord_mult(A,B)
                print("product:\n{0}".format(C))
                print("number of multiplications: Strassen's={0}, "
                      "ordinary={1}\n".format(scount,ocount))
                order=None
                beginning=True
                numMat=0
            count=0

                   

#This function returns the logarithm of a value, base 2. If the return value
#is not an integer then we know that the value is not a power of 2
def log2(x): 
    return (math.log10(x) / 
            math.log10(2)); 



#This function implements the Strassen's algorithm using recursion. The number 
#of multiplications used in this function are counted
def strassen(a,b):
    n=len(a)

    if n==1:
        product=int(a[0,0])*int(b[0,0])
        scount=1
        return scount,product
    else:
        n=n//2
        a11=a[0:n,0:n]
        a12=a[0:n,n:]
        a21=a[n:,0:n]
        a22=a[n:,n:]
        b11=b[0:n,0:n]
        b12=b[0:n,n:]
        b21=b[n:,0:n]
        b22=b[n:,n:]
        
        s1=b12-b22
        s2=a11+a12
        s3=a21+a22
        s4=b21-b11
        s5=a11+a22
        s6=b11+b22
        s7=a12-a22
        s8=b21+b22
        s9=a11-a21
        s10=b11+b12
        
        p1_c,p1=strassen(a11,s1)
        p2_c,p2=strassen(s2,b22)
        p3_c,p3=strassen(s3,b11)
        p4_c,p4=strassen(a22,s4)
        p5_c,p5=strassen(s5,s6)
        p6_c,p6=strassen(s7,s8)
        p7_c,p7=strassen(s9,s10)
        
        scount=p1_c+p2_c+p3_c+p4_c+p5_c+p6_c+p7_c

        C11=p5+p4-p2+p6
        C12=p1+p2
        C21=p3+p4
        C22=p5+p1-p3-p7
        
        #if C11,C12,C21 and C22 are integers, then combine them into a 2d 
        #array. Otherwise, concatenate the 4 submatrices into 1
        if type(C11)==int:
            C=np.array([[C11,C12],[C21,C22]])
        else:
            C=np.concatenate((np.concatenate((C11,C12),axis=1),
                              np.concatenate((C21,C22),axis=1)),axis=0)

    return scount,C;    


#This function implements the ordinary matrix multiplcation using the 
#iterative approach. The number of multiplications used in this function are 
#counted
def ord_mult(a,b):
    n=len(a)
    ocount=0
    C=np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i,j]=C[i,j]+a[i,k]*b[k,j]
                ocount+=1
    return ocount,C;


if __name__ == '__main__':
    main()
                                                                               
   