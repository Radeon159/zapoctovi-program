class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

        
    def to_string(self, level = 0):
        strings = []
        if self.right is not None:
            strings.append(self.right.to_string(level + 1))
        strings.append(' ' * 4 * level + '-> ' + str(self.data))
        if self.left is not None:
            strings.append(self.left.to_string(level + 1))
        return "\n".join(strings)

class Head:
    #Vytvoření hlavy stromu, která ukazuje na jeho kořen.
    #Pokud chci zavolat funci na strom, budu volat jeho "hlavu".
    #Tím odpadá problém volání funkce na prázdný strom, nebo pokud se mění kořen stromu, kvůli otáčení.
    #každá funkce má dvě části jednu pro hlavu, a jednu pro strom, která je rekurzivně volána postupně na každý potřebný vrchol stromu.
    def __init__(self):
        self.root=None

def Vypis(x):
    #K vypsání stromu jsem použil vaši funkci ze cvičení
    if x.root==None:
        print("prázdný strom")
    else:
        print(x.root.to_string())

def Pridej(x, value):
    #Pridá do stromu nový vrchol s danou hodnotou
    if x.root==None:
        x.root=Node(value)
    else:
        x.root=PridejS(x.root, value)

def PridejaVypis(x, value):
    if x.root==None:
        x.root=Node(value)
    else:
        x.root=PridejS(x.root, value)
    Vypis(x)

def PridejH(x, seznam):
    #Pro přidávání velkého množství dat najednou
    seznam=seznam.split()
    for i in seznam:
        i=int(i)
        Pridej(x, i)

def PridejS(x, value):
    #nejříve hledám správnou pozici kam vložit nový vrchol, tak aby byl strom vyhledávací
    #vždy vklám nový vrchol jako list stromu
    if value<=x.data:
        if x.left==None:
            x.left=Node(value)
        else:
            x.left=PridejS(x.left, value)
    else:
        if x.right==None:
            x.right=Node(value)
        else:
            x.right=PridejS(x.right, value)
    #poté procházím strom zpět ke kořenu a kontroluji zda se jedná o AVL strom, pokud ne provedu příslušnou rotaci pro zajištění vyváženosti
    x.height=1+max(GetHeight(x.left), GetHeight(x.right))
    balance=GetBalance(x)
    if balance >= -1 and balance <= 1:
        return(x)
    if balance >1 and value < x.left.data:
        y = RightTurn(x)
        return (y)
    if balance < -1 and value > x.right.data:
        y = LeftTurn(x)
        return (y)
    if balance >1 and value > x.left.data:
        x.left=LeftTurn(x.left)
        y=RightTurn(x)
        return(y)
    if balance <-1 and value < x.right.data:
        x.right=RightTurn(x.right)
        y=LeftTurn(x)
        return(y)

def GetHeight(x):
    #vrací výšku ve které se nachází daný vrchol
     if x != None:
         return(x.height)
     else:
         return(0)
        
def GetBalance(x):
    #vrací rozdíl ve výškách podstromů daného vrcholu
    if x != None:
        return(GetHeight(x.left)-GetHeight(x.right))
    
def RightTurn(x):
    #otáčení vrcholů stromu pro zajištění vyváženosti
    y=x.left
    z=y.right
    y.right=x
    x.left=z
    x.height=1+max(GetHeight(x.left), GetHeight(x.right))
    y.height=1+max(GetHeight(y.left), GetHeight(y.right))
    return(y)

def LeftTurn(x):
    #otáčení vrcholů stromu pro zajištění vyváženosti
    y=x.right
    z=y.left
    y.left=x
    x.right=z
    x.height=1+max(GetHeight(x.left), GetHeight(x.right))
    y.height=1+max(GetHeight(y.left), GetHeight(y.right))
    return(y)

def Odstran(x, value):
    if x.root==None:
        return("Prázdný strom")
    elif IsxInS(x.root, value): # nejdříve zjistím zda strom daný vrchol vůbec obsahuje
        x.root=OdstranS(x.root, value)
    else:
        return("strom neobsahuje danou hodnotu")
    
def OdstranH(x, seznam):
    #slouží pro odstranění velkého množstvího vrcholů
    seznam=seznam.split()
    for i in seznam:
        i=int(i)
        Odstran(x, i)
        
def OdstranS(x, value):
    # Nejdříve najdu kde vrchol leží
    if x.data > value:
        x.left=OdstranS(x.left, value)
    elif x.data < value:
        x.right=OdstranS(x.right, value)
    else: #Po nalezení vrchol odstraním jedním ze 3 způsobů, podle počtu synů, které daný vrchol má
        if x.left==None and x.right ==None:
            return(None)
        elif x.left==None:
            return(x.right)
        elif x. right== None:
            return(x.left)
        else:
            tempvalue=MinimumS(x.right)
            x.data=tempvalue
            x.right=OdstranS(x.right, tempvalue)
            x.height=1+max(GetHeight(x.left), GetHeight(x.right))
            return(x)
    #poté procházím strom zpět ke kořenu a kontroluji zda se jedná o AVL strom, pokud ne provedu příslušnou rotaci pro zajištění vyváženosti
    x.height=1+max(GetHeight(x.left), GetHeight(x.right))
    balance=GetBalance(x)
    if balance >= -1 and balance <= 1:
        return(x)
    if balance >1:
        balancepod=GetBalance(x.left)
        if balancepod >=0:
            y=RightTurn(x)
            return(y)
        else:
            x.left=LeftTurn(x.left)
            y=RightTurn(x)
            return(y)
    if balance< -1:
        balancepod=GetBalance(x.right)
        if balancepod <=0:
            y=LeftTurn(x)
            return(y)
        else:
            x.right=RightTurn(x.right)
            y=LeftTurn(x)
            return(y)
    
#Odstranění minima a maxima
def OdstranMax(x):
    if x.root==None:
        return("prázdný strom")
    M=MaximumS(x.root)
    x.root=OdstranS(x.root, M)

def OdstranMin(x):
    if x.root==None:
        return("prázdný strom")
    m=MinimumS(x.root)
    x.root=OdstranS(x.root, m)

#zjišťuje zda je strom vyvážený
def IsAVL(x):
    return(IsAVLS(x.root))

def IsAVLS(x):
    if x==None:
        return(True)
    AVLl = IsAVLS(x.left)
    AVLr = IsAVLS(x.right)
    delta=GetBalance(x)
    if AVLl==True and AVLr==True and delta>=-1 and delta<=1:
        return(True)
    else:
        return(False)

#Hledá nejvetší hodnotu ve stromu
def Max(x):
    if x.root==None:
        return("prázdný strom")
    else:
        return(MaximumS(x.root))

def MaximumS(x):
    while x.right !=None:
        x=x.right
    return(x.data)

#Hledá nejmenší hodnotu ve stromu
def Min(x):
    if x.root==None:
        return("prázdný strom")
    else:
        return(MinimumS(x.root))

def MinimumS(x):
    while x.left!=None:
        x=x.left
    return(x.data)

#Hledá zda se nachází daná hodntota ve stromě
def IsxIn(x, value):
    if x.root==None:
        return("prázdný strom")
    else:
        return(IsxInS(x.root, value))

def IsxInS(x, hodnota):
    if x==None:
        return(False)
    if x.data > hodnota:
        if x.left ==None:
            return(False)
        else:
            return(IsxInS(x.left, hodnota))
    elif x.data < hodnota:
        if x.right ==None:
            return(False)
        else:
            return(IsxInS(x.right, hodnota))
    else:
        return(True)



K=Head() #vytvořím prázdný strom
