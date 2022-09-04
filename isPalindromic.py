
def isPalindromic(number: int) -> bool:
    isPalindromic = False
    strNumber = str(number)
    reversedStrNumber = strNumber[::-1]
    if strNumber == reversedStrNumber:
        isPalindromic = True

    return isPalindromic

if __name__ == "__main__":
    print(isPalindromic(99999999))