# Python program to compute the sum of digits of each number whether postive or negative in a given list.. 
# below are the lists
#LIS = [10, 2, 56] 
#LIS2 = [10, 20, 4, 5, 'b', 70, 'a']
#LIS3 = [10, 20, -4, 5, -70]
LIS4 = [2,-5667,10]
a=[]
def length_of_num(i):
    counter = 0
    n=1
    while(i!=0):
        n=abs(i)%10
        a.append(n)
        i=abs(i)//10
        counter+=1
    return counter


n=0
digits=[]
x=0
for i in LIS4:
    if type(i) == int:
        while(i>0):
            n = i%10
            digits.append(n)
            i = i//10
        while(i<0):        
            i = abs(i)
            n=i%10
            for x in range(length_of_num(i)):
                count = length_of_num(i)
                if x  == count-1: 
                    if count == 1:
                        digits.append(-i)
                    else:
                        digits.append(n)        
              
            i= i//10  
            i = -i
    else:
        pass

print(sum(digits))
print(digits)