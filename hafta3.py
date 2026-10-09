"""Hafta 3 · Enerji ve Isı — Ders 3.1–3.4.
  python hafta3.py   → ekran/3.x/*.txt + *.png, OLCUMLER.json (d3_*)"""
import numpy as np
import matplotlib.pyplot as plt
from ortak import olc, oturum, sekil, kol_kutle
from arac import kutu, ok, bos_eksen, tr, dirsek_isi, ORNEK, TURUNCU, MAVI, YESIL, MOR, GRI, KIRMIZI
from kaynaklar import OZ_ISI, OLUSUM, KUTLE


def ders_3_1():
    """Isı ve sıcaklık: iki kavramın farkı, birimler, aynı ısı farklı maddede farklı sıcaklık artışı."""
    fig, ax = bos_eksen("Sıcaklık bir durum, ısı bir alışveriş")
    kutu(ax, 0.04, 0.60, 0.40, 0.22, "SICAKLIK", KIRMIZI, boy=36)
    kutu(ax, 0.56, 0.60, 0.40, 0.22, "ISI", MAVI, boy=36)
    kutu(ax, 0.04, 0.26, 0.40, 0.28, "taneciklerin ortalama\nhareket enerjisinin ölçüsü\n\nbirimi: °C ya da kelvin\ntermometre ile ölçülür", "#FEF2F2", boy=23, yazi="#111111")
    kutu(ax, 0.56, 0.26, 0.40, 0.28, "sıcaklık farkı yüzünden\naktarılan enerji\n\nbirimi: joule\nhesapla bulunur", "#EFF6FF", boy=23, yazi="#111111")
    kutu(ax, 0.10, 0.04, 0.80, 0.14, "ısı kendiliğinden hep sıcaktan soğuğa akar", "#1F2937", boy=30)
    sekil("3.1", "isi-ve-sicaklik")
    ns = oturum("3.1", "birimler", """
from arac import ORNEK
def kelvin(santigrat):
    return santigrat + 273.15
cay, oda = ORNEK["cay_C"], ORNEK["oda_C"]       # ÖRNEK sıcaklıklar, °C
kelvin(cay), kelvin(oda)
cay - oda, kelvin(cay) - kelvin(oda)            # fark iki ölçekte de aynı
kalori = 4.184                                  # bir kalori kaç joule (tanım)
watt_saat = 3600                                # bir watt saat kaç joule (tanım)
round(1000 / kalori), round(1000 / watt_saat, 3)   # bin joule: kalori, watt saat
""")
    Q = 1000.0; m = 100.0
    ad = ["su", "alüminyum", "cam", "demir", "bakır"]; dT = [Q / (m * OZ_ISI[a]) for a in ad]
    fig, ax = plt.subplots()
    ax.bar(range(5), dT, color=[MAVI, TURUNCU, YESIL, GRI, MOR])
    for i, v in enumerate(dT):
        ax.text(i, v + 0.5, tr(v, 1) + " °C", ha="center", fontsize=28, weight="bold")
    ax.set_xticks(range(5)); ax.set_xticklabels(ad, fontsize=26); ax.set_ylabel("sıcaklık artışı (°C)"); ax.set_ylim(0, max(dT) * 1.15)
    ax.grid(axis="x", visible=False)
    ax.set_title("Aynı ısı (1000 J), aynı kütle (100 g), farklı madde · öz ısılar kaynak tablosundan")
    sekil("3.1", "ayni-isi-farkli-artis")
    olc(d3_1_cay_K=ns["kelvin"](ns["cay"]), d3_1_oda_K=ns["kelvin"](ns["oda"]), d3_1_fark=ns["cay"] - ns["oda"], d3_1_ornek_cay_C=ns["cay"],
        d3_1_ornek_oda_C=ns["oda"], d3_1_bin_joule_kalori=round(1000 / 4.184), d3_1_dT={a: round(v, 1) for a, v in zip(ad, dT)},
        d3_1_bakir_su_orani=round(dT[4] / dT[0], 1), d3_1_kelvin_ek=273.15, d3_1_isi_J=Q, d3_1_kutle_g=m)


