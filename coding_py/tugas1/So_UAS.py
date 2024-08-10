import tkinter as tk
from tkinter import messagebox
import time

class Order:
    def __init__(self, name, order):
        self.name = name
        self.order = order
        self.start_time = time.time()
        self.finish_time = self.start_time + 10 * 60

class OrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FCFS Order System")
        self.root.geometry("360x640")
        self.orders = []
        self.served_orders = []

        self.main_menu()

    def main_menu(self):
        self.clear_frame()

        self.main_frame = tk.Frame(self.root, bg="#e0f7fa")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.title_label = tk.Label(self.main_frame, text="Lakukan Layanan!", font=("Helvetica", 20, "bold"), bg="#e0f7fa")
        self.title_label.pack(pady=20)

        self.layanan_button = tk.Button(self.main_frame, text="Lakukan Pelayanan", command=self.order_service, width=20, height=2, bg="#00796b", fg="white", font=("Helvetica", 10, "bold"))
        self.layanan_button.pack(pady=10)

        self.list_button = tk.Button(self.main_frame, text="List Pesanan", command=self.show_orders, width=20, height=2, bg="#00796b", fg="white", font=("Helvetica", 10, "bold"))
        self.list_button.pack(pady=10)
        
        self.history_button = tk.Button(self.main_frame, text="Riwayat Pelanggan", command=self.show_history, width=20, height=2, bg="#00796b", fg="white", font=("Helvetica", 10, "bold"))
        self.history_button.pack(pady=10)

    def order_service(self):
        self.clear_frame()

        self.service_frame = tk.Frame(self.root, bg="#fffde7")
        self.service_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.name_label = tk.Label(self.service_frame, text="Nama Pelanggan", font=("Helvetica", 12, "bold"), bg="#fffde7")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.service_frame, width=30, font=("Helvetica", 10))
        self.name_entry.pack(pady=5)

        self.order_label = tk.Label(self.service_frame, text="Pesanan", font=("Helvetica", 12, "bold"), bg="#fffde7")
        self.order_label.pack(pady=5)
        self.order_entry = tk.Entry(self.service_frame, width=30, font=("Helvetica", 10))
        self.order_entry.pack(pady=5)

        self.add_button = tk.Button(self.service_frame, text="Tambah ke antrian", command=self.add_order, width=20, height=2, bg="#00796b", fg="white", font=("Helvetica", 10, "bold"))
        self.add_button.pack(pady=10)

        self.menu_button = tk.Button(self.service_frame, text="<- Menu", command=self.main_menu, width=20, height=2, bg="#00796b", fg="white", font=("Helvetica", 10, "bold"))
        self.menu_button.pack(pady=10)

    def add_order(self):
        name = self.name_entry.get()
        order = self.order_entry.get()
        if name and order:
            new_order = Order(name, order)
            self.orders.append(new_order)
            messagebox.showinfo("Info", "Pesanan telah ditambahkan ke antrian")
        else:
            messagebox.showwarning("Warning", "Nama dan Pesanan harus diisi")

    def show_orders(self):
        self.clear_frame()

        self.order_frame = tk.Frame(self.root, bg="#fce4ec")
        self.order_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.order_listbox = tk.Listbox(self.order_frame, width=70, height=15, font=("Helvetica", 10, "bold"))
        self.order_listbox.grid(row=0, column=0, columnspan=2, pady=10)

        self.scrollbar = tk.Scrollbar(self.order_frame, orient="horizontal")
        self.scrollbar.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.order_listbox.config(xscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.order_listbox.xview)

        self.update_order_list()

        self.call_button = tk.Button(self.order_frame, text="Panggil Pelanggan", command=self.call_customer, width=15, height=2, bg="#00796b", fg="white", font=("Helvetica", 10, "bold"))
        self.call_button.grid(row=2, column=0, pady=10, padx=5)

        self.menu_button = tk.Button(self.order_frame, text="<- Menu", command=self.main_menu, width=15, height=2, bg="#00796b", fg="white", font=("Helvetica", 10, "bold"))
        self.menu_button.grid(row=2, column=1, pady=10, padx=5)

    def show_history(self):
        self.clear_frame()

        self.history_frame = tk.Frame(self.root, bg="#f3e5f5")
        self.history_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.history_listbox = tk.Listbox(self.history_frame, width=50, height=15, font=("Helvetica", 10, "bold"))
        self.history_listbox.grid(row=0, column=0, columnspan=2, pady=10)

        self.scrollbar = tk.Scrollbar(self.history_frame)
        self.scrollbar.grid(row=0, column=2, sticky="ns")

        self.history_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.history_listbox.yview)

        self.update_history_list()

        self.menu_button = tk.Button(self.history_frame, text="<- Menu", command=self.main_menu, width=20, height=2, bg="#00796b", fg="white", font=("Helvetica", 10, "bold"))
        self.menu_button.grid(row=1, column=0, columnspan=2, pady=10)

    def auto_update(self):
        self.update_order_list()
        self.root.after(1000, self.auto_update)

    def update_order_list(self):
        self.order_listbox.delete(0, tk.END)
        for i, order in enumerate(self.orders):
            elapsed_time = time.time() - order.start_time
            remaining_time = max(0, order.finish_time - time.time())
            status = "makanan siap" if elapsed_time >= 10*60 else "menunggu"
            wait_time = time.strftime("%M:%S", time.gmtime(remaining_time))
            finish_time = time.strftime("%H:%M:%S", time.localtime(order.finish_time))
            self.order_listbox.insert(tk.END, f"{i+1}. {order.name} - {order.order}\n({status})\nWaktu tunggu: {wait_time}\nWaktu selesai: {finish_time}")

    def update_history_list(self):
        self.history_listbox.delete(0, tk.END)
        for i, order in enumerate(self.served_orders):
            self.history_listbox.insert(tk.END, f"{i+1}. {order.name} - {order.order}\nWaktu selesai: {time.strftime('%H:%M:%S', time.localtime(order.finish_time))}")

    def call_customer(self):
        if self.orders:
            called_order = self.orders.pop(0)
            self.served_orders.append(called_order)
            messagebox.showinfo("Info", f"{called_order.name}, pesanan anda ({called_order.order}) siap!")
            self.update_order_list()
        else:
            messagebox.showwarning("Warning", "Tidak ada pesanan dalam antrian")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderApp(root)
    root.mainloop()