# aula 5 de Python Turma 21 - 29/11/2023

# Funções para serem chamadas no arquivo conversor.py
def celsius_para_fahrenheit (celsius):
    return (9 * celsius / 5) + 32 # fórmula para converter celsius em fahrenheit
def fahrenheit_para_celsius (fahrenheit):
    return ((fahrenheit - 32) / 9) * 5 # fórmula para converter fahrenheit em celsius

# teste
# print(f'{0}°C = {celsius_para_fahrenheit(0)}°F')
# print(f'{-40}°C = {celsius_para_fahrenheit(-40)}°F')
# print(f'{38}°C = {celsius_para_fahrenheit(38)}°F')
