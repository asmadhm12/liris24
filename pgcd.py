


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def main():
    num1 = int(input("Entrez le premier nombre : "))
    num2 = int(input("Entrez le deuxième nombre : "))
    resultat = pgcd(num1, num2)
    print(f"Le PGCD de {num1} et {num2} est : {resultat}")

if __name__ == "__main__":
    main()
