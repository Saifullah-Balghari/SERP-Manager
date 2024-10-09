from CTkMessagebox import CTkMessagebox

from ..settings import *

# Color scheme
bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"   
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

def show_info(title, message):

    CTkMessagebox(
        title=title, 
        message=message,
        option_1="Okay",
        icon_size=(50, 50),
        fg_color=fg,
        bg_color=fg,
        icon=info_icon_path,
        topmost=True,
        button_color=btn_active,
        button_hover_color=btn_hvr,
        button_height=12,
        button_width=40,
        text_color=text_fg,
        title_color=text_fg,
        border_color=btn_active,
        cancel_button_color=btn_active,
    )

def show_success(title, message):

    CTkMessagebox(
        title=title, 
        message=message,
        option_1="Okay",
        icon=success_icon_path,
        icon_size=(50, 50),
        fg_color=fg,
        bg_color=fg,
        topmost=True,
        button_color=btn_active,
        button_hover_color=btn_hvr,
        button_height=12,
        button_width=40,
        text_color=text_fg,
        title_color=text_fg,
        border_color=btn_active,
        cancel_button_color=btn_active,
    )
    
def show_error(title, message):

    CTkMessagebox(
        title=title, 
        message=message,
        option_1="Okay",
        icon=error_icon_path,
        icon_size=(50, 50),
        fg_color=fg,
        bg_color=fg,
        topmost=True,
        button_color=btn_active,
        button_hover_color=btn_hvr,
        button_height=12,
        button_width=40,
        text_color=text_fg,
        title_color=text_fg,
        border_color=btn_active,
        cancel_button_color=btn_active,
    )
    
def show_warning(title, message):

    CTkMessagebox(
        title=title, 
        message=message,
        icon=warn_icon_path, 
        option_1="OK",
        icon_size=(50, 50),
        fg_color=fg,
        bg_color=fg,
        topmost=True,
        button_color=btn_active,
        button_hover_color=btn_hvr,
        button_height=12,
        button_width=40,
        text_color=text_fg,
        title_color=text_fg,
        border_color=btn_active,
        cancel_button_color=btn_active,
    )
   
def show_yes_no(title, message) -> bool:
    msg = CTkMessagebox(
        title=title, 
        message=message,
        icon=yes_no_icon_path, 
        option_1="Yes", 
        option_2="No",
        icon_size=(50, 50),
        fg_color=fg,
        bg_color=fg,
        topmost=True,
        button_color=btn_active,
        button_hover_color=btn_hvr,
        button_height=12,
        button_width=40,
        text_color=text_fg,
        title_color=text_fg,
        border_color=btn_active,
        cancel_button_color=btn_active,
    )

    response = msg.get()
    
    if response=="Yes":
        return True       
    else:
        return False
