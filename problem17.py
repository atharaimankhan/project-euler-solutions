"""
Problem 17:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

URL: https://projecteuler.net/problem=17

"""


from utils import print_timed

def problem17():
    sum=0
    num_words = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }
    for i in range(1,1001):
        
        if i<=20:
            sum+=len(num_words[i])
        
        elif i<100:
            temp = str(i)
            sum+=len(num_words[int(temp[0]+'0')]+num_words[int(temp[1])])

        elif i<1000:
            temp = str(i)
            if temp[1]==temp[2]=='0':
                sum+=len(num_words[int(temp[0])]+'hundred')
            elif int(temp[1]+temp[2])<=20:
                sum+=len(num_words[int(temp[0])]+'hundred'+'and'+num_words[int(temp[1]+temp[2])])
            else:
                sum+=len(num_words[int(temp[0])]+'hundred'+'and'+num_words[int(temp[1]+'0')]+num_words[int(temp[2])])
        
        elif i==1000: 
            sum+=len('oneThousand')
    
    return sum

if __name__ == '__main__':
    
    print_timed(problem17)
