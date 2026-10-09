"""Hafta 1 · Robotun Malzemesi — Ders 1.1–1.4 (+ tanıtım dersi için kurs haritası).
  python hafta1.py   → ekran/1.x/*.txt + *.png, ekran/0.1/*.png, OLCUMLER.json (d0_*, d1_*)"""
import numpy as np
import matplotlib.pyplot as plt
from ortak import olc, oturum, sekil, kol_kutle, kayit
from arac import kutu, ok, bos_eksen, tr, TURUNCU, MAVI, YESIL, MOR, GRI, KIRMIZI
from kaynaklar import ELEMENT, MALZEME


def ders_1_1():
    """Atom ve periyodik özellikler: kolun kütle tablosu, beş elementin kimlik kartı, periyodik eğilim."""
    ns = oturum("1.1", "kol-tablosu", """
from ortak import kol_kutle
parcalar = kol_kutle()
for ad, kutle in parcalar:
    print(f"{ad:22s} {kutle:6.3f} kg")
toplam = sum(kutle for ad, kutle in parcalar)
len(parcalar), round(toplam, 2)
""")
    ns2 = oturum("1.1", "element-karti", """
from kaynaklar import ELEMENT
print("simge  ad         atom no  kütle    elektroneg.  iyonlaşma")
for simge, e in ELEMENT.items():
    print(f"{simge:6s} {e['ad']:10s} {e['Z']:5d}  {e['kutle']:7.3f}", end="")
    print(f"  {e['en']:8.2f}  {e['iyonlasma']:9.1f}")
oran = ELEMENT["C"]["iyonlasma"] / ELEMENT["Li"]["iyonlasma"]
round(oran, 2)
""")
    sim = list(ELEMENT); x = np.arange(len(sim))
    fig, (a1, a2) = plt.subplots(1, 2)
    renk = [MOR, GRI, TURUNCU, MAVI, YESIL]
    a1.bar(x, [ELEMENT[s]["en"] for s in sim], color=renk)
    a2.bar(x, [ELEMENT[s]["iyonlasma"] for s in sim], color=renk)
    for ax, alan, bas, bs in [(a1, "en", "Elektronegatiflik (Pauling)", 2), (a2, "iyonlasma", "Birinci iyonlaşma enerjisi (kJ/mol)", 1)]:
        for i, s in enumerate(sim):
            v = ELEMENT[s][alan]
            ax.text(i, v * 1.02, tr(v, bs), ha="center", fontsize=24 if bs == 2 else 21, weight="bold")
        ax.set_xticks(x); ax.set_xticklabels([f"{s}\n{ELEMENT[s]['Z']}" for s in sim], fontsize=26)
        ax.set_title(bas); ax.set_ylim(0, max(ELEMENT[s][alan] for s in sim) * 1.14); ax.grid(axis="x", visible=False)
    fig.suptitle("Elektronunu kim sıkı tutuyor? · altta atom numarası · değerler kaynak tablosundan", fontsize=26)
    sekil("1.1", "periyodik-egilim")
    olc(d1_1_parca=len(ns["parcalar"]), d1_1_kol_kutle_kg=round(ns["toplam"], 2), d1_1_iyonlasma_Li=ELEMENT["Li"]["iyonlasma"],
        d1_1_iyonlasma_C=ELEMENT["C"]["iyonlasma"], d1_1_oran_C_Li=round(ns2["oran"], 2), d1_1_en_Li=ELEMENT["Li"]["en"], d1_1_en_C=ELEMENT["C"]["en"],
        d1_1_en_Al=ELEMENT["Al"]["en"], d1_1_iyonlasma_Al=ELEMENT["Al"]["iyonlasma"],
        d1_1_en_Fe=ELEMENT["Fe"]["en"], d1_1_en_Cu=ELEMENT["Cu"]["en"])


