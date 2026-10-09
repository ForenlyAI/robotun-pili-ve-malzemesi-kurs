"""Hafta 2 · Pil Kimyası — Ders 2.1–2.4.
  python hafta2.py   → ekran/2.x/*.txt + *.png, OLCUMLER.json (d2_*)"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from ortak import olc, oturum, sekil, kayit
from arac import kutu, ok, bos_eksen, tr, dirsek_isi, ORNEK, TURUNCU, MAVI, YESIL, MOR, GRI, KIRMIZI
from kaynaklar import E0, KUTLE, FARADAY


def ders_2_1():
    """Yükseltgenme ve indirgenme: elektron alışverişi, yükseltgenme basamağı, metallerin aktiflik sırası."""
    fig, ax = bos_eksen("Elektron veren yükseltgenir, elektron alan indirgenir")
    kutu(ax, 0.04, 0.56, 0.38, 0.24, "Zn  →  Zn²⁺ + 2 e⁻", TURUNCU, boy=34)
    kutu(ax, 0.58, 0.56, 0.38, 0.24, "Cu²⁺ + 2 e⁻  →  Cu", MAVI, boy=34)
    ax.text(0.23, 0.86, "yükseltgenme · elektron verir", ha="center", fontsize=26, weight="bold", color=TURUNCU)
    ax.text(0.77, 0.86, "indirgenme · elektron alır", ha="center", fontsize=26, weight="bold", color=MAVI)
    ok(ax, 0.435, 0.68, 0.565, 0.68); ax.text(0.5, 0.72, "2 e⁻", ha="center", fontsize=28, weight="bold")
    kutu(ax, 0.04, 0.30, 0.38, 0.16, "çinko: indirgen\n(karşısındakini indirger)", "#FFF7ED", boy=24, yazi="#111111")
    kutu(ax, 0.58, 0.30, 0.38, 0.16, "bakır iyonu: yükseltgen\n(karşısındakini yükseltger)", "#EFF6FF", boy=24, yazi="#111111")
    kutu(ax, 0.16, 0.05, 0.68, 0.15, "toplam:  Zn + Cu²⁺  →  Zn²⁺ + Cu", "#1F2937", boy=32)
    sekil("2.1", "elektron-alisverisi")
    ns = oturum("2.1", "yukseltgenme-basamagi", """
def basamak(formul, bilinen, yuk=0):
    # bilinmeyen tek elementin yükseltgenme basamağı
    aranan = [e for e in formul if e not in bilinen][0]
    toplam = sum(bilinen[e] * n for e, n in formul.items() if e in bilinen)
    return aranan, (yuk - toplam) / formul[aranan]
