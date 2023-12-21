# ANALISIS PERGERAKAN HARGA SAHAM GARUDA INDONESIA MENGGUNAKAN METODE LSTM

Projek Sains Data Deep Learning Kelompok 3 RB

Disusun oleh:

  1. Adelia Mutiara Zulna (120450104)

  2. Annesa Azizi 				(120450040)

  3. Gregorius Gama			  (120450018)

  4. Very Andreas				  (120450110)

**Deskripsi:**

Proyek ini bertujuan untuk mengaplikasikan metode LSTM dalam menganalisis pergerakan harga saham Garuda Indonesia. Dengan menggunakan data harga saham historis bersama dengan state dari model LSTM, penelitian ini diharapkan dapat memberikan wawasan yang lebih mendalam tentang pergerakan harga saham Garuda Indonesia, memprediksi tren pasar, dan membantu para investor dalam mengambil keputusan investasi yang lebih cerdas. dari pemodelan dilakukan evaluasi kinerja model menggunakan MAE, RMSE, MAPE, dan RMSPE.

**Metode:**

Metode yang digunakan dalam proyek ini adalah metode LSTM (Long Short-Term Memory). LSTM adalah model jaringan saraf tiruan yang dapat mempelajari pola temporal dalam data. Dalam proyek ini, LSTM digunakan untuk menganalisis pergerakan harga saham.

**Data:**

Data yang digunakan adalah data saham emiten maskapai BUMN yakni PT Garuda Indonesia Tbk (GIAA) bersumber dari aplikasi BNI Sekuritas. Data yang dipergunakan mulai dari 08-01-2013 sampai 08-31-2023, total data berjumlah 2444 dan 6 variabel.

**Tahapan:**

Adapun proses yang dilakukan untuk memperoleh pemodelan dengan metode LSTM sebagai berikut:
1. Import Data di tools google colab
2. Melakukan prapemrosesan sebagai tahap untuk mengetahui kriteria variabel data
3. Melakukan EDA sebagai tahap ekplorasi data analisis untuk melakukan tahap statistika dan beberapa visualisai yang diperlukan
4. Melakukan Scalling data dengan tujuan untuk melakukan skala antar data tidak memiliki jarak yang terlalu jauh
5. Splitting data sebagai tahap pembagian data train (data latih model( dan data test (data uji)
7. Pemodelan dengan metode LSTM
8. Evaluasi model, penelitian menggunakan MAE, RMSE, MAPE, dan RMSPE.

**Hasil:**

Tingkat keakuratan metode LSTM yang digunakan dalam memprediksi gerakan saham Garuda Indonesia memperoleh keakuratan yang sangat baik diperoleh dari MAPE 1.37%, dan RMSPE 2.86%. dan didalam projek ini kami menggunakan perbandingan 2 optimizer yaitu Adam dan RMSprop.

![image](https://github.com/sains-data/Kelompok3_RB/assets/124365388/051b6010-1489-49b0-88f9-c5cc7f045505)

