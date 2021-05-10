import PySimpleGUI as sg
import sympy as sym

initial_matrix = [
        [1,2,-3,9],
        [2,-1,1,0],
        [-3,4,-2,12]
    ]

layout =  [
    [sg.Input(size=(4,1), pad=(0,0), key=(('a', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), key=(('b', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), key=(('c', i))) for i in range(4)],
    [sg.Button('Execute', size=(15,1), pad=(0,8))],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('d', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('e', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('f', i))) for i in range(4)],
    [sg.Text('  🠗', pad=((0,0),(6,0)), font='30')],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('g', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('h', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('i', i))) for i in range(4)],
    [sg.Text('  🠗', pad=((0,0),(6,0)), font='30')],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('j', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('k', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('l', i))) for i in range(4)],
    [sg.Text('  🠗', pad=((0,0),(6,0)), font='30')],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('m', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('n', i))) for i in range(4)],
    [sg.Input(size=(4,1), pad=(0,0), disabled=True, key=(('o', i))) for i in range(4)],
]

window = sg.Window('Echelon Matrix Solver', layout, margins=(20,20), finalize=True)

DIFFERENT_FIELDS = {
    'initial': ('a', 'b', 'c'),
    'lowest_terms': ('d', 'e', 'f'),
    'first_n_second_step': ('g', 'h', 'i'),
    'third_step': ('j', 'k', 'l'),
    'values': ('m', 'n', 'o')
}

def put_calculations_into_fields(matrix, field):
    for x in DIFFERENT_FIELDS[field]:
        for i in range(4):
            window[(x,i)].update(value=matrix[DIFFERENT_FIELDS[field].index(x)][i])

put_calculations_into_fields(initial_matrix, 'initial')

def turn_input_into_list():
    input_matrix = []
    for x in ('a', 'b', 'c'):
        row = []
        for i in range(4):
            row.append(int(values[(x,i)]))
        input_matrix.append(row)
    return(input_matrix)

def make_matrix_with_lowest_terms(matrix):
    print(matrix)
    new_matrix = []
    for row in matrix:
        new_row = []
        gcd = sym.igcd(*row)
        print(gcd)
        for i in row:
            new_row.append(int(i/gcd))
        new_matrix.append(new_row)
    return(new_matrix)

def perform_row_reduction(matrix):
    matrix = make_matrix_with_lowest_terms(matrix)
    put_calculations_into_fields(matrix, 'lowest_terms')

    # First & second step
    new_matrix_0 = matrix[:1]
    for row in matrix[1:]:
        new_row = []
        for i in range(4):
            new_row.append(int((matrix[0][i]*row[0]-matrix[0][0]*row[i])/(sym.igcd(new_matrix_0[0][0], row[0]))))
        new_matrix_0.append(new_row)
    put_calculations_into_fields(new_matrix_0, 'first_n_second_step')

    # Third step
    new_matrix_1 = new_matrix_0[:2]
    for row in new_matrix_0[2:]:
        new_row = []
        for i in range(4):
            new_row.append(int((row[i]*new_matrix_0[1][1]-new_matrix_0[1][i]*row[1])/(sym.igcd(new_matrix_0[1][1], row[1]))))
        new_matrix_1.append(new_row)
    put_calculations_into_fields(new_matrix_1, 'third_step')

    # Values
    new_matrix_2 = sym.Matrix(new_matrix_1).rref(pivots=False)
    new_matrix_2 = new_matrix_2.tolist()
    put_calculations_into_fields(new_matrix_2, 'values')


while True:
    event, values = window.read()
    print(event, values)

    if event == 'Execute':
        perform_row_reduction(turn_input_into_list())

    if event in ('None', sg.WINDOW_CLOSED):
        break

window.close()