kural = {"O": -2, "Li": +1}
basamak({"Al": 2, "O": 3}, kural)
basamak({"Li": 1, "Co": 1, "O": 2}, kural)        # boşalmış pilin artı ucu
basamak({"Co": 1, "O": 2}, kural)   # lityumu çıkmış hâli (kuramsal)
basamak({"Cu": 1}, kural, yuk=+2)
""")
    ad = {"Li": "lityum", "Mg": "magnezyum", "Al": "alüminyum", "Zn": "çinko", "Fe": "demir", "Ni": "nikel", "Pb": "kurşun",
          "H2": "hidrojen", "Cu": "bakır", "Ag": "gümüş"}
    sim = sorted(E0, key=lambda s: E0[s]); v = [E0[s] for s in sim]
    fig, ax = plt.subplots()
    ax.barh(range(len(sim)), v, color=[TURUNCU if x < 0 else MAVI if x > 0 else GRI for x in v])
    for i, (s, x) in enumerate(zip(sim, v)):
        ax.text(x - 0.06 if x < 0 else x + 0.06, i, tr(x, 2), va="center", ha="right" if x < 0 else "left", fontsize=24, weight="bold")
    ax.set_yticks(range(len(sim))); ax.set_yticklabels([ad[s] for s in sim], fontsize=25); ax.invert_yaxis()
    ax.set_xlim(-3.7, 1.5); ax.axvline(0, color="#111111", lw=2); ax.grid(axis="y", visible=False)
    ax.set_xlabel("standart indirgenme potansiyeli E° (volt)")
    ax.set_title("Aktiflik sırası: üstteki metal elektronunu daha kolay verir · kaynak tablosundan")
    sekil("2.1", "aktiflik-sirasi")
    b = ns["basamak"]; kural = ns["kural"]
    olc(d2_1_Al=b({"Al": 2, "O": 3}, kural)[1], d2_1_Co_dolu_lityum=b({"Li": 1, "Co": 1, "O": 2}, kural)[1],
        d2_1_Co_lityumsuz=b({"Co": 1, "O": 2}, kural)[1], d2_1_en_aktif=sim[0], d2_1_en_az_aktif=sim[-1], d2_1_metal_sayisi=len(sim),
        d2_1_E0_Li=E0["Li"], d2_1_E0_Ag=E0["Ag"])


def ders_2_2():
    """Elektrokimyasal hücre ve hücre gerilimi: galvanik hücre, E°hücre = E°katot − E°anot."""
    fig, ax = bos_eksen("Galvanik hücre: çinko–bakır")
    for x, renk, ad, iyon, rol in [(0.10, TURUNCU, "Zn", "Zn²⁺ çözeltisi", "anot (−)\nyükseltgenme"), (0.62, MAVI, "Cu", "Cu²⁺ çözeltisi", "katot (+)\nindirgenme")]:
        ax.add_patch(Rectangle((x, 0.08), 0.28, 0.42, fc="#E0F2FE", ec="#111111", lw=3))
        ax.add_patch(Rectangle((x + 0.11, 0.18), 0.06, 0.46, fc=renk, ec="#111111", lw=2))
        ax.text(x + 0.14, 0.42, ad, ha="center", va="center", fontsize=26, color="#ffffff", weight="bold")
        ax.text(x + 0.14, 0.12, iyon, ha="center", fontsize=22)
        ax.text(x + 0.14, 0.01, rol, ha="center", va="center", fontsize=24, weight="bold", color=renk, linespacing=1.2)
    ax.plot([0.24, 0.24, 0.76, 0.76], [0.64, 0.84, 0.84, 0.64], color="#111111", lw=4, zorder=0)
    ax.add_patch(FancyBboxPatch((0.44, 0.78), 0.12, 0.12, boxstyle="round,pad=0.01", fc="#FDE68A", ec="#111111", lw=2))
    ax.text(0.5, 0.84, "V", ha="center", va="center", fontsize=34, weight="bold")
    ok(ax, 0.28, 0.90, 0.40, 0.90); ax.text(0.34, 0.94, "e⁻", ha="center", fontsize=28, weight="bold")
    ok(ax, 0.60, 0.90, 0.72, 0.90); ax.text(0.66, 0.94, "e⁻", ha="center", fontsize=28, weight="bold")
    ax.add_patch(FancyBboxPatch((0.36, 0.40), 0.28, 0.07, boxstyle="round,pad=0.01", fc="#D1D5DB", ec="#111111", lw=2))
    ax.text(0.5, 0.435, "tuz köprüsü", ha="center", va="center", fontsize=24)
    ax.set_ylim(-0.06, 1.0)
    sekil("2.2", "galvanik-hucre")
    ns = oturum("2.2", "hucre-gerilimi", """
from kaynaklar import E0, ELEKTROT
def hucre(anot, katot):
    return round(E0[katot] - E0[anot], 4)
ciftler = [("Zn", "Cu"), ("Fe", "Cu"), ("Zn", "Ag"), ("Al", "Cu"), ("Li", "Cu")]
for anot, katot in ciftler:
    E = hucre(anot, katot)
    print(f"{anot:2s} | {katot:2s}  {E0[katot]:+.4f} − ({E0[anot]:+.4f}) = {E:.4f} V")
