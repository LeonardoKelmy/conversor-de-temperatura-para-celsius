#Interface gráfica do conversor de temp

import PySimpleGUI as psg

import funcoesConversorTemperatura
from funcoesConversorTemperatura import fahrenheit_para_celsius

layout = [
              [psg.Text('Informe a temperatura em Fahrenheit: '), psg.InputText(key= 'valores')],
              [psg.Text('Celsius -'), psg.Text( text= '', key= 'resultado')],
              [psg.Button('calcular'), psg.Button('limpar')],
        ]

janela = psg.Window('Conversor de temperatura para Celsius', layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'limpar':
        janela['valores'].update('')
        janela['resultado'].update('')
        janela['valores'].set_focus()
    else:
        valores = int(valores['valores'])
        janela['resultado'].update(funcoesConversorTemperatura.fahrenheit_para_celsius(valores))

janela.close()
