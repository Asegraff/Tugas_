#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

// ============================================================
// STRUKTUR DATA TERPUSAT - Menggabungkan semua data per pesawat
// ============================================================
struct FlightSchedule {
    string kode_airlane;    // Kode pesawat (contoh: 01A1)
    string airlane;         // Nama maskapai (contoh: Angkasa)
    string flight;          // Kode penerbangan (contoh: IW)
    string tujuan;          // Kota tujuan (contoh: Surabaya)
    string waktu;           // Jam keberangkatan (contoh: 08:20)
    string terminal;        // Terminal keberangkatan (contoh: A)
    string remark;          // Catatan khusus (contoh: Holding)
};

// Array untuk menyimpan semua data jadwal penerbangan (maksimal 100)
FlightSchedule jadwal[100];
int totalJadwal = 0;

// ============================================================
// FUNGSI 1: Menampilkan Menu Utama
// ============================================================
void tampilkanMenu() {
    cout << "\n╔═════════════════════════════════════════╗" << endl;
    cout << "║  SISTEM MANAJEMEN JADWAL PESAWAT BANDARA║" << endl;
    cout << "║              BANDARA XYZ               ║" << endl;
    cout << "╚═════════════════════════════════════════╝" << endl;
    cout << "\n1. ➕ Tambah Jadwal Pesawat Baru" << endl;
    cout << "2. 📋 Lihat Semua Jadwal Penerbangan" << endl;
    cout << "3. ✏️  Ubah Jadwal Pesawat" << endl;
    cout << "4. ❌ Hapus Jadwal Pesawat" << endl;
    cout << "5. 🔍 Cari Jadwal Berdasarkan Kode" << endl;
    cout << "6. 🚪 Keluar dari Program" << endl;
    cout << "\nPilih menu (1-6): ";
}

// ============================================================
// FUNGSI 2: Menambah Jadwal Pesawat Baru
// ============================================================
void tambahJadwal() {
    // Cek apakah kapasitas array masih ada
    if (totalJadwal >= 100) {
        cout << "\n❌ Kapasitas jadwal penuh (maksimal 100)! Tidak bisa menambah lebih lanjut." << endl;
        return;
    }
    
    cout << "\n╔══════════════════════════════════════╗" << endl;
    cout << "║  FORM TAMBAH JADWAL PESAWAT BARU     ║" << endl;
    cout << "╚══════════════════════════════════════╝" << endl;
    
    cout << "Kode Airlane (contoh: 01A1): ";
    cin >> jadwal[totalJadwal].kode_airlane;
    
    cout << "Nama Maskapai (contoh: Angkasa): ";
    cin.ignore();  // Membersihkan buffer input
    getline(cin, jadwal[totalJadwal].airlane);
    
    cout << "Kode Flight (contoh: IW): ";
    getline(cin, jadwal[totalJadwal].flight);
    
    cout << "Kota Tujuan (contoh: Surabaya): ";
    getline(cin, jadwal[totalJadwal].tujuan);
    
    cout << "Waktu Keberangkatan HH:MM (contoh: 08:20): ";
    getline(cin, jadwal[totalJadwal].waktu);
    
    cout << "Terminal (A/B/C/D): ";
    getline(cin, jadwal[totalJadwal].terminal);
    
    cout << "Remark/Catatan (contoh: Holding/Landed): ";
    getline(cin, jadwal[totalJadwal].remark);
    
    totalJadwal++;
    cout << "\n✅ Jadwal pesawat berhasil ditambahkan!" << endl;
}

// ============================================================
// FUNGSI 3: Menampilkan Semua Jadwal Penerbangan
// ============================================================
void tampilkanSemuaJadwal() {
    if (totalJadwal == 0) {
        cout << "\n⚠️  Tidak ada jadwal pesawat yang tersimpan." << endl;
        return;
    }
    
    cout << "\n╔═══════════════════════════════════════════════════════════════════════════════════╗" << endl;
    cout << "║                     JADWAL PENERBANGAN BANDARA XYZ                                ║" << endl;
    cout << "║                                APRIL 2022                                         ║" << endl;
    cout << "╚═══════════════════════════════════════════════════════════════════════════════════╝" << endl;
    
    // Header tabel dengan format rapi
    cout << left 
         << setw(12) << "Kode AL" 
         << setw(15) << "Tujuan" 
         << setw(12) << "Maskapai" 
         << setw(8) << "Flight" 
         << setw(10) << "Terminal" 
         << setw(10) << "Waktu" 
         << "Remark" << endl;
    cout << "───────────────────────────────────────────────────────────────────────────────────" << endl;
    
    // Tampilkan semua data jadwal
    for (int i = 0; i < totalJadwal; i++) {
        cout << left 
             << setw(12) << jadwal[i].kode_airlane
             << setw(15) << jadwal[i].tujuan
             << setw(12) << jadwal[i].airlane
             << setw(8) << jadwal[i].flight
             << setw(10) << jadwal[i].terminal
             << setw(10) << jadwal[i].waktu
             << jadwal[i].remark << endl;
    }
    cout << "═══════════════════════════════════════════════════════════════════════════════════" << endl;
    cout << "\n📊 Total jadwal aktif: " << totalJadwal << endl;
}

