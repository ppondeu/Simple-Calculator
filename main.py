import tkinter as tk
import calculation as cal
bracket_flag = 0
op_flag = True
def click_button(exp_value, btn_text):
    txt_display = exp_value.get()
    txt_output = txt_display
    if txt_display == "Error":
        txt_display = "0"

    global bracket_flag, op_flag
    if btn_text == "=":
        try:
            txt_output = cal.infix_to_postfix(cal.tokenize(txt_display))
        except:
            txt_output = "Error"
    elif btn_text == "C":
        txt_output = "0"
    elif btn_text == "CE":
        txt_output = txt_display[:-1]
        if txt_output == "":
            txt_output = "0"
    elif cal.is_operator(btn_text) or btn_text == "(" or btn_text == ")" or btn_text.isdigit() or btn_text == ".":
        if txt_display == "0" and btn_text != ".":
            txt_output = btn_text
        else:
            txt_output = txt_display + btn_text
    else:
        return
    exp_value.set(txt_output)
def create_display():
    # display frame
    display_frame = tk.Frame(app, bg="black")
    display_frame.place(width=APP_WIDTH, height=100)
    exp_value = tk.StringVar(value="0")
    exp_label = tk.Label(display_frame, textvariable=exp_value, anchor="e", bg="#c41c37", fg="white", padx=10,  font=("Arial", 20), highlightbackground="#EDBB00", highlightthickness=8)
    exp_label.place(x=0, y=0, width=APP_WIDTH, height=100)
    return exp_value, exp_label

def create_button(exp_value, exp_label):
    # button frame
    button_frame = tk.Frame(app, bg="green")
    button_frame.place(x=0, y=100, width=APP_WIDTH, height=APP_HEIGHT - 100)
    # button
    buttons = [
        "C", "CE", "(", ")",
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "=", "+"
    ]
    btns = []
    for i in range(5):
        for j in range(4):
            btn = tk.Button(button_frame, text=buttons[i * 4 + j], font=("Arial", 20), borderwidth=0, highlightthickness=2, command=lambda btn_text=buttons[i * 4 + j]: click_button(exp_value, btn_text))
            btn.place(x=j * APP_WIDTH / 4, y=i * (APP_HEIGHT - 100) / 5, width=APP_WIDTH / 4, height=(APP_HEIGHT - 100) / 5)
            btns.append(btn)
    return btns

if __name__ == '__main__':
    app = tk.Tk()
    app.title("Calculator")

    # set window size
    APP_WIDTH, APP_HEIGHT = 320, 500
    app.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
    app.resizable(0, 0)

    # create display
    exp_value, exp_label = create_display()
    # create button
    btns = create_button(exp_value, exp_label)
 
    app.bind('<Key>', lambda event: click_button(exp_value, event.char))
    app.bind('<Return>', lambda event: click_button(exp_value, "="))
    # clear display
    app.bind('<Escape>', lambda event: click_button(exp_value, "C"))
    # delete last character
    app.bind('<BackSpace>', lambda event: click_button(exp_value, "CE"))
    # press e to exit
    app.bind('<e>', lambda event: app.destroy())
    # set window to center of screen
    app.update_idletasks()
    app_width = app.winfo_width()
    app_height = app.winfo_height()
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width - app_width) // 2
    y = (screen_height - app_height) // 2
    app.geometry(f"{app_width}x{app_height}+{x}+{y}")
    app.mainloop()