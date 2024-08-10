from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import time

class Order:
    def __init__(self, name, order):
        self.name = name
        self.order = order
        self.start_time = time.time()
        self.finish_time = self.start_time + 10 * 60

class ColoredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 0.5, 0, 1)  # Warna oranye
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class OrderApp(App):
    def build(self):
        self.orders = []
        self.served_orders = []

        self.main_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        self.menu_layout = ColoredBoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.8))

        self.title_label = Label(text="Lakukan Layanan!", font_size='20sp', color=(1, 1, 1, 1), size_hint=(1, 0.1))
        self.menu_layout.add_widget(self.title_label)

        self.layanan_button = Button(text="Lakukan Pelayanan", size_hint=(1, 0.2), on_press=self.order_service, background_color=(1, 0, 0, 1))
        self.menu_layout.add_widget(self.layanan_button)

        self.list_button = Button(text="List Pesanan", size_hint=(1, 0.2), on_press=self.show_orders, background_color=(1, 0, 0, 1))
        self.menu_layout.add_widget(self.list_button)

        self.history_button = Button(text="Riwayat Pelanggan", size_hint=(1, 0.2), on_press=self.show_history, background_color=(1, 0, 0, 1))
        self.menu_layout.add_widget(self.history_button)

        self.main_layout.add_widget(self.menu_layout)
        return self.main_layout

    def order_service(self, instance):
        self.main_layout.clear_widgets()

        self.service_layout = ColoredBoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.8, 0.8))

        self.name_input = TextInput(hint_text="Nama Pelanggan", size_hint=(1, 0.1))
        self.service_layout.add_widget(self.name_input)

        self.order_input = TextInput(hint_text="Pesanan", size_hint=(1, 0.1))
        self.service_layout.add_widget(self.order_input)

        self.add_button = Button(text="Tambah ke antrian", size_hint=(1, 0.2), on_press=self.add_order, background_color=(1, 0, 0, 1))
        self.service_layout.add_widget(self.add_button)

        self.menu_button = Button(text="<- Menu", size_hint=(1, 0.2), on_press=self.main_menu, background_color=(1, 0, 0, 1))
        self.service_layout.add_widget(self.menu_button)

        self.main_layout.add_widget(self.service_layout)

    def add_order(self, instance):
        name = self.name_input.text
        order = self.order_input.text
        if name and order:
            new_order = Order(name, order)
            self.orders.append(new_order)
            popup = Popup(title='Info', content=Label(text='Pesanan telah ditambahkan ke antrian'), size_hint=(0.8, 0.2))
            popup.open()
        else:
            popup = Popup(title='Warning', content=Label(text='Nama dan Pesanan harus diisi'), size_hint=(0.8, 0.2))
            popup.open()

    def show_orders(self, instance):
        self.main_layout.clear_widgets()

        self.order_layout = GridLayout(cols=1, size_hint_y=None)
        self.order_layout.bind(minimum_height=self.order_layout.setter('height'))

        self.scroll_view = ScrollView(size_hint=(1, 0.8), bar_width='10dp')
        self.scroll_view.add_widget(self.order_layout)

        self.update_order_list()

        self.button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.call_button = Button(text="Panggil Pelanggan", size_hint=(0.5, 1), on_press=self.call_customer, background_color=(1, 0, 0, 1))
        self.menu_button = Button(text="<- Menu", size_hint=(0.5, 1), on_press=self.main_menu, background_color=(1, 0, 0, 1))
        self.button_layout.add_widget(self.call_button)
        self.button_layout.add_widget(self.menu_button)

        self.main_layout.add_widget(self.scroll_view)
        self.main_layout.add_widget(self.button_layout)

    def show_history(self, instance):
        self.main_layout.clear_widgets()

        self.history_layout = GridLayout(cols=1, size_hint_y=None)
        self.history_layout.bind(minimum_height=self.history_layout.setter('height'))

        self.scroll_view = ScrollView(size_hint=(1, 0.8), bar_width='10dp')
        self.scroll_view.add_widget(self.history_layout)

        self.update_history_list()

        self.menu_button = Button(text="<- Menu", size_hint=(1, 0.2), on_press=self.main_menu, background_color=(1, 0, 0, 1))
        self.main_layout.add_widget(self.scroll_view)
        self.main_layout.add_widget(self.menu_button)

    def update_order_list(self):
        self.order_layout.clear_widgets()
        for i, order in enumerate(self.orders):
            elapsed_time = time.time() - order.start_time
            remaining_time = max(0, order.finish_time - time.time())
            status = "makanan siap" if elapsed_time >= 10*60 else "menunggu"
            wait_time = time.strftime("%M:%S", time.gmtime(remaining_time))
            finish_time = time.strftime("%H:%M:%S", time.localtime(order.finish_time))
            order_label = Label(
                text=f"{i+1}. {order.name} - {order.order}\n({status})\nWaktu tunggu: {wait_time}\nWaktu selesai: {finish_time}",
                size_hint_y=None,
                height=100,
                color=(1, 1, 1, 1),
                halign='center',
                valign='middle'
            )
            order_label.bind(size=order_label.setter('text_size'))
            self.order_layout.add_widget(order_label)

    def update_history_list(self):
        self.history_layout.clear_widgets()
        for i, order in enumerate(self.served_orders):
            history_label = Label(
                text=f"{i+1}. {order.name} - {order.order}\nWaktu selesai: {time.strftime('%H:%M:%S', time.localtime(order.finish_time))}",
                size_hint_y=None,
                height=100,
                color=(1, 1, 1, 1),
                halign='center',
                valign='middle'
            )
            history_label.bind(size=history_label.setter('text_size'))
            self.history_layout.add_widget(history_label)

    def call_customer(self, instance):
        if self.orders:
            called_order = self.orders.pop(0)
            self.served_orders.append(called_order)
            popup = Popup(title='Info', content=Label(text=f"{called_order.name}, pesanan anda ({called_order.order}) siap!"), size_hint=(0.8, 0.2))
            popup.open()
            self.update_order_list()
        else:
            popup = Popup(title='Warning', content=Label(text='Tidak ada pesanan dalam antrian'), size_hint=(0.8, 0.2))
            popup.open()

    def main_menu(self, instance=None):
        self.main_layout.clear_widgets()
        self.main_layout.add_widget(self.menu_layout)

if __name__ == "__main__":
    OrderApp().run()