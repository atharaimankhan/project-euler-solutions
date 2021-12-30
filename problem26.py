"""
Problem 26

URL: https://projecteuler.net/problem=26

"""


from utils import is_prime, print_timed


def problem26():
    # after researching about this topic i came to know that when its a prime number decimal part will always be recurring. 
    # Also from wikiepedia, i've found a farmula for finding the recurring numbers which is :
    #   ((10 ** (prime_number - 1)) - 1) / prime_number
    # 
    
    max_d = 999
    l = []

    for d in range(max_d,6,-1):
        if (is_prime(d)):
            count_zero = 0                      # problem is that when we use that farmula we dont get the first 0's after the decimal
            for s in str(1/d).split('.')[1]:    # finding how many zeros are there at the start in decimal part
                if s != '0':
                    break
                else:
                    count_zero+=1
            temp = ''
            if (count_zero >0):                                 
                temp = '0'*count_zero + str((10**(d-1) -1)//d)    
            else:
                temp = str((10**(d-1) -1)//d)
            
            s1 = temp[:len(temp)//2]
            s2 = temp[len(temp)//2:]

            if(s1 == s2):
                temp = s1
            
            l.append((d, len(temp)))
    
    
    l = max(l, key=lambda x:x[1])

    return l[0]
    
    
    
        

if __name__ == '__main__':
    
    print_timed(problem26)
