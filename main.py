import tkinter as tk
import calculation as cal

def click_button(exp_value, btn_text): 
    txt_display = exp_value.get()
    if btn_text == "=":
        try:
            txt_display = cal.infix_to_postfix(cal.tokenize_expression(txt_display))
        except:
            txt_display = "Error"
    elif btn_text == '0':
        if txt_display == '0':
            txt_display = '0'
        else:
            txt_display += btn_text
    else:
        if (txt_display == '0' and btn_text != '.') or (txt_display == "Error"):
            txt_display = btn_text
        else:
            txt_display += btn_text
    exp_value.set(txt_display)
    
def create_display():
    # display frame
    display_frame = tk.Frame(app, bg="black")
    display_frame.place(width=APP_WIDTH, height=100)
    exp_value = tk.StringVar(value="0")
    exp_label = tk.Label(display_frame, textvariable=exp_value, anchor="e", bg="red", fg="white", padx=10,  font=("Arial", 20))
    exp_label.place(x=0, y=0, width=APP_WIDTH, height=100)
    return exp_value, exp_label

def create_button(exp_value, exp_label):
    # button frame
    button_frame = tk.Frame(app, bg="green")
    button_frame.place(x=0, y=100, width=APP_WIDTH, height=400)
    # button
    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "=", "+"
    ]
    btns = []
    for i in range(4):
        for j in range(4):
            btn = tk.Button(button_frame, text=buttons[i*4+j], font=("Arial", 20), command = lambda btn_text=buttons[i*4+j]: click_button(exp_value,btn_text))
            btn.place(x=j*100, y=i*100, width=100, height=100)
            btns.append(btn)
    return btns

if __name__ == '__main__':
    app = tk.Tk()
    app.title("Calculator")

    # set window size
    APP_WIDTH, APP_HEIGHT = 400, 500
    app.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
    app.resizable(0, 0)

    # create display
    exp_value, exp_label = create_display()
    # create button
    btns = create_button(exp_value, exp_label)

    app.mainloop()