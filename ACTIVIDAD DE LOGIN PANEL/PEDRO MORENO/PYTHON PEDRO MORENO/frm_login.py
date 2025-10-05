import tkinter as tk
from tkinter import messagebox
from usuario import Usuario
from frm_dashboard import FrmDashboard

class FrmLogin:
    def __init__(self, master):
        self.master = master
        self.master.title('Ingreso al Sistema')
        self.master.geometry('780x480')
        self.master.resizable(False, False)
        self.master.configure(bg='#f0f2f5')

        self.usuario = Usuario()

        self._build_ui()

    def _build_ui(self):
        # Left panel - logo and branding
        self.left_frame = tk.Frame(self.master, width=350, height=480, bg='#4a90e2')
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        logo_label = tk.Label(
            self.left_frame, text='Unitecnar', 
            font=('Segoe UI', 36, 'bold'), fg='white', bg='#4a90e2'
        )
        logo_label.place(relx=0.5, rely=0.3, anchor='center')

        slogan_label = tk.Label(
            self.left_frame, text='Sistema de Gestión Académica', 
            font=('Segoe UI', 14), fg='white', bg='#4a90e2'
        )
        slogan_label.place(relx=0.5, rely=0.4, anchor='center')

        # Right panel - login form
        self.right_frame = tk.Frame(self.master, width=430, height=480, bg='white')
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        title_label = tk.Label(
            self.right_frame, text='Ingreso al Sistema', 
            font=('Segoe UI', 24, 'bold'), fg='#333', bg='white'
        )
        title_label.pack(pady=(60, 20))

        # Username
        user_label = tk.Label(
            self.right_frame, text='Usuario:', 
            font=('Segoe UI', 12), fg='#555', bg='white'
        )
        user_label.pack(anchor='w', padx=60)
        self.ent_user = tk.Entry(self.right_frame, font=('Segoe UI', 12), width=30, bd=2, relief='groove')
        self.ent_user.pack(padx=60, pady=(0, 20))
        self.ent_user.focus_set()

        # Password
        pass_label = tk.Label(
            self.right_frame, text='Clave:', 
            font=('Segoe UI', 12), fg='#555', bg='white'
        )
        pass_label.pack(anchor='w', padx=60)
        self.ent_pass = tk.Entry(self.right_frame, font=('Segoe UI', 12), width=30, bd=2, relief='groove', show='*')
        self.ent_pass.pack(padx=60, pady=(0, 30))

        # Login button with hover effect
        self.btn_login = tk.Button(
            self.right_frame, text='Iniciar sesión', 
            font=('Segoe UI', 14, 'bold'), bg='#4a90e2', fg='white', 
            activebackground='#357ABD', activeforeground='white',
            relief='flat', cursor='hand2', command=self.login
        )
        self.btn_login.pack(padx=60, pady=10, fill='x')

        # Bind Enter key to login
        self.master.bind('<Return>', lambda event: self.login())

    def login(self):
        username = self.ent_user.get().strip()
        clave = self.ent_pass.get().strip()

        if not username or not clave:
            messagebox.showwarning('Atención', 'Por favor ingrese usuario y clave')
            if not username:
                self.ent_user.focus_set()
            else:
                self.ent_pass.focus_set()
            return

        user = self.usuario.validarUsuario(username, clave)
        if user:
            # 👇 Aquí cambiamos .get() por ['columna']
            messagebox.showinfo('Bienvenido', f"Bienvenido {user['nombres']} {user['apellidos']}")
            self.master.withdraw()
            dash = tk.Toplevel(self.master)
            FrmDashboard(dash, user)
        else:
            messagebox.showerror('Error', 'Usuario o clave incorrectos')
            self.ent_pass.delete(0, tk.END)
            self.ent_pass.focus_set()

if __name__ == '__main__':
    root = tk.Tk()
    app = FrmLogin(root)
    root.mainloop()
