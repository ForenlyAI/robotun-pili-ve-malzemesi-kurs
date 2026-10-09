"""Hafta 4 · Çözeltiler ve Çay — Ders 4.1–4.4 (bitirme projesi dahil).
  python hafta4.py   → ekran/4.x/*.txt + *.png, OLCUMLER.json (d4_*)"""
import numpy as np
import matplotlib.pyplot as plt
from ortak import olc, oturum, sekil, kayit
from arac import kutu, ok, bos_eksen, tr, dirsek_isi, ORNEK, TURUNCU, MAVI, YESIL, MOR, GRI, KIRMIZI
from kaynaklar import SAKKAROZ, SITRIK, OZ_ISI, mol_kutlesi


def ders_4_1():
    """Çözünme ve derişim: çözücü, çözünen, moleküler ve iyonik çözünme; kütlece yüzde, molarite, milyonda bir."""
    fig, ax = bos_eksen("Çözelti = çözücü + çözünen")
    kutu(ax, 0.03, 0.66, 0.26, 0.18, "çözücü\nsu (çay)", MAVI, boy=28)
    ax.text(0.325, 0.75, "+", fontsize=44, ha="center", va="center", weight="bold")
    kutu(ax, 0.36, 0.66, 0.26, 0.18, "çözünen\nşeker", TURUNCU, boy=28)
    ok(ax, 0.64, 0.75, 0.70, 0.75)
    kutu(ax, 0.72, 0.66, 0.25, 0.18, "çözelti\nşekerli çay", YESIL, boy=28)
    kutu(ax, 0.03, 0.22, 0.41, 0.34, "Moleküler çözünme\n\nşeker molekülleri bütün kalır,\nsu molekülleri arasına dağılır\n\nçözelti elektriği iletmez", "#FFF7ED", boy=23, yazi="#111111")
    kutu(ax, 0.56, 0.22, 0.41, 0.34, "İyonik çözünme\n\nsofra tuzu artı ve eksi\niyonlarına ayrılır\n\nçözelti elektriği iletir", "#EFF6FF", boy=23, yazi="#111111")
    ax.text(0.5, 0.09, "Pilin içindeki elektrolit de iyon taşıyan bir çözeltidir", ha="center", fontsize=26)
    sekil("4.1", "cozunme")
    ns = oturum("4.1", "derisim", """
from arac import ORNEK
from kaynaklar import mol_kutlesi
seker = mol_kutlesi({"C": 12, "H": 22, "O": 11})
round(seker, 2)                                   # çay şekerinin mol kütlesi, g/mol
m, V = ORNEK["seker_g"], ORNEK["cay_mL"]   # ÖRNEK: iki küp şeker, bir bardak çay
m, V
mol = m / seker
round(mol, 4)
round(mol / (V / 1000), 3)   # molarite, mol/L (hacim aynı sayıldı)
cozelti_g = ORNEK["cay_g"] + m
round(100 * m / cozelti_g, 2)                     # kütlece yüzde
round(1e6 * m / cozelti_g)                        # milyonda bir (ppm)
""")
    kup = np.arange(1, 5); M = kup * 2.5 / ns["seker"] / (ns["V"] / 1000)
    fig, ax = plt.subplots()
    ax.bar(kup, M, color=TURUNCU, width=0.55)
    for k, v in zip(kup, M):
        ax.text(k, v + 0.006, tr(v, 3) + " mol/L", ha="center", fontsize=28, weight="bold")
    ax.set_xticks(kup); ax.set_xticklabels([f"{k} küp" for k in kup], fontsize=28); ax.set_ylabel("molarite (mol/L)"); ax.set_ylim(0, M.max() * 1.15)
    ax.grid(axis="x", visible=False)
    ax.set_title("Şeker arttıkça derişim artar · bir küp 2,5 g ve bardak 100 mL (ÖRNEK)")
    sekil("4.1", "derisim-kup")
    olc(d4_1_seker_g_mol=round(ns["seker"], 2), d4_1_ornek_seker_g=ns["m"], d4_1_ornek_cay_mL=ns["V"], d4_1_mol=round(ns["mol"], 4),
        d4_1_molarite=round(ns["mol"] / (ns["V"] / 1000), 3), d4_1_yuzde=round(100 * ns["m"] / ns["cozelti_g"], 2),
        d4_1_ppm=round(1e6 * ns["m"] / ns["cozelti_g"]), d4_1_dort_kup_M=round(float(M[-1]), 3))


