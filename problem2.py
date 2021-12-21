"""Problem 2"""


from utils import print_timed


def problem2(n1=1, n2=2):

    sum = 0 

    if(n2 > 4000000): return 0
    sum+= n1 if n1%2==0 else 0
    sum+= n2 if n2%2==0 else 0
    
    return sum + problem2(n1+n2, n1+n2+n2)

        

if __name__ == '__main__':
    print_timed(problem2)
