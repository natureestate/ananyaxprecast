# Ananya x Nature Estate Project System

ระบบจัดการเอกสาร ข้อเสนอราคา และรายงานปิดโครงการอนัญญา (นครพนม) โดย บริษัท เนเจอร์ เอ็ซเทท จำกัด

## 📁 โครงสร้างโครงการ

- `reports/`
  - `source/`: ไฟล์ Markdown ต้นฉบับสำหรับรายงาน (`.md`)
  - `output/`: ไฟล์รายงาน PDF ที่ Export สำเร็จแล้ว
  - `assets/`: ทรัพยากรประกอบรายงาน เช่น พื้นหลังหน้าปก
- `Ananya_Nakhonphanom_Cost_Proposal.md`: รายละเอียดงบประมาณโครงการ
- `Ananya_Nakhonphanom_Precast_Proposal.md`: ข้อเสนอระบบ Precast CPAC
- `Ananya_Nakhonphanom_Windsor_Proposal.md`: ข้อเสนอระบบประตู-หน้าต่าง WINDSOR
- `export_report_pdf.py`: สคริปต์หลักสำหรับแปลง Markdown เป็น PDF เกรดพรีเมียม

## 🛠️ การใช้งานระบบ PDF Export

ระบบใช้สถาปัตยกรรม **WeasyPrint** ร่วมกับ **Python** เพื่อการจัดรูปแบบ PDF ระดับมืออาชีพ

### 1. การติดตั้ง (ครั้งแรก)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install weasyprint markdown
```

### 2. การสั่ง Export รายงาน
เมื่อแก้ไขข้อมูลใน `reports/source/` เรียบร้อยแล้ว ให้รันคำสั่ง:
```bash
.venv/bin/python export_report_pdf.py
```
*ระบบจะสร้างไฟล์ PDF พร้อมระบุเวลา (Timestamp) ในโฟลเดอร์ `reports/output/` อัตโนมัติ*

## ✨ คุณสมบัติการออกแบบ (Design Specs)

- **Typography**: 
  - English: `Inter`
  - Thai Headings: `IBM Plex Sans Thai`
  - Thai Body: `Sarabun`
- **Icons**: ใช้ `Lucide Icons` (SVG) ทั้งระบบ
- **Layout**:
  - หน้าปกสไตล์โมเดิร์น (Modern Architecture)
  - สารบัญระบบ Dot Leaders พร้อมเลขหน้า
  - ระบบ Header/Footer แสดงชื่อโครงการและเลขหน้าทุกหน้า (ยกเว้นหน้าปก)
  - สีกระดาษและตารางโทน Nature Estate Green (#1a4d2e)

## 📌 หมายเหตุ
- เอกสารทั้งหมดในระบบถือเป็นความลับ (Confidential)
- การแก้ไข Design สารบัญหรือ Layout หลัก สามารถปรับแต่งได้ที่ `export_report_pdf.py` (CSS Section)