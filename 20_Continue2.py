#Lindo devorador de vocales
palabra = input("Introduce una palabra: ")
palabra = palabra.upper()

word_without_vowels = ""

for letra in palabra:
    if letra in "AEIOU":
        continue
    word_without_vowels += letra

print(word_without_vowels)