from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>ระบบพยากรณ์ข้าวหอมมะลิ</title>
            <meta charset="utf-8">
            <style>
                body { font-family: 'Sarabun', sans-serif; background-color: #f4f9f4; text-align: center; padding-top: 50px; }
                .container { background-color: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1 style="color: #2c7a2c;">🌾 ระบบพยากรณ์และแนะนำช่วงเวลาหว่านข้าวหอมมะลิ</h1>
                <h2>จังหวัดอุบลราชธานี</h2>
                <hr>
                <p style="color: #e67e22; font-size: 20px;"><b>⏳ สถานะระบบ:</b> กำลังพัฒนาและเทรนโมเดล Machine Learning</p>
                <p style="font-size: 18px;"><b>📍 พื้นที่ทดสอบนำร่อง:</b> อำเภอเมือง</p>
                <div style="background-color: #e8f5e9; padding: 15px; border-radius: 10px; margin-top: 20px;">
                    <h3 style="color: #2e7d32;">✅ ผลการทำนายจำลอง (Proof of Concept)</h3>
                    <p><b>ช่วงเวลาแนะนำ:</b> สัปดาห์ที่ 2 ของเดือนพฤษภาคม</p>
                    <p><b>ความเสี่ยงฝนทิ้งช่วง:</b> ต่ำมาก (12%)</p>
                </div>
                <br>
                <p style="color: gray; font-size: 14px;">จัดทำโดย นายธฤต คำบุรมย์ (เสนอหัวข้อโครงงาน)</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

