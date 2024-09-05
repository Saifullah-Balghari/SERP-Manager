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

        self.title("")
        self.resizable(False, False)

        main_frame1 = ctk.CTkFrame(
            self,
            fg_color=fg,
            corner_radius=0,
            border_width=0,
            border_color=text_fg
        )
        main_frame1.grid(padx=0, pady=0)

        # Add a title label to the frame
        title = ctk.CTkLabel(
            main_frame1,
            text="Contact Us",
            text_color=text_fg,
            font=("Helvetica", 22, "bold")
        )
        title.pack(side="top", fill="x", padx=10, pady=5)

        # Add a label with contact information to the frame
        info = ctk.CTkLabel(
            main_frame1,
            text="For any queries, please contact us at:\n\nEmail: balgharisaifullah@gmail.com\nPhone: +92355-4300937",
            text_color=text_fg,
            font=("Helvetica", 16)
        )
        info.pack(side="top", fill="x", expand=True, padx=10, pady=10)

        # Add a close button to the frame to close the window when clicked
        close_button = ctk.CTkButton(
            main_frame1,
            text="Close",
            text_color=text_fg_2,
            font=("Helvetica", 14),
            fg_color=btn_active,
            hover_color=btn_hvr,
            command=self.destroy
        )
        close_button.pack(side="top", fill="x", padx=50, pady=10)