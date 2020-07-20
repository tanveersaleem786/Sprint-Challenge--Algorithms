'''
Your function should take in a single parameter (a string word)
Your function should return a count of how many occurences of *"th"* occur within word. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    word_size = len(word)
    #print(word)
    # Base case
    if word_size == 0 or word_size < 2:
        return 0

    # Checking the substring is matches 
    if word[0 : 2] == "th":
        return count_th(word[2 : ]) + 1

    return  count_th(word[1 : ])

#word = "Hello mr smith how your wife marthew the is not the printh"
#word = "th"
#print(count_th(word))