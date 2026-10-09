"""Robotun Pili ve Malzemesi — robotla ilgili ortak hesaplar ve çizim yardımcıları.
  dirsek_isi()        : benzetim kaydından dirsek ekleminin torku, gücü ve yaptığı iş (basitleştirilmiş: yalnız yerçekimi torku)
  bardak_yukselmesi() : kayıtta bardağın en çok ne kadar yükseldiği (m)
  ORNEK               : kayıtta ve kaynak tablolarında OLMAYAN, derste ÖRNEK diye işaretlenen değerler (tek yerde)"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from ortak import kayit, yumusat, dirsek_karti, g

TURUNCU, MAVI, YESIL, MOR, GRI, KIRMIZI = "#C2410C", "#1D4ED8", "#0F766E", "#7E22CE", "#6B7280", "#B91C1C"

# ÖRNEK değerler: belirli bir robotun, pilin ya da bardağın gerçek değeri DEĞİLDİR; hesabı göstermek için seçilmiş yuvarlak sayılardır.
ORNEK = dict(
    hucre_gerilimi_V=3.7,      # lityum iyon hücresinin anma gerilimi (tipik, ÖRNEK)
    hucre_kapasite_Ah=10.0,    # bir hücrenin kapasitesi
    hucre_sayisi=12,           # seri bağlı hücre
    bekleme_gucu_W=200.0,      # robotun ayakta dururken çektiği güç
    verim=0.50,                # pilden eklemin mekanik işine verim
    motor_sabiti=1.0,          # N·m / √W : tork başına ısı gücü  P = (tork / sabit)²
    soguma_sabiti_s=600.0,     # motor gövdesinin soğuma zaman sabiti
    oda_C=22.0, cay_C=90.0, cay_g=100.0, bardak_g=80.0,   # ince belli bardak ve çay
    cay_soguma_sabiti_s=900.0, # çayın bardakta soğuma zaman sabiti
    seker_g=5.0,               # iki küp şeker
    cay_mL=100.0,
    limon_mL=5.0,              # bir dilim limondan sıkılan su
    bardak_kutle_kg=0.2,       # dolu bardak
)


def dirsek_isi():
    """Dirsek: tork = −(yerçekimi torku), güç = tork × açısal hız; ilk 3 saniye (yerleşme) dışarıda. Döner: t, tork, guc, W_arti, W_eksi."""
    k = kayit(); kart = dirsek_karti()
    t, q, w = k["zaman_s"], k["dirsek_rad"], yumusat(k["dirsek_hiz_rad_s"])
    m = t > 3
    tork = -(kart["cos"] * np.cos(q) + kart["sin"] * np.sin(q))
    guc = tork * w
    dt = t[1] - t[0]
    return t[m], tork[m], guc[m], float((guc[m] * (guc[m] > 0)).sum() * dt), float((guc[m] * (guc[m] < 0)).sum() * dt)


def bardak_yukselmesi():
    z = kayit()["bardak_z_m"]
    return float(z.max() - z[0])


def kutu(ax, x, y, w, h, metin, renk, boy=24, yazi="#ffffff"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03", fc=renk, ec="none"))
    ax.text(x + w / 2, y + h / 2, metin, ha="center", va="center", color=yazi, fontsize=boy, linespacing=1.4)


def ok(ax, x1, y1, x2, y2, renk="#111111"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", color=renk, lw=3, mutation_scale=28))


def bos_eksen(baslik):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off"); ax.set_title(baslik)
    return fig, ax


def tr(x, basamak=2):
    return f"{x:.{basamak}f}".replace(".", ",")
