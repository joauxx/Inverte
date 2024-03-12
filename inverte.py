def inverte(string):
    invertido = ""
    for char in string:
        invertido = char + invertido
    return invertido

def main():
    string = input("Digite uma String: ")
    invertido = inverte(string)
    print("Invertido:", invertido)

if __name__ == "__main__":
    main()