def ders_3_2():
    """Öz ısı ve ısı alışverişi: Q = m c ΔT, alınan ısı = verilen ısı, denge sıcaklığı."""
    ns = oturum("3.2", "oz-isi", """
from kaynaklar import OZ_ISI
for madde, c in OZ_ISI.items():
    print(f"{madde:10s} {c:6.3f} J/(g·°C)")
def isi(kutle_g, madde, ilk_C, son_C):
    return kutle_g * OZ_ISI[madde] * (son_C - ilk_C)
round(isi(100, "su", 22, 90))   # 100 g su, 22 → 90 °C, joule
round(isi(100, "alüminyum", 22, 90))        # aynı kütlede alüminyum
round(isi(100, "su", 22, 90) / isi(100, "alüminyum", 22, 90), 2)
""")
    ns2 = oturum("3.2", "denge-sicakligi", """
from kaynaklar import OZ_ISI
def denge(parcalar):
    # parcalar: (kütle g, madde, sıcaklık °C); alınan ısı = verilen ısı
    pay = sum(m * OZ_ISI[madde] * T for m, madde, T in parcalar)
    payda = sum(m * OZ_ISI[madde] for m, madde, T in parcalar)
    return pay / payda
round(denge([(200, "su", 60), (100, "su", 20)]), 1)   # ılık + soğuk su (ÖRNEK)
T = denge([(100, "su", 90), (30, "demir", 22)])   # çay + demir kaşık (ÖRNEK)
round(T, 1)
verilen = 100 * OZ_ISI["su"] * (90 - T)
alinan = 30 * OZ_ISI["demir"] * (T - 22)
round(verilen), round(alinan)
""")
    d = ns2["denge"]; T1 = d([(200, "su", 60), (100, "su", 20)]); T2 = ns2["T"]
    fig, (a1, a2) = plt.subplots(1, 2)
    for ax, ad, once, son, bas in [(a1, ["200 g su", "100 g su"], [60, 20], T1, "Ilık su + soğuk su"),
                                    (a2, ["100 g çay", "30 g kaşık"], [90, 22], T2, "Çay + demir kaşık")]:
        ax.bar([0, 1], once, color=[KIRMIZI, MAVI], width=0.55)
        for i, v in enumerate(once):
            ax.text(i, v + 1.5, f"{v} °C", ha="center", fontsize=28, weight="bold")
        ax.axhline(son, color="#111111", lw=4, ls="--")
        ax.text(0.5, son + 2.5 if son < 80 else son - 9, f"denge {tr(son, 1)} °C", ha="center", fontsize=28, weight="bold",
                bbox=dict(fc="#ffffff", ec="none", pad=4))
        ax.set_xticks([0, 1]); ax.set_xticklabels(ad, fontsize=26); ax.set_ylim(0, 108); ax.set_title(bas); ax.set_ylabel("sıcaklık (°C)")
        ax.grid(axis="x", visible=False)
    fig.suptitle("Alınan ısı = verilen ısı · kütle ve sıcaklıklar ÖRNEK, öz ısılar kaynak tablosundan", fontsize=26)
    sekil("3.2", "isi-alisverisi")
    isi = ns["isi"]
    olc(d3_2_oz_isi=OZ_ISI, d3_2_su_J=round(isi(100, "su", 22, 90)), d3_2_al_J=round(isi(100, "alüminyum", 22, 90)),
        d3_2_su_al_orani=round(isi(100, "su", 22, 90) / isi(100, "alüminyum", 22, 90), 2), d3_2_denge_su=round(T1, 1),
        d3_2_denge_kasik=round(T2, 1), d3_2_verilen_J=round(ns2["verilen"]), d3_2_alinan_J=round(ns2["alinan"]),
        d3_2_kasik_artis=round(T2 - 22, 1), d3_2_cay_dusus=round(90 - T2, 1), d3_2_ornek_kasik_g=30, d3_2_ornek_cay_g=100)