// ============================================================
// FUNGSI 4: Mengubah Data Jadwal Pesawat
// ============================================================
void ubahJadwal() {
    if (totalJadwal == 0) {
        cout << "\n⚠️  Tidak ada jadwal pesawat untuk diubah." << endl;
        return;
    }
    
    string kode;
    cout << "\n╔══════════════════════════════════════╗" << endl;
    cout << "║  UBAH DATA JADWAL PESAWAT             ║" << endl;
    cout << "╚══════════════════════════════════════╝" << endl;
    cout << "Masukkan kode airlane yang ingin diubah: ";
    cin >> kode;
    cin.ignore();
    
    // Cari jadwal dengan kode yang sesuai
    int index = -1;
    for (int i = 0; i < totalJadwal; i++) {
        if (jadwal[i].kode_airlane == kode) {
            index = i;
            break;
        }
    }
    
    if (index == -1) {
        cout << "❌ Kode airlane '" << kode << "' tidak ditemukan!" << endl;
        return;
    }
    
    // Tampilkan data saat ini
    cout << "\n📋 Data saat ini:" << endl;
    cout << "─────────────────────────────────────" << endl;
    cout << "Maskapai     : " << jadwal[index].airlane << endl;
    cout << "Tujuan       : " << jadwal[index].tujuan << endl;
    cout << "Flight       : " << jadwal[index].flight << endl;
    cout << "Waktu        : " << jadwal[index].waktu << endl;
    cout << "Terminal     : " << jadwal[index].terminal << endl;
    cout << "Remark       : " << jadwal[index].remark << endl;
    
    // Input data baru
    cout << "\n✏️  Masukkan data baru (tekan Enter untuk skip/tidak mengubah):" << endl;
    cout << "Nama Maskapai: ";
    string temp;
    getline(cin, temp);
    if (!temp.empty()) jadwal[index].airlane = temp;
    
    cout << "Kode Flight: ";
    getline(cin, temp);
    if (!temp.empty()) jadwal[index].flight = temp;
    
    cout << "Kota Tujuan: ";
    getline(cin, temp);
    if (!temp.empty()) jadwal[index].tujuan = temp;
    
    cout << "Waktu (HH:MM): ";
    getline(cin, temp);
    if (!temp.empty()) jadwal[index].waktu = temp;
    
    cout << "Terminal: ";
    getline(cin, temp);
    if (!temp.empty()) jadwal[index].terminal = temp;
    
    cout << "Remark: ";
    getline(cin, temp);
    if (!temp.empty()) jadwal[index].remark = temp;
    
    cout << "\n✅ Jadwal pesawat berhasil diubah!" << endl;
}

// ============================================================
// FUNGSI 5: Menghapus Jadwal Pesawat
// ============================================================
void hapusJadwal() {
    if (totalJadwal == 0) {
        cout << "\n⚠️  Tidak ada jadwal pesawat untuk dihapus." << endl;
        return;
    }
    
    string kode;
    cout << "\n╔══════════════════════════════════════╗" << endl;
    cout << "║  HAPUS DATA JADWAL PESAWAT            ║" << endl;
    cout << "╚══════════════════════════════════════╝" << endl;
    cout << "Masukkan kode airlane yang ingin dihapus: ";
    cin >> kode;
    
    // Cari jadwal dengan kode yang sesuai
    int index = -1;
    for (int i = 0; i < totalJadwal; i++) {
        if (jadwal[i].kode_airlane == kode) {
            index = i;
            break;
        }
    }
    
    if (index == -1) {
        cout << "❌ Kode airlane '" << kode << "' tidak ditemukan!" << endl;
        return;
    }
    
    // Tampilkan data yang akan dihapus
    cout << "\n⚠️  Data yang akan dihapus:" << endl;
    cout << "Kode: " << jadwal[index].kode_airlane << " | Tujuan: " << jadwal[index].tujuan << endl;
    
    char konfirmasi;
    cout << "Apakah Anda yakin ingin menghapus? (y/n): ";
    cin >> konfirmasi;
    
    if (konfirmasi == 'y' || konfirmasi == 'Y') {
        // Geser data setelah index ke posisi sebelumnya
        for (int i = index; i < totalJadwal - 1; i++) {
            jadwal[i] = jadwal[i + 1];
        }
        totalJadwal--;
        cout << "\n✅ Jadwal pesawat berhasil dihapus!" << endl;
    } else {
        cout << "\n❌ Penghapusan dibatalkan." << endl;
    }
}

