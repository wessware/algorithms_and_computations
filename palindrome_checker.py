def palindrome(s, startIndex, endIndex, subs):

    result = ""
    for i in range(startIndex):
        if _isPalindrome(s[startIndex[i]:endIndex[i]], subs[i]):
            result += "1"
        else:
            result += "0"

    return result

def _isPalindrome(s, subs):

    n = len(s)
    count = 0
    for i in range(n //2):
        if s[i] != s[n-i-1]:
            count += 1

    if count <= subs:
        return True
    else:
        return False