hucre("Cu", "Zn")   # ters bağlanırsa: kendiliğinden yürümez
katot = ELEKTROT["PbO2 + SO4 2- + 4H+ + 2e- -> PbSO4 + 2H2O"][0]
anot = ELEKTROT["PbSO4 + 2e- -> Pb + SO4 2-"][0]
round(katot - anot, 4)                              # kurşunlu akünün bir hücresi
""")
    cift = [("Fe", "Cu"), ("Zn", "Cu"), ("Zn", "Ag"), ("Al", "Cu"), ("Li", "Cu")]
    v = [ns["hucre"](a, k) for a, k in cift] ; kursun = ns["katot"] - ns["anot"]
    ad = ["demir–bakır", "çinko–bakır", "çinko–gümüş", "alüminyum–bakır", "lityum–bakır"]
    fig, ax = plt.subplots()
    ax.bar(range(5), v, color=[GRI, TURUNCU, MAVI, YESIL, MOR])
    for i, x in enumerate(v):
        ax.text(i, x + 0.05, tr(x, 2) + " V", ha="center", fontsize=28, weight="bold")
    ax.set_xticks(range(5)); ax.set_xticklabels(ad, fontsize=23); ax.set_ylabel("standart hücre gerilimi (volt)"); ax.set_ylim(0, 3.9)
    ax.grid(axis="x", visible=False)
    ax.set_title("Hücre gerilimi = katodun potansiyeli − anodun potansiyeli · standart koşullar, hesap")
    sekil("2.2", "gerilim-karsilastirma")
    olc(d2_2_Zn_Cu=v[1], d2_2_Fe_Cu=v[0], d2_2_Zn_Ag=v[2], d2_2_Al_Cu=v[3], d2_2_Li_Cu=v[4], d2_2_ters=ns["hucre"]("Cu", "Zn"),
        d2_2_kursun=round(kursun, 4), d2_2_E0_Zn=E0["Zn"], d2_2_E0_Cu=E0["Cu"])


def ders_2_3():
    """Lityum iyon pil: yapı, yarı tepkimeler, neden lityum (gram başına yük ve potansiyel)."""
    fig, ax = bos_eksen("Lityum iyon pil boşalırken")
    ax.add_patch(Rectangle((0.06, 0.12), 0.22, 0.52, fc="#4B5563", ec="#111111", lw=3))
    ax.add_patch(Rectangle((0.72, 0.12), 0.22, 0.52, fc=MOR, ec="#111111", lw=3))
    ax.add_patch(Rectangle((0.28, 0.12), 0.44, 0.52, fc="#FEF3C7", ec="#111111", lw=3))
    ax.text(0.17, 0.38, "grafit\n(karbon)\n\neksi uç", ha="center", va="center", fontsize=26, color="#ffffff", weight="bold")
    ax.text(0.83, 0.38, "lityum\nkobalt oksit\n\nartı uç", ha="center", va="center", fontsize=26, color="#ffffff", weight="bold")
    ax.text(0.5, 0.56, "elektrolit: yalnız iyon geçer", ha="center", fontsize=24)
    for y in (0.44, 0.32, 0.20):
        ok(ax, 0.33, y, 0.67, y, renk=KIRMIZI); ax.text(0.5, y + 0.022, "Li⁺", ha="center", fontsize=26, weight="bold", color=KIRMIZI)
    ax.plot([0.17, 0.17, 0.83, 0.83], [0.64, 0.84, 0.84, 0.64], color="#111111", lw=4, zorder=0)
    kutu(ax, 0.40, 0.77, 0.20, 0.14, "motor", "#FDE68A", boy=28, yazi="#111111")
    ok(ax, 0.20, 0.90, 0.36, 0.90); ax.text(0.28, 0.935, "e⁻", ha="center", fontsize=28, weight="bold")
    ok(ax, 0.64, 0.90, 0.80, 0.90); ax.text(0.72, 0.935, "e⁻", ha="center", fontsize=28, weight="bold")
    ax.text(0.5, 0.03, "Şarj olurken iyonlar ve elektronlar ters yöne döner", ha="center", fontsize=26)
    sekil("2.3", "lityum-iyon")
    ns = oturum("2.3", "neden-lityum", """
