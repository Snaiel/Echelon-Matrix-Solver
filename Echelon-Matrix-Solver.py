from typing import Text
import PySimpleGUI as sg

layout =  [
    [sg.Text('Raw values:')],
    [sg.Input(size=(4,1), pad=(0,0)) for _ in range(4)],
    [sg.Input(size=(4,1), pad=(0,0)) for _ in range(4)],
    [sg.Input(size=(4,1), pad=(0,0)) for _ in range(4)]
]

window = sg.Window('Echelon Matrix Solver', layout, size=(300,300))

while True:
    event, values = window.read()

    if event in ('None', sg.WINDOW_CLOSED):
        break

window.close()