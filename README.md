# 🎲 Şanslı Sayı Simülatörü

Python ile geliştirilmiş, **renkli terminal arayüzüne** sahip şanslı sayı belirleme aracı. Sayısal Loto için 6-6 zar kuralına göre şanslı sayılar üretir.

<img src="https://i.imgur.com/JQ9q6W7.gif" width="500" alt="Demo Gif">

## ✨ Özellikler
- 1-90 arası sayılar için çift zar atma mekanizması
- Sadece 6-6 gelen sayıları şanslı kabul etme
- Renkli terminal çıktıları ve animasyon efektleri
- Ctrl+C ile güvenli çıkış

## 🛠 Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/metatronslove/sansli-sayi.git
   cd sansli-sayi
   ```

2. Gereksinimleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Çalıştırın:
   ```bash
   python sans_oyunu.py
   ```

## 📊 Nasıl Çalışır?
- Her sayı için 2 zar atar
- 7 adet 6-6 kombinasyonu yakalayana kadar devam eder
- Şanslı sayılar numaralandırılmış liste halinde gösterilir

## 🌟 Örnek Çıktı
```text
╔════════════════════════════╗
║     ŞANS LİSTESİ (6-6)     ║
╚════════════════════════════╝
1. 12
2. 42
3. 55
...
```

## 📜 Lisans
MIT Lisansı - [metatronslove](https://github.com/metatronslove) tarafından geliştirilmiştir.

> ⚠️ Not: Bu proje eğlence amaçlıdır. Gerçek şans oyunlarıyla bağlantısı yoktur.
```