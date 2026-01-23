import markdown
import os
import glob
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(BASE_DIR, 'reports', 'source')
OUTPUT_DIR = os.path.join(BASE_DIR, 'reports', 'output')
ASSETS_DIR = os.path.join(BASE_DIR, 'reports', 'assets')

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Lucide Icons SVG Definitions (Same as main report)
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

# Custom CSS
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

@page {{
    size: A4;
    margin: 2.5cm 2cm 2cm 2cm;
    
    @top-right {{
        content: "เอกสารแนบประกอบสัญญา";
        font-family: var(--font-thai-body);
        font-size: 9pt;
        color: #888;
    }}
    
    @bottom-center {{
        content: "Nature Estate Co., Ltd.";
        font-family: var(--font-english);
        font-size: 8pt;
        color: #aaa;
    }}
}}

body {{
    font-family: var(--font-thai-body);
    font-size: 10.5pt;
    line-height: 1.6;
    color: var(--text-color);
}}

h1, h2, h3 {{
    font-family: var(--font-thai-heading);
    color: var(--primary-color);
}}

h1 {{
    font-size: 24pt;
    border-bottom: 3px solid var(--primary-color);
    padding-bottom: 15px;
    margin-bottom: 30px;
}}

h2 {{
    font-size: 18pt;
    margin-top: 30px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 10px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}}

th, td {{
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
    vertical-align: top;
}}

th {{
    background-color: var(--primary-color);
    color: white;
    font-weight: 500;
}}

.document-box {{
    border: 1px solid var(--border-color);
    padding: 30px;
    margin: 20px 0;
    background: white;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}}

.header-row {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 30px;
}}

.client-info, .company-info {{
    flex: 1;
}}

.total-row {{
    font-weight: bold;
    background-color: var(--bg-light);
}}

.page-break {{
    page-break-after: always;
}}

.signature-section {{
    margin-top: 50px;
    display: flex;
    justify-content: space-between;
    page-break-inside: avoid;
}}

.signature-box {{
    text-align: center;
    width: 45%;
}}

.sign-line {{
    border-bottom: 1px dotted #000;
    margin: 40px 0 10px 0;
    height: 1px;
}}
"""

def generate_attachments():
    # Find all attachment markdown files
    files = glob.glob(os.path.join(SOURCE_DIR, 'Attachment_Section_*.md'))
    files.sort()
    
    if not files:
        print("❌ No attachment files found!")
        return

    font_config = FontConfiguration()

    for file_path in files:
        filename = os.path.basename(file_path)
        print(f"🔄 Processing {filename}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        html_body = markdown.markdown(md_content, extensions=['tables', 'md_in_html'])

        full_html = f"""
        <!DOCTYPE html>
        <html lang="th">
        <head>
            <meta charset="utf-8">
            <style>{CSS_STYLES}</style>
        </head>
        <body>
            {LUCIDE_ICONS}
            {html_body}
        </body>
        </html>
        """

        output_filename = filename.replace('.md', '.pdf')
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        
        HTML(string=full_html, base_url=BASE_DIR).write_pdf(output_path, font_config=font_config)
        print(f"✅ Generated: {output_filename}")

if __name__ == "__main__":
    generate_attachments()
