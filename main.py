import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_mp4_files(url):
    try:
        # Mengunduh konten halaman web
        response = requests.get(url)
        response.raise_for_status()
        
        # Mengurai konten HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Mencari semua tag <a> dan <source> untuk link file
        links = soup.find_all(['a', 'source'])
        
        # Menyaring link yang mengarah ke file .mp4
        mp4_files = []
        for link in links:
            href = link.get('href')
            if href and href.endswith('.mp4'):
                # Membuat link absolut jika diperlukan
                absolute_url = urljoin(url, href)
                mp4_files.append(absolute_url)
        
        return mp4_files
    
    except requests.RequestException as e:
        print(f"Terjadi kesalahan saat mengunduh halaman: {e}")
        return []

# Input link dari pengguna
input_url = input("Masukkan URL halaman web: ")
mp4_files = find_mp4_files(input_url)

# Menampilkan hasil
if mp4_files:
    print("File .mp4 ditemukan:")
    for file in mp4_files:
        print(file)
else:
    print("Tidak ada file .mp4 ditemukan.")
