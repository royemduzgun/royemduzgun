import hashlib


def calculate_sha256(file_path):
    # Dosyanın SHA256 hash değerini hesapla
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def scan_file_virustotal(api_key, file_path):
    # Dosyanın SHA256 hash değerini hesapla
    sha256_hash = calculate_sha256(file_path)
    # VirusTotal API'ye tarama isteği yap
    params = {'apikey': api_key, 'resource': sha256_hash}
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
    result = response.json()
    # Tarama sonucunu işle
    if result['response_code'] == 1:
        print("Scan results for file:", file_path)
        print("SHA256 Hash:", sha256_hash)
        print("Detected by", result['positives'], "out of", result['total'], "antivirus engines.")
        if result['positives'] > 0:
            print("Detected antivirus engines:", result['scans'])
    else:
        print("No results found on VirusTotal for file:", file_path)

if __name__ == "__main__":
    api_key = input("Enter your VirusTotal API key: ")
    file_path = input("Enter the path of the file to scan: ")
    scan_file_virustotal(api_key, file_path)
