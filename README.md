# Robotun Pili ve Malzemesi — kurs dosyaları

Forenly AI Academy'deki **Robotun Pili ve Malzemesi** kursunun hesap dosyaları. Derslerde ekranda gördüğünüz her Python oturumu, tablo ve şekil bu betiklerle üretildi.

Kursu izlemek için program yazmanız gerekmez; bütün alıştırmalar kâğıt, kalem ve hesap makinesiyle yapılabilir. Bu dosyalar, derslerdeki hesapları kendi bilgisayarında yinelemek isteyenler içindir.

## Gerekenler

- **Python 3.10 veya üstü**, `numpy` (2.0 ya da üstü) ve `matplotlib`. Hepsi ücretsizdir.
- Kurulum: `python -m pip install -r requirements.txt`
- Bilgisayarınıza kurmak istemezseniz tarayıcıda çalışan bir not defterine (ör. Google Colab) bu klasörü yükleyip aynı betikleri çalıştırabilirsiniz.

## Nasıl çalıştırılır

1. Bu depoyu indirin (Code → Download ZIP) ve klasörde bir terminal açın.
2. Haftaları sırayla çalıştırın: `python hafta1.py`, `python hafta2.py`, `python hafta3.py`, `python hafta4.py`.
3. Betikler çalışınca `ekran/<ders>/` klasöründe şekiller (`.png`) ve Python oturum kayıtları (`.txt`), kökte de hesaplanan sayılar (`OLCUMLER.json`) oluşur.
4. İsteğe bağlı: `python komut_ciz.py` oturum kayıtlarını derslerdeki gibi resme çizer (Pillow ve DejaVu yazı tipi gerekir).

## Sonucunuzu karşılaştırın

`beklenen/OLCUMLER.json` ekibimizin 2026-10-08 koşumunda hesapladığı sayılardır; `beklenen/ekran/` aynı koşumun şekilleri ve oturum kayıtlarıdır.

## Dosyalar

| Dosya | İçerik |
|---|---|
| `kaynaklar.py` | Kaynaklı değer tabloları: atom kütleleri, elektronegatiflik, iyonlaşma enerjisi, yoğunluk, malzeme dayanımı, standart indirgenme potansiyelleri, öz ısılar, oluşum entalpileri, çay şekerinin çözünürlüğü, sitrik asit. Her tablonun kaynağı ve nasıl doğrulandığı dosyanın başındaki `KAYNAK` sözlüğündedir |
| `ortak.py` | Kaydı ve kol tablosunu okuma, hesaplanan sayıyı yazma, oturum kaydı ve şekil kaydetme |
| `arac.py` | Robotla ilgili hesaplar (dirseğin torku, gücü ve işi), çizim yardımcıları ve **ÖRNEK** değerlerin tek listesi (`ORNEK`) |
| `hafta1.py` | Robotun malzemesi: element kartı, bağ türü, malzeme tablosu, mol, yoğunluk, gram başına dayanım |
| `hafta2.py` | Pil kimyası: yükseltgenme basamağı, aktiflik sırası, hücre gerilimi, gram başına yük, enerji bütçesi |
| `hafta3.py` | Enerji ve ısı: birimler, öz ısı, denge sıcaklığı, tepkime entalpisi, motorun ısınması ve soğuması |
| `hafta4.py` | Çözeltiler ve çay: derişim, çözünürlük eğrisi, çayın soğuması, limon suyunun pH hesabı, bitirme projesinin adımları |
| `komut_ciz.py` | Oturum kayıtlarını resme çizer (isteğe bağlı) |
| `veri/cay_servisi_kaydi.csv` | Çay servisi benzetim kaydı: zaman, kol eklem açıları, bardağın konumu × 5666 örnek (saniyede 50) |
| `veri/kol_kutle.csv`, `veri/kol_parametre.csv` | Benzetimdeki robot modelinin kol parçası kütleleri ve eklem kartı (elin kütlesi VARSAYIM) |

## Sayılar nereden geliyor

Bu kursta her sayı üç yerden birinden gelir ve derslerde hangisinden geldiği söylenir:

1. **Benzetim kaydı.** Robotla ilgili sayılar (servis süresi, dirseğin torku ve işi, kol parçalarının kütlesi) bir insansı robotun kafede çay servisi yaptığı benzetimin kaydından ve benzetim modelinden hesaplanır. **Gerçek robot ölçümü değildir.** Dirsek hesabı basitleştirilmiştir: yalnız yerçekimine karşı gereken tork sayılır.
2. **Kaynak tablosu.** Kimya değerleri `kaynaklar.py` içindedir; her değerin kaynağı ve hangi sayfadan okunduğu yazılıdır. Bazı değerler ikincil sayfalar üzerinden okunmuştur; bu, ilgili kaynağın `dogrulama` alanında belirtilir. Malzeme dayanımları **tipik** değerlerdir.
3. **ÖRNEK.** Pil paketi (hücre gerilimi, kapasite, hücre sayısı), verim, bekleme gücü, motor sabiti, soğuma süreleri, çay, bardak, şeker ve limon miktarları hesabı göstermek için seçilmiş yuvarlak sayılardır (`arac.py` içindeki `ORNEK`). Belirli bir robotun, pilin ya da motorun gerçek değeri **değildir**; kendi değerlerinizle değiştirip betiği yeniden çalıştırabilirsiniz.

## Güvenlik

Bu kursta evde deney yoktur. Pil sökmeyin, şişmiş ya da hasarlı pili kullanmayın, asit ya da temizlik maddesi karıştırmayın, bir şey yakmayın. Mutfak gözlemlerini (ör. ılık suyun soğumasını ölçmek) kaynar suyla değil ılık suyla ve bir yetişkinin bilgisiyle yapın.

## Müfredat

Dersler Millî Eğitim Bakanlığı lise kimya programındaki konulara bağlanır (9. sınıf: periyodik özellikler ve kimyasal bağlar; 10. sınıf: mol kavramı ve çözeltiler; 11. sınıf: tepkimelerde enerji, asit ve baz dengesi; 12. sınıf: indirgenme-yükseltgenme ve elektrokimyasal hücreler). Isı alışverişi hesabı ayrıca fizik dersinde işlenir. Kurs okul dersine destektir; ders kitabının ve öğretmeninizin yerini tutmaz.
