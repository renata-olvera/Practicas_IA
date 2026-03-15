def primo(n):
    if n < 2:
        return False

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True


for i in range(1, 20):
    if primo(i):
        print(i, end=" ")

print()