def ders_4_2():
    """Çözünürlük ve sıcaklık: sakkarozun çözünürlük tablosu ve eğrisi; doymamış, doymuş, aşırı doymuş."""
    ns = oturum("4.2", "cozunurluk-tablosu", """
from kaynaklar import SAKKAROZ
for T in (0, 20, 40, 60, 80, 100):
    print(f"{T:4d} °C   {SAKKAROZ[T]:6.1f} g şeker / 100 mL su")
round(SAKKAROZ[100] / SAKKAROZ[0], 2)
round(SAKKAROZ[90] / SAKKAROZ[20], 2)
""")
    T = np.array(sorted(SAKKAROZ)); S = np.array([SAKKAROZ[t] for t in T])
    fig, ax = plt.subplots()
    ax.fill_between(T, S, 0, color=MAVI, alpha=0.10); ax.fill_between(T, S, 560, color=TURUNCU, alpha=0.10)
    ax.plot(T, S, "o-", color=MAVI, lw=4, ms=12)
    ax.text(40, 80, "doymamış\n(daha şeker çözünür)", fontsize=27, ha="center", color=MAVI, weight="bold")
    ax.text(28, 430, "çözünmez, dibe çöker\n(ya da aşırı doymuş)", fontsize=27, ha="center", color=TURUNCU, weight="bold")
    ax.annotate("eğrinin üzerindeki nokta: doymuş", xy=(70, SAKKAROZ[70]), xytext=(58, 150), fontsize=26, arrowprops=dict(arrowstyle="-|>", lw=3, color="#111111"))
    ax.set_xlabel("sıcaklık (°C)"); ax.set_ylabel("çözünürlük (g şeker / 100 mL su)"); ax.set_xlim(0, 100); ax.set_ylim(0, 560)
    ax.set_title("Çay şekerinin sudaki çözünürlüğü sıcaklıkla artar · kaynak tablosundan")
    sekil("4.2", "cozunurluk-egrisi")
    ns2 = oturum("4.2", "doymus-mu", """
from kaynaklar import SAKKAROZ
from arac import ORNEK
seker, su = ORNEK["seker_g"], ORNEK["cay_mL"]      # ÖRNEK: iki küp şeker, 100 mL
round(100 * seker / SAKKAROZ[90], 1)               # 90 °C'de sınırın yüzde kaçı
int(SAKKAROZ[20] / 2.5)   # 20 °C'de en çok kaç küp (küp 2,5 g ÖRNEK)
sicak, soguk = SAKKAROZ[90], SAKKAROZ[20]
sicak, soguk
round(sicak - soguk, 1)   # 90 → 20 °C soğuyunca çöken şeker, g
""")
    olc(d4_2_tablo={str(t): SAKKAROZ[t] for t in (0, 20, 40, 60, 80, 100)}, d4_2_oran_100_0=round(SAKKAROZ[100] / SAKKAROZ[0], 2),
        d4_2_oran_90_20=round(SAKKAROZ[90] / SAKKAROZ[20], 2), d4_2_sinirin_yuzdesi=round(100 * ns2["seker"] / SAKKAROZ[90], 1),
        d4_2_en_cok_kup=int(SAKKAROZ[20] / 2.5), d4_2_S90=SAKKAROZ[90], d4_2_S20=SAKKAROZ[20], d4_2_coken_g=round(SAKKAROZ[90] - SAKKAROZ[20], 1))


