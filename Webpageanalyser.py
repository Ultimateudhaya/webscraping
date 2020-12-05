import PySimpleGUI as sg
from Webpageutilis import get_html_content,parse_html_using_tag
from utilis import get_statistics
layout=[
    [sg.Text("Webpage analyser",font=("Arial,18"))],
    [sg.Text("Enter the URL",font=("Arial,18")),
     sg.InputText("",font=("Arial,18"),key='url'),sg.Button("Getdata",font=("Arial",18),key='get')],
    [sg.Multiline('',font=("Arial",20), size=(40,15) ,key='output')]
]
def get_details(values):
    html_content=get_html_content('url')
    data = parse_html_using_tag(html_content,'p')
    statistics = get_statistics(data)
    display_data(statistics)
def display_statistics(statistics):
    window["output"].Update("")
    window["output"].print("The Web Page Contains The Following Information:\n")
    window["output"].print(statistics["line_count"],"sentences")
    window["output"].print(statistics["word_count"],"words")
    window["output"].print(statistics["unique_words"],"unique words")
    window["output"].print("The Top Words Are:\n")
    for word in statistics["top_words"]:
        window["output"].print(word)


if __name__ == '__main__':
    window= sg.Window("Webpage analyser",layout)
    while True:
     event,values=window.Read()
     if event == sg.WINDOW_CLOSED:
        break
     elif event == "get":
        get_details(values['url'])
    window.Close()