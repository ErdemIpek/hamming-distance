import random

def matris_olustur():
   global A
   global B
   A = []
   B = []
   for i in range(64):
      A.append(random.randint(0,1))
      B.append(random.randint(0,1))
      
def matris_gosterimi():
   print("A matrisi:\n")
   count = 0
   for i in range(1,8):
      print(A[(i-1)*8:i*8])
      
   
   print("B matrisi:\n")
   for i in range(1,8):
      print(B[(i-1)*8:i*8])
      



def hamming(A,B):
    global uzaklik
    uzaklik = 0
    y=(zip(list(A),list(B)))
    for u,v in y:
      if u != v:
            uzaklik += 1
    return uzaklik
    

matris_olustur()
hamming(A,B)
matris_gosterimi()
print("\n\nRastgele olusturulan 2 matris arasindaki HAMMING UZAKLIGI---->{}".format(uzaklik))
input()
