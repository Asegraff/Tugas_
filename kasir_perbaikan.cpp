#include<iostream>
#include<iomanip>
#include<vector>
#include<cctype>
using namespace std;

struct programmer{
    string user_id="xander";
    string password="12345";
    string namaProgrammer="..++..";
};
programmer pro;

struct barang{
    string namaBarang;
    string kodeBarang;
    string supplier;
    int jumlahStock;
};

void line(){
    for(int i=0;i<60;i++){
        cout<<"=";
    }cout<<endl;
}

void menuUtama(){
    cout<<endl;
    cout<<"================== MENU UTAMA =================="<<endl;
    line();
    cout<<"[I] Tampil data inventory"<<endl;
    cout<<"[P] Pengambilan barang"<<endl;
    cout<<"[T] Tambah stock barang"<<endl;
    cout<<"[E] Exit"<<endl;
    cout<<"Pilihan [I/P/T/E]? ";
}

void tampilInventory(vector<barang>& barangDagang){
    cout<<endl;
    cout<<"==================== INVENTORY ===================="<<endl;
    cout<<setiosflags(ios::left);
    cout<<setw(5)<<"No"<<setw(12)<<"Kode Barang"<<setw(20)<<"Nama Barang"<<setw(10)<<"Stock"<<setw(20)<<"Supplier"<<endl;
    line();
    for (int i = 0; i < barangDagang.size(); i++)
    {
        cout<<setw(5)<<i+1<<setw(12)<<barangDagang[i].kodeBarang<<setw(20)<<barangDagang[i].namaBarang
            <<setw(10)<<barangDagang[i].jumlahStock<<setw(20)<<barangDagang[i].supplier<<endl;
    }
    line();
}

void pengambilanBarang(vector<barang>& barangDagang){
    cout<<endl;
    cout<<"==================== PENGAMBILAN BARANG ===================="<<endl;
    line();
    
    string ambilKode;
    int jumlahAmbil;
    
    cout<<"Kode Barang : ";cin>>ambilKode;
    cout<<"Jumlah Diambil : ";cin>>jumlahAmbil;
    
    int indexFound = -1;
    
    // Cari barang dengan kode yang sesuai
    for (int j = 0; j < barangDagang.size(); j++)
    {
        if(ambilKode == barangDagang[j].kodeBarang){
            indexFound = j;
            break;
        }
    }
    
    // Validasi hasil pencarian
    if(indexFound == -1){
        cout<<"[GAGAL] Kode barang '"<<ambilKode<<"' tidak ditemukan!"<<endl;
    }
    // Validasi jumlah pengambilan
    else if(jumlahAmbil <= 0){
        cout<<"[GAGAL] Jumlah yang diambil harus lebih dari 0!"<<endl;
    }
    // Validasi stock cukup
    else if(jumlahAmbil > barangDagang[indexFound].jumlahStock){
        cout<<"[GAGAL] Stock tidak cukup!"<<endl;
        cout<<"Stock saat ini : "<<barangDagang[indexFound].jumlahStock<<" unit"<<endl;
    }
    // Proses pengambilan barang
    else{
        barangDagang[indexFound].jumlahStock -= jumlahAmbil;
        cout<<"[SUKSES] Pengambilan berhasil!"<<endl;
        cout<<"Barang : "<<barangDagang[indexFound].namaBarang<<endl;
        cout<<"Jumlah diambil : "<<jumlahAmbil<<" unit"<<endl;
        cout<<"Sisa Stock : "<<barangDagang[indexFound].jumlahStock<<" unit"<<endl;
    }
    line();
}

