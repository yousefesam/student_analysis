import tkinter as tk
from tkinter import filedialog
from controller.analysis_service import Controller
from service.analysis_service import AnalysisService
from strategies.multithread_strategy import MultiThreadStrategy
from strategies.batch_strategy import BatchStrategy

BG     = "#0f1117"
PANEL  = "#1a1d2e"
BLUE   = "#3b82f6"
PURPLE = "#8b5cf6"
TEXT   = "#e2e8f0"
MUTED  = "#64748b"
GREEN  = "#22c55e"

controller = Controller()
students   = controller.load_data("data/students.csv")
file_var   = None  # will be set after root is created

root = tk.Tk()
root.title("Student Analysis System")
root.configure(bg=BG)
root.geometry("700x560")
root.resizable(True, True)

file_var = tk.StringVar(value="data/students.csv")

# ── Header ──────────────────────────────────────────
header = tk.Frame(root, bg=PANEL, height=56)
header.pack(fill="x")
tk.Label(header, text="🎓  Student Analysis System", bg=PANEL,
         fg=TEXT, font=("Segoe UI", 16, "bold")).pack(side="left", padx=20, pady=14)

status_var = tk.StringVar(value="● Ready")
tk.Label(header, textvariable=status_var, bg=PANEL,
         fg=GREEN, font=("Segoe UI", 11)).pack(side="right", padx=20)

# ── File picker bar ─────────────────────────────────
file_bar = tk.Frame(root, bg="#13161f", height=46)
file_bar.pack(fill="x")
file_bar.pack_propagate(False)

tk.Label(file_bar, text="📂  File:", bg="#13161f",
         fg=MUTED, font=("Segoe UI", 10)).pack(side="left", padx=(16, 6), pady=12)

file_entry = tk.Entry(file_bar, textvariable=file_var, bg="#0f1117", fg=TEXT,
                      font=("Consolas", 10), relief="flat", bd=4,
                      insertbackground=TEXT, readonlybackground="#0f1117")
file_entry.pack(side="left", fill="x", expand=True, pady=8)

def browse():
    path = filedialog.askopenfilename(
        title="Select student CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if path:
        file_var.set(path)
        global students
        students = controller.load_data(path)
        status_var.set("● File loaded")

tk.Button(file_bar, text="Browse", bg=BLUE, fg="white",
          font=("Segoe UI", 10, "bold"), relief="flat",
          activebackground=BLUE, activeforeground="white",
          cursor="hand2", bd=0, padx=14, pady=4,
          command=browse).pack(side="right", padx=10, pady=8)

# ── Body ────────────────────────────────────────────
body = tk.Frame(root, bg=BG)
body.pack(fill="both", expand=True, padx=16, pady=14)

# Left panel
left = tk.Frame(body, bg=PANEL, width=180)
left.pack(side="left", fill="y", padx=(0, 12))
left.pack_propagate(False)

tk.Label(left, text="ANALYSIS MODE", bg=PANEL, fg=MUTED,
         font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=14, pady=(16, 6))

def make_btn(text, color, cmd):
    tk.Button(left, text=text, bg=color, fg="white",
              font=("Segoe UI", 12, "bold"), relief="flat",
              activebackground=color, activeforeground="white",
              cursor="hand2", bd=0, padx=10, pady=10,
              command=cmd).pack(fill="x", padx=12, pady=4)

def run(strategy_cls, label):
    status_var.set(f"● {label}...")
    root.update()
    result = AnalysisService(strategy_cls()).run(students)
    output.config(state="normal")
    output.delete("1.0", "end")
    output.insert("end", f"{'─'*44}\n  {label} Results\n{'─'*44}\n\n{result}")
    output.config(state="disabled")
    status_var.set("● Ready")

make_btn("⚡  Multi-Thread", BLUE,   lambda: run(MultiThreadStrategy, "Multi-Thread"))
make_btn("📦  Batch",        PURPLE, lambda: run(BatchStrategy,       "Batch"))

tk.Frame(left, bg="#2d3148", height=1).pack(fill="x", padx=12, pady=10)

clear_lbl = tk.Label(left, text="🗑  Clear", bg=PANEL, fg=MUTED,
                     font=("Segoe UI", 11), cursor="hand2")
clear_lbl.pack(anchor="w", padx=14)
clear_lbl.bind("<Button-1>", lambda e: [output.config(state="normal"),
                                         output.delete("1.0", "end"),
                                         output.config(state="disabled")])

# Right panel – output
right = tk.Frame(body, bg=PANEL)
right.pack(side="left", fill="both", expand=True)

tk.Label(right, text="Output", bg=PANEL, fg=MUTED,
         font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=14, pady=(12, 4))

output = tk.Text(right, bg="#0f1117", fg=TEXT, font=("Consolas", 12),
                 relief="flat", bd=0, padx=12, pady=10,
                 insertbackground=TEXT, wrap="word", state="disabled")
output.pack(fill="both", expand=True, padx=12, pady=(0, 12))

root.mainloop()