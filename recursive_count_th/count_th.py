'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
   
    # occur = 0
    i = word.find("th")
    # print(i)
    if i == -1:
        print(i)
        return 0
    g = 1 + count_th(word[i + 2: ])

    return g
    # TBC
print(count_th("thdatestthisthhardth"))