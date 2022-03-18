print("Tugas Dasar Pemrograman".center(85))
print("Kelompok 1")
print("|No|\t\t\t\tNama\t\t\t\t|\tNim")
print("|1 |Mahfudh Hidayat                     |19207228")
print("|2 |Angga Maulana Saputra               |19207201")
print("|3 |Amir Fathahullah                    |19217071")
print("|4 |Mohamad Rival                       |19207016")
print("\r")


print("DAFTAR GUDANG".center(85))
print("\r")
print("----------------------------------------------------------------------------------")
print("|\tNo\t|\t\t\tNama Barang\t\t\t|\t\tCode\t\t|\t\tStock\t\t|")
print("----------------------------------------------------------------------------------")
print("|   1   |            Laptop             |         LTP       |         7         |")
print("|   2   |            PC                 |         PC        |         3         |")
print("|   3   |            Printer            |         PRT       |         3         |")
print("|   4   |            keyboard           |         KYB       |         4         |")
print("|   5   |            Mouse              |         MOS       |         9         |")
print("|   6   |            Webcam             |         CAM       |         6         |")
print("|   7   |            Monitor            |         MTR       |         5         |")
print("|   8   |            Mouse Pad          |         PAD       |        10         |")
print("|   9   |            HDD External       |         HDE       |         7         |")
print("|   10  |            SSD                |         SSD       |         3         |")

print("\r")

ulang = "yes"
while(ulang == "yes"):

