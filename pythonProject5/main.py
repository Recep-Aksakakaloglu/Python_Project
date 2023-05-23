import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Grafik verileri
x = [10, 15, 20, 25, 30]
y = [30, 15, 25, 20, 10]

# Grafik oluşturma fonksiyonu
def create_graph():
    plt.clf()  # Önceki grafikleri temizle
    renk = ['green']
    plt.bar(x, y, color=renk)  # Çubuk grafik oluştur
    canvas.draw()  # Grafikleri güncelle

# Sıralama fonksiyonları
def bubble_sort(index=0):
    if index < len(y) - 1:
        for j in range(len(y) - index - 1):
            if y[j] > y[j+1]:
                y[j], y[j+1] = y[j+1], y[j]
        create_graph()  # Sıralama adımını görselleştir
        panel.after(500, bubble_sort, index + 1)

def selection_sort(index=0):
    if index < len(y):
        min_idx = index
        for j in range(index+1, len(y)):
            if y[j] < y[min_idx]:
                min_idx = j
        y[index], y[min_idx] = y[min_idx], y[index]
        create_graph()
        panel.after(500, selection_sort, index + 1)

def insertion_sort(index=1):
    if index < len(y):
        key = y[index]
        j = index - 1
        while j >= 0 and y[j] > key:
            y[j+1] = y[j]
            j -= 1
        y[j+1] = key
        create_graph()  # Sıralama adımını görselleştir
        panel.after(500, insertion_sort, index + 1)

def perform_sort():
    selected_algorithm = var.get()
    if selected_algorithm == 1:
        bubble_sort()
    elif selected_algorithm == 2:
        selection_sort()
    elif selected_algorithm == 3:
        insertion_sort()


# Tkinter uygulaması oluşturma
panel = tk.Tk()
panel.title("Yazlab Sıralama")

ikon_yolu = "logoyazlab.ico"
panel.iconbitmap(ikon_yolu)

# Grafik alanı
fig = plt.figure(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=panel)
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Sıralama seçenekleri
frame = tk.Frame(panel)
frame.pack(side=tk.RIGHT, padx=10)


var = tk.IntVar()
var.set(1)

bubble_button = tk.Radiobutton(frame, text="Bubble Sort", variable=var, value=1)
bubble_button.pack(anchor=tk.W)

selection_button = tk.Radiobutton(frame, text="Selection Sort", variable=var, value=2)
selection_button.pack(anchor=tk.W)

insertion_button = tk.Radiobutton(frame, text="Insertion Sort", variable=var, value=3)
insertion_button.pack(anchor=tk.W)

sort_button = tk.Button(frame, text="Sırala", command=perform_sort,bg="gray", fg="white")
sort_button.pack(anchor=tk.W)



yenileme = tk.Button(frame, text="->", bg="gray", fg="white")
yenileme.pack(anchor=tk.W,pady=10)

# Başlangıçta grafik oluştur
create_graph()

# Uygulamayı başlat
panel.mainloop()
