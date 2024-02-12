########      #      ########   #     #             #   #  #     # ########   ######## ##### 
#       #    #  #    #       #   #   #              #  #    #   #  #       #  #        #    #
#       #   #    #   #       #    # #               # #      # #   #       #  #        #   #
########   ########  ########      #                #         #    ########   #######  # #
#       #  #      #  #       #     #                # #       #    #       #  #        #  # 
#       #  #      #  #       #     #                #   #     #    #       #  #        #   #
########   #      #  ########      #                #    #    #    ########   ######## #    #

import Crypto
import sys
import libnum
import math
import cmath 
import numpy as np
from sympy import symbols, div


def multiply(A, B):  ####### Function to multply 2 polynomials
    m=len(A)
    n=len(B)
    prod = [0] * (m + n - 1);  
    for i in range(m): 
        for j in range(n): 
            prod[i + j] += A[i] * B[j]; 
    return prod


def add(a,b): ####### Function to add 2 polynomials
    A=len(a)
    B=len(b)
    res=[]
    for j in range(min(A,B)):
        res.append((a[j]+b[j]))
    if(A>B):
        for j in range(B,A,1):
            res.append(a[j])
    else:
        for j in range(A,B,1):
            res.append(b[j])
    return res


def mod(a,q):
    b=[]
    for j in range(len(a)):
        b.append(a[j]%q)
    return b


def reverse(string):
    string = [string[i] for i in range(len(string)-1, -1, -1)]
    return "".join(string)


def binary_to_string(bits):
    return ''.join([chr(int(i, 2)) for i in bits])


def polymod(a,b): ###### polynomial mod polynomial
    res=[]
    for j in range(len(a)):
        poly1_reversed = a[j][::-1]
        poly2_reversed = b[::-1]
        quotient, remainder = np.polydiv(poly1_reversed, poly2_reversed)
        remainder = remainder[::-1]
        remainder = np.round(remainder, decimals=10)
        remainder_list = remainder.tolist()
        remainder_res=[]
        for k in remainder_list:
            remainder_res.append(int(k))
        res.append(mod(remainder_res,q))
    return res


def FIND1(a):  #######  When Max entered power of modulo is x^6       ENCRYPTION
    num=ord(a)
    if(num>=97 and num<=122):
        res=num-97
        return res,True
    elif(num>=65 and num<=90):
        res=num-65+26
        return res,True
    elif(num>=48 and num<57):
        res=num-48+52
        return res,True
    else:
        return -1,False


def FIND2(a): ########## When Max entered power of modulo is x^5     ENCRYPTION
    num=ord(a)
    if(num>=97 and num<=122):
        res=num-97
        return res,True
    else:
        return -1,False


def FIND3(a): ########## When Max entered power of modulo is x^4     ENCRYPTION
    num=ord(a)
    if(num>=48 and num<=57):
        res=num-48
        return res,True
    else:
        return -1,False


def DEFIND1(a):  ########## When Max entered power of modulo is x^6  DECRYPTION
    if(a>=0 and a<=25):
        return (chr(a+97))
    elif(a>25 and a<=51):
        return (chr(a+65-26))
    else:
        return (chr(a+48-52))


def DEFIND2(a):  ########## When Max entered power of modulo is x^5   DECRYPTION
    return (chr(a+97))


def DEFIND3(a): ########## When Max entered power of modulo is x^4  DECRYPTION
    return (chr(a+48))


