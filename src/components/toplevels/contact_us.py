import customtkinter as ctk

bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

class ContactUs(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Toplevel - Contact Us")
        self.resizable(1, 1)
        self.attributes("-topmost", True)
        self.update()
        self.grab_set()

        main_frame = ctk.CTkFrame(
            self,
            fg_color=bg,
            corner_radius=0,
            border_width=1,
            border_color=btn_active,
        )
        main_frame.grid(padx=0, pady=0)

        self.widgets(main_frame)

    def widgets(self, frame):
        
        info_frame = ctk.CTkFrame(frame, fg_color=fg)
        info_frame.pack(side="top", fill="both", expand="true", padx=10, pady=10)




        ctk.CTkButton(
            frame,
            text="Submit",
            command=lambda: self.destroy(),
            width=10,
            height=2,
            fg_color=btn_active,
            hover_color=btn_hvr,
        ).pack(side="bottom", padx=50, pady=50, ipadx=10, ipady=2)