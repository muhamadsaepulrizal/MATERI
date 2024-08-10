import tkinter as tk
from tkinter import messagebox

class AplikasiAntrianRestoran:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Antrian Restoran")
        self.queue = []
        
        self.title_label = tk.Label(root, text="Sistem Antrian Restoran", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(root, text="Nama Pelanggan:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)

        self.order_label = tk.Label(root, text="Pesanan:")
        self.order_label.pack(pady=5)
        self.order_entry = tk.Entry(root)
        self.order_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Tambahkan ke Antrian", command=self.add_to_queue, bg="green", fg="white")
        self.add_button.pack(pady=5)

        self.show_queue_button = tk.Button(root, text="Tampilkan Antrian", command=self.show_queue, bg="blue", fg="white")
        self.show_queue_button.pack(pady=5)

        self.next_customer_button = tk.Button(root, text="Pelanggan Berikutnya", command=self.next_customer, bg="orange", fg="white")
        self.next_customer_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Keluar", command=root.quit, bg="red", fg="white")
        self.exit_button.pack(pady=5)

        self.queue_text = tk.Text(root, height=15, width=50)
        self.queue_text.pack(pady=5)
        self.queue_text.config(state=tk.DISABLED)

    def add_to_queue(self):
        name = self.name_entry.get()
        order = self.order_entry.get()
        if name and order:
            self.queue.append((name, order))
            self.name_entry.delete(0, tk.END)
            self.order_entry.delete(0, tk.END)
            messagebox.showinfo("Sukses", f"{name} dengan pesanan {order} ditambahkan ke antrian")
            self.show_queue()  # Update queue display
        else:
            messagebox.showerror("Error", "Masukkan nama dan pesanan terlebih dahulu")

    def show_queue(self):
        self.queue_text.config(state=tk.NORMAL)
        self.queue_text.delete(1.0, tk.END)
        
        if self.queue:
            for index, (name, order) in enumerate(self.queue, start=1):
                self.queue_text.insert(tk.END, f"{index}. {name} - {order}\n")
        else:
            self.queue_text.insert(tk.END, "Antrian kosong.\n")

        self.queue_text.config(state=tk.DISABLED)

    def next_customer(self):
        if self.queue:
            next_customer = self.queue.pop(0)
            messagebox.showinfo("Pelanggan Berikutnya", f"Pelanggan berikutnya: {next_customer[0]} dengan pesanan: {next_customer[1]}")
            self.show_queue()
        else:
            messagebox.showinfo("Antrian Kosong", "Tidak ada pelanggan dalam antrian")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiAntrianRestoran(root)
    root.mainloop()