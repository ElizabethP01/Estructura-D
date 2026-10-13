import tkinter as tk
from tkinter import messagebox

CAPACIDAD = 8          
ALTO = 40              
ANCHO = 160            
X_IZQ = 90             
BASE_Y = 400          
Y_ENTRADA = 20         
VELOCIDAD = 8          
PALETA = ["#4e9af1", "#f1a94e", "#6cc447", "#e0607e",
          "#a77bdc", "#4ec9c0", "#d4b92f", "#f08a5d"]


class AppPila:
    def __init__(self, root):
        self.root = root
        root.title("Funcionamiento de una Pila (LIFO)")
        root.resizable(False, False)

        self.items = []        
        self.graficos = []     
        self.ocupado = False   

        self._crear_interfaz()
        self._dibujar_contenedor()
        self._actualizar_estado()
        self._log("Pila creada (vacía). Capacidad: %d" % CAPACIDAD)

    
    def _crear_interfaz(self):
        self.canvas = tk.Canvas(self.root, width=380, height=440, bg="#f7f7f9",
                                highlightthickness=0)
        self.canvas.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

        panel = tk.Frame(self.root)
        panel.grid(row=0, column=1, sticky="n", padx=(0, 10), pady=10)

        tk.Label(panel, text="PILA  ·  LIFO", font=("Arial", 16, "bold")).pack()
        tk.Label(panel, text="Último en entrar, primero en salir",
                 fg="#555").pack(pady=(0, 10))

        tk.Label(panel, text="Valor a apilar:").pack(anchor="w")
        self.entrada = tk.Entry(panel, font=("Arial", 12), width=18)
        self.entrada.pack(pady=(0, 8))
        self.entrada.bind("<Return>", lambda e: self.apilar())
        self.entrada.focus()

        botones = [
            ("push  (Apilar)", self.apilar, "#4caf50"),
            ("pop  (Desapilar)", self.desapilar, "#e53935"),
            ("peek  (Ver tope)", self.ver_tope, "#1e88e5"),
            ("Vaciar pila", self.vaciar, "#757575"),
        ]
        for texto, comando, color in botones:
            tk.Button(panel, text=texto, command=comando, width=18,
                      bg=color, fg="white", font=("Arial", 10, "bold"),
                      activebackground=color, relief="flat",
                      pady=4).pack(pady=3)

        self.lbl_estado = tk.Label(panel, justify="left", anchor="w",
                                   font=("Consolas", 10), bg="#eef", padx=8,
                                   pady=6, width=28)
        self.lbl_estado.pack(pady=10)

        tk.Label(panel, text="Registro de operaciones:").pack(anchor="w")
        marco = tk.Frame(panel)
        marco.pack()
        barra = tk.Scrollbar(marco)
        self.registro = tk.Listbox(marco, width=32, height=9,
                                   yscrollcommand=barra.set,
                                   font=("Consolas", 9))
        barra.config(command=self.registro.yview)
        self.registro.pack(side="left")
        barra.pack(side="right", fill="y")

    def _dibujar_contenedor(self):
        izq, der = X_IZQ - 10, X_IZQ + ANCHO + 10
        self.canvas.create_line(izq, BASE_Y - CAPACIDAD * ALTO - 5, izq, BASE_Y + 2,
                                der, BASE_Y + 2, der, BASE_Y - CAPACIDAD * ALTO - 5,
                                width=4, fill="#333")
        self.canvas.create_text((izq + der) / 2, BASE_Y + 22, text="FONDO",
                                font=("Arial", 10, "bold"), fill="#777")
        self.canvas.create_text((izq + der) / 2, 6, text="▼ entrada / salida ▲",
                                font=("Arial", 9), fill="#777")

    
    def _y_bloque(self, indice):
        return BASE_Y - (indice + 1) * ALTO + 2

    def _log(self, mensaje):
        self.registro.insert(tk.END, mensaje)
        self.registro.see(tk.END)

    def _actualizar_estado(self):
        vacia = "Sí" if not self.items else "No"
        tope = self.items[-1] if self.items else "—"
        self.lbl_estado.config(
            text=f"Tamaño : {len(self.items)} / {CAPACIDAD}\n"
                 f"Vacía  : {vacia}\n"
                 f"Tope   : {tope}")
        
        self.canvas.delete("tope")
        if self.items:
            y = self._y_bloque(len(self.items) - 1) + (ALTO - 4) / 2
            texto = "◄ TOPE"
        else:
            y = BASE_Y - (ALTO - 4) / 2
            texto = "◄ (vacía)"
        self.canvas.create_text(X_IZQ + ANCHO + 25, y, text=texto, anchor="w",
                                font=("Arial", 11, "bold"), fill="#d32f2f",
                                tags="tope")

    def _mover_a(self, ids, y_destino, al_terminar):
        """Anima los elementos gráficos verticalmente hasta y_destino."""
        y_actual = self.canvas.coords(ids[0])[1]
        dy = y_destino - y_actual
        if abs(dy) <= VELOCIDAD:
            for i in ids:
                self.canvas.move(i, 0, dy)
            al_terminar()
        else:
            paso = VELOCIDAD if dy > 0 else -VELOCIDAD
            for i in ids:
                self.canvas.move(i, 0, paso)
            self.root.after(15, lambda: self._mover_a(ids, y_destino, al_terminar))

  
    def apilar(self):
        """push: agrega un elemento en la cima."""
        if self.ocupado:
            return
        valor = self.entrada.get().strip()
        if not valor:
            messagebox.showwarning("Falta valor", "Escribe un valor para apilar.")
            return
        if len(self.items) >= CAPACIDAD:
            self._log("push(%s) → ¡DESBORDAMIENTO!" % valor)
            messagebox.showerror("Desbordamiento (Overflow)",
                                 "La pila está llena. No se puede apilar más.")
            return

        self.ocupado = True
        indice = len(self.items)
        color = PALETA[indice % len(PALETA)]
        alto_rect = ALTO - 4
        rect = self.canvas.create_rectangle(
            X_IZQ, Y_ENTRADA, X_IZQ + ANCHO, Y_ENTRADA + alto_rect,
            fill=color, outline="#333", width=2)
        texto = self.canvas.create_text(
            X_IZQ + ANCHO / 2, Y_ENTRADA + alto_rect / 2, text=valor,
            font=("Arial", 14, "bold"), fill="white")

        def terminar():
            self.items.append(valor)
            self.graficos.append((rect, texto))
            self.ocupado = False
            self.entrada.delete(0, tk.END)
            self._log("push(%s)" % valor)
            self._actualizar_estado()

        self._mover_a([rect, texto], self._y_bloque(indice), terminar)

    def desapilar(self):
        """pop: quita y devuelve el elemento de la cima."""
        if self.ocupado:
            return
        if not self.items:
            self._log("pop() → ¡SUBDESBORDAMIENTO!")
            messagebox.showerror("Subdesbordamiento (Underflow)",
                                 "La pila está vacía. No hay nada que desapilar.")
            return

        self.ocupado = True
        rect, texto = self.graficos[-1]

        def terminar():
            self.canvas.delete(rect)
            self.canvas.delete(texto)
            self.graficos.pop()
            valor = self.items.pop()
            self.ocupado = False
            self._log("pop() → %s" % valor)
            self._actualizar_estado()

        self._mover_a([rect, texto], Y_ENTRADA, terminar)

    def ver_tope(self):
        """peek: consulta la cima sin quitar el elemento."""
        if self.ocupado:
            return
        if not self.items:
            self._log("peek() → pila vacía")
            messagebox.showinfo("Pila vacía", "No hay elemento en el tope.")
            return
        rect, _ = self.graficos[-1]
        self.canvas.itemconfig(rect, outline="#d32f2f", width=5)
        self.root.after(900, lambda: self.canvas.itemconfig(rect, outline="#333", width=2))
        self._log("peek() → %s" % self.items[-1])

    def vaciar(self):
        if self.ocupado:
            return
        for rect, texto in self.graficos:
            self.canvas.delete(rect)
            self.canvas.delete(texto)
        self.graficos.clear()
        self.items.clear()
        self._log("Pila vaciada")
        self._actualizar_estado()


if __name__ == "__main__":
    ventana = tk.Tk()
    AppPila(ventana)
    ventana.mainloop()
