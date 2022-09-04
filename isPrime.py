

def isPrime(number: int) -> bool:
    prime = False
    if number > 1:
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break

    return prime

if __name__ == "__main__":
    x = isPrime()
    print("is Prime?", x)