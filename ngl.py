import concurrent.futures
import random
import string
import time
import requests

# --- ANSI Colors & Banner ---
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"
BOLD = "\033[1m"

BANNER = f"""{CYAN}{BOLD}
  _  _  ___  _     
 | \| |/ __|| |    
 | .` | (_ || |__  
 |_|\_|\___||____| 
{RESET}{MAGENTA}
┌──────────────────────────────────────────┐
│ {YELLOW}NGL Automated Message Sender v2.0{MAGENTA}        │
│ {GREEN}Status: Ready{MAGENTA} | {CYAN}Mode: Multi-Threaded{MAGENTA}       │
└──────────────────────────────────────────┘{RESET}
"""



def generate_device_id():
    return "".join(
        random.choices(string.ascii_lowercase + string.digits, k=36)
    )


def send_message(username, message, index, total):
    url = "https://ngl.link/api/submit"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML,"
            " like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
        ),
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://ngl.link",
        "Referer": f"https://ngl.link/{username}",
    }
    data = {
        "username": username,
        "question": message,
        "deviceId": generate_device_id(),
        "gameSlug": "",
        "referrer": "",
    }

    try:
        res = requests.post(url, headers=headers, data=data, timeout=5)
        if res.status_code == 200:
            print(f"[{index}/{total}] ส่งสำเร็จ -> {message}")
            return True
        else:
            print(
                f"[{index}/{total}] ล้มเหลว (Status: {res.status_code}) - ติด Rate Limit"
            )
            return False
    except Exception as e:
        print(f"[{index}/{total}] ข้อผิดพลาด: {e}")
        return False


def main():
    print(BANNER)

    username = input("ระบุ Username NGL: ").strip()
    message = input("ข้อความที่ต้องการสแปม: ").strip()

    try:
        count = int(input("จำนวนข้อความที่ต้องการสแปม: "))
        workers = int(
            input("จำนวน Thread ที่ส่งพร้อมกัน (แนะนำ 3-5): ")
        )
    except ValueError:
        print("\n[!] กรุณากรอกตัวเลขให้ถูกต้อง")
        return

    print("\n[!] กำลังเริ่มสแปมข้อความแบบเร่งด่วน...\n")

    success_count = 0
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=workers
    ) as executor:
        futures = [
            executor.submit(send_message, username, message, i, count)
            for i in range(1, count + 1)
        ]
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                success_count += 1

    print(
        f"\n[+] เสร็จสิ้น: ส่งสำเร็จ {success_count} / {count} ข้อความ"
    )


if __name__ == "__main__":
    main()
