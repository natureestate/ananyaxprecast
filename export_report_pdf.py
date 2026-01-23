import markdown
import os
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(BASE_DIR, 'reports', 'source')
OUTPUT_DIR = os.path.join(BASE_DIR, 'reports', 'output')
ASSETS_DIR = os.path.join(BASE_DIR, 'reports', 'assets')

INPUT_FILE = os.path.join(SOURCE_DIR, 'Ananya_Nakhonphanom_Project_Closure_Report.md')
TIMESTAMP = datetime.now().strftime('%Y%m%d_%H%M')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, f'Ananya_Nakhonphanom_Report_{TIMESTAMP}.pdf')
COVER_IMAGE = os.path.join(ASSETS_DIR, 'cover_bg.png')

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Lucide Icons SVG Definitions
LUCIDE_ICONS = """
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
  <!-- ClipboardList -->
  <symbol id="icon-clipboard-list" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/>
  </symbol>
  <!-- FileText -->
  <symbol id="icon-file-text" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/>
  </symbol>
  <!-- Users -->
  <symbol id="icon-users" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>
  </symbol>
  <!-- MapPin -->
  <symbol id="icon-map-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>
  </symbol>
  <!-- GitBranch -->
  <symbol id="icon-git-branch" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>
  </symbol>
  <!-- Shield -->
  <symbol id="icon-shield" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
  </symbol>
  <!-- CheckCircle -->
  <symbol id="icon-check-circle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>
  </symbol>
  <!-- AlertCircle -->
  <symbol id="icon-alert-circle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/>
  </symbol>
  <!-- Check -->
  <symbol id="icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="20 6 9 17 4 12"/>
  </symbol>
  <!-- Square (Checkbox) -->
  <symbol id="icon-square" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <rect width="18" height="18" x="3" y="3" rx="2"/>
  </symbol>
</svg>
"""

# Custom CSS for WeasyPrint with Inter, IBM Plex Sans Thai, Sarabun
CSS_STYLES = f"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&display=swap');

:root {{
    --primary-color: #1a4d2e;
    --secondary-color: #4a7c59;
    --accent-color: #e9ecef;
    --text-color: #2d3748;
    --border-color: #e2e8f0;
    --bg-light: #f8fafc;
    
    --font-english: 'Inter', sans-serif;
    --font-thai-heading: 'IBM Plex Sans Thai', sans-serif;
    --font-thai-body: 'Sarabun', sans-serif;
}}

/* Page Setup */
@page {{
    size: A4;
    margin: 2.5cm 2cm 3cm 2cm;
    
    @top-left {{
        content: "โครงการอนัญญา นครพนม";
        font-family: var(--font-thai-body);
        font-size: 9pt;
        color: #888;
    }}
    
    @top-right {{
        content: "Ananya Project Closure Report";
        font-family: var(--font-english);
        font-size: 9pt;
        color: #888;
    }}
    
    @bottom-left {{
        content: "Nature Estate Co., Ltd. | Confidential";
        font-family: var(--font-english);
        font-size: 8pt;
        color: #aaa;
    }}
    
    @bottom-right {{
        content: "หน้า " counter(page) " / " counter(pages);
        font-family: var(--font-thai-body);
        font-size: 9pt;
        color: var(--primary-color);
        font-weight: 600;
    }}
}}

@page :first {{
    margin: 0;
    background-image: url('file://{COVER_IMAGE}');
    background-size: cover;
    background-position: center;
    
    @top-left {{ content: none; }}
    @top-right {{ content: none; }}
    @bottom-left {{ content: none; }}
    @bottom-right {{ content: none; }}
}}

/* Base Styles */
body {{
    font-family: var(--font-thai-body);
    font-size: 10.5pt;
    line-height: 1.7;
    color: var(--text-color);
    margin: 0;
    padding: 0;
}}

/* Cover Page */
.cover-page {{
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between; /* แยกหัวข้อกับข้อมูลลงบน-ล่าง */
    padding: 3cm 2cm;
    box-sizing: border-box;
    color: white;
    background: linear-gradient(135deg, rgba(26,77,46,0.7) 0%, rgba(0,0,0,0.4) 100%);
}}

.cover-content {{
    margin-top: 2cm;
    width: 100%;
}}

.cover-page h1 {{
    font-family: var(--font-english);
    font-size: 40pt;
    font-weight: 700;
    text-transform: uppercase;
    margin: 0;
    line-height: 1.1;
    color: white;
    letter-spacing: 2px;
    border: none;
}}

