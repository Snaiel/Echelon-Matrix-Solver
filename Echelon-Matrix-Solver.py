import PySimpleGUI as sg
import sympy as sym

input_matrix = [
        [1,2,-3,9],
        [2,-1,1,0],
        [-3,4,-2,12]
    ]

# input_matrix = [
#         [0,0,-3,9],
#         [0,0,0,0],
#         [0,0,0,0]
#     ]


matrix = sym.Matrix(input_matrix).rref(pivots=False)
matrix = matrix.tolist()
print(matrix)
# matrix = [[str(x) for x in i] for i in matrix]
# print(matrix)

layout =  [
    [sg.Text('Raw values:')],
    [sg.Input(size=(4,1), pad=(0,0), key=(('a', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), key=(('b', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), key=(('c', i))) for i in range(4)],
    [sg.Button('Execute', size=(15,1))],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('d', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('e', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('f', i))) for i in range(4)],
]

window = sg.Window('Echelon Matrix Solver', layout, margins=(20,20))

def turn_input_into_list():
    input_matrix = []
    for x in ('a', 'b', 'c'):
        row = []
        for i in range(4):
            print((x,i))
            row.append(values[(x,i)])
        input_matrix.append(row)
    return(input_matrix)

def perform_row_reduction(input_matrix):
    matrix = sym.Matrix(input_matrix).rref(pivots=False)
    matrix = matrix.tolist()
    return(matrix)

def put_calculations_into_fields(matrix):
    for x in ('d', 'e', 'f'):
        for i in range(4):
            window[(x,i)].update(value=matrix[('d', 'e', 'f').index(x)][i])

while True:
    event, values = window.read()
    print(event, values)

    if event == 'Execute':
        put_calculations_into_fields(perform_row_reduction(turn_input_into_list()))

    if event in ('None', sg.WINDOW_CLOSED):
        break

window.close()