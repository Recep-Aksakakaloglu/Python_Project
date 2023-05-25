import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import random
import re

# Grafik verileri
#x = [10, 15, 20, 25, 30]
#y = [30, 15, 25, 20, 10]

x = []
y = []
colors = []

sorting_in_progress = False
sorting_speed = 500
comparison_count = 0

# Grafik oluşturma fonksiyonu
def create_graph():
    plt.clf()  # Önceki grafikleri temizle
    colors = generate_colors(len(x))
    selected_plot = var_plot.get()
    if selected_plot == 1:
        plt.bar(x, y, color=colors)  # Çubuk grafik oluştur
        for i, value in enumerate(y):
            plt.text(x[i], value, str(value), ha='center', va='bottom')  # Rakamları çubukların içine yazdır
    elif selected_plot == 2:
        plt.scatter(x, y, color=colors)  # Nokta grafik oluştur
        for i, value in enumerate(y):
            plt.text(x[i], value, str(value), ha='center', va='bottom',
                     fontsize=8)  # Rakamları noktaların yanına yazdır
    elif selected_plot == 3:
        plt.stem(x, y, linefmt='C0-', markerfmt='C0o', basefmt='k-')
    canvas.draw()  # Grafikleri güncelle

def generate_colors(count):
    colors = []
    for _ in range(count):
        color = "#%06x" % random.randint(0, 0xFFFFFF)  # Rastgele bir renk üret
        colors.append(color)
    return colors

# Sıralama fonksiyonları
def bubble_sort(index=0):
    global sorting_in_progress
    global comparison_count

    if index < len(y) - 1:
        for j in range(len(y) - index - 1):
            comparison_count += 1
            if y[j] > y[j+1]:
                y[j], y[j+1] = y[j+1], y[j]
        create_graph()  # Sıralama adımını görselleştir
        if sorting_in_progress:
            panel.after(speed_slider.get(), bubble_sort, index + 1)

def selection_sort(index=0):
    if index < len(y):
        min_idx = index
        for j in range(index+1, len(y)):
            comparison_count += 1
            if y[j] < y[min_idx]:
                min_idx = j
        y[index], y[min_idx] = y[min_idx], y[index]
        create_graph()
        if sorting_in_progress:
            panel.after(speed_slider.get(), selection_sort, index + 1)

def insertion_sort(index=1):
    if index < len(y):
        key = y[index]
        j = index - 1
        while j >= 0 and y[j] > key:
            comparison_count += 1
            y[j+1] = y[j]
            j -= 1
        y[j+1] = key
        create_graph()  # Sıralama adımını görselleştir
        if sorting_in_progress:
            panel.after(speed_slider.get(), insertion_sort, index + 1)

def merge_sort(arr):
    index = 1
    if len(arr) > index:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        # Sıralama adımını görselleştir
        create_graph()
        if sorting_in_progress:
            panel.after(500)

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        create_graph()
        if sorting_in_progress:
            panel.after(100)
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def perform_complexity_analysis():
    n = len(y)  # Veri dizisinin uzunluğu
    complexity = n**2
    complexity_label.config(text="Sıralama Karmaşıklığı: O(n^2)")

def perform_sort():
    selected_algorithm = var.get()
    global sorting_in_progress
    sorting_in_progress = True

    if selected_algorithm == 1:
        bubble_sort()
    elif selected_algorithm == 2:
        selection_sort()
    elif selected_algorithm == 3:
        insertion_sort()
    elif selected_algorithm == 4:
        merge_sort(y)
    elif selected_algorithm == 5:
        quick_sort(y, 0, len(y) - 1)

    perform_complexity_analysis()


def clear_data():
    global x, y
    x.clear()
    y.clear()
    create_graph()

def add_data():
    try:
        value = int(entry.get())
        x.append(len(x) + 1)
        y.append(value)
        create_graph()
        entry.delete(0, tk.END)
    except ValueError:
        print("Geçersiz giriş!")

def generate_random_data():
    try:
        count = int(entry_count.get())
        x.clear()
        y.clear()
        for i in range(count):
            x.append(i + 1)
            y.append(random.randint(1, 100))  # 1 ile 100 arasında rastgele sayı üretin
        colors = generate_colors(count)
        create_graph()
    except ValueError:
        print("Geçersiz giriş!")

def start_sort():
    global sorting_in_progress
    sorting_in_progress = True
    bubble_sort()

def stop_sort():
    global sorting_in_progress
    sorting_in_progress = False

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

merge_button = tk.Radiobutton(frame, text="Merge Sort", variable=var, value=4)
merge_button.pack(anchor=tk.W)

quick_button = tk.Radiobutton(frame, text="Quick Sort", variable=var, value=5)
quick_button.pack(anchor=tk.W)

sort_button = tk.Button(frame, text="Sırala", command=perform_sort,bg="gray", fg="white")
sort_button.pack(anchor=tk.W)

complexity_label = tk.Label(frame, text="")
complexity_label.pack(anchor=tk.W, pady=10)


# Veri ekleme alanı
data_frame = tk.Frame(panel)
data_frame.pack(side=tk.RIGHT, padx=10)

entry_label = tk.Label(data_frame, text="Sayılar: ")
entry_label.pack()

entry = tk.Entry(data_frame)
entry.pack()

add_button = tk.Button(data_frame, text="Ekle", command=add_data, bg="gray", fg="white")
add_button.pack(anchor=tk.CENTER)

tk.Label(data_frame, text="").pack()

entry_label = tk.Label(data_frame, text="Eleman Adeti: ")
entry_label.pack()

entry_count = tk.Entry(data_frame)
entry_count.pack()

generate_button = tk.Button(data_frame, text="Rastgele Veri Üret", command=generate_random_data, bg="gray", fg="white")
generate_button.pack(anchor=tk.CENTER)

tk.Label(data_frame, text="").pack()

clear_data_button = tk.Button(data_frame, text="Verileri Temizle", command=clear_data, bg="red", fg="white")
clear_data_button.pack(anchor=tk.CENTER)

plot_frame = tk.Frame(panel)
plot_frame.pack(side=tk.RIGHT, padx=10)

var_plot = tk.IntVar()
var_plot.set(1)

entry_label = tk.Label(plot_frame, text="Grafik Tipi")
entry_label.pack()
tk.Label(plot_frame, text="").pack()

bar_button = tk.Radiobutton(plot_frame, text="Çubuk (Bar)", variable=var_plot, value=1)
bar_button.pack(anchor=tk.W)

scatter_button = tk.Radiobutton(plot_frame, text="Nokta (Scatter)", variable=var_plot, value=2)
scatter_button.pack(anchor=tk.W)

stem_button = tk.Radiobutton(plot_frame, text="Stem", variable=var_plot, value=3)
stem_button.pack(anchor=tk.W)

sort_frame = tk.Frame(panel)
sort_frame.pack(side=tk.RIGHT, padx=10)

start_button = tk.Button(sort_frame, text="Sıralamayı Başlat  ", command=start_sort)
start_button.pack()

stop_button = tk.Button(sort_frame, text="Sıralamayı Durdur", command=stop_sort)
stop_button.pack()

speed_slider = tk.Scale(frame, from_=100, to=1000, resolution=100, orient=tk.HORIZONTAL, length=200)
speed_slider.set(500)  # Başlangıç hızı
speed_slider.pack(anchor=tk.W, pady=10)

# Başlangıçta grafik oluştur
create_graph()

# Uygulamayı başlat
panel.mainloop()
