"""Robotun Pili ve Malzemesi — kaynaklı değer tabloları.
Bu dosyadaki her sayı bir kaynağa bağlıdır (KAYNAK sözlüğündeki anahtar). Değerler 2026-10-08'de belirtilen sayfadan okunarak
doğrulandı; "dogrulama" alanı değerin hangi sayfada görüldüğünü söyler. Kaynağı olmayan sayı bu dosyaya yazılmaz.
Robotla ilgili sayılar burada DEĞİL: onlar benzetim kaydından (veri/) hesaplanır ya da derste ÖRNEK diye işaretlenir."""

KAYNAK = {
    "ciaaw2024": dict(yazar="IUPAC Commission on Isotopic Abundances and Atomic Weights (CIAAW)", yil=2024,
        baslik="Abridged Standard Atomic Weights", yer="ciaaw.org/abridged-atomic-weights.htm",
        dogrulama="CIAAW sayfasından okundu: H, Li, C, O, Al, Fe, Co, Cu, Zn, Pb, S değerleri"),
    "crc_en": dict(yazar="Lide, D. R. (ed.)", yil=2003, baslik="CRC Handbook of Chemistry and Physics, 84. baskı — Electronegativity (Pauling ölçeği)",
        yer="CRC Press", dogrulama="Wikipedia 'Electronegativities of the elements (data page)' CRC sütunundan okundu; üç sütun (WebElements, CRC, Lange) aynı"),
    "crc_ie": dict(yazar="Lide, D. R. (ed.)", yil=2003, baslik="CRC Handbook of Chemistry and Physics, 84. baskı — Ionization Potentials of Atoms and Atomic Ions",
        yer="CRC Press, s. 10-178", dogrulama="Wikipedia 'Ionization energies of the elements (data page)' üzerinden okundu; eV değerleri kJ/mol ile tutarlı"),
    "crc_yogunluk": dict(yazar="Lide, D. R. (ed.)", yil=2003, baslik="CRC Handbook of Chemistry and Physics, 84. baskı — Physical Constants of Inorganic Compounds",
        yer="CRC Press, bölüm 4", dogrulama="Wikipedia 'Densities of the elements (data page)' CRC sütunundan okundu"),
    "malzeme": dict(yazar="Wikipedia katkıcıları (birincil: ASM malzeme veri sayfaları; Goodfellow naylon 6 veri sayfası; McGraw-Hill Encyclopedia of Science & Technology)",
        yil=2026, baslik="Specific strength — malzeme tablosu", yer="en.wikipedia.org/wiki/Specific_strength",
        dogrulama="tablo satırları sayfadan okundu; değerler TİPİK değerlerdir, üretim biçimine göre değişir (ikincil kaynak)"),
    "crc_elektrot": dict(yazar="Vanýsek, P.", yil=2011, baslik="Electrochemical Series — CRC Handbook of Chemistry and Physics, 92. ve 93. baskı (Al için 87. baskı)",
        yer="CRC Press", dogrulama="Wikipedia 'Standard electrode potential (data page)' üzerinden okundu: Li, Mg, Al, Zn, Ni, Ag, PbSO4/Pb"),
    "bard1985": dict(yazar="Bard, A. J., Parsons, R., & Jordan, J.", yil=1985, baslik="Standard Potentials in Aqueous Solution",
        yer="Marcel Dekker (IUPAC)", dogrulama="LibreTexts 'P1: Standard Reduction Potentials by Element' tablosundan okundu: Cu, Fe, Pb, PbO2/PbSO4"),
    "codata2022": dict(yazar="CODATA / NIST", yil=2022, baslik="CODATA Recommended Values of the Fundamental Physical Constants: Faraday constant",
        yer="physics.nist.gov/cgi-bin/cuu/Value?f", dogrulama="NIST sayfasından okundu: 96 485,332 12 C/mol (kesin)"),
    "oz_isi": dict(yazar="Wikipedia katkıcıları (birincil: NIST-JANAF Thermochemical Tables, 4. baskı, Chase 1998; mühendislik tabloları)", yil=2026,
        baslik="Table of specific heat capacities", yer="en.wikipedia.org/wiki/Table_of_specific_heat_capacities",
        dogrulama="sayfadan okundu: su 4,181 · alüminyum 0,897 · bakır 0,385 · demir 0,449 · cam (silika) 0,840 J/(g·K) (ikincil kaynak; sayfa kendi doğruluğu için uyarı taşıyor)"),
    "nist_webbook": dict(yazar="NIST Chemistry WebBook, SRD 69 (birincil: Cox, Wagman & Medvedev 1984, CODATA Key Values for Thermodynamics; Manion 2002)",
        yil=2026, baslik="Condensed / gas phase thermochemistry data", yer="webbook.nist.gov",
        dogrulama="NIST sayfalarından okundu: Al2O3 −1675,7 · CO2 −393,51 · H2O(s) −285,83 · CH4 −74,6 kJ/mol"),
    "sakkaroz": dict(yazar="Wikipedia katkıcıları", yil=2026, baslik="Solubility table — Sucrose satırı (g / 100 mL su)",
        yer="en.wikipedia.org/wiki/Solubility_table",
        dogrulama="satır sayfadan okundu; satırın kendi atfı YOK (zayıf kaynak). 25 °C için PubChem'deki 200–212 g/100 mL (ICSC 1507; Yalkowsky & Dannenfelser 1992) ile tutarlı"),
    "goldberg2002": dict(yazar="Goldberg, R. N., Kishore, N., & Lennen, R. M.", yil=2002,
        baslik="Thermodynamic quantities for the ionization reactions of buffers", yer="Journal of Physical and Chemical Reference Data, 31(2)",
        dogrulama="Wikipedia 'Citric acid' maddesindeki atıf üzerinden okundu: pKa1 3,128 (25 °C); mol kütlesi 192,12 g/mol PubChem"),
    "penniston2008": dict(yazar="Penniston, K. L., Nakada, S. Y., Holmes, R. P., & Assimos, D. G.", yil=2008,
        baslik="Quantitative assessment of citric acid in lemon juice, lime juice, and commercially-available fruit juice products",
        yer="Journal of Endourology, 22(3), 567–570", dogrulama="PubMed özeti (PMID 18290732): taze limon suyunda 1,44 g/oz sitrik asit"),
    "meb2024": dict(yazar="Millî Eğitim Bakanlığı", yil=2024, baslik="Türkiye Yüzyılı Maarif Modeli — Ortaöğretim Kimya Dersi Öğretim Programı (9, 10, 11 ve 12. sınıflar)",
        yer="mufredat.meb.gov.tr", dogrulama="program dosyası indirilip içerik çerçeveleri okundu (tema ve konu adları planlama/course.yml içinde)"),
}