def ders_3_3():
    """Tepkime ısısı: ekzotermik ve endotermik, oluşum entalpilerinden tepkime entalpisi, gram başına enerji."""
    fig, (a1, a2) = plt.subplots(1, 2)
    for ax, bas, y0, y1, renk, isaret in [(a1, "Ekzotermik: ısı verir", 0.75, 0.25, KIRMIZI, "ΔH < 0"), (a2, "Endotermik: ısı alır", 0.25, 0.75, MAVI, "ΔH > 0")]:
        ax.plot([0.08, 0.40], [y0, y0], color="#111111", lw=6); ax.plot([0.60, 0.92], [y1, y1], color="#111111", lw=6)
        ax.text(0.24, y0 + 0.05, "tepkenler", ha="center", fontsize=28); ax.text(0.76, y1 + 0.05, "ürünler", ha="center", fontsize=28)
        ax.annotate("", xy=(0.5, y1), xytext=(0.5, y0), arrowprops=dict(arrowstyle="-|>", color=renk, lw=6, mutation_scale=40))
        ax.text(0.54, 0.5, isaret, fontsize=34, weight="bold", color=renk, va="center")
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylabel("entalpi"); ax.set_title(bas); ax.grid(False)
    sekil("3.3", "ekzotermik-endotermik")
    ns = oturum("3.3", "tepkime-entalpisi", """
from kaynaklar import OLUSUM, KUTLE
def tepkime_entalpisi(tepkenler, urunler):
    # ürünlerin oluşum entalpileri toplamı − tepkenlerinki, kJ
    topla = lambda liste: sum(n * OLUSUM[madde] for n, madde in liste)
    return topla(urunler) - topla(tepkenler)
metan = tepkime_entalpisi([(1, "CH4(g)"), (2, "O2(g)")],
                          [(1, "CO2(g)"), (2, "H2O(s)")])
round(metan, 1)                             # CH4 + 2 O2 → CO2 + 2 H2O, kJ
aluminyum = tepkime_entalpisi([(4, "Al(k)"), (3, "O2(g)")], [(2, "Al2O3(k)")])
round(aluminyum, 1)                         # 4 Al + 3 O2 → 2 Al2O3, kJ
metan_g = -metan / (KUTLE["C"] + 4 * KUTLE["H"])
al_g = -aluminyum / (4 * KUTLE["Al"])
round(metan_g, 1), round(al_g, 1)           # gram başına açığa çıkan ısı, kJ
""")
    fig, ax = plt.subplots()
    v = [ns["metan_g"], ns["al_g"]]
    ax.bar([0, 1], v, color=[MAVI, TURUNCU], width=0.5)
    for i, x in enumerate(v):
        ax.text(i, x + 1.2, tr(x, 1) + " kJ/g", ha="center", fontsize=32, weight="bold")
    ax.set_xticks([0, 1]); ax.set_xticklabels(["metan yanarken\n(doğal gaz)", "alüminyum oksitlenirken\n(gövdenin yüzeyi)"], fontsize=26)
    ax.set_ylabel("gram başına açığa çıkan ısı (kJ)"); ax.set_ylim(0, 66); ax.set_xlim(-0.6, 1.6); ax.grid(axis="x", visible=False)
    ax.set_title("İkisi de ekzotermik · oluşum entalpilerinden hesap, kaynak tablosundan")
    sekil("3.3", "gram-basina-isi")
    olc(d3_3_metan_kJ=round(ns["metan"], 1), d3_3_aluminyum_kJ=round(ns["aluminyum"], 1), d3_3_metan_kJ_g=round(ns["metan_g"], 1),
        d3_3_al_kJ_g=round(ns["al_g"], 1), d3_3_olusum=OLUSUM)


