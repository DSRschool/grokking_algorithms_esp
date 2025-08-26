def cuenta_atras(i): 
    print(i)
    if i <= 1:
        return
    else:
        cuenta_atras(i-1)

cuenta_atras(3)
