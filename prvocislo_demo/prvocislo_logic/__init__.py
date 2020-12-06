"""
prvocislo.py
Autor: Klimeková Barbora, Kubásková Lucia, Příkaský Tomáš
Vytvoř program, který vyhodnotí,
zdali je vložené číslo prvočíslo.
Prvočísla mají právě dva dělitele,
jsou dělitelná pouze 1 a sami sebou.
"""

cislo = input("Vlož číslo: ")

if cislo.isdigit() and int(cislo) > 0:
    cislo = int(cislo)
    delitele = []
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            delitele.append(i)
    print(f"Dělitelé: {delitele}")
    if len(delitele) == 2:
        print(f"Číslo {cislo} je prvočíslo.")
    else:
        print(f"Číslo {cislo} není prvočíslo.")
else:
    print("Nebylo zadáno kladné číslo.")