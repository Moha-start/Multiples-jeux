def input_str(question):
    import tkinter as tk

    root = tk.Tk()
    root.withdraw()

    dialog = tk.Toplevel(root)
    dialog.title("Jeux de rôle")
    dialog.state('zoomed')
    dialog.configure(bg="#2E2E2E")

    label = tk.Label(dialog, text=question, font=("Arial", 24), bg="#2E2E2E", fg="#8B0000")
    label.pack(pady=20)

    entry = tk.Entry(dialog, font=("Arial", 20))
    entry.pack(pady=20)

    result = tk.StringVar()

    def valider():
        result.set(entry.get())
        dialog.destroy()

    btn = tk.Button(dialog, text="Valider", font=("Arial", 24), bg="gray", fg="#8B0000", command=valider)
    btn.pack(pady=20)

    dialog.wait_window()
    root.destroy()
    return result.get()

def input_int(question):
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.withdraw()

    dialog = tk.Toplevel(root)
    dialog.title("Jeux de rôle")
    dialog.state('zoomed')
    dialog.configure(bg="#2E2E2E")


    label = tk.Label(dialog, text=question, font=("Arial", 24), bg="#2E2E2E", fg="#8B0000")
    label.pack(pady=20)

    entry = tk.Entry(dialog, font=("Arial", 24))
    entry.pack(pady=20)

    result = tk.IntVar()

    def valider():
        try:
            value = int(entry.get())
            result.set(value)
            dialog.destroy()
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

    btn = tk.Button(dialog, text="Valider", font=("Arial", 20), bg="gray", fg="#8B0000", command=valider)
    btn.pack(pady=20)

    dialog.wait_window()
    root.destroy()
    return result.get()

def affiche_grande(TxT, taille=24):
    import tkinter as tk
    #from PIL import Image, ImageTk

    root = tk.Tk()
    root.title("Jeux de rôle")
    root.state('zoomed')
    root.configure(bg="#2E2E2E")

    label = tk.Label(root, text=TxT, font=("Arial", taille), bg="#2E2E2E", fg="#8B0000")
    label.pack(expand=True)

    root.after(2000, root.destroy)
    root.mainloop()

def affiche_tab(tab, taille=24):
    import tkinter as tk
    root = tk.Tk()
    root.title("Contenu de la liste")
    root.state('zoomed')
    root.configure(bg="#2E2E2E")


    content = "\n".join(str(item) for item in tab)

    label = tk.Label(root, text=content, font=("Arial", taille), bg="#2E2E2E", fg="#8B0000", justify="left")
    label.pack(expand=True, fill="both", padx=20, pady=20)

    root.after(2000, root.destroy)
    root.mainloop()

def choix_tab(tab, index_depart=0):
    import tkinter as tk
    #from PIL import Image, ImageTk

    root = tk.Tk()
    root.title("Faites votre choix")
    root.configure(bg="#2E2E2E")
    root.state('zoomed')
    
    choix = tk.IntVar()
    choix.set(-1)

    def bouton_click(i):
        choix.set(i)
        root.destroy()

    for i, element in enumerate(tab[index_depart:], start=index_depart):
        btn = tk.Button(root, text=str(element), font=("Arial", 24),
                        command=lambda i=i: bouton_click(i),
                        bg="gray", fg="#8B0000")
        btn.pack(fill="x", padx=20, pady=10)

    root.mainloop()
    return choix.get()
