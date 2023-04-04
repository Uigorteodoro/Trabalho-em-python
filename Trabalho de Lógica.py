# -*- coding: utf-8 -*-
Numero = input("Digite um número: ")

if Numero < 1 or Numero > 9999:
    print "número inválido"
else:
    Numero1 = Numero / 1000
    Numeroa = Numero -(Numero1 * 1000)

    Numero2 = Numeroa / 100
    Numerob = Numeroa -(Numero2 * 100)

    Numero3 = Numerob / 10
    Numeroc = Numerob -(Numero3 * 10)

    Numero4 = Numeroc / 1

    if Numero >= 1000 and Numero <= 1999:
        milhar = "unidade de milhar"
    if Numero >= 2000 and Numero <= 9999:
        milhar = "unidades de milhar"
    if Numeroa >= 100 and Numeroa <= 199:
        centena = "centena"
    if Numeroa >= 200 and Numeroa <= 999:
        centena = "centenas"
    if Numerob >= 10 and Numerob <= 19:
        dezena = "dezena"
    if Numerob >= 20 and Numerob <= 99:
        dezena = "dezenas"
    if Numeroc == 1:
        unidade = "unidade"
    if Numeroc >= 2 and Numeroc <= 9:
        unidade = "unidades"
        
    if Numero1 == 0 and Numero2 == 0 and Numero3 == 0:
        print Numero4, unidade
        
    elif Numero2 == 0 and Numero3 == 0 and Numero4 == 0:
        print Numero1, milhar
        
    elif Numero1 == 0 and Numero2 == 0 and Numero4 == 0:
        print Numero3, dezena
        
    elif Numero1 == 0 and Numero3 == 0 and Numero4 == 0:
        print Numero2, centena

    elif Numero3 == 0 and Numero4 == 0:
        print Numero1, milhar, "e", Numero2, centena

    elif Numero1 == 0 and Numero4 == 0:
        print Numero2, centena,"e", Numero3, dezena
        
    elif Numero1 == 0 and Numero3 == 0:
        print Numero2, centena,"e", Numero4, unidade
        
    elif Numero1 == 0 and Numero2 == 0:
        print Numero3, dezena,"e",Numero4, unidade
        
    elif Numero2 == 0 and Numero3 == 0:
        print Numero1, milhar,"e", Numero4, unidade
        
    elif Numero2 == 0 and Numero4 == 0:
        print Numero1, milhar,"e", Numero3, dezena
        
    elif Numero1 == 0:
        print Numero2, centena+",", Numero3, dezena,"e", Numero4, unidade
        
    elif Numero2 == 0:
        print Numero1, milhar+",", Numero3, dezena,"e", Numero4, unidade
        
    elif Numero3 == 0:
        print Numero1, milhar+",", Numero2, centena,"e", Numero4, unidade
        
    elif Numero4 == 0:
        print Numero1, milhar+",",Numero2, centena,"e", Numero3, dezena
        
    elif Numero1 > 0 and Numero2 > 0 and Numero3 > 0 and Numero4 > 0:
        print Numero1, milhar+",",Numero2, centena+",", Numero3, dezena,"e", Numero4, unidade