from kaynaklar import E0, KUTLE, FARADAY
def gram_basina_yuk(metal, elektron):
    # bir gram metal yükseltgenince verdiği yük, miliamper saat
    return elektron * FARADAY / KUTLE[metal] / 3.6
for metal, elektron in [("Li", 1), ("Al", 3), ("Zn", 2), ("Pb", 2)]:
    q = gram_basina_yuk(metal, elektron)
    print(f"{metal:2s} {KUTLE[metal]:7.2f} g/mol {q:6.0f} mAh/g  E° {E0[metal]:+.2f} V")
round(gram_basina_yuk("Li", 1) / gram_basina_yuk("Pb", 2), 1)
""")
    ns2 = oturum("2.3", "elektrot-kapasitesi", """
from kaynaklar import mol_kutlesi, FARADAY
print("eksi uç:  LiC6  →  6 C + Li⁺ + e⁻")
print("artı uç:  CoO2 + Li⁺ + e⁻  →  LiCoO2")
grafit = mol_kutlesi({"C": 6})
katot = mol_kutlesi({"Li": 1, "Co": 1, "O": 2})
round(grafit, 2), round(katot, 2)
round(FARADAY / grafit / 3.6, 1)          # grafit: en çok kaç mAh/g (kuramsal)
round(FARADAY / katot / 3.6, 1)   # lityum kobalt oksit (kuramsal)
""")
    gy = ns["gram_basina_yuk"]; met = [("Li", 1, "lityum"), ("Al", 3, "alüminyum"), ("Zn", 2, "çinko"), ("Pb", 2, "kurşun")]
    fig, (a1, a2) = plt.subplots(1, 2)
    q = [gy(m, e) for m, e, _ in met]; e0 = [-E0[m] for m, _, _ in met]; renk = [MOR, TURUNCU, MAVI, GRI]
    a1.bar(range(4), q, color=renk); a2.bar(range(4), e0, color=renk)
    for i in range(4):
        a1.text(i, q[i] + 60, f"{q[i]:.0f}", ha="center", fontsize=28, weight="bold")
        a2.text(i, e0[i] + 0.05, "−" + tr(e0[i], 2), ha="center", fontsize=28, weight="bold")
    for ax, bas, ust in [(a1, "Gram başına yük (mAh/g) · hesap", max(q) * 1.14), (a2, "E° ne kadar eksi (volt) · kaynak", 3.6)]:
        ax.set_xticks(range(4)); ax.set_xticklabels([m[2] for m in met], fontsize=24); ax.set_title(bas); ax.set_ylim(0, ust); ax.grid(axis="x", visible=False)
    fig.suptitle("Neden lityum: en hafif metal ve elektronunu en kolay veren metal", fontsize=27)
    sekil("2.3", "neden-lityum-grafik")
    olc(d2_3_mAh_g={m: round(gy(m, e)) for m, e, _ in met}, d2_3_Li_Pb_orani=round(gy("Li", 1) / gy("Pb", 2), 1),
        d2_3_grafit_mAh_g=round(FARADAY / ns2["grafit"] / 3.6, 1), d2_3_katot_mAh_g=round(FARADAY / ns2["katot"] / 3.6, 1),
        d2_3_grafit_g_mol=round(ns2["grafit"], 2), d2_3_katot_g_mol=round(ns2["katot"], 2), d2_3_kutle_Li=KUTLE["Li"], d2_3_kutle_Pb=KUTLE["Pb"])


def ders_2_4():
    """Kapasite ve enerji: ÖRNEK pil paketinin yükü ve enerjisi, dirseğin işi (benzetim kaydı), servis bütçesi."""
    ns = oturum("2.4", "pil-enerjisi", """