.cover-page h2 {{
    font-family: var(--font-english);
    font-size: 20pt;
    font-weight: 300;
    margin: 20px 0 0 0;
    color: rgba(255,255,255,0.9);
    border: none;
    letter-spacing: 5px;
    text-transform: uppercase;
}}

.cover-info {{
    background: transparent; /* ลบพื้นหลังออก */
    color: white; /* เปลี่ยนเป็นสีขาวเพื่อให้เห็นชัดบนพื้นหลังเข้ม */
    padding: 0;
    border: none;
    width: 100%;
    margin-bottom: 3cm; /* เว้นระยะจากขอบล่าง */
    box-shadow: none;
}}

.cover-info p {{
    margin: 8px 0;
    font-size: 11pt;
    font-family: var(--font-thai-body);
}}

/* Table of Contents */
.toc {{
    background: transparent;
    padding: 1.5cm 0;
    border: none;
    margin: 0;
    box-shadow: none;
}}

.toc-title {{
    font-family: var(--font-thai-heading);
    text-align: center;
    font-size: 28pt;
    margin: 0 0 40px 0;
    color: var(--primary-color);
    border-bottom: 3px solid var(--primary-color);
    padding-bottom: 15px;
}}

.toc-list {{
    margin: 0;
    padding: 0;
}}

.toc-item {{
    display: flex;
    align-items: baseline;
    margin-bottom: 18px;
    line-height: 1.5;
}}

.toc-number {{
    font-family: var(--font-thai-body);
    font-weight: 600;
    color: var(--primary-color);
    min-width: 30px;
    font-size: 11pt;
}}

.toc-text {{
    font-family: var(--font-thai-body);
    font-size: 11pt;
    color: var(--text-color);
}}

.toc-dots {{
    flex-grow: 1;
    border-bottom: 1.5px dotted #ccc;
    margin: 0 15px 3px 15px;
    min-width: 30px;
}}

.toc-page {{
    font-family: var(--font-english);
    font-weight: 600;
    color: var(--primary-color);
    min-width: 30px;
    text-align: right;
    font-size: 11pt;
}}

.toc-list table {{
    display: none;
}}

/* Typography */
h2 {{
    font-family: var(--font-thai-heading);
    color: var(--primary-color);
    border-bottom: 3px solid var(--secondary-color);
    padding-bottom: 12px;
    margin-top: 0;
    margin-bottom: 25px;
    font-size: 22pt;
    font-weight: 700;
    page-break-after: avoid;
}}

h3 {{
    font-family: var(--font-thai-heading);
    color: var(--secondary-color);
    margin-top: 30px;
    margin-bottom: 15px;
    font-size: 14pt;
    font-weight: 600;
    page-break-after: avoid;
}}

.section-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(90deg, var(--bg-light) 0%, transparent 100%);
    padding: 12px 15px;
    border-left: 4px solid var(--primary-color);
    margin: 25px 0 15px 0;
}}

.section-header .icon {{
    width: 20px;
    height: 20px;
    color: var(--primary-color);
}}

/* Lucide Icons */
.icon {{
    display: inline-block;
    width: 18px;
    height: 18px;
    vertical-align: middle;
    margin-right: 8px;
}}

.icon-inline {{
    display: inline-block;
    width: 14px;
    height: 14px;
    vertical-align: middle;
    margin-right: 6px;
    color: var(--primary-color);
}}

