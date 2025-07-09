import tkinter as tk #gilt als Abkürzung
root = tk.Tk() #Hauptfenster
root.title("Countdown Timer")
root.geometry("400x300")
root.resizable(False, False) #unveränderbare Größe


hour_var = tk.StringVar() # speichert die Eingaben der Eingabefelder
min_var = tk.StringVar()
sec_var = tk.StringVar()

input_frame = tk.Frame(root) #Rahmen innerhalb des Fensters
input_frame.pack(pady=10) #sorgt für etwas Abstand nach oben und unten

hour_entry = tk.Entry(input_frame, textvariable=hour_var, width=5, font=("Helvetica", 18), justify='center')
min_entry = tk.Entry(input_frame, textvariable=min_var, width=5, font=("Helvetica", 18), justify='center')
sec_entry = tk.Entry(input_frame, textvariable=sec_var, width=5, font=("Helvetica", 18), justify='center')
# entry vs Entry
hour_entry.grid(row=0, column=0, padx=5) #row, column, grid, padx
tk.Label(input_frame, text=":", font=("Helvetica", 18)).grid(row=0, column=1)
min_entry.grid(row=0, column=2, padx=5)
tk.Label(input_frame, text=":", font=("Helvetica", 18)).grid(row=0, column=3)
sec_entry.grid(row=0, column=4, padx=5)

time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 36), fg="blue")
time_label.pack(pady=20)



button_frame = tk.Frame(root)
button_frame.pack(pady=10)



running = False
paused = False
remaining_seconds = 0
def start_timer():
    global running, paused, remaining_seconds
    if running:
        return
    try:
        h = int(hour_var.get()) if hour_var.get() else 0
        m = int(min_var.get()) if min_var.get() else 0
        s = int(sec_var.get()) if sec_var.get() else 0
    except ValueError:
        time_label.config(text="Ungültige Eingabe")
        return
    total = h * 3600 + m * 60 + s
    if total <= 0:
        time_label.config(text="Zeit = 0?")
        return
    remaining_seconds = total
    running = True
    paused = False

    start_btn.config(state=tk.DISABLED)
    pause_btn.config(state=tk.NORMAL, text="Pause")
    reset_btn.config(state=tk.NORMAL)

    update_timer()

def update_timer():
    global remaining_seconds, running, paused

    if running and not paused:
        mins, secs = divmod(remaining_seconds, 60)
        hours, mins = divmod(mins, 60)
        time_str = f"{hours:02d}:{mins:02d}:{secs:02d}"
        time_label.config(text=time_str)

        if remaining_seconds > 0:
            remaining_seconds -= 1
            root.after(1000, update_timer)

        else:
            time_label.config(text="Time is up!")
            running = False
            start_btn.config(state=tk.NORMAL)
            pause_btn.config(state=tk.DISABLED)
            reset_btn.config(state=tk.DISABLED)

def pause_timer():
    global paused

    if not running:
        return

    paused = not paused

    if paused:
        pause_btn.config(text="Resume")
    else:
        pause_btn.config(text="Pause")
        update_timer()

def reset_timer():
    global running, paused, remaining_seconds

    running = False
    paused = False
    remaining_seconds = 0

    time_label.config(text="00:00:00")

    hour_var.set("")
    min_var.set("")
    sec_var.set("")

    start_btn.config(state=tk.NORMAL)
    pause_btn.config(state=tk.DISABLED, text="Pause")
    reset_btn.config(state=tk.DISABLED)

start_btn = tk.Button(button_frame, text="Start", font=("Helvetica", 14), command=start_timer)
start_btn.grid(row=0, column=0, padx=10)

pause_btn = tk.Button(button_frame, text="Pause", font=("Helvetica", 14), command=pause_timer, state=tk.DISABLED)
pause_btn.grid(row=0, column=1, padx=10)

reset_btn = tk.Button(button_frame, text="Reset", font=("Helvetica", 14), command=reset_timer, state=tk.DISABLED)
reset_btn.grid(row=0, column=2, padx=10)

root.mainloop() #startet das Fenster dauerhaft