void tambahStock(vector<barang>& barangDagang){
    cout<<endl;
    cout<<"==================== TAMBAH STOCK BARANG ===================="<<endl;
    line();
    
    string tambahKode;
    int jumlahTambah;
    
    cout<<"Kode Barang : ";cin>>tambahKode;
    cout<<"Jumlah Penambahan : ";cin>>jumlahTambah;
    
    int indexFound = -1;
    
    // Cari barang dengan kode yang sesuai
    for (int j = 0; j < barangDagang.size(); j++)
    {
        if(tambahKode == barangDagang[j].kodeBarang){
            indexFound = j;
            break;
        }
    }
    
    // Validasi hasil pencarian
    if(indexFound == -1){
        cout<<"[GAGAL] Kode barang '"<<tambahKode<<"' tidak ditemukan!"<<endl;
    }
    // Validasi jumlah penambahan
    else if(jumlahTambah <= 0){
        cout<<"[GAGAL] Jumlah yang ditambah harus lebih dari 0!"<<endl;
    }
    // Proses penambahan stock
    else{
        barangDagang[indexFound].jumlahStock += jumlahTambah;
        cout<<"[SUKSES] Penambahan stock berhasil!"<<endl;
        cout<<"Barang : "<<barangDagang[indexFound].namaBarang<<endl;
        cout<<"Jumlah ditambah : "<<jumlahTambah<<" unit"<<endl;
        cout<<"Total Stock : "<<barangDagang[indexFound].jumlahStock<<" unit"<<endl;
    }
    line();
}

int main(){
    string user_id;
    string password;
    char pilih;
    int coba=0;
    int jumlahBarang;
    
    cout<<endl;
    cout<<"   ============================================"<<endl;
    cout<<"   = SISTEM MANAJEMEN INVENTORY PT 'SUPPLY' ="<<endl;
    cout<<"   ============================================"<<endl;
    
    // Login
    do{
        cout<<endl;
        cout<<"Programmer : "<<pro.namaProgrammer<<endl;
        cout<<"------------- LOGIN -------------"<<endl;
        cout<<"User Id: ";cin>>user_id;
        cout<<"Password: ";cin>>password;
        
        if(user_id==pro.user_id && password==pro.password){
            cout<<"[SUKSES] Login berhasil!"<<endl;
            coba=100;
        }
        else{
            coba++;
            if(coba == 3){
                cout<<"[GAGAL] Kesempatan login habis! Program dihentikan."<<endl;
                return 0;
            }
            cout<<"[GAGAL] User Id atau Password salah! Kesempatan tinggal "<<(3-coba)<<" kali."<<endl;
        }
    }while(coba<3);

    // Input jumlah barang
    cout<<endl;
    cout<<"Input berapa barang yang akan didata? ";
    cin>>jumlahBarang;
    
    if(jumlahBarang <= 0){
        cout<<"Jumlah barang harus lebih dari 0!"<<endl;
        return 0;
    }
    
    vector<barang> barangDagang(jumlahBarang);
    
    // Input data barang
    cout<<endl;
    cout<<"==================== INPUT DATA BARANG ===================="<<endl;
    for (int i = 0; i < jumlahBarang; i++)
    {
        cout<<"Barang ke-"<<i+1<<endl;
        cout<<"Kode Barang : ";cin>>barangDagang[i].kodeBarang;
        cout<<"Nama barang : ";cin.ignore();getline(cin, barangDagang[i].namaBarang);
        cout<<"Stock : ";cin>>barangDagang[i].jumlahStock;
        
        // Validasi stock tidak boleh negatif
        if(barangDagang[i].jumlahStock < 0){
            cout<<"[PERINGATAN] Stock tidak boleh negatif! Diset ke 0."<<endl;
            barangDagang[i].jumlahStock = 0;
        }
        
        cout<<"Supplier : ";cin.ignore(); getline(cin, barangDagang[i].supplier);
        cout<<endl;
    }

    // Menu utama
    do{
        menuUtama();
        cin>>pilih;
        
        // Convert input ke uppercase
        pilih = toupper(pilih);
        
        switch (pilih)
        {
        case 'I':
            tampilInventory(barangDagang);
            break;
            
        case 'P':
            pengambilanBarang(barangDagang);
            break;
            
        case 'T':
            tambahStock(barangDagang);
            break;
            
        case 'E':
            cout<<endl;
            cout<<"Terima kasih telah menggunakan sistem ini!"<<endl;
            return 0;
            
        default:
            cout<<"[GAGAL] Pilihan tidak valid! Silahkan pilih [I/P/T/E]"<<endl;
            break;
        }
        
        cout<<"Kembali ke Menu utama?[Y/T]: ";cin>>pilih;
        pilih = toupper(pilih);
        
    }while(pilih=='Y');
    
    cout<<endl;
    cout<<"Program berakhir."<<endl;
    return 0;
}
