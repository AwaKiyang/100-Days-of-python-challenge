import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Define color constants for UI styling
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#ecd104"

# Font and timer durations
FONT_NAME = "Courier"
WORK_MIN = 25         # Duration of work session in minutes
SHORT_BREAK_MIN = 5   # Duration of short break in minutes
LONG_BREAK_MIN = 20   # Duration of long break in minutes

# Global variables to track session state
reps = 0              # Number of completed sessions
timer = None          # Reference to the active timer

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Reset the timer and UI elements to initial state."""
    window.after_cancel(timer)  # Cancel the scheduled countdown
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer display
    timer_label.config(text="Timer")  # Reset label text
    check_label.config(text="")  # Clear check marks
    global reps
    reps = 0  # Reset session counter

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Start the timer based on the current session count."""
    global reps
    reps += 1  # Increment session count

    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine session type and start countdown
    if reps % 8 == 0:
        count_down(long_break_sec)  # Long break every 8th session
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)  # Short break on even sessions
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)  # Work session on odd reps
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Update the timer every second and handle session transitions."""
    count_min = math.floor(count / 60)  # Calculate minutes
    count_sec = count % 60  # Calculate seconds

    # Format seconds with leading zero if needed
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Update timer display on canvas
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        # Schedule the next countdown tick after 1 second
        timer = window.after(1000, count_down, count - 1)
    else:
        # Start the next session when countdown finishes
        start_timer()

        # Display check marks for completed work sessions
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
# Create main window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label at the top
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

# Canvas with tomato image and timer text
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")  # Load image
canvas.create_image(100, 112, image=tomato_img)  # Center image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Timer text
canvas.grid(column=2, row=2)

# Start button
start_but = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_but.grid(column=1, row=3)

# Reset button
reset_but = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_but.grid(column=3, row=3)

# Label to show check marks for completed work sessions
check_label = tkinter.Label(text="", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=2, row=4)

# Start the Tkinter event loop
window.mainloop()