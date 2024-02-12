# Baby-Kyber
Baby Kyber implementation

## Intro:
Baby Kyber is the scaled down version of Kyber, meaing that the security paramters are smaller than the originally intended Kyber.  

## Explanation of the Code:  
https://github.com/7h4nd5RG0d/Baby-Kyber/blob/main/baby_kyber.py  
### 1)Initialisation:  
The code will ask you for the coeefecient modulus(q) as well as the polynomial modulus(pmod).  
### 2)Key Generation:  
You will be prompted for the private key(s),error vector(e) and the initial matrix 'A' as input parameters.  
From this we will compute t=A*s+e.  
**Here the private key consists of (s) and the public key consists of (A,t)**  
The security of Kyber is dependent on the problem of solving for s,when A,t are given.  
### 3)Encryption:  
You will be prompted first for three inputs, namely the randomizer polynomial(r),the error vector(e1) and he error polynomial(e2).  
Then message is taken as input.  
The message is first converted to its polynomial representation followed by multiplication by [q/2] so that we are able to decrypt it.  
It then computes ,the polynomial vector(u)=(A')*r + e1 where A' denotes the transpose of A.  
It is followed by the calculation of v=(t')*r + e2 + m.
**The ciphertext consists of (u,v)**   
### 4)Decryption:  
Here first it computes mn=v - (s')*u  which when simplified results in mn=(e')*r + e2 + m + (s')*e1  
**From the above equation we can make an observation that he coeffecients of mn are either close to (0,q) or q/2 as a result of multiplication by q/2 during encryption.**    
This gives an interesting decryption scheme.  
We decrypt the coefficient as '1' if it close to q/2 and as '0' if it is more close to 0 or q.  





