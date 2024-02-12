# Baby-Kyber
Baby Kyber implementation

## Intro:
Baby Kyber is the scaled down version of Kyber, meaing that the security paramters are smaller than the originally intended Kyber.  

## Explanation of the Code:  
https://github.com/7h4nd5RG0d/Baby-Kyber/blob/main/baby_kyber.py  
### 1)Initialisation:  
The code will ask you for the coeefecient modulus(q) as well as the polynomial modulus(pmod).  
![image](https://github.com/7h4nd5RG0d/Baby-Kyber/assets/128285431/26da8b41-f735-4cb7-b49f-29f4526a01ce)  
### 2)Key Generation:  
You will be prompted for the private key(s),error vector(e) and the initial matrix 'A' as input parameters.  
![image](https://github.com/7h4nd5RG0d/Baby-Kyber/assets/128285431/c34a433a-3c59-4b0f-83a1-d58dbcc08224)  
From this we will compute t=A*s+e. 
![image](https://github.com/7h4nd5RG0d/Baby-Kyber/assets/128285431/ac5c84af-6ed1-4ffc-b9c2-0121e1f2fe16)  
**Here the private key consists of (s) and the public key consists of (A,t)**  
The security of Kyber is dependent on the problem of solving for s,when A,t are given.  
### 3)Encryption:  
You will be prompted first for three inputs, namely the randomizer polynomial(r),the error vector(e1) and he error polynomial(e2).  
![image](https://github.com/7h4nd5RG0d/Baby-Kyber/assets/128285431/05fd5ec4-64a1-4d40-897f-1db4137f2378)  
Then message is taken as input.  
![image](https://github.com/7h4nd5RG0d/Baby-Kyber/assets/128285431/518a48ae-42ef-4b3e-b118-f91cd79840b1)  
The message is first converted to its polynomial representation followed by multiplication by [q/2] so that we are able to decrypt it.  
It then computes ,the polynomial vector(u)=(A')*r + e1 where A' denotes the transpose of A.  
It is followed by the calculation of v=(t')*r + e2 + m.
![image](https://github.com/7h4nd5RG0d/Baby-Kyber/assets/128285431/ebf851e1-dc66-4d93-9691-e832c128d3c1)  
**The ciphertext consists of (u,v)**   
### 4)Decryption:  
Here first it computes mn=v - (s')*u  which when simplified results in mn=(e')*r + e2 + m + (s')*e1  
![image](https://github.com/7h4nd5RG0d/Baby-Kyber/assets/128285431/58f579d0-979e-4bd2-8058-2ac18c27afb0)  
**From the above equation we can make an observation that he coeffecients of mn are either close to (0,q) or q/2 as a result of multiplication by q/2 during encryption.**    
This gives an interesting decryption scheme.  
We decrypt the coefficient as '1' if it close to q/2 and as '0' if it is more close to 0 or q.  
![image](https://github.com/7h4nd5RG0d/Baby-Kyber/assets/128285431/a3401d67-d137-42ca-86c0-9c15ba6b73ad)  

## Ouput:  
### Case 1: Default meaning pmod=x^4+1  
Therefore there are only 16 possible characters that can be encrypted as after that we get many to one encryption making it impossible to decrypt.  
Here the code only allows 0-9 as input to avoid it.  
![image](https://github.com/7h4nd5RG0d/Baby-Kyber/assets/128285431/f92b9c2c-afee-4b53-9b09-f700e872bb3d)  
### Case 2: using pmod with degree 5.
Therefore we have 32 possible characters during encryption.  
Here the code will only allow a-z as a constraint.  


