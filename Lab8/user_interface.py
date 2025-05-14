import tkinter as tk
from tkinter    import ttk, filedialog
from constants  import LABELS
from log_parser import LogParser 



class LogBrowserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HTTP Log Browser")
        self.parser = LogParser()
        self.filtered_logs = []
        self.current_index = 0
        self.create_widgets()


    def create_widgets(self):
        # === Left Side ========================================================
        left_frame = ttk.Frame(self.root)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

        # Selecting log files
        self.file_path = tk.StringVar()
        ttk.Entry(
            left_frame, textvariable=self.file_path, width=30
        ).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(
            left_frame, text='Open', command=self.open_file
        ).grid(row=0, column=1, padx=5, pady=5, sticky='e')

        # 'From' date
        ttk.Label(left_frame, text="From (YYYY-MM-DD)").grid(row=1, column=0, sticky='w')
        self.date_from = tk.StringVar()
        ttk.Entry(left_frame, textvariable=self.date_from).grid(row=1, column=1, padx=5)

        # 'To" date
        ttk.Label(left_frame, text="To (YYYY-MM-DD)").grid(row=2, column=0, sticky="w")
        self.date_to = tk.StringVar()
        ttk.Entry(left_frame, textvariable=self.date_to).grid(row=2, column=1, padx=5)

        # Applying filtering
        ttk.Button(
            left_frame, text="Apply Filter", command=self.apply_filter
        ).grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='e')

        # Displaying log listbox
        self.log_list = tk.Listbox(left_frame, width=50, height=10)
        self.log_list.grid(row=4, column=0, columnspan=2, pady=10)
        self.log_list.bind('<<ListboxSelect>>', self.on_log_select)

        # Previous and Next buttons
        self.prev_btn = ttk.Button(left_frame, text='Previous', command=self.prev_log)
        self.prev_btn.grid(row=5, column=0, pady=5, sticky='w')
        self.next_btn = ttk.Button(left_frame, text='Next', command=self.next_log)
        self.next_btn.grid(row=5, column=1, pady=5, sticky='e')

        # === Right Side =======================================================
        right_frame = ttk.Frame(self.root)
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ns")

        # Displaying details
        self.detail_vars = {label: tk.StringVar() for label in LABELS}
        for index, label in enumerate(LABELS):
            ttk.Label(right_frame, text=label + ':').grid(row=index, column=0, sticky='w', pady=2)
            entry = ttk.Entry(right_frame, textvariable=self.detail_vars[label], state='readonly', width=20)
            entry.grid(row=index, column=1, pady=2)


    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)
            self.parser.load(file_path)
            self.filtered_logs = self.parser.get_entries()
            self.update_log_list()
            self.display_log(0)


    def apply_filter(self):
        start = self.date_from.get()
        end = self.date_to.get()
        self.filtered_logs = self.parser.get_entries_between_dates(start, end)
        self.update_log_list()
        self.display_log(0)


    def update_log_list(self):
        self.log_list.delete(0, tk.END)
        for entry in self.filtered_logs:
            short = entry['raw'][:50] + '...' if len(entry['raw']) > 50 else entry['raw']
            self.log_list.insert(tk.END, short)


    def on_log_select(self, event):
        try:
            index = self.log_list.curselection()[0]
            self.display_log(index)
        except IndexError:
            pass


    def display_log(self, index):
        if not self.filtered_logs:
            return

        self.current_index = index
        entry = self.filtered_logs[index]

        try:
            self.detail_vars["Remote host"].set(entry["id.orig_h"])
            self.detail_vars["Date"].set(entry["ts"].strftime("%Y-%m-%d"))
            self.detail_vars["Time"].set(entry["ts"].strftime("%H:%M:%S"))
            self.detail_vars["Timezone"].set("UTC")
            self.detail_vars["Status code"].set(str(entry["status_code"]))
            self.detail_vars["Method"].set(entry["method"])
            self.detail_vars["Resource"].set(entry["uri"])
            self.detail_vars["Size"].set(f"{entry['response_body_len']} Bytes")
        except KeyError:
            pass

        self.prev_btn['state'] = 'normal' if index > 0 else 'disabled'
        self.next_btn['state'] = 'normal' if index < len(self.filtered_logs) - 1 else 'disabled'

    def prev_log(self):
        if self.current_index > 0:
            self.display_log(self.current_index - 1)

    def next_log(self):
        if self.current_index < len(self.filtered_logs) - 1:
            self.display_log(self.current_index + 1)
