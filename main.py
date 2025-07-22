import requests
import time
import hashlib

def generate_sign(fid, secret_key, timestamp):
    # نص التوقيع كما شفنا: sign = md5("fid=<fid>&time=<time>" + secret_key)
    raw = f"fid={fid}&time={timestamp}{secret_key}"
    return hashlib.md5(raw.encode()).hexdigest()

def main():
    secret_key = "f8baee0af6af0140f32e2de606176341"
    fid = input("ادخل رقم اللاعب (fid): ").strip()
    timestamp = str(int(time.time() * 1000))

    sign = generate_sign(fid, secret_key, timestamp)

    url = "https://kingshot-giftcode.centurygame.com/api/player"
    data = {
        "fid": fid,
        "time": timestamp,
        "sign": sign
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://ks-giftcode.centurygame.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json, text/plain, */*"
    }

    response = requests.post(url, data=data, headers=headers)

    try:
        result = response.json()
        print(result)
    except Exception as e:
        print("خطأ في قراءة الرد:", e)
        print("النص الكامل للرد:", response.text)

if __name__ == "__main__":
    main()