def ders_1_2():
    """Kimyasal bağ türleri: metalik, kovalent, iyonik; elektronegatiflik farkıyla bağ türü."""
    fig, ax = bos_eksen("Üç güçlü etkileşim, robotta üç yer")
    kart = [("Metalik bağ", "metal + metal", "değerlik elektronları\nortak bir denizde", "alüminyum gövde\nbakır kablo", TURUNCU),
            ("Kovalent bağ", "ametal + ametal", "elektronlar iki atom\narasında ortak", "karbon fiber\nplastik kapak", YESIL),
            ("İyonik bağ", "metal + ametal", "elektron bir atomdan\nötekine geçer", "pilin içindeki\nlityum bileşiği", MOR)]
    for i, (ad, kim, nasil, nerede, renk) in enumerate(kart):
        x = 0.03 + i * 0.33
        kutu(ax, x, 0.72, 0.27, 0.16, ad, renk, boy=30)
        kutu(ax, x, 0.52, 0.27, 0.14, kim, "#E5E7EB", boy=24, yazi="#111111")
        kutu(ax, x, 0.28, 0.27, 0.18, nasil, "#F3F4F6", boy=23, yazi="#111111")
        kutu(ax, x, 0.04, 0.27, 0.18, nerede, "#FFF7ED", boy=24, yazi="#111111")
    sekil("1.2", "uc-bag")
    ns = oturum("1.2", "elektronegatiflik-farki", """
from kaynaklar import EN
def bag_turu(a, b):                 # eşikler okul kitabı ölçütüdür (yaklaşık)
    fark = abs(EN[a] - EN[b])
    if fark < 0.4:
        tur = "apolar kovalent"
    elif fark < 1.7:
        tur = "polar kovalent"
    else:
        tur = "iyonik ağırlıklı"
    return round(fark, 2), tur
ciftler = [("C", "C"), ("C", "H"), ("C", "O"), ("Al", "O"), ("Li", "O"), ("Na", "Cl")]
for a, b in ciftler:
    print(f"{a + '–' + b:6s}", *bag_turu(a, b))
""")
    fig, ax = bos_eksen("Bağ türü özelliği belirler")
    bas = ["bağ", "elektronlar", "sonuç", "robotta"]
    x0 = [0.02, 0.20, 0.47, 0.76]
    for j, b in enumerate(bas):
        ax.text(x0[j], 0.88, b, fontsize=26, weight="bold", va="center")
    satir = [("metalik", "serbest dolaşır", "elektriği iletir,\ndövülür, bükülür", "gövde, kablo", TURUNCU),
             ("kovalent", "atomlar arasında\nsabit", "iletmez (çoğu),\nhafif, sert olabilir", "karbon fiber,\nplastik", YESIL),
             ("iyonik", "bir atomda\ntoplanır", "katıyken iletmez,\niyonları hareket\nedince iletir", "pil elektrotu", MOR)]
    for i, (ad, el, sonuc, nerede, renk) in enumerate(satir):
        y = 0.68 - i * 0.26
        kutu(ax, x0[0], y - 0.08, 0.14, 0.16, ad, renk, boy=24)
        for j, m in enumerate([el, sonuc, nerede]):
            ax.text(x0[j + 1], y, m, fontsize=24, va="center", linespacing=1.3)
    sekil("1.2", "bag-ve-ozellik")
    f = {f"{a}-{b}": ns["bag_turu"](a, b)[0] for a, b in [("C", "C"), ("C", "H"), ("C", "O"), ("Al", "O"), ("Li", "O"), ("Na", "Cl")]}
    olc(d1_2_fark=f, d1_2_esik_apolar=0.4, d1_2_esik_iyonik=1.7)