from arac import ORNEK
from kaynaklar import FARADAY, KUTLE
V, Ah = ORNEK["hucre_gerilimi_V"], ORNEK["hucre_kapasite_Ah"]
n = ORNEK["hucre_sayisi"]
V, Ah, n   # ÖRNEK: volt, amper saat, seri hücre sayısı
yuk = Ah * 3600
yuk                                        # bir hücreden geçen yük, coulomb
mol_elektron = yuk / FARADAY
round(mol_elektron, 3)
round(mol_elektron * KUTLE["Li"], 2)   # bu yükü taşıyan lityum, gram
enerji_Wh = round(n * V * Ah, 1)
enerji_Wh, round(enerji_Wh * 3600 / 1e6, 2)      # watt saat, megajoule
""")
    t, tork, guc, W_arti, W_eksi = dirsek_isi()
    fig, ax = plt.subplots()
    ax.fill_between(t, guc, where=guc > 0, color=YESIL, alpha=0.65, label=f"motor iş yapıyor  +{tr(W_arti, 1)} J")
    ax.fill_between(t, guc, where=guc < 0, color=TURUNCU, alpha=0.65, label=f"motor frenliyor  −{tr(-W_eksi, 1)} J")
    ax.set_xlabel("zaman (s)"); ax.set_ylabel("dirseğin gücü (watt)"); ax.legend(loc="lower left", fontsize=24)
    ax.set_title("Dirseğin mekanik gücü · benzetim kaydı · basitleştirilmiş: yalnız yerçekimine karşı tork")
    sekil("2.4", "dirsek-gucu")
    ns2 = oturum("2.4", "enerji-butcesi", """
from arac import dirsek_isi, ORNEK
from ortak import kayit
t, tork, guc, W_arti, W_eksi = dirsek_isi()
sure = kayit()["zaman_s"][-1]
round(sure, 1), round(W_arti, 1)   # süre (s) ve dirseğin işi (J): benzetim kaydı
pilden = W_arti / ORNEK["verim"]           # verim ÖRNEK
bekleme = ORNEK["bekleme_gucu_W"] * sure   # bekleme gücü ÖRNEK
round(pilden, 1), round(bekleme)
servis_Wh = (pilden + bekleme) / 3600
round(servis_Wh, 2)
paket_Wh = enerji_Wh                       # ÖRNEK paket (önceki ekrandan)
int(paket_Wh / servis_Wh)                  # bir şarjla kaç servis
round(paket_Wh / ORNEK["bekleme_gucu_W"], 1)   # bir şarjla kaç saat
""", ns)
    olc(d2_4_ornek_V=ns["V"], d2_4_ornek_Ah=ns["Ah"], d2_4_ornek_hucre=ns["n"], d2_4_yuk_C=ns["yuk"], d2_4_mol_elektron=round(ns["mol_elektron"], 3),
        d2_4_lityum_g=round(ns["mol_elektron"] * KUTLE["Li"], 2), d2_4_paket_Wh=ns["enerji_Wh"], d2_4_paket_MJ=round(ns["enerji_Wh"] * 3600 / 1e6, 2),
        d2_4_sure_s=float(ns2["sure"]), d2_4_W_arti_J=round(W_arti, 1), d2_4_W_eksi_J=round(W_eksi, 1), d2_4_ornek_verim=ORNEK["verim"],
        d2_4_ornek_bekleme_W=ORNEK["bekleme_gucu_W"], d2_4_pilden_J=round(ns2["pilden"], 1), d2_4_bekleme_J=round(ns2["bekleme"]),
        d2_4_servis_Wh=round(ns2["servis_Wh"], 2), d2_4_servis_sayisi=int(ns2["paket_Wh"] / ns2["servis_Wh"]),
        d2_4_saat=round(ns2["paket_Wh"] / ORNEK["bekleme_gucu_W"], 1), d2_4_bekleme_kat=round(ns2["bekleme"] / ns2["pilden"]))


if __name__ == "__main__":
    ders_2_1(); ders_2_2(); ders_2_3(); ders_2_4()
    print("hafta 2 tamam")
