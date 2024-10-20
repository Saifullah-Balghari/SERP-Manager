from CTkToolTip import CTkToolTip

# Color scheme
bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"   
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

def show(widget, message):
    CTkToolTip(
        widget=widget,
        message=message,
        delay=0.5,
        bg_color=fg,
        alpha=0.4,
        padding=(5, 2)
    )