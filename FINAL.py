import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
from datetime import datetime


class HotelBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Booking Management System")
        self.root.geometry("1400x800")


        self.root.configure(bg='#1a1a2e')

        # Database connection parameters
        self.db_params = {
            'host': 'localhost',
            'port': 5432,
            'database': 'SUBD',
            'user': 'postgres',
            'password': '1234s'
        }


        self.setup_styles()
        self.setup_ui()


        self.animate_window()

    def setup_styles(self):

        style = ttk.Style()
        style.theme_use('clam')


        style.configure("Treeview",
                        background="#ffffff",
                        foreground="#2c3e50",
                        rowheight=30,
                        fieldbackground="#ffffff",
                        font=('Arial', 10))

        style.map('Treeview',
                  background=[('selected', '#3498db')])

        style.configure("Treeview.Heading",
                        background="#34495e",
                        foreground="white",
                        font=('Arial', 11, 'bold'))

    def animate_window(self):

        self.root.attributes('-alpha', 0.0)
        self.fade_in()

    def fade_in(self, alpha=0.0):

        alpha += 0.1
        if alpha <= 1.0:
            self.root.attributes('-alpha', alpha)
            self.root.after(30, lambda: self.fade_in(alpha))

    def connect_db(self):

        try:
            conn = psycopg2.connect(**self.db_params)
            return conn
        except Exception as e:
            messagebox.showerror("Error connect", f"Failed to connect to the database:\n{str(e)}")
            return None

    def create_gradient_frame(self, parent):

        frame = tk.Canvas(parent, bg='#0f3460', highlightthickness=0)
        return frame

    def setup_ui(self):


        header = tk.Canvas(self.root, height=100, bg='#16213e', highlightthickness=0)
        header.pack(fill=tk.X)


        header.create_rectangle(0, 0, 1400, 100, fill='#0f3460', outline='')


        hotel_icon = "🏨"
        header.create_text(700, 35, text=hotel_icon, font=('Arial', 40), fill='#e94560')
        header.create_text(700, 75, text="Hotel Booking Management System",
                           font=('Arial', 20, 'bold'), fill='white')


        main_container = tk.Frame(self.root, bg='#16213e')
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)


        left_panel = tk.Frame(main_container, bg='#0f3460', width=280)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        left_panel.pack_propagate(False)


        menu_header = tk.Frame(left_panel, bg='#0f3460')
        menu_header.pack(pady=20)

        tk.Label(menu_header, text="⚙️", font=('Arial', 20), bg='#0f3460').pack()
        tk.Label(menu_header, text="Операции", font=('Arial', 18, 'bold'),
                 bg='#0f3460', fg='white').pack()

        buttons = [
            ("📋 Display Data", self.show_data_menu, '#3498db'),
            ("🔍 Search Clients", self.search_data, '#9b59b6'),
            ("➕ Add Client", self.add_record_menu, '#27ae60'),
            ("✏️ Update Status", self.update_record_menu, '#f39c12'),
            ("🗑️ Delete Payment", self.delete_record_menu, '#e74c3c'),
            ("🧮 Calculations", self.calculations_menu, '#16a085'),
            ("📊 Reports", self.reports_menu, '#2980b9'),
            ("🔀 Combinations (Cross Join)", self.cross_join_menu, '#8e44ad'),
            ("📈 Dashboard", self.show_dashboard, '#e67e22'),
        ]
        self.button_widgets = []
        for text, command, color in buttons:
            btn_frame = tk.Frame(left_panel, bg='#0f3460')
            btn_frame.pack(pady=6, padx=15, fill=tk.X)

            btn = tk.Button(btn_frame, text=text, command=command,
                            font=('Arial', 11, 'bold'), bg=color, fg='white',
                            relief=tk.FLAT, cursor='hand2',
                            activebackground=self.darken_color(color),
                            activeforeground='white',
                            bd=0, padx=15, pady=12)
            btn.pack(fill=tk.X)


            btn.bind('<Enter>', lambda e, b=btn, c=color: self.on_button_enter(b, c))
            btn.bind('<Leave>', lambda e, b=btn, c=color: self.on_button_leave(b, c))

            self.button_widgets.append(btn)


        right_panel = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=2)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        shadow = tk.Frame(main_container, bg='#0a0a0a', width=5)
        shadow.place(x=295, y=0, relheight=1)


        self.result_frame = tk.Frame(right_panel, bg='white')
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)


        self.show_dashboard()

    def darken_color(self, color):

        color_map = {
            '#3498db': '#2980b9',
            '#9b59b6': '#8e44ad',
            '#27ae60': '#229954',
            '#f39c12': '#e67e22',
            '#e74c3c': '#c0392b',
            '#16a085': '#138d75',
            '#2980b9': '#21618c',
            '#8e44ad': '#7d3c98',
            '#e67e22': '#d35400'
        }
        return color_map.get(color, color)

    def on_button_enter(self, button, original_color):

        button.configure(bg=self.darken_color(original_color))
        button.configure(relief=tk.RAISED, bd=2)

    def on_button_leave(self, button, original_color):

        button.configure(bg=original_color)
        button.configure(relief=tk.FLAT, bd=0)

    def clear_result_frame(self):

        for widget in self.result_frame.winfo_children():
            widget.destroy()

    def create_card(self, parent, title, value, icon, color):

        card = tk.Frame(parent, bg=color, relief=tk.RAISED, bd=0)
        card.pack(side=tk.LEFT, padx=10, pady=10, ipadx=20, ipady=20)

        tk.Label(card, text=icon, font=('Arial', 30), bg=color, fg='white').pack()
        tk.Label(card, text=str(value), font=('Arial', 28, 'bold'),
                 bg=color, fg='white').pack()
        tk.Label(card, text=title, font=('Arial', 11),
                 bg=color, fg='white').pack()

        return card

    def show_dashboard(self):

        self.clear_result_frame()

        # Заголовок
        header = tk.Frame(self.result_frame, bg='white')
        header.pack(fill=tk.X, pady=(0, 20))

        tk.Label(header, text="📊 Dashboard - Overall Statistics",
                 font=('Arial', 20, 'bold'), bg='white', fg='#2c3e50').pack()

        conn = self.connect_db()
        if not conn:
            return

        try:
            cursor = conn.cursor()


            cursor.execute("SELECT COUNT(*) FROM clients")
            total_clients = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM bookings")
            total_bookings = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM rooms WHERE status = 'available'")
            available_rooms = cursor.fetchone()[0]

            cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM payments")
            total_revenue = cursor.fetchone()[0]


            cards_frame = tk.Frame(self.result_frame, bg='white')
            cards_frame.pack(pady=20)

            self.create_card(cards_frame, "Total Clients", total_clients, "👥", '#3498db')
            self.create_card(cards_frame, "Bookings", total_bookings, "📅", '#27ae60')
            self.create_card(cards_frame, "Available Rooms", available_rooms, "🏠", '#f39c12')
            self.create_card(cards_frame, f"Revenue: {total_revenue:.0f} ₸", "", "💰", '#e74c3c')


            tk.Label(self.result_frame, text="🕐 Recent Bookings",
                     font=('Arial', 16, 'bold'), bg='white', fg='#2c3e50').pack(pady=(30, 10))

            query = """
                SELECT b.booking_id, 
                       c.first_name || ' ' || c.last_name as client,
                       r.room_number, 
                       b.check_in_date, 
                       b.check_out_date,
                       b.total_price
                FROM bookings b
                JOIN clients c ON b.client_id = c.client_id
                JOIN rooms r ON b.room_id = r.room_id
                ORDER BY b.booking_id DESC
                LIMIT 5
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            tree_frame = tk.Frame(self.result_frame, bg='white')
            tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

            columns = ['ID', 'Client', 'Room', 'Check-in', 'Check-out', 'Amount']
            tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=5)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=150, anchor='center')

            for row in rows:
                tree.insert('', tk.END, values=row)

            tree.pack(fill=tk.BOTH, expand=True)

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error loading statistics:\n{str(e)}")

            if conn:
                conn.close()

    def show_data_menu(self):

        self.clear_result_frame()

        tk.Label(self.result_frame, text="Select a table to display",
                 font=('Arial', 18, 'bold'), bg='white', fg='#2c3e50').pack(pady=30)

        tables = [
            ("👥 Clients", "clients", '#3498db'),
            ("🏠 Rooms", "rooms", '#27ae60'),
            ("🏷️ Room Types", "room_types", '#9b59b6'),
            ("📅 Bookings", "bookings", '#e67e22'),
            ("👔 Employees", "employees", '#16a085'),
            ("🎁 Services", "services", '#f39c12'),
            ("💳 Payments", "payments", '#e74c3c'),
            ("📊 Rooms (by price ↓)", "rooms_sorted", '#2c3e50'),
        ]

        buttons_container = tk.Frame(self.result_frame, bg='white')
        buttons_container.pack(expand=True)

        for i, (text, table, color) in enumerate(tables):
            row = i // 2
            col = i % 2

            btn = tk.Button(buttons_container, text=text,
                            command=lambda t=table: self.display_table(t),
                            font=('Arial', 12, 'bold'), bg=color, fg='white',
                            width=25, height=2, cursor='hand2',
                            relief=tk.FLAT, bd=0, padx=20, pady=15)
            btn.grid(row=row, column=col, padx=15, pady=10)

            btn.bind('<Enter>', lambda e, b=btn, c=color: b.config(bg=self.darken_color(c), relief=tk.RAISED))
            btn.bind('<Leave>', lambda e, b=btn, c=color: b.config(bg=c, relief=tk.FLAT))

    def display_table(self, table_name):

        self.clear_result_frame()

        conn = self.connect_db()
        if not conn:
            return

        try:
            cursor = conn.cursor()


            if table_name == "rooms_sorted":
                query = """
                    SELECT room_id, room_number, price, status
                    FROM rooms
                    ORDER BY price DESC
                """
                title = "📊 Rooms (sorted by price)"

                icon = "📊"
            elif table_name == "clients":
                query = "SELECT client_id, first_name, last_name, email, phone FROM clients"
                title = "👥 Clients"
                icon = "👥"
            elif table_name == "rooms":
                query = "SELECT room_id, room_number, price, status FROM rooms"
                title = "🏠 Rooms"
                icon = "🏠"
            elif table_name == "room_types":
                query = "SELECT room_type_id, type_name, description FROM room_types"
                title = "🏷️ Room type"
                icon = "🏷️"
            elif table_name == "bookings":
                query = """
                    SELECT b.booking_id, c.first_name || ' ' || c.last_name as client,
                           r.room_number, b.check_in_date, b.check_out_date, b.total_price
                    FROM bookings b
                    JOIN clients c ON b.client_id = c.client_id
                    JOIN rooms r ON b.room_id = r.room_id
                """
                title = "📅 Bookings"
                icon = "📅"
            elif table_name == "employees":
                query = "SELECT employee_id, first_name, last_name, position FROM employees"
                title = "👔 Employees"
                icon = "👔"
            elif table_name == "services":
                query = "SELECT service_id, service_name, description, price FROM services"
                title = "🎁 services"
                icon = "🎁"
            elif table_name == "payments":
                query = """
                    SELECT p.payment_id, b.booking_id, p.amount, 
                           p.payment_date, p.payment_method
                    FROM payments p
                    JOIN bookings b ON p.booking_id = b.booking_id
                """
                title = "💳 payments"
                icon = "💳"
            else:
                query = f"SELECT * FROM {table_name}"
                title = table_name
                icon = "📋"

            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]


            header_frame = tk.Frame(self.result_frame, bg='white')
            header_frame.pack(fill=tk.X, pady=(0, 15))

            tk.Label(header_frame, text=title,
                     font=('Arial', 18, 'bold'), bg='white', fg='#2c3e50').pack()


            tree_frame = tk.Frame(self.result_frame, bg='white')
            tree_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

            scrollbar_y = ttk.Scrollbar(tree_frame)
            scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

            scrollbar_x = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
            scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

            tree = ttk.Treeview(tree_frame, columns=columns, show='headings',
                                yscrollcommand=scrollbar_y.set,
                                xscrollcommand=scrollbar_x.set)

            scrollbar_y.config(command=tree.yview)
            scrollbar_x.config(command=tree.xview)


            for col in columns:
                tree.heading(col, text=col.upper())
                tree.column(col, width=150, anchor='center')


            for i, row in enumerate(rows):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tree.insert('', tk.END, values=row, tags=(tag,))

            tree.tag_configure('evenrow', background='#f8f9fa')
            tree.tag_configure('oddrow', background='#ffffff')

            tree.pack(fill=tk.BOTH, expand=True)


            info_frame = tk.Frame(self.result_frame, bg='white')
            info_frame.pack(fill=tk.X, pady=10)

            tk.Label(info_frame, text=f"✓ Всего записей: {len(rows)}",
                     font=('Arial', 11, 'bold'), bg='white', fg='#27ae60').pack()

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error loading data:\n{str(e)}")
            if conn:
                conn.close()

    def cross_join_menu(self):

        self.clear_result_frame()

        tk.Label(self.result_frame, text="🔀 All possible combinations",
                 font=('Arial', 18, 'bold'), bg='white', fg='#2c3e50').pack(pady=20)

        tk.Label(self.result_frame,
                 text="Showing all combinations of clients, services, and employees\n(Cross Join demonstration)",
                 font=('Arial', 11), bg='white', fg='#7f8c8d').pack(pady=5)

        conn = self.connect_db()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """
                SELECT 
                    c.first_name || ' ' || c.last_name AS client,
                    s.service_name,
                    s.price as service_price,
                    e.first_name || ' ' || e.last_name AS employee,
                    e.position
                FROM clients c
                CROSS JOIN services s
                CROSS JOIN employees e
                LIMIT 50
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            tree_frame = tk.Frame(self.result_frame, bg='white')
            tree_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

            scrollbar_y = ttk.Scrollbar(tree_frame)
            scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

            columns = ['Client', 'Service', 'Service Price', 'Employee', 'Position']

            tree = ttk.Treeview(tree_frame, columns=columns, show='headings',
                                yscrollcommand=scrollbar_y.set)

            scrollbar_y.config(command=tree.yview)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=180, anchor='center')

            for i, row in enumerate(rows):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tree.insert('', tk.END, values=row, tags=(tag,))

            tree.tag_configure('evenrow', background='#f8f9fa')
            tree.tag_configure('oddrow', background='#ffffff')

            tree.pack(fill=tk.BOTH, expand=True)

            tk.Label(self.result_frame, text=f"✓ Showing the first 50 combinations",
                     font=('Arial', 10), bg='white', fg='#7f8c8d').pack(pady=5)

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка выполнения Cross Join:\n{str(e)}")
            if conn:
                conn.close()

    def search_data(self):

        self.clear_result_frame()

        tk.Label(self.result_frame, text="🔍 Search Clients",
                 font=('Arial', 18, 'bold'), bg='white', fg='#2c3e50').pack(pady=20)

        search_frame = tk.Frame(self.result_frame, bg='white')
        search_frame.pack(pady=15)

        tk.Label(search_frame, text="Enter first name or last name:",
                 font=('Arial', 12), bg='white', fg='#34495e').grid(row=0, column=0, padx=10, pady=10)

        search_entry = tk.Entry(search_frame, font=('Arial', 12), width=30,
                                relief=tk.SOLID, bd=1)
        search_entry.grid(row=0, column=1, padx=10, pady=10)

        def perform_search():
            keyword = search_entry.get()
            if not keyword:
                messagebox.showwarning("⚠️ Предупреждение", "Введите ключевое слово для поиска")
                return

            conn = self.connect_db()
            if not conn:
                return

            try:
                cursor = conn.cursor()
                query = """
                    SELECT client_id, first_name, last_name, email, phone
                    FROM clients
                    WHERE first_name ILIKE %s OR last_name ILIKE %s
                """
                cursor.execute(query, (f'%{keyword}%', f'%{keyword}%'))
                rows = cursor.fetchall()

                # Очистка предыдущих результатов
                for widget in self.result_frame.winfo_children()[2:]:
                    widget.destroy()

                if rows:
                    # Создание таблицы результатов
                    tree_frame = tk.Frame(self.result_frame, bg='white')
                    tree_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

                    columns = ['ID', 'First Name', 'Last Name', 'Email', 'Phone']
                    tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=12)

                    for col in columns:
                        tree.heading(col, text=col)
                        tree.column(col, width=150, anchor='center')

                    for i, row in enumerate(rows):
                        tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                        tree.insert('', tk.END, values=row, tags=(tag,))

                    tree.tag_configure('evenrow', background='#f8f9fa')
                    tree.tag_configure('oddrow', background='#ffffff')

                    tree.pack(fill=tk.BOTH, expand=True)

                    tk.Label(self.result_frame, text=f"✓ Found: {len(rows)} records",

                             font=('Arial', 11, 'bold'), bg='white', fg='#27ae60').pack(pady=10)
                else:
                    tk.Label(self.result_frame, text="❌ Ничего не найдено",
                             font=('Arial', 14, 'bold'), bg='white', fg='#e74c3c').pack(pady=30)

                cursor.close()
                conn.close()

            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка поиска:\n{str(e)}")
                if conn:
                    conn.close()

        search_btn = tk.Button(search_frame, text="🔍 Search", command=perform_search,
                               font=('Arial', 11, 'bold'), bg='#3498db', fg='white',
                               width=15, height=1, cursor='hand2', relief=tk.FLAT, bd=0,
                               padx=10, pady=8)
        search_btn.grid(row=0, column=2, padx=10)

        search_btn.bind('<Enter>', lambda e: search_btn.config(bg='#2980b9'))
        search_btn.bind('<Leave>', lambda e: search_btn.config(bg='#3498db'))

    def add_record_menu(self):
        self.clear_result_frame()

        tk.Label(self.result_frame, text="➕ Add New Client",
                 font=('Arial', 18, 'bold'), bg='white', fg='#2c3e50').pack(pady=20)

        # Красивая форма в рамке
        form_container = tk.Frame(self.result_frame, bg='#ecf0f1', relief=tk.RAISED, bd=2)
        form_container.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)

        tk.Label(form_container, text="Заполните все поля",
                 font=('Arial', 12), bg='#ecf0f1', fg='#7f8c8d').pack(pady=15)

        form_frame = tk.Frame(form_container, bg='#ecf0f1')
        form_frame.pack(pady=20)

        fields = [
            ("👤 First name:", "first_name"),
            ("👤 Last Name:", "last_name"),
            ("📧 Email:", "email"),
            ("📱 Phone:", "phone")
        ]

        entries = {}

        for i, (label, field) in enumerate(fields):
            tk.Label(form_frame, text=label, font=('Arial', 12, 'bold'),
                     bg='#ecf0f1', fg='#2c3e50').grid(row=i, column=0, padx=15, pady=12, sticky='e')
            entry = tk.Entry(form_frame, font=('Arial', 12), width=35, relief=tk.SOLID, bd=1)
            entry.grid(row=i, column=1, padx=15, pady=12)
            entries[field] = entry

        def save_client():
            values = {k: v.get() for k, v in entries.items()}

            if not all(values.values()):
                messagebox.showwarning("⚠️ Предупреждение", "Заполните все поля")
                return

            conn = self.connect_db()
            if not conn:
                return

            try:
                cursor = conn.cursor()
                query = """
                    INSERT INTO clients (first_name, last_name, email, phone)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (values['first_name'], values['last_name'],
                                       values['email'], values['phone']))
                conn.commit()
                cursor.close()
                conn.close()

                messagebox.showinfo("✓ Success", "Client added successfully!")

                for entry in entries.values():
                    entry.delete(0, tk.END)

            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при добавлении:\n{str(e)}")
                if conn:
                    conn.close()

        save_btn = tk.Button(form_container, text="💾 Save", command=save_client,
                             font=('Arial', 13, 'bold'), bg='#27ae60', fg='white',
                             width=25, height=2, cursor='hand2', relief=tk.FLAT, bd=0)
        save_btn.pack(pady=20)

        save_btn.bind('<Enter>', lambda e: save_btn.config(bg='#229954'))
        save_btn.bind('<Leave>', lambda e: save_btn.config(bg='#27ae60'))

    def update_record_menu(self):
        """Меню обновления записи"""
        self.clear_result_frame()

        tk.Label(self.result_frame, text="✏️ Update Room Status",
                 font=('Arial', 18, 'bold'), bg='white', fg='#2c3e50').pack(pady=20)

        form_container = tk.Frame(self.result_frame, bg='#ecf0f1', relief=tk.RAISED, bd=2)
        form_container.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)

        form_frame = tk.Frame(form_container, bg='#ecf0f1')
        form_frame.pack(pady=40)

        tk.Label(form_frame, text="🏠 ID Room:", font=('Arial', 12, 'bold'),
                 bg='#ecf0f1', fg='#2c3e50').grid(row=0, column=0, padx=15, pady=15)
        room_id_entry = tk.Entry(form_frame, font=('Arial', 12), width=35, relief=tk.SOLID, bd=1)
        room_id_entry.grid(row=0, column=1, padx=15, pady=15)

        tk.Label(form_frame, text="📊 New status:", font=('Arial', 12, 'bold'),
                 bg='#ecf0f1', fg='#2c3e50').grid(row=1, column=0, padx=15, pady=15)
        status_var = tk.StringVar()
        status_combo = ttk.Combobox(form_frame, textvariable=status_var,
                                    values=['available', 'occupied', 'maintenance'],
                                    font=('Arial', 12), width=33, state='readonly')
        status_combo.grid(row=1, column=1, padx=15, pady=15)

        def update_room():
            room_id = room_id_entry.get()
            status = status_var.get()

            if not room_id or not status:
                messagebox.showwarning("⚠️ Предупреждение", "Заполните все поля")
                return

            conn = self.connect_db()
            if not conn:
                return

            try:
                cursor = conn.cursor()
                query = "UPDATE rooms SET status = %s WHERE room_id = %s"
                cursor.execute(query, (status, room_id))
                conn.commit()

                if cursor.rowcount > 0:
                    messagebox.showinfo("✓ Success", "Room status updated!")

                    room_id_entry.delete(0, tk.END)
                    status_var.set('')
                else:
                    messagebox.showwarning("⚠️ Предупреждение", "Номер с таким ID не найден")

                cursor.close()
                conn.close()

            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при обновлении:\n{str(e)}")
                if conn:
                    conn.close()

        update_btn = tk.Button(form_container, text="✏️ Update", command=update_room,
                               font=('Arial', 13, 'bold'), bg='#f39c12', fg='white',
                               width=25, height=2, cursor='hand2', relief=tk.FLAT, bd=0)
        update_btn.pack(pady=20)

        update_btn.bind('<Enter>', lambda e: update_btn.config(bg='#e67e22'))
        update_btn.bind('<Leave>', lambda e: update_btn.config(bg='#f39c12'))

    def delete_record_menu(self):

        self.clear_result_frame()

        tk.Label(self.result_frame, text="🗑️ Delete Paeyment",
                 font=('Arial', 18, 'bold'), bg='white', fg='#2c3e50').pack(pady=20)

        form_container = tk.Frame(self.result_frame, bg='#ecf0f1', relief=tk.RAISED, bd=2)
        form_container.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)

        form_frame = tk.Frame(form_container, bg='#ecf0f1')
        form_frame.pack(pady=60)

        tk.Label(form_frame, text="💳 ID payment:", font=('Arial', 12, 'bold'),
                 bg='#ecf0f1', fg='#2c3e50').grid(row=0, column=0, padx=15, pady=15)
        payment_id_entry = tk.Entry(form_frame, font=('Arial', 12), width=35, relief=tk.SOLID, bd=1)
        payment_id_entry.grid(row=0, column=1, padx=15, pady=15)

        def delete_payment():
            payment_id = payment_id_entry.get()

            if not payment_id:
                messagebox.showwarning("⚠️ Предупреждение", "Введите ID платежа")
                return

            confirm = messagebox.askyesno("❓ Confirmation", "Are you sure you want to delete this payment?")
            if not confirm:
                return

            conn = self.connect_db()
            if not conn:
                return

            try:
                cursor = conn.cursor()
                query = "DELETE FROM payments WHERE payment_id = %s"
                cursor.execute(query, (payment_id,))
                conn.commit()

                if cursor.rowcount > 0:
                    messagebox.showinfo("✓ Success", "Payment deleted!")
                    payment_id_entry.delete(0, tk.END)
                else:
                    messagebox.showwarning("⚠️ Предупреждение", "Платеж с таким ID не найден")

                cursor.close()
                conn.close()

            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при удалении:\n{str(e)}")
                if conn:
                    conn.close()

        delete_btn = tk.Button(form_container, text="🗑️ Delete", command=delete_payment,
                               font=('Arial', 13, 'bold'), bg='#e74c3c', fg='white',
                               width=25, height=2, cursor='hand2', relief=tk.FLAT, bd=0)
        delete_btn.pack(pady=20)

        delete_btn.bind('<Enter>', lambda e: delete_btn.config(bg='#c0392b'))
        delete_btn.bind('<Leave>', lambda e: delete_btn.config(bg='#e74c3c'))

    def calculations_menu(self):
        """Меню вычислений"""
        self.clear_result_frame()

        tk.Label(self.result_frame, text="🧮 Calculate Stay Cost",
                 font=('Arial', 18, 'bold'), bg='white', fg='#2c3e50').pack(pady=20)

        tk.Label(self.result_frame,
                 text="Calculated field: (Check-out date - Check-in date) × Price per day",
                 font=('Arial', 11), bg='white', fg='#7f8c8d').pack(pady=5)

        conn = self.connect_db()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """
                SELECT 
                    b.booking_id,
                    c.first_name || ' ' || c.last_name AS client,
                    r.room_number,
                    (b.check_out_date - b.check_in_date) AS days,
                    r.price,
                    (b.check_out_date - b.check_in_date) * r.price AS total_cost
                FROM bookings b
                JOIN clients c ON b.client_id = c.client_id
                JOIN rooms r ON b.room_id = r.room_id
                ORDER BY total_cost DESC
                LIMIT 20
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            tree_frame = tk.Frame(self.result_frame, bg='white')
            tree_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

            columns = ['ID', 'Client', 'Room', 'Days', 'Price/Day', 'Total']
            tree = ttk.Treeview(tree_frame, columns=columns, show='headings')

            scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=150, anchor='center')

            for i, row in enumerate(rows):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tree.insert('', tk.END, values=row, tags=(tag,))

            tree.tag_configure('evenrow', background='#f8f9fa')
            tree.tag_configure('oddrow', background='#ffffff')

            tree.pack(fill=tk.BOTH, expand=True)

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка вычислений:\n{str(e)}")
            if conn:
                conn.close()

    def reports_menu(self):
        """Меню отчетов"""
        self.clear_result_frame()

        tk.Label(self.result_frame, text="📊 Booking Statistics by Room Type",
                 font=('Arial', 18, 'bold'), bg='white', fg='#2c3e50').pack(pady=20)

        tk.Label(self.result_frame,
                 text="Grouping with Totals (GROUP BY with Aggregate Functions)",
                 font=('Arial', 11), bg='white', fg='#7f8c8d').pack(pady=5)

        conn = self.connect_db()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            query = """
                SELECT 
                    rt.type_name,
                    COUNT(b.booking_id) AS total_bookings,
                    COALESCE(SUM(b.total_price), 0) AS total_revenue
                FROM room_types rt
                LEFT JOIN rooms r ON rt.room_type_id = r.room_type_id
                LEFT JOIN bookings b ON r.room_id = b.room_id
                GROUP BY rt.type_name
                ORDER BY total_bookings DESC
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            tree_frame = tk.Frame(self.result_frame, bg='white')
            tree_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

            columns = ['Room Type', 'Total Bookings', 'Total Revenue (₸)']
            tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=10)

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=250, anchor='center')

            for i, row in enumerate(rows):
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                tree.insert('', tk.END, values=row, tags=(tag,))

            tree.tag_configure('evenrow', background='#f8f9fa')
            tree.tag_configure('oddrow', background='#ffffff')

            tree.pack(fill=tk.BOTH, expand=True)

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка загрузки отчета:\n{str(e)}")
            if conn:
                conn.close()


def main():
    root = tk.Tk()
    app = HotelBookingSystem(root)
    root.mainloop()


if __name__ == "__main__":
    main()