import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from converter import convert_to_xth

class XteinkApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("xth-genXteink v1.0")
        self.geometry("400x250")

        self.label = ctk.CTkLabel(self, text="Convertidor PNG a XTH", font=("Arial", 20))
        self.label.pack(pady=20)

        self.btn_convert = ctk.CTkButton(self, text="Seleccionar Imagen", command=self.process_image)
        self.btn_convert.pack(pady=20)

    def process_image(self):

        file_path = filedialog.askopenfilename(filetypes=[("Imágenes PNG", "*.png")])
        
        if file_path:

            output_path = os.path.splitext(file_path)[0] + ".xth"
            
            if convert_to_xth(file_path, output_path):
                messagebox.showinfo("Éxito", f"Archivo guardado como:\n{os.path.basename(output_path)}")
            else:
                messagebox.showerror("Error", "No se pudo convertir la imagen")

if __name__ == "__main__":
    app = XteinkApp()
    app.mainloop()