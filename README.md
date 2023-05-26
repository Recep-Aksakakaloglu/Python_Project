# Sorting Algorithms By Python
## Proje Konusu
Bu projenin amacı kullanıcının sıralama algoritmalarını ve grafik türlerini kullanarak bir listenin sıralanmasını ve sıralama işleminin adımlarını görsel bir şekilde görmesini sağlamaktır. 

## Sıralama Algoritmaları Nelerdir?
### Bubble Sort
* Kabarcık sıralama, sıralama algoritmaları arasında yazılması en kolay olan, ama büyük dizilerde çok yavaş kalan ve O(n2) grubuna giren bir sıralama yöntemidir.
* Bu algoritmanın işleyişi şu şekildedir; Baştan sona veya sondan başa doğru komşu elemanlar karşılaştırılarak büyüklük küçüklük durumlarına göre yerleri değiştirilir. Komşu elemanların bu karşılaştırmalı taraması, dizinin eleman sayısı kadar tekrarlanır.

### Insertion Sort
* Sıralı diziyi her adımda öğe öğe oluşturan bir sıralama algoritmasıdır. Büyük dizilerle çalışıldığında hızlı sıralama, birleştirmeli sıralama ve yığın sıralaması gibi daha gelişmiş sıralama algoritmalarından daha verimsiz çalışır. Uygulaması kolaydır. Küçük Veri kümeleri üzerinde kullanıldığında ve çoğunluğu zaten sıralanmış olan diziler üzerinde kullanıldığında verimlidir. Karmaşıklığı O(n2) olan seçmeli sıralama ve kabarcık sıralaması gibi çoğu yalın sıralama algoritmalarından da daha verimlidir. Sıralanacak diziyi yerinde sıralar, ek bir bellek alanı gerektirmez. Sıralanacak dizinin hepsinin algoritmanın girdisi olmasına gerek yoktur. Dizi parça parça da alınabilir ve sıralama işlemi sırasında diziye yeni veriler eklenebilir.
* Bu algoritmanın işleyişi şu şekildedir; Her eleman, kendinden önceki alt dizideki elemanlarla karşılaştırılmakta ve daha küçükse ilgili yerdeki araya yerleştirilmektedir. Yani rastlanan her küçük eleman dizideki araya girerek, diğer dizi elemanlarını sona doğru ittirmektedir.

### Selection Sort
* Seçmeli sıralama algoritması O(n2) grubuna giren bir sıralama yöntemidir. Dolayısıyla büyük sayıda verileri sıralamak için kullanışlı değildir.
* Bu algoritmanın işleyişi şu şekildedir; Rastgele (random) olarak sıralanmış bir diziyi küçükten büyüğe doğru sıralamak istediğimizde, dizinin her döndürülmesinde en küçük elemanını seçerek en başa yazdırmaktadır. Yani birinci taramada bulunan en küçük eleman birinci sıraya; ikinci elemandan başlayarak yapılan ikinci taramada bulunan en küçük ikinci elaman ikinci sıraya vb. yerleştirirlerek sıralama işlemi tamamlanmaktadır.

### Merge Sort
* O (n log(n)) derecesinde karmaşıklığa sahip bir sıralama algoritmasıdır.
* Bu algoritmanın işleyişi şu şekildedir: Dizimiz, alt dizilere ayrıştırılarak her biri ayrı ayrı sıralanıp birleştirilmektedir. Yinelemeli olan bu algoritmanın çalışması aşağıdaki gibi özetlenebilir:
* I. Diziyi eşit iki alt diziye ayır.
* II. Bu ayırma işlemini, alt dizilerde en fazla 2 eleman kalıncaya kadar sürdür.
* III. Alt dizileri kendi içinde büyükten küçüğe doğru sırala.
* IV. Sıralı alt dizileri birleştir.
* Sıralı iki alt dizi elemanları bitinceye kadar, sırada ki elemanları alınarak karşılaştırılır.
* Her iki alt dizi elemanları bitinceye kadar, sıradaki elemanları alınarak karşılaştırılır.
### 1.1
*  Eğer birinci alt dizinin sırada ki elemanı, 2. alt dizinin sıradaki elemanından küçükse, oluşan birleştirilmiş dizinin sırada ki elemanı olarak atanır. 1. dizi için sıradaki elemanı gösteren indis ve oluşan birleştirilmiş dizinin indisi bir arttırılır.
### 1.2
*  Eğer 1. alt dizinin sıradaki elemanı, 2. dizinin sıradaki elemanından büyükse, 2. Alt dizinin sıradaki elemanı; oluşan birleştirilmiş dizinin sıradaki elemanı olarak atanır. 2. dizi için sıradaki elemanı gösteren indis ve oluşan birleştirilmiş dizinin indisi bir arttırılır.
### 2
* Eğer herhangi  bir alt dizide sona ulaşılmamışsa; bu dizinin elemanları, oluşan birleştirilmiş diziye eklenir.

### Quick Sort
* n adet sayıyı, ortalama bir durumda, O(n log(n)) karmaşıklığıyla, en kötü durumda ise O (n2) karmaşıklığıyla sıralar. Yinelemeli olup sık kullanılır. Algoritmanın karmaşıklığı aynı zamanda yapılan karşılaştırma sayısına eşittir.
* Bu algoritmanın işleyişi şu şekildedir; Belirli kriterlere göre pivot eleman seçilir. Diziyi 3 alt diziye ayrıştırır bunlar pivot elemandan küçük olan elemanları birinci (soldaki) diziye, pivot elemanı ikinci (ortadaki) diziye, pivot elemandan büyük olanları da üçüncü (sağdaki) diziye. Aynı işlemi birinci (soldaki) ve üçüncü (sağdaki) alt dizilere, tek elemanlı kalıncaya kadar uygulanır. Ve en son olarak sıralı alt dizileri birleştirir.

## Kullanılan Teknolojiler
### A. Python
![alt text](https://github.com/Recep-Aksakakaloglu/Python_Project/blob/main/python.png)
