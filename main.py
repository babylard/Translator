# Imports
import PySimpleGUI as sg
from translate import Translator
import subprocess

# Functions
def translate_text(text, target_lang):
    translator = Translator(to_lang=target_lang)
    translation = translator.translate(text)
    return translation

def copy_to_clipboard(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def clear_output_element(window):
    window['-OUT-'].update("")

def show_error_message(message):
    sg.popup_error(message)

# GUI
sg.theme("Reddit")

def main():
    
    # Languages
    language_options = [
    'English', 'Spanish', 'French', 'German', 'Italian',
    'Chinese', 'Japanese', 'Korean', 'Russian', 'Arabic',
    'Portuguese', 'Dutch', 'Turkish', 'Swedish', 'Polish',
    'Danish', 'Finnish', 'Norwegian', 'Greek', 'Hungarian',
    'Czech', 'Romanian', 'Bulgarian', 'Hebrew', 'Hindi',
    'Thai', 'Indonesian', 'Vietnamese', 'Malay', 'Tagalog',
    'Bengali', 'Punjabi', 'Gujarati', 'Tamil', 'Urdu',
    'Swahili', 'Yoruba', 'Zulu', 'Mongolian', 'Slovak'
]

    layout = [  
        [sg.Text("Translate to:")],
        [sg.Combo(language_options, key="-LANG-")],
        [sg.Text("Input text:                                                              Output text:")],
        [sg.Multiline(key="-IN-", size=(40, 10)), sg.Output(key="-OUT-", size=(40, 10))],
        [sg.Button("Translate", key="-SUBMIT-"), sg.Button("Copy output to Clipboard", key="-COPY-")]
    ]

    window = sg.Window('Translator', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == '-SUBMIT-':
            target_lang = values["-LANG-"]
            input_text = values["-IN-"]

            clear_output_element(window)

            if target_lang and input_text:
                try:
                    translated_text = translate_text(input_text, target_lang)
                    print(f"{translated_text}")
                except Exception as e:
                    show_error_message(f"Translation error: {e}")
        elif event == '-COPY-':
            output_text = window['-OUT-'].get()
            try:
                copy_to_clipboard(output_text)
                sg.popup("Output copied to clipboard.", title="Success")
            except Exception as e:
                show_error_message(f"Clipboard copy error: {e}")

    window.close()


    window.Close()

# Program start
if __name__ == "__main__":
    main()