#dataspesifikasi
    Laptop_merek = ["Merek         :",
                    "Processor     :",
                    "RAM           :",
                    "Penyimpanan   :",
                    "Harga         :"]
    Laptop_data  = ["Acer",
                    "Intel Core 7",
                    "8 Gb",
                    "1 Tb",
                    "Rp. 8.000.000"]
    PC_merek = ["Merek              :",
                "Processor          :",
                "RAM                :",
                "Penyimpanan        :",
                "VGA                :",
                "Harga              :" ]
    PC_data = ["Intel Core I7 2600/ 16 GB / 1 TB/ SSD 120 GB",
            "Intel Core I7 2600 (3,4 GHZ) dan Motherboard Intel H61 / 1155",
            "16 GB",
            "1 TB/SSD 120 GB",
            "VGA N Vidia GTX 1050 TI 4 GB DDR 5",
            "Rp. 6.500.000"]
    P_Spek  = ["Merek               :",
            "Garansi             :",
            "Kelengkapan Paket   :",
            "Dimensi             :",
            "Tipe Tinta          :",
            "Fitur Copy          :",
            "Fitur Scan          :",
            "Fitur Cetak         :",
            "Tipe Koneksi        :",
            "Kecepatan Cetak     :",
            "Resolusi Cetak      :",
            "Maks Besaran Kertas :",
            "Fungsi              :",
            "Harga               :"]
    P_Data  = ["Epson L4160 Printer Multifungsi [Print/ Scan/ Copy/ Wi-Fi",
            "Distributor Resmi 2 Tahun",
            "Unit Printer dan Tinta 001",
            "37.5 x 34.7 x 18.7 cm",
            "001 (Black, Cyan, Magenta, Yellow)",
            "Ya",
            "Ya",
            "Ya",
            "USB, Wi-Fi"
            "33 / 15 ppm",
            "5760 x 1440 dpi",
            "A4",
            "Print, Scan, Copy",
            "Rp 1.300.000"]
    key_merek = ["Merek                     :",
                "Tipe                      :",
                "Tracking Technology       :",
                "Sensitivitas              :",
                "Koneksi                   :",
                "Kebutuhan sistem          :",
                "Color                     :",
                "Operating Sistem          :",
                "Garansi                   :",
                "Harga                     :"]
    key_data  = ["Keyboard Logitech K120 USB",
                "Wired",
                "Optical",
                "800 dpi",
                "USB",
                "Windows XP, Windows Vista, Windows 7, Windows 8, Windows 10",
                "Black",
                " Linux kernel 2.6+, Windows Vista, Windows XP, Windows 7",
                "1 Tahun",
                "Rp 105.000"]
    mouse_merek = ["Merek                   :",
                "Berat mause             :",
                "Berat Nano Receiver     :",
                "Jenis Koneksi           :",
                "Jangkauan Wireless      :",
                "Baterai                 :",
                "Daya Tahan Baterai      :",
                "Isi Kemasan             :",
                "Informasi Garansi       :",
                "Harga                   :"]
    mouse_data  = ["M171 Mouse Wireless",
                "70,5 g dengan baterai",
                "2,0 g",
                "2.4 Ghz wireless",
                "10 m/32 kaki",
                "1xAA",
                "1 Tahun",
                "Mouse,Receiver dan Dokumentasi pengguna",
                "Garansi perangkat keras terbatas 1 Tahun",
                "Rp 560.000"]
    webcam_merek = ["Merek                          :",
                    "Berat                          :",
                    "Panjang Kabel                  :",
                    "Kompatibel Dengan              :",
                    "Resolusi Maks                  :",
                    "Jenis Focus                    :",
                    "Jenis Lensa                    :",
                    "Microfon Internal              :",
                    "Bidang Pandang diagonal/dFoV   :",
                    "Informasi Garansi              :",
                    "Nomor Suku Cadang              :",
                    "Harga                          :"]
    webcam_data  = ["C920 HD PRO WEBCAM",
                    "162 G",
                    "1,5 m",
                    "Windows 7 or later, macOS 10.10 or later, Chrome OS, Port USB-A. Kompatibel dengan platform panggilan yang populer",
                    "1080p/30fps - 720p/30fps",
                    "Autofocus",
                    "Kaca",
                    "Stereo",
                    "78 derajat",
                    "Garansi Hardward Terbatas 2 Tahun",
                    "960-000770",
                    "Rp 799.000"]
    monitor_merek =[" merek                 :",
                    "Aspect Ratio           :",
                    "Brightness/Typical     :",
                    "Resolution             :",
                    "Respon Time            :",
                    "Warna                  :",
                    "HDMI Cable             :",
                    "Garansi                :",
                    "Harga                  :"]
    monitor_data = ["Monitor LED SAMSUNG 24 INCH",
                    "16:9",
                    "250cd/m2",
                    "1920x1080",
                    "4 GTG",
                    "Black High Glossy",
                    "Yes",
                    "Garansi Terbatas 6 Bulan",
                    "Rp 3.200.000"]
    mp_merek = ["Merek              :",
                "Berat              :",
                "Lebar              :",
                "Tipis              :",
                "Nomor Suku Cadang  :",
                "Harga              :",]
    mp_data = ["G440 HARD GAMING MOUSEPAD",
            "229 g",
            "340 mm",
            "3 mm",
            "943-000052",
            "Rp 499.000"]
    hdd_merek = ["Merek                 :",
                "Color                 :",
                "Type USB              :",
                "Connection Interface  :",
                "Storage Capacity      :",
                "Storage Media         :",
                "Garansi               :",
                "Harga                 :"]
    hdd_data = ["TRANSCEND StoreJet 25M3 USB Type C 2TB [TS2TSJ25M3C]",
                "Iron Gray",
                "USB Type C to USB Type A/USB Type C to USB Type C",
                "USB 3.1 Gen 1",
                "2 TB",
                "Garansi Resmi 1 Tahun",
                "Rp 999.000"]
    ssd_merek = ["Merek                                 :",
                "Capacity                              :",
                "Form Factor                           :",
                "NAND Flash                            :",
                "Controller                            :",
                "Dimensions (L x W x H)                :",
                "Weigh                                 :",
                "Interface                             :",
                "Performance (Max)                     :",
                "Maximum 4K random read/write IOPS     :",
                "Power Consumption                     :",
                "Operating temperature                 :",
                "Storage temperature                   :",
                "Shock resistance                      :",
                "MTBF                                  :",
                "Certifications                        :",
                "Warranty                              :",
                "Harga                                 :"]
    ssd_data = ["SSD Adata XPG SX8200 Pro NVMe ",
                "256GB / 512GB / 1TB / 2TB",
                "M.2 2280",
                "3D TLC",
                "SMI",
                "80 x 22 x 3.5 mm",
                "8g / 0.28oz",
                "PCIe Gen3x4",
                "Read 3500MB/s, Write 3000MB/s",
                "up to 390K/380K",
                "0.33W Active (Typical), 0.14W Slumber (Typical)",
                "0°C – 70°C",
                "– 40°C – 85°C",
                "1500G/0.5ms",
                "2,000,000 hours",
                "RoHS, CE, FCC, BSMI, VCCI, KC",
                "5-year limited warranty",
                "Rp 1.433.000"]

    #spesifikasi
    spesifikasi = input("lihat spesifikasi No :")
    if spesifikasi == "1" :
        for merek,data in zip(Laptop_merek,Laptop_data):
            print(merek,data)
    elif spesifikasi == "2" :
        for merek,data in zip(PC_merek,PC_data):
            print(merek,data)
    elif spesifikasi == "3" :
        for merek,data in zip(P_Spek,P_Data):
            print(merek,data)
    elif spesifikasi == "4" :
        for merek,data in zip(key_merek,key_data):
            print(merek,data)
    elif spesifikasi == "5" :
        for merek,data in zip(mouse_merek,mouse_data):
            print(merek,data)
    elif spesifikasi == "6" :
        for merek,data in zip(webcam_merek,webcam_data):
            print(merek,data)
    elif spesifikasi == "7" :
        for merek,data in zip(monitor_merek,monitor_data):
            print(merek,data)
    elif spesifikasi == "8" :
        for merek,data in zip(mp_merek,mp_data):
            print(merek,data)
    elif spesifikasi == "9" :
        for merek,data in zip(hdd_merek,hdd_data):
            print(merek,data)
    elif spesifikasi == "10" :
        for merek,data in zip(ssd_merek,ssd_data):
            print(merek,data)
    else:
        print("Barang Tidak Teredia")
    ulang = str (input("ingin melihat spesifikasi lainnya? (yes/no) : "))