import tkinter as tk

def calcular_imc():
    try:
        altura_user = float(altura.get())
        peso = float(kilo.get())
        imc = peso / (altura_user ** 2)
        result.config(text=f'Seu imc é {imc:.2f}')
    except ValueError:
        result.config(text='Por favor digite apenas numeros')

    

main_window = tk.Tk()
main_window.title('Calcular imc')
main_window.resizable(False, False)
main_window.minsize(300, 300)

altura_label = tk.Label(main_window, text='Digite sua altura em metro')
altura_label.pack(pady=10)
altura = tk.Entry(main_window)
altura.pack(pady=10)

kilos_label = tk.Label(main_window, text='Digite seu peso')
kilos_label.pack(pady=10)
kilo = tk.Entry(main_window)
kilo.pack(pady=10)

ver_imc = tk.Button(main_window, text='Calcular', command=calcular_imc)
ver_imc.pack(pady=10)

result = tk.Label(main_window, text='')
result.pack(pady=10)

main_window.mainloop()
