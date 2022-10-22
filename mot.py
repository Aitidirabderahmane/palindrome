def palindrome(c):
    i = 0
    j = len(c)-1
    while((c[i] == c[j]) and (i<j)):
        i += 1
        j -= 1
    if(i>j):
        print("la chaine",c,"est une chaine palindrome")
    else:
        print("la chaine",c,"n'est pas une chaine palindrome")

#test de le fonction palindrome
palindrome("abaa")