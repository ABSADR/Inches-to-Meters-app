import PySimpleGUI as sg
from test2 import convertor

text = sg.Text('Enter feet')
inpp = sg.Input(key='feet')
text2 = sg.Text('Enter inches')
inpp2 = sg.Input(key='inches')
button = sg.Button('Convert',button_color='Black')
exit_button= sg.Button("Exit!",key='exit',button_color='red4')

output = sg.Text(key='output',text_color='orange')

window = sg.Window('Convertor',layout=[[text,inpp],
                                       [text2,inpp2],
                                       [button],
                                       [output],
                                       [exit_button]],background_color='black')


while True:
    try:

        event, value = window.read()
        match event:
            case 'exit':
                break
            case sg.WIN_CLOSED:
                break

        feet = int(value['feet'])
        inches = int(value['inches'])
        window['output'].update(value=convertor(feet,inches))
    except ValueError:
        sg.popup('Please provide two numbers',background_color='red')


window.close()