def key_generation(q,pmod,ANS):  ########    KEY GENERATION

    n=input(("Enter the dimension of matrix A "))
    if (n==''):
        n=2
    n=int(n)
    print("YOUR VALUE OF DIMENSION IS : ",n)
    print("##########################################################################################################################################################")

    print("Enter the polynomials in the Matrix A ")
    A=[]
    x=0
    for i in range(n):
        A1=[]
        for j in range(n):
            A1.append(list(map(int,input("Enter the polynomials in the "+str(i)+"th row and "+str(j)+"th column of Matrix A in increasing order " ).strip().split())))
            if (A1==[[]]):
               x=-1
               break
        if(x==-1):
           break
        A.append(A1)
    if (A==[]):
        A=[[[11,16,16,6],[3 ,6 ,4, 9]],[[1 ,10, 3, 5],[15, 9, 1 ,6]]]
    print("YOUR VALUE OF MATRIX IS : ",A)
    print("##########################################################################################################################################################")
    
    s=[]
    for j in range(n):
        A1=(list(map(int,input("Enter the coeffecients of "+str(j)+"th polynomial of private key in increasing order " ).strip().split())))
        if(A1==[]):
            s=[[0,1,-1,-1],[0,-1,0,-1]]
            break
        s.append(A1)
    print("YOUR VALUE OF PRIVATE KEY IS : ",s)
    print("##########################################################################################################################################################")
    
    e=[]
    for j in range(n):
        A1=(list(map(int,input("Enter the coeffecients of "+str(j)+"th polynomial of error vector in increasing order " ).strip().split())))
        if(A1==[]):
            e=[[0,0,1,0],[0,-1,1,0]]
            break
        e.append(A1)
    print("YOUR VALUE OF ERROR VECTOR IS : ",e)
    print("##########################################################################################################################################################")
    
    t=[]        #################### t=A*s+e
    for i in range(n):
        sum=[0]*n
        for j in range(n):
            sum=add(sum,multiply(A[i][j],s[j]))
        sum=add(sum,e[i])
        sum=mod(sum,q)
        t.append(sum)
    t=polymod(t,pmod)
    print("YOUR VALUE OF PUBLIC KEY VECTOR IS : ",t)
    print("##########################################################################################################################################################")
    ############ public key=(A,t)
    ############ private key=(s)
    a=input("WANT TO CONTINUE WITH ENCRYPTION? PRESS 1 ....,ELSE PRESS ANY BUTTON ")
    if(a=='1'):
       print("ENCRYPTION PROCESS IS STARTING!!!!!!")
       encryption(A,t,n,q,pmod,s,ANS)
    else:
        print("EXITING!!!!!!")


