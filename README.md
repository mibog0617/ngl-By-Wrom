# NGL Message Sender Tool

สคริปต์ Python สำหรับส่งข้อความไปยัง NGL ผ่าน Termux

## วิธีติดตั้งและใช้งานใน Termux

```bash
# 1. อัปเดตแพ็กเกจระบบ
pkg update && pkg upgrade -y

# 2. ติดตั้ง Python และ Git
pkg install python git -y

# 3. ติดตั้ง 라이บรารี requests
pip install requests

# 4. คลอน Repository นี้
git clone [https://github.com/USERNAME/REPOSITORY-NAME.git](https://github.com/USERNAME/REPOSITORY-NAME.git)

# 5. เข้าโฟลเดอร์และรันโปรแกรม
cd REPOSITORY-NAME
python main.py
