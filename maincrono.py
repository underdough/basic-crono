import tkinter as tk

class Cronometro:
    def __init__(self, master): # ventana que será el parametro master
        self.master = master
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.corriendo = False
        self.display = tk.StringVar()
        self.actualizar_display("00:00:00.000")
        
        # configuración de la interfaz
        self.master.title("Cronómetro con Tkinter")
        self.master.configure(bg="black")
        self.master.geometry("400x200")
        self.display_label = tk.Label(master, textvariable=self.display, font=("Lorin", 40), bg="black", fg="#ffffff")
        self.display_label.pack()
        
        self.button_frame = tk.Frame(master, bg="black")
        self.button_frame.pack()
        
        self.start_bttn = tk.Button(self.button_frame, text="Iniciar", command=self.iniciar, bg="#197d1e", fg="#ffffff")
        
        self.start_bttn.pack(side=tk.LEFT, padx=6, pady=12)
        
        self.stop_bttn = tk.Button(self.button_frame, text="Detener", command=self.detener, bg="#801818", fg="#ffffff")
        
        self.stop_bttn.pack(side=tk.LEFT, padx=6, pady=12)
        
        self.reset_bttn = tk.Button(self.button_frame, text="Reiniciar", command=self.reiniciar, bg="#163c80", fg="#ffffff")
        
        self.reset_bttn.pack(side=tk.RIGHT, padx=6, pady=12)
        
    # Métodos: 
    
    # Actualizar el display
    def actualizar_display(self, tiempo):
        self.display.set(tiempo)
        
    # Iniciar
    def iniciar(self):
        if not self.corriendo:
            self.corriendo = True
            self.actualizar_Cronometro()
            
    # Detener
    def detener(self):
        self.corriendo = False
    # Reiniciar
    def reiniciar(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.actualizar_display("00:00:00.000")
    
    # Actualizar cronometro
    def actualizar_Cronometro(self):
        if self.corriendo:
            self.milisegundos += 10
            if self.milisegundos >=1000:
                self.milisegundos = 0
                self.segundos += 1
            if self.segundos == 60:
                self.segundos = 0
                self.minutos += 1
            if self.minutos == 60:
                self.minutos = 0
                self.horas += 1
            
            # formato para el tiempo
            tiempo_formateado = f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}.{self.milisegundos:03}"
            self.actualizar_display(tiempo_formateado)
            # cada 10 milisegundos se actualiza el cronometro
            self.master.after(10, self.actualizar_Cronometro)
    
if __name__ == "__main__":
# Crear la ventana principal
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()
