import PySimpleGUI as sg

title = "Converter"
layout = [
            [sg.Text('text'), 
            sg.Spin(['item 1', 'item 2'])
            ],
            [sg.Button('Button')], [sg.Input()], 
            [sg.Text('text'), sg.Button('Other Button')]
         ]
window = sg.Window(title, layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()