.icon-clipboard-list::before {{ content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%231a4d2e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect width='8' height='4' x='8' y='2' rx='1' ry='1'/%3E%3Cpath d='M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2'/%3E%3Cpath d='M12 11h4'/%3E%3Cpath d='M12 16h4'/%3E%3Cpath d='M8 11h.01'/%3E%3Cpath d='M8 16h.01'/%3E%3C/svg%3E"); }}

.icon-file-text::before {{ content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%231a4d2e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z'/%3E%3Cpolyline points='14 2 14 8 20 8'/%3E%3Cline x1='16' x2='8' y1='13' y2='13'/%3E%3Cline x1='16' x2='8' y1='17' y2='17'/%3E%3Cline x1='10' x2='8' y1='9' y2='9'/%3E%3C/svg%3E"); }}

.icon-users::before {{ content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%231a4d2e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2'/%3E%3Ccircle cx='9' cy='7' r='4'/%3E%3Cpath d='M22 21v-2a4 4 0 0 0-3-3.87'/%3E%3Cpath d='M16 3.13a4 4 0 0 1 0 7.75'/%3E%3C/svg%3E"); }}

.icon-map-pin::before {{ content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%231a4d2e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z'/%3E%3Ccircle cx='12' cy='10' r='3'/%3E%3C/svg%3E"); }}

.icon-git-branch::before {{ content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%231a4d2e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cline x1='6' x2='6' y1='3' y2='15'/%3E%3Ccircle cx='18' cy='6' r='3'/%3E%3Ccircle cx='6' cy='18' r='3'/%3E%3Cpath d='M18 9a9 9 0 0 1-9 9'/%3E%3C/svg%3E"); }}

.icon-shield::before {{ content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%231a4d2e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/%3E%3C/svg%3E"); }}

.icon-check-circle::before {{ content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%231a4d2e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M22 11.08V12a10 10 0 1 1-5.93-9.14'/%3E%3Cpolyline points='22 4 12 14.01 9 11.01'/%3E%3C/svg%3E"); }}

.icon-alert-circle::before {{ content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%231a4d2e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3Cline x1='12' x2='12' y1='8' y2='12'/%3E%3Cline x1='12' x2='12.01' y1='16' y2='16'/%3E%3C/svg%3E"); }}

.icon-check::before {{ content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%231a4d2e' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E"); }}

/* Checkbox */
.checkbox {{
    display: inline-block;
    width: 14px;
    height: 14px;
    border: 2px solid var(--secondary-color);
    border-radius: 3px;
    background: white;
    vertical-align: middle;
}}

/* Tables */
table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 20px 0;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 15px rgba(0,0,0,0.06);
    font-size: 10pt;
}}

th {{
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    font-family: var(--font-thai-heading);
    font-weight: 600;
    padding: 14px 12px;
    text-align: center;
    font-size: 10pt;
    letter-spacing: 0.3px;
}}

td {{
    padding: 12px;
    border-bottom: 1px solid var(--border-color);
    font-family: var(--font-thai-body);
    vertical-align: middle;
    background: white;
}}

tr:nth-child(even) td {{
    background: var(--bg-light);
}}

tr:last-child td {{
    border-bottom: none;
}}

/* Note Box */
.note-box {{
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border: 1px solid #86efac;
    border-left: 4px solid var(--primary-color);
    padding: 20px 25px;
    border-radius: 6px;
    margin: 20px 0;
}}

.note-box li {{
    list-style: none;
    margin: 10px 0;
    font-family: var(--font-thai-body);
}}

/* Signature Section */
.signature-section {{
    margin-top: 3cm;
}}

.signature-row {{
    display: flex;
    justify-content: space-between;
    gap: 30px;
    margin-bottom: 2cm;
}}

.signature-single {{
    justify-content: center;
}}

.signature-box {{
    flex: 1;
    max-width: 45%;
    text-align: center;
    padding: 20px;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    background: var(--bg-light);
}}

.signature-single .signature-box {{
    max-width: 50%;
}}

.signature-title {{
    font-family: var(--font-thai-heading);
    font-weight: 700;
    font-size: 12pt;
    color: var(--primary-color);
    margin-bottom: 50px;
}}

.signature-line {{
    border-bottom: 2px dotted var(--text-color);
    margin: 40px auto 15px;
    width: 80%;
}}

.signature-label {{
    font-family: var(--font-thai-body);
    font-size: 10pt;
    color: #666;
    margin: 8px 0;
}}

/* Document Footer */
.document-footer {{
    text-align: center;
    margin-top: 3cm;
    padding-top: 1cm;
    border-top: 2px solid var(--border-color);
    color: #666;
}}

.document-footer strong {{
    font-family: var(--font-thai-heading);
    font-size: 12pt;
    color: var(--primary-color);
}}

.confidential {{
    font-size: 9pt;
    color: #999;
    margin-top: 15px;
    font-style: italic;
}}

/* Page Break */
.page-break {{
    page-break-after: always;
}}

/* Org Chart */
.org-chart table {{
    width: auto;
    margin: 0 auto;
}}

/* Lists */
ul, ol {{
    font-family: var(--font-thai-body);
}}

li {{
    margin: 8px 0;
}}

strong {{
    font-weight: 600;
}}
"""

def generate_pdf():
    # Read Markdown
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # MD to HTML
    html_body = markdown.markdown(md_content, extensions=['tables', 'md_in_html'])

    # Full HTML wrapper
    full_html = f"""
    <!DOCTYPE html>
    <html lang="th">
    <head>
        <meta charset="utf-8">
        <title>Ananya Project Closure Report</title>
        <style>{CSS_STYLES}</style>
    </head>
    <body>
        {LUCIDE_ICONS}
        {html_body}
    </body>
    </html>
    """

    # Generate PDF
    font_config = FontConfiguration()
    HTML(string=full_html, base_url=BASE_DIR).write_pdf(OUTPUT_FILE, font_config=font_config)
    print(f"✅ PDF generated successfully!")
    print(f"📄 Output: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_pdf()
