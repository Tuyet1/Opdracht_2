#!/usr/bin/python
import sys

welcomeMessage = "Welkom bij de Valori FST intake opdracht. Werk zorgvuldig en netjes, succes!"
motivatie =  " Mijn naam is tuyet en FST is waar ik thuis hoor. Graag wil ik u bedanken voor uw aandacht en overweging. Een uiteenzetting van mijn kwaliteiten en motivatie licht ik graag toe in een persoonlijk gesprek. Met vriendelijke groet, Tuyet Tran


def printWelcomeText():
    welcome = welcomeMessage
    return welcome

def printExercise():
    motivatie = motivatie
    return motivatie

if len(welcomeMessage) != 76:
    sys.exit("Nice try, but not quite right :)")

print(printWelcomeText())
