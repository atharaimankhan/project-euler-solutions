"""
Problem 3:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""


from utils import print_timed

def problem4():
    palindroms = set()
    for i in range(999,0,-1):
        for j in range(999,0, -1):
            str_product = str(i*j)
            if(str_product == str_product[::-1]):
                palindroms.add(i*j)


    return sorted(palindroms)[-1]
        

if __name__ == '__main__':
    print_timed(problem4)
