import tkinter as tk
from tkinter import messagebox, simpledialog
from database import ExcelDatabase

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Login")
        self.root.geometry("300x400")
        
        self.db = ExcelDatabase()
        
        self.create_login_page()

    def create_login_page(self):
        # Hapus widget sebelumnya jika ada
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame Login
        login_frame = tk.Frame(self.root, padx=20, pady=20)
        login_frame.pack(expand=True)
        
        # Label Judul
        tk.Label(login_frame, text="LOGIN", font=("Arial", 16)).pack(pady=10)
        
        # Username
        tk.Label(login_frame, text="Username").pack()
        self.username_entry = tk.Entry(login_frame, width=30)
        self.username_entry.pack(pady=5)
        
        # Password
        tk.Label(login_frame, text="Password").pack()
        self.password_entry = tk.Entry(login_frame, show="*", width=30)
        self.password_entry.pack(pady=5)
        
        # Tombol Login
        tk.Button(login_frame, text="Login", command=self.login).pack(pady=10)
        
        # Tombol Register
        tk.Button(login_frame, text="Register", command=self.register).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        role = self.db.validate_login(username, password)
        
        if role:
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
            self.open_main_menu(username, role)
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah")

    def register(self):
        username = simpledialog.askstring("Register", "Masukkan Username:")
        if username:
            password = simpledialog.askstring("Register", "Masukkan Password:", show='*')
            if password:
                if self.db.register_user(username, password):
                    messagebox.showinfo("Registrasi", "Berhasil mendaftar!")
                else:
                    messagebox.showerror("Registrasi", "Username sudah ada!")

    def open_main_menu(self, username, role):
        # Hapus widget sebelumnya
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame Menu Utama
        menu_frame = tk.Frame(self.root, padx=20, pady=20)
        menu_frame.pack(expand=True)
        
        # Label Selamat Datang
        tk.Label(menu_frame, text=f"Selamat Datang, {username}", font=("Arial", 14)).pack(pady=10)
        
        # Menu Kasir (hanya tampil jika role kasir)
        if role == 'kasir':
            tk.Button(menu_frame, text="Menu Kasir", command=self.open_kasir_menu).pack(pady=5)
        
        # Tombol Logout
        tk.Button(menu_frame, text="Logout", command=self.create_login_page).pack(pady=5)

    def open_kasir_menu(self):
        # Frame Menu Kasir
        for widget in self.root.winfo_children():
            widget.destroy()
        
        kasir_frame = tk.Frame(self.root, padx=20, pady=20)
        kasir_frame.pack(expand=True)
        
        tk.Label(kasir_frame, text="MENU KASIR", font=("Arial", 16)).pack(pady=10)
        
        # Contoh submenu kasir
        tk.Button(kasir_frame, text="Transaksi Penjualan", command=self.dummy_action).pack(pady=5)
        tk.Button(kasir_frame, text="Laporan Penjualan", command=self.dummy_action).pack(pady=5)
        tk.Button(kasir_frame, text="Kembali", command=self.create_login_page).pack(pady=5)

    def dummy_action(self):
        messagebox.showinfo("Informasi", "Fitur dalam pengembangan")

def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
