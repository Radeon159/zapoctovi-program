#
# Návod na instelaci
# Funkce
## Jak Strom funguje?

## Vkládání do Stromu
### Vložení
Pro přidání uzlu s hodnotou __value__ do stromu použijte funkci _Pridej(Head, value)_. 
### Vložení více uzlů najednou
Pokud chcete vložit více uzlů současně můžete použít funkci _PridejH(Head, seznam)_. Tato funkce rozdělí __seznam__, podle mezer, na jednotlivé hodnoty a ty vloží do stromu.
## Hledání ve stromu
### Maxima, minima
Pro nalezení maxima/minima použijeme respektivní funkce _Max(Head)/Min(Head)_.
### Obsahuje daný strom hodnotu?
okud chceme vědět zda daný stom obsahuje specifickou hodnotu mmůžeme použít funkci _IsxIn(Head)_. Funkce vrací hodnoty __True/False__.
## Odstranováí ze stromu
### Odstranění 
Funkce _Odstran(Head, value)_ odstraní uzel s __value__ ze stromu, pokud strom danou funkc obsahuje.
### Odstranování více uzlů ze stromu
Pokud chcete odstranit více uzlů současně můžete použít funkci _OdstranH(Head, seznam)_. Tato funkce rozdělí __seznam__, podle mezer, na jednotlivé hodnoty a ty vloží do stromu.
### Odstraňování maxima/minima
Pokud potřebujete můžete rovnou odstranit maximum/minimum využitím funkce _OdstranMin(Head)/OdstranMin(Head)_. Pozor funkce nevrací odstranenou hodnotu!
# Demonstrace kódu