// ============================================================
// FUNGSI 6: Mencari Jadwal Berdasarkan Kode
// ============================================================
void cariJadwal() {
    if (totalJadwal == 0) {
        cout << "\n⚠️  Tidak ada jadwal pesawat." << endl;
        return;
    }
    
    string kode;
    cout << "\n╔══════════════════════════════════════╗" << endl;
    cout << "║  CARI JADWAL PESAWAT                  ║" << endl;
    cout << "╚══════════════════════════════════════╝" << endl;
    cout << "Masukkan kode airlane yang dicari: ";
    cin >> kode;
    
    // Cari jadwal dengan kode yang sesuai
    int index = -1;
    for (int i = 0; i < totalJadwal; i++) {
        if (jadwal[i].kode_airlane == kode) {
            index = i;
            break;
        }
    }
    
    if (index == -1) {
        cout << "\n❌ Jadwal dengan kode '" << kode << "' tidak ditemukan!" << endl;
        return;
    }
    
    // Tampilkan detail jadwal yang ditemukan
    cout << "\n✅ HASIL PENCARIAN:" << endl;
    cout << "═════════════════════════════════════" << endl;
    cout << "Kode Airlane : " << jadwal[index].kode_airlane << endl;
    cout << "Maskapai     : " << jadwal[index].airlane << endl;
    cout << "Flight       : " << jadwal[index].flight << endl;
    cout << "Tujuan       : " << jadwal[index].tujuan << endl;
    cout << "Waktu        : " << jadwal[index].waktu << endl;
    cout << "Terminal     : " << jadwal[index].terminal << endl;
    cout << "Remark       : " << jadwal[index].remark << endl;
    cout << "═════════════════════════════════════" << endl;
}

// ============================================================
// FUNGSI 7: Inisialisasi Data Contoh
// ============================================================
void inisialisasiData() {
    // Data default yang sudah ada di program awal
    jadwal[0] = {"01A1", "Angkasa", "IW", "Surabaya", "08:20", "A", "Holding"};
    jadwal[1] = {"02E1", "Eagle", "ID", "Pontianak", "09:00", "A", "Landed 09:48"};
    jadwal[2] = {"01A2", "Angkasa", "IW", "Pekanbaru", "10:00", "B", "Holding"};
    jadwal[3] = {"02E2", "Eagle", "ID", "Denpasar", "10:40", "B", "Landed 10:15"};
    totalJadwal = 4;
    
    cout << "\n✅ Data contoh dimuat (4 jadwal penerbangan)" << endl;
}

// ============================================================
// FUNGSI MAIN - Program Utama
// ============================================================
int main(){
    int pilihan;
    bool berjalan = true;
    
    // Muat data contoh saat program dimulai
    inisialisasiData();
    
    // Loop menu utama - program akan terus berjalan sampai user memilih keluar
    while (berjalan) {
        tampilkanMenu();
        cin >> pilihan;
        
        // Switch case untuk menangani pilihan menu
        switch (pilihan) {
            case 1:
                tambahJadwal();
                break;
            case 2:
                tampilkanSemuaJadwal();
                break;
            case 3:
                ubahJadwal();
                break;
            case 4:
                hapusJadwal();
                break;
            case 5:
                cariJadwal();
                break;
            case 6:
                cout << "\n👋 Terima kasih telah menggunakan Sistem Manajemen Jadwal Pesawat." << endl;
                cout << "Sampai jumpa lagi!" << endl;
                berjalan = false;  // Keluar dari loop
                break;
            default:
                cout << "\n❌ Pilihan tidak valid! Silakan pilih menu 1-6." << endl;
        }
    }
    
    return 0;
}
