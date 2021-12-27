"""
Problem 22

URL: https://projecteuler.net/problem=22

"""


from utils import print_timed


letter_scores = {}
def get_score(name:str):
    score =0
    for letter in name:
        score += letter_scores[letter]

    return score

def problem22():

    names_string = ''
    global letter_scores
    sum_of_all_name_scores= 0
    with open('p022_names.txt', 'r') as f:
        names_string = f.read()
    
    
    for i, ascii in enumerate(range(65, 91)):
        letter_scores[''.join(chr(ascii))] = i+1


    names = list(map(lambda x:x.strip("\""),names_string.split(',')))
    names.sort()

    for i in range(len(names)):
        sum_of_all_name_scores += get_score(names[i])*(i+1)
    

    return  sum_of_all_name_scores
    
if __name__ == '__main__':
    
    print_timed(problem22)