def ders_3_4():
    """Motor neden ısınır, nasıl soğur: dirsek torku (benzetim kaydı), tork başına ısı (ÖRNEK sabit), ısınma ve soğuma eğrisi."""
    t, tork, guc, W_arti, W_eksi = dirsek_isi()
    fig, ax = plt.subplots()
    ax.plot(t, tork, color=MOR)
    ax.axhline(np.abs(tork).mean(), color=TURUNCU, ls="--", lw=3, label=f"ortalama {tr(np.abs(tork).mean(), 2)} N·m")
    ax.set_xlabel("zaman (s)"); ax.set_ylabel("dirseğin tuttuğu tork (N·m)"); ax.set_ylim(0, 3.6); ax.legend(loc="lower right", fontsize=26)
    ax.set_title("Kol dururken bile motor tork üretir · benzetim kaydı · basitleştirilmiş: yalnız yerçekimi")
    sekil("3.4", "dirsek-torku")
    ns = oturum("3.4", "motor-isisi", """
import numpy as np
from arac import dirsek_isi, ORNEK
from ortak import kol_kutle
from kaynaklar import OZ_ISI
t, tork, guc, W_arti, W_eksi = dirsek_isi()
isi_gucu = (tork / ORNEK["motor_sabiti"]) ** 2       # watt; motor sabiti ÖRNEK
round(isi_gucu.mean(), 2)
Q = isi_gucu.mean() * (t[-1] - t[0])
round(Q), round(W_arti, 1)   # bir serviste ısı ve iş, joule
m = dict(kol_kutle())["üst kol"] * 1000   # gram; alüminyum sayıldı (VARSAYIM)
round(Q / (m * OZ_ISI["alüminyum"]), 2)   # soğumasa kaç °C ısınır
""")
    P = float(ns["isi_gucu"].mean()); mc = ns["m"] * OZ_ISI["alüminyum"]; ts = ORNEK["soguma_sabiti_s"]; oda = ORNEK["oda_C"]
    dT_son = P * ts / mc
    z = np.linspace(0, 3600, 721); T = np.where(z <= 2400, oda + dT_son * (1 - np.exp(-z / ts)),
                                               oda + dT_son * (1 - np.exp(-2400 / ts)) * np.exp(-(z - 2400) / ts))
    fig, ax = plt.subplots()
    ax.plot(z / 60, T, color=KIRMIZI, lw=4)
    ax.axhline(oda + dT_son, color=GRI, ls="--", lw=3); ax.text(1, oda + dT_son + 0.12, f"denge: oda + {tr(dT_son, 1)} °C", fontsize=26, color="#374151")
    ax.axvline(40, color="#111111", ls=":", lw=3); ax.text(40.6, oda + 0.4, "motor durdu", fontsize=26)
    ax.axvspan(0, 40, color=TURUNCU, alpha=0.08)
    ax.set_xlabel("zaman (dakika)"); ax.set_ylabel("motor gövdesinin sıcaklığı (°C)"); ax.set_ylim(oda - 0.3, oda + dT_son + 0.9)
    ax.set_title("Isınma ve soğuma · tork benzetim kaydından · motor sabiti ve soğuma süresi ÖRNEK")
    sekil("3.4", "isinma-soguma")
    olc(d3_4_tork_ort=round(float(np.abs(tork).mean()), 2), d3_4_tork_max=round(float(np.abs(tork).max()), 2), d3_4_isi_gucu_W=round(P, 2),
        d3_4_Q_J=round(float(ns["Q"])), d3_4_W_arti_J=round(W_arti, 1), d3_4_isi_is_orani=round(float(ns["Q"]) / W_arti),
        d3_4_ust_kol_g=ns["m"], d3_4_servis_dT=round(float(ns["Q"]) / mc, 2), d3_4_denge_dT=round(dT_son, 1),
        d3_4_ornek_motor_sabiti=ORNEK["motor_sabiti"], d3_4_ornek_soguma_s=ts, d3_4_sure_s=round(float(t[-1] - t[0]), 1))


if __name__ == "__main__":
    ders_3_1(); ders_3_2(); ders_3_3(); ders_3_4()
    print("hafta 3 tamam")
