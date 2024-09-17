# Jak kód využít
## Zpuštění kódu
Pro zpuštění kódu potřebujete nainstelovat python. K tomu použijte odkaz na webu https://www.python.org/downloads/. Poté s pomocí python idle otevřte tento program.
## Využití kódu
Kód lze využít na ukládání dat, ve fromátu tak, aby se v něm dalo rychle vyhledávat, i při velkém množství dat. 
Například pokud sbíráte velké množství dat, a chcete vědět nejvyšší hodnotu která se vyskytla.
# Funkce programu
## Jak Strom funguje?
Nejdříve vytvoříte nový strom pomocí funkce _hlava=Head()_, kde __hlava__ je méno daného stromu__.Poté na strom můžete volat potřebné funkce. Halava ukazuje na kořen stromu, kořen se může měnit, proto pro označení stromu používám hlavu. Po zavolání libovolné funkce, která změní počet uzlů ve stromě, se strom sám automaticky opraví tak aby byl částečně vyvážený, to zajištuje rychlost operací.
## Vkládání do Stromu
### Vložení uzlu
Pro přidání uzlu s hodnotou __value__ do stromu použijte funkci _Pridej(hlava, value)_. 
### Vložení více uzlů najednou
Pokud chcete vložit více uzlů současně můžete použít funkci _PridejH(hlava, seznam)_. Tato funkce rozdělí __seznam__, podle mezer, na jednotlivé hodnoty a ty vloží do stromu.
## Hledání ve stromu
### Maxima, minima
Pro nalezení maxima/minima použijeme respektivní funkce _Max(hlava)/Min(hlava)_.
### Obsahuje daný strom hodnotu?
Pokud chctee vědět zda daný stom obsahuje specifickou hodnotu mmůžeme použít funkci _IsxIn(hlava)_. Funkce vrací hodnoty __True/False__.
## Odstranováí ze stromu
### Odstranění uzlu
Funkce _Odstran(Head, value)_ odstraní uzel s __value__ ze stromu, pokud strom danou funkc obsahuje.
### Odstranování více uzlů ze stromu
Pokud chcete odstranit více uzlů současně můžete použít funkci _OdstranH(hlava, seznam)_. Tato funkce rozdělí __seznam__, podle mezer, na jednotlivé hodnoty a ty vloží do stromu.
### Odstraňování maxima/minima
Pokud potřebujete můžete rovnou odstranit maximum/minimum využitím funkce _OdstranMin(hlava)/OdstranMin(hlava)_. Pozor funkce nevrací odstranenou hodnotu!
## Vypisování stromu
Pro vypsání stromu, lze použít funkci _Vypis(hlava)_ která strom vypíše. Také lze využít funkce _OdstranaVypis(hlava, value)_ nebo _PridejaVypis(hlava, value)_ ktere nejdrive provedou svoji příslušnou operaci Pridej/odstran a poté strom také vypíší.
# Demonstrace kódu
Funkce _Test()_ provede několik základních funkcí pro demonstraci kódu. Provede tyto operace:
1. Vytvoří strom s názvem K
2. do stromu vloží uzli s hodnotami __1, 5, 10, 8, 25. 41. 23. 24. 45. 54. -2 a 0__
3. Odstraní uzle s maximální a minimální hodnotou
4. Strom vypíše
5. Vypíše minimum ve stromě
6. Přidá uzel s hodnotou __12__ a strom opět vypíše