def ders_1_3():
    """Metal, polimer, karbon fiber: üç malzeme ailesi, tipik dayanım ve yoğunluk, polimer zinciri."""
    fig, ax = bos_eksen("Üç malzeme ailesi · yoğunluklar kaynak tablosundan (tipik)")
    kart = [("Metal", "alüminyum alaşımı", "metalik bağ\natomlar sıkı dizilir", "2,70 g/cm³", TURUNCU),
            ("Polimer", "naylon", "uzun kovalent zincirler\nzincirler arası zayıf\netkileşim", "1,13 g/cm³", MAVI),
            ("Kompozit", "karbon fiber + epoksi", "kovalent karbon lifleri\npolimer içine gömülü", "1,58 g/cm³", YESIL)]
    for i, (ad, ornek, yapi, yog, renk) in enumerate(kart):
        x = 0.03 + i * 0.33
        kutu(ax, x, 0.72, 0.27, 0.16, ad, renk, boy=30)
        kutu(ax, x, 0.54, 0.27, 0.12, ornek, "#E5E7EB", boy=24, yazi="#111111")
        kutu(ax, x, 0.26, 0.27, 0.22, yapi, "#F3F4F6", boy=22, yazi="#111111")
        kutu(ax, x, 0.06, 0.27, 0.14, yog, "#FFF7ED", boy=28, yazi="#111111")
    sekil("1.3", "uc-malzeme")
    ns = oturum("1.3", "malzeme-tablosu", """
from kaynaklar import MALZEME
print("malzeme                       dayanım (MPa)  yoğunluk (g/cm³)")
for ad, dayanim, yogunluk in MALZEME:
    print(f"{ad:30s} {dayanim:8d} {yogunluk:14.2f}")
en_saglam = max(MALZEME, key=lambda m: m[1])
en_hafif = min(MALZEME, key=lambda m: m[2])
en_saglam[0], en_hafif[0]
""")
    ns2 = oturum("1.3", "polimer-zinciri", """
from kaynaklar import mol_kutlesi
birim = {"C": 6, "H": 11, "N": 1, "O": 1}     # naylon 6 zincirinin yinelenen birimi
m_birim = mol_kutlesi(birim)
round(m_birim, 2)
n = 200                                       # zincirdeki birim sayısı (ÖRNEK)
round(n * m_birim)
su = mol_kutlesi({"H": 2, "O": 1})
round(n * m_birim / su)
""")
    olc(d1_3_tablo={m[0]: [m[1], m[2]] for m in MALZEME}, d1_3_malzeme=len(MALZEME), d1_3_en_saglam=ns["en_saglam"][0], d1_3_en_hafif=ns["en_hafif"][0],
        d1_3_birim_g_mol=round(ns2["m_birim"], 2), d1_3_zincir_birim_ornek=ns2["n"], d1_3_zincir_g_mol=round(ns2["n"] * ns2["m_birim"]),
        d1_3_zincir_su_kati=round(ns2["n"] * ns2["m_birim"] / ns2["su"]))