# element: ad, atom numarası, atom kütlesi (g/mol), Pauling elektronegatifliği, birinci iyonlaşma enerjisi (kJ/mol), yoğunluk (g/cm³)
ELEMENT = {
    "Li": dict(ad="lityum",    Z=3,  kutle=6.94,   en=0.98, iyonlasma=520.2,  yogunluk=0.534),
    "C":  dict(ad="karbon",    Z=6,  kutle=12.011, en=2.55, iyonlasma=1086.5, yogunluk=2.2),     # yoğunluk: grafit
    "Al": dict(ad="alüminyum", Z=13, kutle=26.982, en=1.61, iyonlasma=577.5,  yogunluk=2.70),
    "Fe": dict(ad="demir",     Z=26, kutle=55.845, en=1.83, iyonlasma=762.5,  yogunluk=7.87),
    "Cu": dict(ad="bakır",     Z=29, kutle=63.546, en=1.90, iyonlasma=745.5,  yogunluk=8.96),
}
ELEMENT_KAYNAK = dict(kutle="ciaaw2024", en="crc_en", iyonlasma="crc_ie", yogunluk="crc_yogunluk")

# yalnız atom kütlesi (g/mol) ve elektronegatifliği gereken öteki elementler
KUTLE = {"H": 1.008, "Li": 6.94, "C": 12.011, "N": 14.007, "O": 15.999, "Na": 22.990, "Al": 26.982, "S": 32.06, "Cl": 35.45,
         "Fe": 55.845, "Co": 58.933, "Cu": 63.546, "Zn": 65.38, "Pb": 207.2}                      # ciaaw2024