def ders_4_3():
    """Çayın soğuması: bardağa dökülünce denge sıcaklığı; servis süresince soğuma (süre benzetim kaydından, soğuma sabiti ÖRNEK)."""
    ns = oturum("4.3", "bardaga-dokulunce", """
from arac import ORNEK
from kaynaklar import OZ_ISI
cay_g, cay_C = ORNEK["cay_g"], ORNEK["cay_C"]              # ÖRNEK: 100 g çay, 90 °C
bardak_g, oda_C = ORNEK["bardak_g"], ORNEK["oda_C"]   # ÖRNEK: 80 g cam bardak, 22 °C
C_cay = cay_g * OZ_ISI["su"]                               # çay su sayıldı
C_bardak = bardak_g * OZ_ISI["cam"]
round(C_cay, 1), round(C_bardak, 1)                        # ısı sığaları, J/°C
T0 = (C_cay * cay_C + C_bardak * oda_C) / (C_cay + C_bardak)
round(T0, 1)   # ortak sıcaklık, °C
round(C_cay * (cay_C - T0))   # bardağa geçen ısı, joule
""")
    T0 = ns["T0"]; oda = ns["oda_C"]; ts = ORNEK["cay_soguma_sabiti_s"]; sure = float(kayit()["zaman_s"][-1])
    z = np.linspace(0, 1800, 361); Tz = oda + (T0 - oda) * np.exp(-z / ts); Ts = oda + (T0 - oda) * np.exp(-sure / ts)
    fig, ax = plt.subplots()
    ax.plot(z / 60, Tz, color=KIRMIZI, lw=4)
    ax.axvspan(0, sure / 60, color=YESIL, alpha=0.18)
    ax.plot([sure / 60], [Ts], "o", color=YESIL, ms=18)
    ax.annotate(f"servis bitti: {tr(sure, 1)} s\n{tr(Ts, 1)} °C", xy=(sure / 60, Ts), xytext=(6, 76), fontsize=27,
                arrowprops=dict(arrowstyle="-|>", lw=3, color="#111111"))
    ax.axhline(oda, color=GRI, ls="--", lw=3); ax.text(24, oda + 1.5, f"oda {tr(oda, 0)} °C", fontsize=26, color="#374151")
    ax.set_xlabel("zaman (dakika)"); ax.set_ylabel("çayın sıcaklığı (°C)"); ax.set_ylim(15, 90); ax.set_xlim(0, 30)
    ax.set_title("Çay yolda ne kadar soğur · servis süresi benzetim kaydından · soğuma sabiti ÖRNEK")
    sekil("4.3", "soguma-egrisi")
    ns2 = oturum("4.3", "servis-sonu", """
import numpy as np
from ortak import kayit
from arac import ORNEK, dirsek_isi
sure = kayit()["zaman_s"][-1]   # süre: benzetim kaydı
sabit = ORNEK["cay_soguma_sabiti_s"]   # soğuma zaman sabiti ÖRNEK
T_son = oda_C + (T0 - oda_C) * np.exp(-sure / sabit)
round(sure, 1), round(T_son, 1)
round(T0 - T_son, 1)                                       # yolda kaç derece soğudu
Q_hava = (C_cay + C_bardak) * (T0 - T_son)
round(Q_hava)   # havaya verilen ısı, joule
W_arti = dirsek_isi()[3]
round(W_arti, 1), round(Q_hava / W_arti)                   # dirseğin işi ve oran
""", ns)
    olc(d4_3_ornek_cay_g=ns["cay_g"], d4_3_ornek_cay_C=ns["cay_C"], d4_3_ornek_bardak_g=ns["bardak_g"], d4_3_ornek_oda_C=oda,
        d4_3_C_cay=round(ns["C_cay"], 1), d4_3_C_bardak=round(ns["C_bardak"], 1), d4_3_T0=round(T0, 1), d4_3_bardaga_J=round(ns["C_cay"] * (ns["cay_C"] - T0)),
        d4_3_sure_s=sure, d4_3_ornek_soguma_s=ts, d4_3_T_son=round(float(ns2["T_son"]), 1), d4_3_dusus=round(float(T0 - ns2["T_son"]), 1),
        d4_3_Q_hava_J=round(float(ns2["Q_hava"])), d4_3_W_arti_J=round(ns2["W_arti"], 1), d4_3_oran=round(float(ns2["Q_hava"]) / ns2["W_arti"]),
        d4_3_ilk_dusus=round(ns["cay_C"] - T0, 1))


