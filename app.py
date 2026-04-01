from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="th">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mockup: ระบบพยากรณ์ข้าวหอมมะลิ</title>
        <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Prompt', sans-serif;
                background-color: #f0f4f8;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .ai-banner {
                background-color: #ffe082;
                color: #d35400;
                width: 100%;
                text-align: center;
                padding: 10px;
                font-size: 14px;
                font-weight: 600;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .container {
                background-color: white;
                width: 90%;
                max-width: 600px;
                margin-top: 30px;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
                border-top: 5px solid #2ecc71;
            }
            h1 {
                color: #27ae60;
                font-size: 24px;
                text-align: center;
                margin-bottom: 5px;
            }
            h2 {
                color: #7f8c8d;
                font-size: 16px;
                text-align: center;
                font-weight: 400;
                margin-top: 0;
                margin-bottom: 25px;
            }
            .status-box {
                background-color: #e8f8f5;
                border-left: 4px solid #1abc9c;
                padding: 15px;
                margin-bottom: 20px;
                border-radius: 4px;
            }
            .status-box p {
                margin: 5px 0;
                font-size: 14px;
            }
            .prediction-card {
                background-color: #fff;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                padding: 20px;
                text-align: center;
                background-image: linear-gradient(to bottom right, #ffffff, #f9fdfa);
            }
            .prediction-card h3 {
                color: #2c3e50;
                margin-top: 0;
            }
            .highlight {
                color: #e67e22;
                font-size: 20px;
                font-weight: 600;
            }
            .footer {
                margin-top: 30px;
                text-align: center;
                font-size: 12px;
                color: #95a5a6;
            }
        </style>
    </head>
    <body>
        <div class="ai-banner">
            🤖 หมายเหตุ: หน้าเว็บจำลองนี้เขียนโค้ดโดยใช้ AI ช่วยสร้าง เพื่อทำ Proof of Concept (PoC) เสนออาจารย์ครับ
        </div>
        
        <div class="container">
            <h1>🌾 ระบบพยากรณ์ช่วงเวลาหว่านข้าวหอมมะลิ</h1>
            <h2>(Mockup Version) จังหวัดอุบลราชธานี</h2>
            
            <div class="status-box">
                <p><b>📌 สถานะ:</b> นำเสนอแนวคิดโครงงาน (กำลังศึกษาการเทรน Machine Learning)</p>
                <p><b>📍 พื้นที่เป้าหมาย:</b> จังหวัดอุบลราชธานี</p>
                <p><b>📊 ข้อมูลอ้างอิง:</b> สถิติจากแบบสอบถามเกษตรกร 100% พบปัญหาฝนทิ้งช่วง</p>
            </div>

            <div class="prediction-card">
                <h3>ผลการคำนวณจำลอง (ตัวอย่าง)</h3>
                <p>ช่วงเวลาที่เหมาะสมที่สุดในการหว่านข้าวคือ:</p>
                <p class="highlight">สัปดาห์ที่ 2 ของเดือนพฤษภาคม</p>
                <p style="font-size: 14px; color: #27ae60;">โอกาสรอดพ้นจากฝนทิ้งช่วง: 88%</p>
            </div>

            <div class="footer">
                จัดทำโดย นายธฤต คำบุรมย์ (เมฆ)<br>
                เพื่อขอความอนุเคราะห์เรียนเชิญเป็นอาจารย์ที่ปรึกษาโครงงาน
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
