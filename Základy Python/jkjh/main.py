def diskriminant(cislo1,cislo2,cislo3)

    
for a in range(-3, 3, 2):
    for b in range(-3, 3, 2):
        for c in range(-3, 3, 2):
            D, reseni = diskriminant(a, b, c)
            stav = "má" if reseni else "nemá"
            print(f"Diskriminant funkce {a}x²{b:+}x{c:+} je {D}, takže rovnice {stav} řešení v ℝ")