def ders_1_4():
    """Yoğunluk, mol ve dayanım: ön kol alüminyum olsaydı kaç mol; aynı hacim başka malzemeden; özgül dayanım."""
    ns = oturum("1.4", "on-kol-mol", """
from ortak import kol_kutle
from kaynaklar import ELEMENT, AVOGADRO
kutle_g = dict(kol_kutle())["ön kol"] * 1000
al = ELEMENT["Al"]
kutle_g   # tablodan; tamamı alüminyum sayıldı (VARSAYIM)
hacim = kutle_g / al["yogunluk"]
round(hacim, 1)                           # cm³
mol = kutle_g / al["kutle"]
round(mol, 2)
f"{mol * AVOGADRO:.2e}"                   # atom sayısı
""")
    hacim = ns["hacim"]
    ad = [m[0].replace(" (", "\n(").replace("–epoksi ", "–epoksi\n") for m in MALZEME]
    kutle = [hacim * m[2] for m in MALZEME]
    ozgul = [m[1] / m[2] for m in MALZEME]
    renk = [GRI, TURUNCU, MOR, MAVI, YESIL]
    fig, ax = plt.subplots()
    ax.bar(range(5), kutle, color=renk)
    for i, v in enumerate(kutle):
        ax.text(i, v + 25, f"{v:.0f} g", ha="center", fontsize=26, weight="bold")
    ax.set_xticks(range(5)); ax.set_xticklabels(ad, fontsize=21); ax.set_ylabel("kütle (g)"); ax.set_ylim(0, max(kutle) * 1.14)
    ax.grid(axis="x", visible=False)
    ax.set_title(f"Aynı hacim ({tr(hacim, 0)} cm³), farklı malzeme · hacim: ön kol alüminyum sayılarak (VARSAYIM)")
    sekil("1.4", "ayni-hacim-kutle")
    fig, ax = plt.subplots()
    ax.bar(range(5), ozgul, color=renk)
    for i, v in enumerate(ozgul):
        ax.text(i, v + 12, f"{v:.0f}", ha="center", fontsize=28, weight="bold")
    ax.set_xticks(range(5)); ax.set_xticklabels(ad, fontsize=21); ax.set_ylabel("dayanım ÷ yoğunluk  (MPa·cm³/g)")
    ax.set_ylim(0, max(ozgul) * 1.14); ax.grid(axis="x", visible=False)
    ax.set_title("Hafif ama sağlam: gram başına dayanım · tipik değerler, kaynak tablosundan")
    sekil("1.4", "ozgul-dayanim")
    olc(d1_4_on_kol_g=ns["kutle_g"], d1_4_hacim_cm3=round(hacim, 1), d1_4_mol=round(ns["mol"], 2), d1_4_atom_carpan=round(ns["mol"] * ns["AVOGADRO"] / 1e25, 2), d1_4_atom=float(f"{ns['mol'] * ns['AVOGADRO']:.3e}"),
        d1_4_ayni_hacim_g={m[0]: round(k) for m, k in zip(MALZEME, kutle)}, d1_4_ozgul={m[0]: round(o) for m, o in zip(MALZEME, ozgul)},
        d1_4_kompozit_al_orani=round(ozgul[4] / ozgul[1], 1), d1_4_celik_al_kutle_orani=round(kutle[0] / kutle[1], 2))


def tanitim():
    """Tanıtım dersi: kurs haritası — robotun dört parçası, dört hafta."""
    fig, ax = bos_eksen("Bir robot, dört soru, dört hafta")
    kart = [("Hafta 1", "Robotun Malzemesi", "Gövde neden hafif\nama sağlam?", TURUNCU),
            ("Hafta 2", "Pil Kimyası", "Pil gerilimini\nnereden alıyor?", MOR),
            ("Hafta 3", "Enerji ve Isı", "Motor neden ısınıyor,\nnasıl soğuyor?", YESIL),
            ("Hafta 4", "Çözeltiler ve Çay", "Taşınan çay yolda\nne kadar soğuyor?", MAVI)]
    for i, (h, ad, soru, renk) in enumerate(kart):
        x = 0.03 + i * 0.25
        kutu(ax, x, 0.70, 0.19, 0.14, h, renk, boy=30)
        kutu(ax, x, 0.48, 0.19, 0.16, ad, "#E5E7EB", boy=24, yazi="#111111")
        kutu(ax, x, 0.20, 0.19, 0.22, soru, "#FFF7ED", boy=22, yazi="#111111")
    k = kayit()
    ax.text(0.5, 0.07, f"Robot verisi: çay servisi benzetim kaydı · {tr(k['zaman_s'][-1], 1)} saniye · kimya değerleri kaynaklı tablolardan",
            ha="center", fontsize=24)
    sekil("0.1", "kurs-haritasi")
    olc(d0_1_sure_s=float(k["zaman_s"][-1]), d0_1_ornek=len(k["zaman_s"]), d0_1_hafta=4, d0_1_ders=16)


if __name__ == "__main__":
    ders_1_1(); ders_1_2(); ders_1_3(); ders_1_4(); tanitim()
    print("hafta 1 tamam")