def ders_4_4():
    """Asit, baz ve pH: zayıf asit hesabı (limon suyu, çaya sıkılan limon); bitirme projesinin dört adımı."""
    ns = oturum("4.4", "limon-ph", """
import numpy as np
from kaynaklar import SITRIK
from arac import ORNEK
g_L = SITRIK["limon_g_ons"] / SITRIK["ons_mL"] * 1000   # sitrik asit, g/L (kaynak)
C = g_L / SITRIK["mol_kutlesi"]
round(g_L, 1), round(C, 3)                                 # g/L ve mol/L
Ka = 10 ** -SITRIK["pKa1"]
def pH(C):
    # zayıf asit, yalnız birinci iyonlaşma:  x² / (C − x) = Ka
    x = (-Ka + np.sqrt(Ka ** 2 + 4 * Ka * C)) / 2
    return -np.log10(x)
round(pH(C), 2)                                            # limon suyu (hesap)
C_cay = C * ORNEK["limon_mL"] / (ORNEK["cay_mL"] + ORNEK["limon_mL"])
round(C_cay, 4), round(pH(C_cay), 2)   # suya 5 mL limon (ÖRNEK)
""")
    pH_limon = float(ns["pH"](ns["C"])); pH_sulu = float(ns["pH"](ns["C_cay"]))
    fig, ax = plt.subplots()
    renkler = plt.cm.RdYlBu(np.linspace(0.05, 0.95, 140))
    for i in range(140):
        ax.axvspan(i / 10, (i + 1) / 10, ymin=0.38, ymax=0.62, color=renkler[i])
    for x, ad, y in [(pH_limon, f"limon suyu\n{tr(pH_limon, 2)} (hesap)", 0.80), (pH_sulu, f"suya limon\n{tr(pH_sulu, 2)} (hesap)", 0.20), (7, "saf su\n7 (25 °C)", 0.80)]:
        ax.annotate(ad, xy=(x, 0.62 if y > 0.5 else 0.38), xytext=(x + (1.3 if y < 0.5 else 0), y), fontsize=27, ha="center", va="center", weight="bold",
                    arrowprops=dict(arrowstyle="-|>", lw=3, color="#111111"))
    ax.text(2.3, 0.50, "ASİT", fontsize=34, weight="bold", ha="center", va="center", color="#ffffff")
    ax.text(11.5, 0.50, "BAZ", fontsize=34, weight="bold", ha="center", va="center", color="#ffffff")
    ax.text(7, 0.50, "NÖTR", fontsize=28, weight="bold", ha="center", va="center", color="#111111")
    ax.text(7, 0.05, "pH bir birim düşerse hidrojen iyonu derişimi on katına çıkar", fontsize=26, ha="center")
    ax.set_xlim(0, 14); ax.set_ylim(0, 1); ax.set_xticks(range(15)); ax.set_yticks([]); ax.set_xlabel("pH"); ax.grid(False)
    ax.set_title("pH ölçeği · hesap: yalnız sitrik asit ve su; gerçek çayda başka maddeler de var")
    sekil("4.4", "ph-olcegi")
    fig, ax = bos_eksen("Bitirme projesi: robotun enerji ve malzeme raporu")
    adim = [("1", "Mekanik iş", "benzetim kaydından\ndirseğin işi", YESIL),
            ("2", "Enerji bütçesi", "görev süresi için\nwatt saat\n(pil değerleri ÖRNEK)", MOR),
            ("3", "Pil kimyası", "potansiyel ve gram\nbaşına yük tablosuyla\ngerekçe", TURUNCU),
            ("4", "Gövde malzemesi", "yoğunluk ve dayanım\ntablosuyla gerekçe", MAVI)]
    for i, (no, ad, ne, renk) in enumerate(adim):
        x = 0.03 + i * 0.25
        kutu(ax, x, 0.62, 0.19, 0.20, f"{no} · {ad}", renk, boy=24)
        kutu(ax, x, 0.26, 0.19, 0.28, ne, "#F3F4F6", boy=21, yazi="#111111")
    ax.text(0.5, 0.11, "Her sayının yanına kaynağını yazın: kayıt, kaynak tablosu ya da ÖRNEK", ha="center", fontsize=26)
    sekil("4.4", "bitirme-adimlari")
    olc(d4_4_limon_g_L=round(ns["g_L"], 1), d4_4_limon_M=round(ns["C"], 3), d4_4_pKa1=SITRIK["pKa1"], d4_4_pH_limon=round(pH_limon, 2),
        d4_4_ornek_limon_mL=ORNEK["limon_mL"], d4_4_sulu_M=round(ns["C_cay"], 4), d4_4_pH_sulu=round(pH_sulu, 2),
        d4_4_H_orani=round(10 ** (pH_sulu - pH_limon), 1), d4_4_bitirme_adim=len(adim), d4_4_pH_saf_su=7)


if __name__ == "__main__":
    ders_4_1(); ders_4_2(); ders_4_3(); ders_4_4()
    print("hafta 4 tamam")