def encryption(A,t,n,q,pmod,priv,ANS): ##########    ENCRYPTION

    r=[]
    for j in range(n):
        A1=(list(map(int,input("Enter the coeffecients of "+str(j)+"th polynomial of randomizer polynomial in increasing order ").strip().split())))
        if(A1==[]):
            r=[[0,0,1,-1],[-1,0,1,1]]
            break
        r.append(A1)
    print("YOUR VALUE OF RANDOMIZER POLYNOMIAL IS : ",r)
    print("##########################################################################################################################################################")
    
    e1=[]
    for j in range(n):
        A1=(list(map(int,input("Enter the coeffecients of "+str(j)+"th polynomial of error vector in increasing order ").strip().split())))
        if(A1==[]):
            e1=[[0,1,1,0],[0,0,1,0]]
            break
        e1.append(A1)
    print("YOUR VALUE OF ERROR VECTOR IS : ",e1)
    print("##########################################################################################################################################################")
    
    e2=(list(map(int,input("Enter the coeffecients of error polynomial in increasing order ").strip().split())))
    if(A1==[]):
        e2=[0,0,-1,-1,]
    print("YOUR VALUE OF ERROR POLYNOMIAL IS : ",e2)
    print("##########################################################################################################################################################")
    
    u=[]
    for j in range(n):
        sum=[0]*n
        for k in range(n):
            sum=add(sum,multiply(A[k][j],r[k]))
        sum=mod(add(sum,e1[j]),q)
        u.append(sum)
    u=polymod(u,pmod)
    
    v=[0]
    for k in range(n):
        v=mod(add(multiply(r[k],t[k]),v),q)
    v=add(v,e2)
    v1=[]
    v1.append(v)
    v=polymod(v1,pmod)
    V=[]

    if(ANS==0):
        S=input("ENTER THE MESSAGE TO BE ENCRYPTED ")
        print("YOUR MESSAGE IS: ",S)
        for j in S:
            a1=[]
            A1=[]
            s=(bin(ord(j))[2:].zfill(8))
            for k in s:
                if(k=='1'):
                    A1.append((q//2)*1)
                else:
                    A1.append((q//2)*0)
            A1=A1[::-1]
            a1.append(A1)
            A1=polymod(a1,pmod)
            V.append(mod(add(v[0],A1[0]),q))
    elif(ANS==1):
        S=input("ENTER THE MESSAGE TO BE ENCRYPTED WWHICH CAN ONLY BE (A-Z) AND (a-z) OR (0-9) AS RANGE IS ONLY 64 CHARS ")
        print("YOUR MESSAGE IS: ",S)
        for j in S:
            a1=[]
            A1=[]
            s1,flag=FIND2(j)
            s=bin(s1)[2:]
            if (flag==False):
                print("READ INSTRUCTIONS!!!!")
                return
            for k in s:
                if(k=='1'):
                    A1.append((q//2)*1)
                else:
                    A1.append((q//2)*0)
            A1=A1[::-1]
            a1.append(A1)
            A1=polymod(a1,pmod)
            V.append(mod(add(v[0],A1[0]),q))
    elif(ANS==2):
        S=input("ENTER THE MESSAGE TO BE ENCRYPTED WHICH CAN BE ONLY (a-z) AS RANGE IS ONLY 32 CHARS ")
        print("YOUR MESSAGE IS: ",S)
        for j in S:
            a1=[]
            A1=[]
            s1,flag=FIND2(j)
            s=bin(s1)[2:]
            if (flag==False):
                print("READ INSTRUCTIONS!!!!")
                return
            for k in s:
                if(k=='1'):
                    A1.append((q//2)*1)
                else:
                    A1.append((q//2)*0)
            A1=A1[::-1]
            a1.append(A1)
            A1=polymod(a1,pmod)
            V.append(mod(add(v[0],A1[0]),q))
    elif(ANS==3):
        S=input("ENTER THE MESSAGE TO BE ENCRYPTED WHICH CAN BE ONLY (0-9) AS RANGE IS ONLY 16 CHARS ")
        print("YOUR MESSAGE IS: ",S)
        for j in S:
            a1=[]
            A1=[]
            s1,flag=FIND3(j)
            s=bin(s1)[2:]
            if (flag==False):
                print("READ INSTRUCTIONS!!!!")
                return
            for k in s:
                if(k=='1'):
                    A1.append((q//2)*1)
                else:
                    A1.append((q//2)*0)
            A1=A1[::-1]
            a1.append(A1)
            A1=polymod(a1,pmod)
            V.append(mod(add(v[0],A1[0]),q))
    
    print("YOUR VALUE OF POLYNOMIAL VECTOR CIPHERTEXT IS : ",u)
    print("##########################################################################################################################################################")
    
    print("YOUR VALUE OF POLYNOMIAL CIPHERTEXT IS : ",V)
    print("##########################################################################################################################################################")
    
    a=input("WANT TO CONTINUE WITH DECRYPTION? PRESS 1 ....,ELSE PRESS ANY BUTTON ")
    if(a=='1'):
       print("DECRYPTION PROCESS IS STARTING!!!!!!")
       decryption(A,t,n,q,pmod,priv,u,V,ANS)
    else:
        print("EXITING!!!!!!")


def decryption(A,t,n,q,pmod,s,u,V,ANS):

    sum=[]
    for k in range(n):
        sum=mod(add(multiply(s[k],u[k]),sum),q)
    S=[]
    for j in sum:
        S.append(-1*j)
    sum=[]
    sum=mod(S,q)
    sum1=[]
    sum1.append(sum)
    sum=polymod(sum1,pmod)

    input=""
    for j in range(len(V)):
        mn=mod(add(V[j],sum[0]),q)
        RES=""
        for k in mn:
            if (k>(q//2)):
                if((q-k)>(k-q//2)):
                    RES=RES+'1'
                else:
                    RES=RES+'0'
            else:
                if(k>(q//2-k)):
                    RES=RES+'1'
                else:
                    RES=RES+'0'
        RES=reverse(RES)
        result=int(RES,2)
        if(ANS==0):
            input=input+chr(result)
        elif(ANS==1):
            input=input+DEFIND1(result)
        elif(ANS==2):
            input=input+DEFIND2(result)
        elif(ANS==3):
            input=input+DEFIND3(result)

    print(input)


if __name__=='__main__':
    
    print("IF YOU WANT AN EXAMPLE JUST KEEP PRESSING ENTER FOR DEFAULT VALUES ----->>>>>>.....")
    q=(input("Enter the coeffecient modulus for BABY-KYBER "))
    if(q==''):
        q=17
    q=int(q)
    print("YOUR VALUE OF COEFFECIENT MODULUS IS : ",q)
    print("##########################################################################################################################################################")

    pmod=list(map(int,input("Enter the coeffecients of the polynomial modulus in increasing powers ").strip().split()))
    if (pmod==[]):
        pmod=[1,0,0,0,1]
    print("YOUR VALUE OF POLYNOMIAL MODULUS IS : ",pmod)
    print("##########################################################################################################################################################")
    
    for j in range(len(pmod)):
        if pmod[j]==1:
            a=j
    if(a>6):
        ANS=0
        print("KEY GENERATION PROCESS IS STARTING!!!!!!!")
        key_generation(q,pmod,ANS)
    elif a==6:
        ANS=1
        print("KEY GENERATION PROCESS IS STARTING!!!!!!!")
        key_generation(q,pmod,ANS)
    elif a==5:
        ANS=2
        print("KEY GENERATION PROCESS IS STARTING!!!!!!!")
        key_generation(q,pmod,ANS)
    elif a==4:
        ANS=3
        print("KEY GENERATION PROCESS IS STARTING!!!!!!!")
        key_generation(q,pmod,ANS)
    else:
        print("With "+str(2**(a+1))+" possibilites you wont be able to encrypt the whole printable ascii letters")    