EN = {"H": 2.20, "Li": 0.98, "C": 2.55, "N": 3.04, "O": 3.44, "F": 3.98, "Na": 0.93, "Al": 1.61, "Cl": 3.16, "Fe": 1.83,
      "Co": 1.88, "Cu": 1.90, "Zn": 1.65}                                                         # crc_en

# malzeme: (ad, çekme dayanımı MPa, yoğunluk g/cm³) — TİPİK değerler, kaynak "malzeme"
MALZEME = [
    ("paslanmaz çelik (304)",        505, 8.00),
    ("alüminyum alaşımı (6061-T6)",  310, 2.70),
    ("magnezyum alaşımı",            275, 1.74),
    ("naylon (poliamit 6)",           78, 1.13),
    ("karbon fiber–epoksi kompozit", 1240, 1.58),
]

# standart indirgenme potansiyeli E° (volt, 25 °C): yarı tepkime → (E°, kaynak)
ELEKTROT = {
    "Li+ + e- -> Li":                           (-3.0401, "crc_elektrot"),
    "Mg2+ + 2e- -> Mg":                         (-2.372,  "crc_elektrot"),
    "Al3+ + 3e- -> Al":                         (-1.662,  "crc_elektrot"),
    "Zn2+ + 2e- -> Zn":                         (-0.7618, "crc_elektrot"),
    "Fe2+ + 2e- -> Fe":                         (-0.44,   "bard1985"),
    "PbSO4 + 2e- -> Pb + SO4 2-":               (-0.3588, "crc_elektrot"),
    "Ni2+ + 2e- -> Ni":                         (-0.257,  "crc_elektrot"),
    "Pb2+ + 2e- -> Pb":                         (-0.126,  "bard1985"),
    "2H+ + 2e- -> H2":                          (0.0,     "tanım"),
    "Cu2+ + 2e- -> Cu":                         (0.3419,  "bard1985"),
    "Ag+ + e- -> Ag":                           (0.7996,  "crc_elektrot"),
    "PbO2 + SO4 2- + 4H+ + 2e- -> PbSO4 + 2H2O": (1.690,  "bard1985"),
}
E0 = {"Li": -3.0401, "Mg": -2.372, "Al": -1.662, "Zn": -0.7618, "Fe": -0.44, "Ni": -0.257, "Pb": -0.126, "H2": 0.0,
      "Cu": 0.3419, "Ag": 0.7996}                                                                 # metal/iyon çiftleri, yukarıdaki tablodan

FARADAY = 96485.33212        # C/mol — codata2022 (kesin)
AVOGADRO = 6.02214076e23     # 1/mol — SI tanımı (2019), kesin

# öz ısı, J/(g·K), 25 °C — kaynak "oz_isi"
OZ_ISI = {"su": 4.181, "alüminyum": 0.897, "bakır": 0.385, "demir": 0.449, "cam": 0.840}

# standart oluşum entalpisi, kJ/mol, 25 °C — kaynak "nist_webbook"; elementlerin standart hâli sıfırdır
OLUSUM = {"Al2O3(k)": -1675.7, "CO2(g)": -393.51, "H2O(s)": -285.83, "CH4(g)": -74.6, "O2(g)": 0.0, "Al(k)": 0.0}

# sakkarozun (çay şekeri) sudaki çözünürlüğü: sıcaklık °C → g / 100 mL su — kaynak "sakkaroz" (zayıf kaynak, dogrulama notuna bakın)
SAKKAROZ = {0: 181.9, 10: 190.6, 20: 201.9, 30: 216.7, 40: 235.6, 50: 259.6, 60: 288.8, 70: 323.7, 80: 365.1, 90: 414.9, 100: 476.0}

# sitrik asit — goldberg2002 (pKa1, 25 °C), penniston2008 (taze limon suyu: 1,44 g / ons; 1 ABD sıvı onsu = 29,5735 mL, tanım)
SITRIK = dict(pKa1=3.128, mol_kutlesi=192.12, limon_g_ons=1.44, ons_mL=29.5735)


def mol_kutlesi(formul):
    """{'C': 12, 'H': 22, 'O': 11} → g/mol (atom kütleleri ciaaw2024)."""
    return sum(KUTLE[e] * n for e, n in formul.items())
