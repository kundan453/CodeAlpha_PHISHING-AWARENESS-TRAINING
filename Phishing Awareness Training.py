import tkinter as tk
from tkinter import messagebox

# ================= ROOT =================
root = tk.Tk()
root.title("Phishing Awareness Training Module")
root.geometry("900x600")
root.configure(bg="#020617")

# ================= COLORS (10+) =================
COLORS = {
    "bg": "#020617",
    "title": "#22c55e",
    "text": "#e5e7eb",
    "info": "#38bdf8",
    "warning": "#ef4444",
    "success": "#10b981",
    "yellow": "#facc15",
    "purple": "#a855f7",
    "orange": "#f97316",
    "pink": "#ec4899"
}

slide_index = 0
quiz_index = 0
score = 0
mode = "slides"  # slides | quiz

# ================= TITLE =================
tk.Label(
    root,
    text="PHISHING AWARENESS TRAINING",
    font=("Consolas", 20, "bold"),
    fg=COLORS["title"],
    bg=COLORS["bg"]
).pack(pady=10)

content = tk.Label(
    root,
    text="",
    font=("Consolas", 12),
    fg=COLORS["text"],
    bg=COLORS["bg"],
    justify="left",
    wraplength=850
)
content.pack(pady=20)

# ================= SLIDES =================
slides = [
    ("What is Phishing?",
     "Phishing is a social engineering attack where attackers trick users into revealing sensitive information.\n\nHumans are the main target, not systems."),

    ("Types of Phishing",
     "• Email Phishing\n• Smishing (SMS)\n• Vishing (Calls)\n• Spear Phishing\n• Fake Websites"),

    ("Phishing Email Red Flags",
     "• Urgent language\n• Fake sender email\n• Unknown attachments\n• Requests for passwords or OTPs"),

    ("Fake Websites",
     "• Misspelled URLs\n• HTTPS alone is NOT proof\n• Fake login pages\n• No real contact details"),

    ("Social Engineering",
     "Attackers exploit:\n• Fear\n• Urgency\n• Authority\n• Greed\n• Trust"),

    ("Best Practices",
     "• Verify sender\n• Enable 2FA\n• Never click unknown links\n• Report suspicious emails"),

    ("If You Are Attacked",
     "• Disconnect internet\n• Change passwords\n• Inform IT\n• Scan your device")
]

# ================= QUIZ =================
quiz = [
    {
        "q": "Phishing attacks mainly target?",
        "options": ["Firewalls", "Servers", "Human behavior", "Encryption"],
        "answer": 2
    },
    {
        "q": "HTTPS guarantees a website is safe.",
        "options": ["True", "False"],
        "answer": 1
    },
    {
        "q": "Which is a phishing warning sign?",
        "options": ["Proper grammar", "Urgent action request", "Official domain", "Known sender"],
        "answer": 1
    }
]

# ================= FUNCTIONS =================
def show_slide():
    global slide_index
    title, text = slides[slide_index]
    content.config(
        text=f"{title}\n\n{text}",
        fg=COLORS["info"]
    )

def next_action():
    global slide_index, mode
    if mode == "slides":
        slide_index += 1
        if slide_index < len(slides):
            show_slide()
        else:
            start_quiz()

def start_quiz():
    global mode, quiz_index
    mode = "quiz"
    quiz_index = 0
    next_btn.pack_forget()
    show_question()

def show_question():
    global quiz_index
    if quiz_index < len(quiz):
        q = quiz[quiz_index]
        content.config(text=q["q"], fg=COLORS["purple"])
        for i, btn in enumerate(option_buttons):
            btn.config(
                text=q["options"][i],
                command=lambda i=i: check_answer(i)
            )
            btn.pack(pady=5)
    else:
        end_quiz()

def check_answer(choice):
    global quiz_index, score
    if choice == quiz[quiz_index]["answer"]:
        score += 1
        messagebox.showinfo("Correct", "Correct Answer!")
    else:
        messagebox.showerror("Wrong", "Wrong Answer!")

    quiz_index += 1
    show_question()

def end_quiz():
    for btn in option_buttons:
        btn.pack_forget()

    content.config(
        text=f"Quiz Completed!\nYour Score: {score}/{len(quiz)}",
        fg=COLORS["success"]
    )

    tk.Label(
        root,
        text="Follow On Instagram :- codewithiitian",
        fg=COLORS["pink"],
        bg=COLORS["bg"],
        font=("Consolas", 12, "bold")
    ).pack(pady=20)

# ================= BUTTONS =================
next_btn = tk.Button(
    root,
    text="NEXT",
    bg=COLORS["success"],
    fg="black",
    font=("Consolas", 11, "bold"),
    command=next_action
)
next_btn.pack(pady=10)

option_buttons = []
for _ in range(4):
    btn = tk.Button(
        root,
        width=40,
        bg=COLORS["orange"],
        fg="black",
        font=("Consolas", 11, "bold")
    )
    option_buttons.append(btn)

# ================= START =================
show_slide()
root.mainloop()
