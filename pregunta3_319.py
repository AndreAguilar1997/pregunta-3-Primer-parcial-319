# -*- coding: utf-8 -*-
"""
Created on Sat May 14 19:33:36 2022

@author: USER
"""

"""
Spyder Editor

This is a temporary script file.
"""
#3.	En Python realice un programa lógico de relación abuelos, nietos 
#y primos (usando librerías de Prolog)

from pyswip import Prolog
prolog = Prolog()

prolog.assertz("padres(lisa,marge,homero)")
prolog.assertz("padres(bart,marge,homero)")
prolog.assertz("padres(link,selma,anomimus)")
prolog.asserta("papa(marge,clancy)")
prolog.asserta("mama(marge,jaqueline)")
prolog.asserta("papa(selma,clancy)")
prolog.asserta("mama(selma,jaqueline)")
prolog.asserta("papa(homero,abram)")
prolog.asserta("mama(homero,mona)")
prolog.asserta("hermano(X,Y):- papa(X,P),papa(Y,P),X\=Y,!")
prolog.asserta("abuelo(A,N):- padres(N,M,P),(papa(M,A);papa(P,A))")
prolog.asserta("nieto(X,Y):-padres(X,M,P),papa(M,Y)")
prolog.asserta("primo(A,B):-padres(A,M,P),padres(B,M1,P1),(hermano(M,M1);hermano(M,P1);hermano(P,M1);hermano(P,P1))")




#list(prolog.query("padre(juan,X)"))==[{"X":"maria"},{"Y":"julio"}]

for elemento in prolog.query("papa(X,Y)"):
    print(elemento["Y"], "es el padre de ",elemento["X"])
for elemento in prolog.query("hermano(X,Y)"):
    print(elemento["X"],"es hermana ",elemento["Y"])

for elemento in prolog.query("abuelo(X,Y)"):
    print(elemento["X"],"es abuelo ",elemento["Y"])

for elemento in prolog.query("nieto(X,Y)"):
    print(elemento["X"],"es nieto ",elemento["Y"])

for elemento in prolog.query("primo(A,B)"):
    print(elemento["A"],"es primo ",elemento["B"])
    
    
    


    
    
    
    
    
    
    