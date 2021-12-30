"""
Problem 26

URL: https://projecteuler.net/problem=26

"""


from utils import is_prime, print_timed


def problem26():
    # after researching about this topic i came to know that when its a prime number decimal part will always be recurring. 
    # Also if d is a prime number then the number of repeating digits is d-1
    # Example: 1/7 has the 7-1=6 repeating digits   (0.142857......)
    # So just need to find the largest prime number in the range
    
    max_d = 999
    l = []

    for d in range(max_d,6,-1):
        if (is_prime(d)):
            count_zero = 0
            for s in str(1/d).split('.')[1]:
                if s != '0':
                    break
                else:
                    count_zero+=1
            temp = ''
            if (count_zero >0):
                temp = '0'*count_zero + str((10**(d-1) -1)//d)    
            else:
                temp = str((10**(d-1) -1)//d)
            
            s1 = s[:len(s)//2]
            s2 = s[len(s)//2:]

            if(temp[:len(temp)//2] == temp[len(temp)//2:]):
                temp = temp[:int(len(temp)/2)]
            
            l.append((d, len(temp)))
    
    
    l = max(l, key=lambda x:x[1])

    return l[0]
    
    
    
        

if __name__ == '__main__':
    
    print_timed(problem26)
