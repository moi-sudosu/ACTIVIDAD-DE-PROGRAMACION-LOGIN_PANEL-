import tkinter as tk
from tkinter import Menu, ttk

class FrmDashboard:
    def __init__(self, master, session_user):
        self.master = master
        master.title('Panel Administrativo')
        master.geometry('1200x600')
        master.minsize(900, 500)
        master.configure(bg='#f0f2f5')

        # Configurar menú
        self._create_menu()

        # Crear layout principal con paned window para redimensionar paneles
        self.paned = ttk.Panedwindow(master, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True)

        # Panel izquierdo - info sesión
        self.left_frame = tk.Frame(self.paned, width=320, bg='#2c3e50')
        self.paned.add(self.left_frame, weight=1)

        # Panel derecho - contenido principal
        self.right_frame = tk.Frame(self.paned, bg='white')
        self.paned.add(self.right_frame, weight=4)

        self._build_left_panel(session_user)
        self._build_right_panel()

    def _create_menu(self):
        menubar = Menu(self.master)

        usuarios_menu = Menu(menubar, tearoff=0)
        usuarios_menu.add_command(label='Administración de Usuarios', command=self.admin_usuarios)
        menubar.add_cascade(label='Usuarios', menu=usuarios_menu)

        menubar.add_cascade(label='Clientes', command=self.menu_placeholder)
        menubar.add_cascade(label='Categorías', command=self.menu_placeholder)
        menubar.add_cascade(label='Productos', command=self.menu_placeholder)
        menubar.add_cascade(label='Ventas', command=self.menu_placeholder)

        self.master.config(menu=menubar)

    def _build_left_panel(self, session_user):
        # Título panel izquierdo
        title = tk.Label(
            self.left_frame, text='PANEL ADMINISTRATIVO',
            font=('Segoe UI', 18, 'bold'), fg='white', bg='#2c3e50'
        )
        title.pack(pady=(30, 20))

        # Información usuario
        nombre_completo = f"{session_user['nombres']} {session_user['apellidos']}"
        lbl_name = tk.Label(
            self.left_frame, text=nombre_completo,
            font=('Segoe UI', 14, 'bold'), fg='white', bg='#2c3e50'
        )
        lbl_name.pack(pady=(10, 5))

        lbl_email = tk.Label(
            self.left_frame, text=session_user['email'],
            font=('Segoe UI', 11), fg='#bdc3c7', bg='#2c3e50'
        )
        lbl_email.pack(pady=(0, 5))

        lbl_rol = tk.Label(
            self.left_frame, text=session_user['rol'],
            font=('Segoe UI', 12, 'italic'), fg='#ecf0f1', bg='#2c3e50'
        )
        lbl_rol.pack(pady=(10, 20))

        # Separador
        separator = ttk.Separator(self.left_frame, orient='horizontal')
        separator.pack(fill='x', padx=20, pady=10)

        # Opciones adicionales (ejemplo)
        opciones_label = tk.Label(
            self.left_frame, text='Opciones',
            font=('Segoe UI', 14, 'underline'), fg='white', bg='#2c3e50'
        )
        opciones_label.pack(pady=(10, 10))

        btn_admin_usuarios = tk.Button(
            self.left_frame, text='Administrar Usuarios',
            font=('Segoe UI', 12), bg='#34495e', fg='white',
            activebackground='#1abc9c', activeforeground='white',
            relief='flat', cursor='hand2', command=self.admin_usuarios
        )
        btn_admin_usuarios.pack(fill='x', padx=20, pady=5)

    def _build_right_panel(self):
        welcome = tk.Label(
            self.right_frame, text='BIENVENIDO AL SISTEMA',
            font=('Segoe UI', 28, 'bold'), fg='#34495e', bg='white'
        )
        welcome.pack(anchor='n', pady=40)

    def admin_usuarios(self):
        top = tk.Toplevel(self.master)
        top.title('Administración de Usuarios')
        top.geometry('700x500')
        top.configure(bg='white')

        lbl = tk.Label(
            top, text='Aquí irá la administración de usuarios',
            font=('Segoe UI', 16), fg='#34495e', bg='white'
        )
        lbl.pack(pady=30)

    def menu_placeholder(self):
        from tkinter import messagebox
        messagebox.showinfo('Información', 'Funcionalidad en desarrollo')


if __name__ == '__main__':
    # Ejemplo de usuario para prueba
    usuario_demo = {
        'nombres': 'pedro',
        'apellidos': 'louis',
        'email': 'pedro@example.com',
        'rol': 'Administrador'
    }

    root = tk.Tk()
    app = FrmDashboard(root, usuario_demo)
    root.mainloop()
