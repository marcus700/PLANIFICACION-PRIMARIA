import streamlit as st
from google import genai
from google.genai import types
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import io
import re
import time
from PIL import Image
import cneb_primaria_datos as cneb

# ==============================================================================
# CONFIGURACIÓN DE LA PÁGINA STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="PlanificaPrimaria - Plataforma para Docentes de Aula",
    page_icon="🍎",
    layout="wide"
)

# ==============================================================================
# INYECCIÓN CSS/JS NIVEL INGENIERÍA PARA ESTILOS, TABLAS CON COLOR Y LIMPIEZA
# ==============================================================================
st.markdown("""
<style>
    /* 1. ANULACIÓN Y COLAPSO ABSOLUTO DE ELEMENTOS DE STREAMLIT CLOUD */
    header, footer, [data-testid="stHeader"], [data-testid="stDecoration"], 
    [data-testid="stStatusWidget"], [data-testid="stViewerBadge"], 
    [data-testid="manage-app-button"], .stAppDeployButton, .viewerBadge_container__1613n,
    button[title*="Streamlit"], div[class*="stDeployButton"], div[class*="viewerBadge"], 
    div[class*="ViewerBadge"], a[class*="viewerBadge"], a[class*="ViewerBadge"], 
    div[class*="profile"], div[class*="Profile"], div[class*="crown"], div[class*="Crown"], 
    div[class*="hostBadge"], div[class*="HostBadge"], div[class*="badge"], div[class*="Badge"], 
    div[class*="floating"], div[class*="Floating"], a[href*="streamlit"], a[href*="share.streamlit.io"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        width: 0px !important;
        height: 0px !important;
        max-width: 0px !important;
        max-height: 0px !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        pointer-events: none !important;
        position: absolute !important;
        left: -9999px !important;
        top: -9999px !important;
        z-index: -9999 !important;
        transform: scale(0) !important;
    }
    
    /* 2. FONDO CLARO Y ELEGANTE PARA TODA LA PÁGINA */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
    }
    
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 1rem !important;
        background-color: #F8FAFC !important;
    }
    
    /* Encabezados */
    .main-header {
        font-size: 2.1rem;
        color: #1E3A8A;
        font-weight: 800;
        margin-bottom: 0.2rem;
        line-height: 1.2;
    }
    .sub-header {
        font-size: 1.0rem;
        color: #4B5563;
        margin-bottom: 1.2rem;
    }

    /* 3. CAMPOS DE ENTRADA Y TEXTOS */
    .stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 1px solid #94A3B8 !important;
        border-radius: 8px !important;
    }
    .stTextInput label, .stTextArea label, .stSelectbox label, .stSlider label, p, span, h1, h2, h3, h4 {
        color: #0F172A !important;
        font-weight: 600 !important;
    }

    /* 4. COLORES EXCLUSIVOS PARA CADA BOTÓN DE HERRAMIENTA */
    div.st-key-btn_proyecto > button {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        background-color: #059669 !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35) !important;
    }
    div.st-key-btn_proyecto > button p { color: #FFFFFF !important; font-weight: 800 !important; font-size: 1.05rem !important; }

    div.st-key-btn_unidad > button {
        background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%) !important;
        background-color: #7C3AED !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.35) !important;
    }
    div.st-key-btn_unidad > button p { color: #FFFFFF !important; font-weight: 800 !important; font-size: 1.05rem !important; }

    div.st-key-btn_sesion > button {
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%) !important;
        background-color: #2563EB !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.35) !important;
    }
    div.st-key-btn_sesion > button p { color: #FFFFFF !important; font-weight: 800 !important; font-size: 1.05rem !important; }

    div.st-key-btn_ficha > button {
        background: linear-gradient(135deg, #F97316 0%, #D97706 100%) !important;
        background-color: #D97706 !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(249, 115, 22, 0.35) !important;
    }
    div.st-key-btn_ficha > button p { color: #FFFFFF !important; font-weight: 800 !important; font-size: 1.05rem !important; }

    div.st-key-btn_afiche > button {
        background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%) !important;
        background-color: #DC2626 !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.35) !important;
    }
    div.st-key-btn_afiche > button p { color: #FFFFFF !important; font-weight: 800 !important; font-size: 1.05rem !important; }

    /* BOTÓN PRINCIPAL DE GENERACIÓN */
    div.stButton > button:not([key="btn_proyecto"]):not([key="btn_unidad"]):not([key="btn_sesion"]):not([key="btn_ficha"]):not([key="btn_afiche"]) {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        background-color: #2563EB !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4) !important;
    }
    div.stButton > button:not([key="btn_proyecto"]):not([key="btn_unidad"]):not([key="btn_sesion"]):not([key="btn_ficha"]):not([key="btn_afiche"]) p {
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
    }

    /* 5. 🎨 ESTILOS PEDAGÓGICOS A COLOR PARA CUADROS Y TABLAS EN STREAMLIT */
    div[data-testid="stMarkdownContainer"] table {
        width: 100% !important;
        border-collapse: separate !important;
        border-spacing: 0 !important;
        border-radius: 10px !important;
        overflow: hidden !important;
        margin: 1.4rem 0 !important;
        border: 1px solid #CBD5E1 !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.06), 0 2px 4px -1px rgba(0, 0, 0, 0.04) !important;
    }

    div[data-testid="stMarkdownContainer"] table thead tr th {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        text-align: center !important;
        padding: 10px 14px !important;
        font-size: 0.94rem !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.3px !important;
    }

    div[data-testid="stMarkdownContainer"] table:nth-of-type(6n+1) thead tr th { background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%) !important; }
    div[data-testid="stMarkdownContainer"] table:nth-of-type(6n+2) thead tr th { background: linear-gradient(135deg, #065F46 0%, #10B981 100%) !important; }
    div[data-testid="stMarkdownContainer"] table:nth-of-type(6n+3) thead tr th { background: linear-gradient(135deg, #6B21A8 0%, #8B5CF6 100%) !important; }
    div[data-testid="stMarkdownContainer"] table:nth-of-type(6n+4) thead tr th { background: linear-gradient(135deg, #9A3412 0%, #F97316 100%) !important; }
    div[data-testid="stMarkdownContainer"] table:nth-of-type(6n+5) thead tr th { background: linear-gradient(135deg, #0E7490 0%, #06B6D4 100%) !important; }
    div[data-testid="stMarkdownContainer"] table:nth-of-type(6n+6) thead tr th { background: linear-gradient(135deg, #BE123C 0%, #F43F5E 100%) !important; }

    div[data-testid="stMarkdownContainer"] table tbody tr:nth-child(even) { background-color: #F8FAFC !important; }
    div[data-testid="stMarkdownContainer"] table tbody tr:nth-child(odd) { background-color: #FFFFFF !important; }
    div[data-testid="stMarkdownContainer"] table tbody tr:hover { background-color: #FEF3C7 !important; transition: background-color 0.2s ease-in-out; }
    div[data-testid="stMarkdownContainer"] table tbody td {
        padding: 9px 12px !important;
        border: 1px solid #E2E8F0 !important;
        color: #1E293B !important;
        font-size: 0.92rem !important;
        vertical-align: top !important;
    }
    div[data-testid="stMarkdownContainer"] table tbody td:first-child {
        font-weight: 600 !important;
        background-color: #F1F5F9 !important;
        color: #1E3A8A !important;
    }
</style>
""", unsafe_allow_html=True)

# SCRIPT JAVASCRIPT GLOBAL
st.markdown("""
<script>
function injectKillStyle() {
    const targets = [window.document, window.parent.document, window.top.document];
    targets.forEach(doc => {
        try {
            if (doc && !doc.getElementById('sys-kill-style')) {
                const style = doc.createElement('style');
                style.id = 'sys-kill-style';
                style.innerHTML = `
                    [data-testid="stViewerBadge"], [data-testid="manage-app-button"],
                    .viewerBadge_container__1613n, .stAppDeployButton,
                    div[class*="viewerBadge"], div[class*="ViewerBadge"],
                    a[class*="viewerBadge"], a[class*="ViewerBadge"],
                    div[class*="profile"], div[class*="Profile"],
                    div[class*="crown"], div[class*="Crown"],
                    div[class*="badge"], div[class*="Badge"],
                    a[href*="streamlit"] {
                        display: none !important; visibility: hidden !important; opacity: 0 !important; width: 0 !important; height: 0 !important;
                    }
                `;
                doc.head.appendChild(style);
            }
        } catch(e) {}
    });
}
setInterval(injectKillStyle, 150);
window.addEventListener('load', injectKillStyle);
</script>
""", unsafe_allow_html=True)

# ==============================================================================
# CONTROL DE ACCESO MEDIANTE CONTRASEÑA
# ==============================================================================
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if st.session_state["password_correct"]:
        return True

    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.subheader("🔒 Acceso Restringido al Sistema")
        st.info("💡 Por favor, ingresa la contraseña para acceder a la plataforma.")
        pwd_input = st.text_input("Contraseña de acceso:", type="password", key="pwd_input")
        
        if st.button("Ingresar 🚀"):
            target_pwd = st.secrets.get("APP_PASSWORD", "docente2026")
            if pwd_input == target_pwd:
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Contraseña incorrecta. Inténtalo de nuevo.")
    return False

if not check_password():
    st.stop()

# ==============================================================================
# LISTA DE MODELOS OFICIALES Y ESTABLES DE GEMINI
# ==============================================================================
MODELOS_DISPONIBLES = [
    "gemini-3.5-flash-lite",  # Recomendado oficial por Google: Rápido y sin saturación
    "gemini-3.5-flash",       # Gran velocidad y alta precisión pedagógica
    "gemini-3.8-flash",       # Modelo frontier de última generación
    "gemini-2.5-flash",       # Razonamiento pedagógico
    "gemini-2.0-flash",       # Versión 2.0 Flash
    "gemini-1.5-flash",       # Compatible universal
    "gemini-1.5-pro"          # Máxima calidad y redacción extensa
]

# INICIALIZACIÓN DE MEMORIA PERSISTENTE
if 'resultado_md' not in st.session_state: st.session_state['resultado_md'] = None
if 'tipo_doc_generado' not in st.session_state: st.session_state['tipo_doc_generado'] = None
if 'fname_clean' not in st.session_state: st.session_state['fname_clean'] = None
if 'ie_nombre_generado' not in st.session_state: st.session_state['ie_nombre_generado'] = None
if 'tipo_documento' not in st.session_state: st.session_state['tipo_documento'] = "Proyecto de Aprendizaje"
if 'imagen_nanobanana' not in st.session_state: st.session_state['imagen_nanobanana'] = None
if 'imagen_bytes' not in st.session_state: st.session_state['imagen_bytes'] = None
if 'model_choice' not in st.session_state: st.session_state['model_choice'] = "gemini-3.5-flash-lite"

# ==============================================================================
# ENCABEZADO PRINCIPAL CON SELECTOR DE MODELO GEMINI INTEGRADO A UN LADO
# ==============================================================================
col_tit, col_mod = st.columns([2.6, 1.4])

with col_tit:
    st.markdown('<div class="main-header">🍎 PlanificaPrimaria - Sistema para Docentes de Aula</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Plataforma Inteligente de Planificación Curricular para Educación Primaria (CNEB - MINEDU)</div>', unsafe_allow_html=True)

with col_mod:
    st.markdown("""
    <div style="background-color: #FFFFFF; border: 1.5px solid #2563EB; border-radius: 10px; padding: 6px 12px; margin-bottom: 5px; box-shadow: 0 2px 6px rgba(37,99,235,0.12);">
        <span style="font-weight: 800; color: #1E3A8A; font-size: 0.88rem;">🤖 MOTOR GEMINI ACTIVO:</span>
    </div>
    """, unsafe_allow_html=True)
    
    idx_actual = MODELOS_DISPONIBLES.index(st.session_state['model_choice']) if st.session_state['model_choice'] in MODELOS_DISPONIBLES else 0
    modelo_seleccionado = st.selectbox(
        "Selecciona el modelo de Gemini a utilizar:",
        options=MODELOS_DISPONIBLES,
        index=idx_actual,
        label_visibility="collapsed",
        key="top_model_selector"
    )
    st.session_state['model_choice'] = modelo_seleccionado
    model_choice = modelo_seleccionado

# ==============================================================================
# BARRA LATERAL (SIDEBAR) - CONFIGURACIÓN Y API KEY
# ==============================================================================
st.sidebar.title("⚙️ Configuración")

if st.sidebar.button("🔒 Cerrar Sesión"):
    st.session_state["password_correct"] = False
    st.rerun()

st.sidebar.markdown("---")

if "GEMINI_API_KEY" in st.secrets and st.secrets["GEMINI_API_KEY"]:
    api_key = st.secrets["GEMINI_API_KEY"]
    st.sidebar.success("🔑 API Key activada desde el servidor.")
else:
    api_key = st.sidebar.text_input(
        "🔑 Google AI Studio API Key:", 
        type="password", 
        help="Consigue tu clave gratuita en https://aistudio.google.com/app/apikey"
    )

st.sidebar.markdown(f"**🤖 Modelo activo:** `{model_choice}`")
st.sidebar.markdown("---")
st.sidebar.info("""
**Alineamiento CNEB Perú:**
• RM N.° 649-2016-MINEDU
• Estándares y Desempeños CNEB Íntegros
• Conexión directa a cneb_primaria_datos.py
• Turno Único: 2 a 3 Sesiones diarias de 90 min
• Nivel Educación Primaria (1.° a 6.° Grado)
• Tablas coloreadas y exportables a Word
""")

# ==============================================================================
# SELECCIÓN DE HERRAMIENTAS DE AULA EN LA PÁGINA PRINCIPAL
# ==============================================================================
st.markdown("### 📋 Selecciona la Herramienta de Aula que deseas elaborar:")

col_b1, col_b2, col_b3, col_b4, col_b5 = st.columns(5)

with col_b1:
    if st.button("🚀 Proyecto de Aprendizaje", key="btn_proyecto", use_container_width=True):
        st.session_state['tipo_documento'] = "Proyecto de Aprendizaje"
        st.rerun()

with col_b2:
    if st.button("📘 Unidad SARA", key="btn_unidad", use_container_width=True):
        st.session_state['tipo_documento'] = "Unidad de Aprendizaje (Modelo SARA)"
        st.rerun()

with col_b3:
    if st.button("🍎 Sesión de Aprendizaje", key="btn_sesion", use_container_width=True):
        st.session_state['tipo_documento'] = "Sesión de Aprendizaje"
        st.rerun()

with col_b4:
    if st.button("📝 Ficha de Aplicación", key="btn_ficha", use_container_width=True):
        st.session_state['tipo_documento'] = "Ficha de Aplicación / Trabajo (Para Alumnos)"
        st.rerun()

with col_b5:
    if st.button("🖼️ Afiche Nano Banana", key="btn_afiche", use_container_width=True):
        st.session_state['tipo_documento'] = "Afiche Educativo de la Sesión (Nano Banana)"
        st.rerun()

tipo_documento = st.session_state['tipo_documento']

COLOR_MAP = {
    "Proyecto de Aprendizaje": "#059669",
    "Unidad de Aprendizaje (Modelo SARA)": "#7C3AED",
    "Sesión de Aprendizaje": "#2563EB",
    "Ficha de Aplicación / Trabajo (Para Alumnos)": "#D97706",
    "Afiche Educativo de la Sesión (Nano Banana)": "#DC2626"
}
banner_color = COLOR_MAP.get(tipo_documento, "#059669")

st.markdown(f"""
<div style="background-color: {banner_color}; color: white; padding: 0.6rem 1rem; border-radius: 8px; font-weight: bold; font-size: 1.05rem; margin-top: 0.8rem; margin-bottom: 1.2rem; text-align: center;">
    📍 Herramienta Seleccionada: {tipo_documento.upper()} | 🤖 Motor Activo: {model_choice}
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# FUNCIONES AUXILIARES Y GENERADOR HÍBRIDO NANO BANANA
# ==============================================================================
def add_formatted_text(paragraph, text):
    parts = re.split(r'(\*\*.*?\*\*)', text)
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            run = paragraph.add_run(part[2:-2])
            run.font.bold = True
        else:
            paragraph.add_run(part)

def markdown_to_docx(md_text, ie_nombre="I.E. N° 22303", es_horizontal=False):
    """Genera el documento Word (.docx) aplicando tonos pasteles en cada tabla"""
    doc = docx.Document()
    PASTEL_COLORS = ['D9E1F2', 'E2EFDA', 'FFF2CC', 'E8D8F8', 'E0F2FE', 'FCE4D6']
    table_count = 0
    
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
        if es_horizontal:
            section.orientation = WD_ORIENT.LANDSCAPE
            section.page_width = Inches(11.69)
            section.page_height = Inches(8.27)
        else:
            section.orientation = WD_ORIENT.PORTRAIT
            section.page_width = Inches(8.27)
            section.page_height = Inches(11.69)
        
    p_box = doc.add_paragraph()
    p_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_box = p_box.add_run(f"🖼️ [ PEGAR AQUÍ LA INSIGNIA / ESCUDO DE LA {ie_nombre.upper()} ]\n")
    run_box.font.size = Pt(10)
    run_box.font.italic = True
    run_box.font.color.rgb = RGBColor(107, 114, 128)

    lines = md_text.split('\n')
    in_table = False
    table_data = []

    def render_table(t_data, color_hex):
        rows = len(t_data)
        cols = max(len(r) for r in t_data) if rows > 0 else 0
        if rows > 0 and cols > 0:
            t = doc.add_table(rows=rows, cols=cols)
            t.style = 'Table Grid'
            for r_idx, row_cells in enumerate(t_data):
                for c_idx, cell_value in enumerate(row_cells):
                    if c_idx < cols:
                        cell = t.cell(r_idx, c_idx)
                        p_cell = cell.paragraphs[0]
                        p_cell.text = ""
                        add_formatted_text(p_cell, cell_value)
                        
                        if r_idx == 0:
                            shading_elm = OxmlElement('w:shd')
                            shading_elm.set(qn('w:val'), 'clear')
                            shading_elm.set(qn('w:color'), 'auto')
                            shading_elm.set(qn('w:fill'), color_hex)
                            cell._tc.get_or_add_tcPr().append(shading_elm)
                            for paragraph in cell.paragraphs:
                                for run in paragraph.runs:
                                    run.font.color.rgb = RGBColor(30, 58, 138)
                                    run.font.bold = True
                        elif r_idx % 2 == 1:
                            shading_elm = OxmlElement('w:shd')
                            shading_elm.set(qn('w:val'), 'clear')
                            shading_elm.set(qn('w:color'), 'auto')
                            shading_elm.set(qn('w:fill'), 'F8FAFC')
                            cell._tc.get_or_add_tcPr().append(shading_elm)

    for line in lines:
        line_str = line.strip()
        line_str = re.sub(r'<br\s*/?>', ' ', line_str)
        line_str = re.sub(r'</?[a-zA-Z0-9]+\s*/>', ' ', line_str)
        line_str = re.sub(r'</?(table|tr|td|th|thead|tbody)[^>]*>', ' ', line_str, flags=re.IGNORECASE)
        
        if line_str.startswith('|') and line_str.endswith('|'):
            in_table = True
            if re.match(r'^\|[\s\:\-\|]+\|$', line_str):
                continue
            cells = [c.strip() for c in line_str.split('|')[1:-1]]
            table_data.append(cells)
            continue
        elif in_table:
            if table_data:
                table_count += 1
                header_color = PASTEL_COLORS[(table_count - 1) % len(PASTEL_COLORS)]
                render_table(table_data, header_color)
            in_table = False
            table_data = []

        heading_match = re.match(r'^(#{1,6})\s*(.*)$', line_str)
        if heading_match:
            hashes = heading_match.group(1)
            title_text = heading_match.group(2).strip()
            level = len(hashes)
            
            p = doc.add_paragraph()
            if level in [1, 2]:
                run = p.add_run(title_text.replace('**', ''))
                run.font.size = Pt(14)
                run.font.bold = True
                run.font.color.rgb = RGBColor(30, 58, 138)
            elif level in [3, 4]:
                run = p.add_run(title_text.replace('**', ''))
                run.font.size = Pt(12)
                run.font.bold = True
                run.font.color.rgb = RGBColor(30, 58, 138)
            else:
                add_formatted_text(p, title_text)
            continue

        if line_str.startswith('• ') or line_str.startswith('- '):
            p = doc.add_paragraph(style='List Bullet')
            clean_bullet = line_str[2:].strip()
            add_formatted_text(p, clean_bullet)
        elif line_str != "":
            p = doc.add_paragraph()
            add_formatted_text(p, line_str)

    if in_table and table_data:
        table_count += 1
        header_color = PASTEL_COLORS[(table_count - 1) % len(PASTEL_COLORS)]
        render_table(table_data, header_color)
            
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

def generar_imagen_nanobanana(client, tema, grado, area):
    prompt_nanobanana = f"""
    Full educational primary school session infographic poster (Estilo Sesión de Aprendizaje e Infografía Oficial MINEDU Perú).
    Grade: {grado}. Subject: {area}. Topic: '{tema}'.
    Visual Poster Layout & Structure: Top title 'SESIÓN DE APRENDIZAJE: {tema.upper()}', step activity cards, cute primary students in classroom, vector clean layout 3:4.
    """
    for mod in ['imagen-4.0-generate-001', 'imagen-3.0-generate-002', 'imagen-3.0-fast-generate-001']:
        try:
            result = client.models.generate_images(
                model=mod, prompt=prompt_nanobanana,
                config=types.GenerateImagesConfig(number_of_images=1, output_mime_type="image/jpeg", aspect_ratio="3:4")
            )
            if hasattr(result, 'generated_images') and result.generated_images:
                img_bytes = result.generated_images[0].image.image_bytes
                return Image.open(io.BytesIO(img_bytes)), img_bytes, None
        except Exception:
            continue
    return None, None, "No se pudo generar la imagen."

# ==============================================================================
# FORMULARIO DE DATOS DE AULA CONECTADO A CNEB
# ==============================================================================
st.subheader(f"📝 Configuración de Datos: {tipo_documento}")

c1, c2, c3 = st.columns(3)
with c1:
    dre_ugel = st.text_input("DRE / UGEL:", "Ica / Ica")
    ie_nombre = st.text_input("Institución Educativa:", "N° 22303 'Santa Rosa de Lima'")
with c2:
    director = st.text_input("Director:", "Lic. Bernardo Francisco Salcedo Barrientos")
    subdirector = st.text_input("Subdirector(es):", "Mg. Mariela Velásquez Cárdenas / Mg. Frank Bernaola Pérez")
with c3:
    docente = st.text_input("Docente de Aula:", "Sara María Quiroz Rodríguez")
    grado_seccion = st.selectbox("Grado y Sección:", ["1er Grado A", "2do Grado A", "3er Grado A", "4to Grado A", "5to Grado A", "6to Grado A"], index=2)

competencia_sel = ""
feriados_custom = ""
tabla_horario_md = ""
reglas_sesiones_diarias_md = ""

lista_areas_completa = [
    "Comunicación", "Matemática", "Personal Social", 
    "Ciencia y Tecnología", "Educación Religiosa", 
    "Arte y Cultura", "Educación Física", "Tutoría"
]
opciones_bloque3 = ["(Ninguna / Solo 2 áreas)"] + lista_areas_completa

def limpiar_texto_bloque3(val):
    if val == "(Ninguna / Solo 2 áreas)":
        return "--- (Solo 2 sesiones este día)"
    return val

def compilar_reglas_diarias(dias_lista):
    reglas = []
    for nombre_dia, a1, a2, a3 in dias_lista:
        if a3 == "(Ninguna / Solo 2 áreas)":
            reglas.append(
                f"  • **{nombre_dia} (OBLIGATORIO: EXACTAMENTE 2 SESIONES - PROHIBIDO COLOCAR SOLO 1 SESIÓN):**\n"
                f"      - Sesión 1 (90 min): **[{a1}]**: [Competencia específica] - [Actividad en 1ª persona plural]\n"
                f"      - Sesión 2 (90 min): **[{a2}]**: [Competencia específica] - [Actividad en 1ª persona plural]\n"
                f"      *(En {nombre_dia} DEBES redactar ambas sesiones completas: Sesión 1 de {a1} Y Sesión 2 de {a2}. No omitas ni fusiones ninguna)*"
            )
        else:
            reglas.append(
                f"  • **{nombre_dia} (OBLIGATORIO: EXACTAMENTE 3 SESIONES COMPLETAS):**\n"
                f"      - Sesión 1 (90 min): **[{a1}]**: [Competencia específica] - [Actividad en 1ª persona plural]\n"
                f"      - Sesión 2 (90 min): **[{a2}]**: [Competencia específica] - [Actividad en 1ª persona plural]\n"
                f"      - Sesión 3 (90 min): **[{a3}]**: [Competencia específica] - [Actividad en 1ª persona plural]"
            )
    return "\n".join(reglas)

if tipo_documento in ["Sesión de Aprendizaje", "Ficha de Aplicación / Trabajo (Para Alumnos)", "Afiche Educativo de la Sesión (Nano Banana)"]:
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        num_doc = st.text_input("N.° de Documento / Sesión / Ficha / Afiche:", "01")
    with f2:
        lista_areas = cneb.obtener_lista_areas()
        area_sel = st.selectbox("Área Curricular:", lista_areas if lista_areas else ["Personal Social", "Comunicación", "Matemática", "Ciencia y Tecnología"], index=0)
    with f3:
        fecha_sugerida = st.text_input("Fecha:", "05 de mayo de 2026")
    with f4:
        duracion_sesion = st.selectbox("Duración de la Sesión:", ["45 minutos", "90 minutos", "135 minutos"], index=1)
    
    # 🎯 JALA LAS COMPETENCIAS EN VIVO DESDE CNEB_PRIMARIA_DATOS.PY
    comps_disponibles = cneb.obtener_competencias(area_sel)
    if comps_disponibles:
        competencia_sel = st.selectbox("🎯 Competencia Oficial CNEB a desarrollar:", comps_disponibles, index=0)
    else:
        competencia_sel = ""

    fechas_duracion = fecha_sugerida
    duracion_semanas = 1

elif tipo_documento == "Proyecto de Aprendizaje":
    f1, f2, f3 = st.columns(3)
    with f1:
        num_doc = st.text_input("N.° de Proyecto:", "01")
    with f2:
        fechas_duracion = st.text_input("Fechas / Duración:", "Del 11 de marzo al 12 de abril de 2026 (4 Semanas)")
    with f3:
        duracion_semanas = st.slider("Número de Semanas del Proyecto:", min_value=2, max_value=5, value=4)
        area_sel = "Multidisciplinar"
        duracion_sesion = "90 minutos"

    # CUADRO DE HORARIOS DE ÁREAS POR CADA DÍA DE LA SEMANA (LUNES A VIERNES)
    st.markdown("""
    <div style="background-color: #ECFDF5; border: 1.5px solid #10B981; border-radius: 10px; padding: 10px 14px; margin-top: 14px; margin-bottom: 12px;">
        <span style="font-weight: 800; color: #065F46; font-size: 1.0rem;">🕒 CUADRO DE HORARIOS DE ÁREAS (DE LUNES A VIERNES - 2 A 3 ÁREAS POR DÍA)</span><br>
        <span style="font-size: 0.88rem; color: #047857;">Configura las áreas pedagógicas que se trabajarán cada día en turno único. Estas áreas determinarán de forma coherente la programación cronológica de actividades.</span>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_m, col_mi, col_j, col_v = st.columns(5)
    with col_l:
        st.markdown("**🟢 LUNES**")
        l_a1 = st.selectbox("Área 1:", lista_areas_completa, index=0, key="proy_l1")
        l_a2 = st.selectbox("Área 2:", lista_areas_completa, index=1, key="proy_l2")
        l_a3 = st.selectbox("Área 3 (opcional):", opciones_bloque3, index=3, key="proy_l3")
    with col_m:
        st.markdown("**🟢 MARTES**")
        m_a1 = st.selectbox("Área 1:", lista_areas_completa, index=1, key="proy_m1")
        m_a2 = st.selectbox("Área 2:", lista_areas_completa, index=0, key="proy_m2")
        m_a3 = st.selectbox("Área 3 (opcional):", opciones_bloque3, index=0, key="proy_m3")
    with col_mi:
        st.markdown("**🟢 MIÉRCOLES**")
        mi_a1 = st.selectbox("Área 1:", lista_areas_completa, index=0, key="proy_mi1")
        mi_a2 = st.selectbox("Área 2:", lista_areas_completa, index=2, key="proy_mi2")
        mi_a3 = st.selectbox("Área 3 (opcional):", opciones_bloque3, index=6, key="proy_mi3")
    with col_j:
        st.markdown("**🟢 JUEVES**")
        j_a1 = st.selectbox("Área 1:", lista_areas_completa, index=1, key="proy_j1")
        j_a2 = st.selectbox("Área 2:", lista_areas_completa, index=3, key="proy_j2")
        j_a3 = st.selectbox("Área 3 (opcional):", opciones_bloque3, index=0, key="proy_j3")
    with col_v:
        st.markdown("**🟢 VIERNES**")
        v_a1 = st.selectbox("Área 1:", lista_areas_completa, index=0, key="proy_v1")
        v_a2 = st.selectbox("Área 2:", lista_areas_completa, index=7, key="proy_v2")
        v_a3 = st.selectbox("Área 3 (opcional):", opciones_bloque3, index=8, key="proy_v3")

    feriados_custom = st.text_input(
        "📌 Feriados o Días No Laborables durante el período (Se indicarán al pie de este cuadro de horarios):",
        value="",
        placeholder="Ej: Jueves y Viernes Santo (02 y 03 de abril), 01 de Mayo. Si lo dejas vacío, la IA identificará feriados oficiales.",
        key="feriados_proy"
    )

    dias_proy = [
        ("LUNES", l_a1, l_a2, l_a3),
        ("MARTES", m_a1, m_a2, m_a3),
        ("MIÉRCOLES", mi_a1, mi_a2, mi_a3),
        ("JUEVES", j_a1, j_a2, j_a3),
        ("VIERNES", v_a1, v_a2, v_a3),
    ]
    reglas_sesiones_diarias_md = compilar_reglas_diarias(dias_proy)

    tabla_horario_md = f"""
| BLOQUE / HORA | LUNES | MARTES | MIÉRCOLES | JUEVES | VIERNES |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sesión 1 (90 min)** | {l_a1} | {m_a1} | {mi_a1} | {j_a1} | {v_a1} |
| **Sesión 2 (90 min)** | {l_a2} | {m_a2} | {mi_a2} | {j_a2} | {v_a2} |
| **Sesión 3 (90 min)** | {limpiar_texto_bloque3(l_a3)} | {limpiar_texto_bloque3(m_a3)} | {limpiar_texto_bloque3(mi_a3)} | {limpiar_texto_bloque3(j_a3)} | {limpiar_texto_bloque3(v_a3)} |
"""

else:  # Unidad SARA
    f1, f2, f3 = st.columns(3)
    with f1:
        num_doc = st.text_input("N.° de Unidad:", "01")
    with f2:
        fechas_duracion = st.text_input("Fechas / Duración:", "Del 01 de abril al 03 de mayo de 2026 (5 Semanas)")
    with f3:
        duracion_semanas = st.slider("Número de Semanas de la Unidad:", min_value=2, max_value=5, value=5)
        area_sel = "Multidisciplinar"
        duracion_sesion = "90 minutos"

    # CUADRO DE HORARIOS DE ÁREAS POR CADA DÍA DE LA SEMANA (LUNES A VIERNES)
    st.markdown("""
    <div style="background-color: #F5F3FF; border: 1.5px solid #8B5CF6; border-radius: 10px; padding: 10px 14px; margin-top: 14px; margin-bottom: 12px;">
        <span style="font-weight: 800; color: #5B21B6; font-size: 1.0rem;">🕒 CUADRO DE HORARIOS DE ÁREAS (DE LUNES A VIERNES - 2 A 3 ÁREAS POR DÍA)</span><br>
        <span style="font-size: 0.88rem; color: #6D28D9;">Configura las áreas pedagógicas que se trabajarán cada día en turno único. Estas áreas determinarán de forma coherente la programación cronológica de actividades.</span>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_m, col_mi, col_j, col_v = st.columns(5)
    with col_l:
        st.markdown("**🟣 LUNES**")
        l_a1 = st.selectbox("Área 1:", lista_areas_completa, index=0, key="uni_l1")
        l_a2 = st.selectbox("Área 2:", lista_areas_completa, index=1, key="uni_l2")
        l_a3 = st.selectbox("Área 3 (opcional):", opciones_bloque3, index=3, key="uni_l3")
    with col_m:
        st.markdown("**🟣 MARTES**")
        m_a1 = st.selectbox("Área 1:", lista_areas_completa, index=1, key="uni_m1")
        m_a2 = st.selectbox("Área 2:", lista_areas_completa, index=0, key="uni_m2")
        m_a3 = st.selectbox("Área 3 (opcional):", opciones_bloque3, index=0, key="uni_m3")
    with col_mi:
        st.markdown("**🟣 MIÉRCOLES**")
        mi_a1 = st.selectbox("Área 1:", lista_areas_completa, index=0, key="uni_mi1")
        mi_a2 = st.selectbox("Área 2:", lista_areas_completa, index=2, key="uni_mi2")
        mi_a3 = st.selectbox("Área 3 (opcional):", opciones_bloque3, index=6, key="uni_mi3")
    with col_j:
        st.markdown("**🟣 JUEVES**")
        j_a1 = st.selectbox("Área 1:", lista_areas_completa, index=1, key="uni_j1")
        j_a2 = st.selectbox("Área 2:", lista_areas_completa, index=3, key="uni_j2")
        j_a3 = st.selectbox("Área 3 (opcional):", opciones_bloque3, index=0, key="uni_j3")
    with col_v:
        st.markdown("**🟣 VIERNES**")
        v_a1 = st.selectbox("Área 1:", lista_areas_completa, index=0, key="uni_v1")
        v_a2 = st.selectbox("Área 2:", lista_areas_completa, index=7, key="uni_v2")
        v_a3 = st.selectbox("Área 3 (opcional):", opciones_bloque3, index=8, key="uni_v3")

    feriados_custom = st.text_input(
        "📌 Feriados o Días No Laborables durante el período (Se indicarán al pie de este cuadro de horarios):",
        value="",
        placeholder="Ej: Jueves y Viernes Santo (02 y 03 de abril), 01 de Mayo. Si lo dejas vacío, la IA identificará feriados oficiales.",
        key="feriados_uni"
    )

    dias_uni = [
        ("LUNES", l_a1, l_a2, l_a3),
        ("MARTES", m_a1, m_a2, m_a3),
        ("MIÉRCOLES", mi_a1, mi_a2, mi_a3),
        ("JUEVES", j_a1, j_a2, j_a3),
        ("VIERNES", v_a1, v_a2, v_a3),
    ]
    reglas_sesiones_diarias_md = compilar_reglas_diarias(dias_uni)

    tabla_horario_md = f"""
| BLOQUE / HORA | LUNES | MARTES | MIÉRCOLES | JUEVES | VIERNES |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sesión 1 (90 min)** | {l_a1} | {m_a1} | {mi_a1} | {j_a1} | {v_a1} |
| **Sesión 2 (90 min)** | {l_a2} | {m_a2} | {mi_a2} | {j_a2} | {v_a2} |
| **Sesión 3 (90 min)** | {limpiar_texto_bloque3(l_a3)} | {limpiar_texto_bloque3(m_a3)} | {limpiar_texto_bloque3(mi_a3)} | {limpiar_texto_bloque3(j_a3)} | {limpiar_texto_bloque3(v_a3)} |
"""

if tipo_documento in ["Sesión de Aprendizaje", "Ficha de Aplicación / Trabajo (Para Alumnos)", "Afiche Educativo de la Sesión (Nano Banana)"]:
    problema_contexto = st.text_input(
        "📌 Tema / Título de la Actividad, Ficha de Trabajo o Afiche:",
        value="Mis derechos y deberes"
    )
    titulo_opcional = ""
else:
    problema_contexto = st.text_area(
        "🚨 Problema, Situación Significativa o Actividades Propuestas (Puedes colocar tu Situación Significativa / Actividades completas para que la IA las respete, o escribir solo el problema de contexto para que la IA las genere automáticamente):",
        height=130,
        value="Poco hábito de recolección de residuos sólidos y acumulación de botellas de plástico en el patio durante el recreo por parte de los estudiantes de 3er grado."
    )
    titulo_opcional = st.text_input("Título Opcional (Déjalo en blanco si deseas que la IA cree un título creativo automático):", value="")

# ==============================================================================
# PROMPTS MAESTROS COMPLETOS ALINEADOS AL CNEB
# ==============================================================================
def generar_prompt_sesion():
    if "45" in duracion_sesion:
        t_inicio, t_desarrollo, t_cierre = "10 min", "30 min", "5 min"
    elif "135" in duracion_sesion:
        t_inicio, t_desarrollo, t_cierre = "20 min", "100 min", "15 min"
    else:
        t_inicio, t_desarrollo, t_cierre = "20 min", "60 min", "10 min"

    # 🔗 JALA EN VIVO LOS DATOS OFICIALES DE CNEB_PRIMARIA_DATOS.PY
    estandar_oficial = cneb.obtener_estandar(area_sel, competencia_sel, grado_seccion)
    desempenos_oficiales = cneb.obtener_desempenos(area_sel, competencia_sel, grado_seccion)
    capacidades_oficiales = cneb.obtener_capacidades(area_sel, competencia_sel)

    desempenos_texto = "\n".join([f"  • {d}" for d in desempenos_oficiales]) if desempenos_oficiales else "  • Desempeño oficial del grado según CNEB."
    capacidades_texto = ", ".join(capacidades_oficiales) if capacidades_oficiales else "Capacidades oficiales de la competencia seleccionada"

    return f"""
Actúa como: Actúa como un docente especialista y planificador curricular del sistema educativo peruano, con dominio del Currículo Nacional de la Educación Básica (CNEB), la planificación por competencias, la evaluación formativa, el Diseño Universal para el Aprendizaje (DUA) y la normativa vigente del MINEDU. Tu función es automatizar la elaboración de sesiones de aprendizaje completos, coherentes, contextualizados y listos para ser utilizados en instituciones educativas públicas y privadas del Perú.
Tu objetivo: Elaborar una propuesta profesional, manteniendo coherencia entre competencias, capacidades, desempeños, criterios de evaluación, evidencias e instrumentos, respetando la estructura establecida por el CNEB.

Datos para la sesión (Configuración):
• Grado y Sección: {grado_seccion}
• Área Curricular: {area_sel}
• Competencia Seleccionada: {competencia_sel}
• Tema/Título de la sesión: {problema_contexto}
• Fecha sugerida: {fecha_sugerida}
• DRE / UGEL: {dre_ugel}
• Institución Educativa: {ie_nombre}
• Director: {director}
• Subdirector(es): {subdirector}
• Docente de Aula: {docente}
• Duración Total: {duracion_sesion}

INFORMACIÓN CURRICULAR OFICIAL JALADA DE CNEB_PRIMARIA_DATOS (OBLIGATORIO UTILIZAR):
• CAPACIDADES OFICIALES: {capacidades_texto}
• ESTÁNDAR DE APRENDIZAJE ÍNTEGRO (Copia este texto completo e idéntico en la sección correspondiente sin resumir ni alterar, resaltando en **negrita** únicamente el fragmento trabajado):
"{estandar_oficial}"

• BANCO DE DESEMPEÑOS OFICIALES PARA {grado_seccion.upper()}:
{desempenos_texto}
(Selecciona de este banco el desempeño oficial más pertinente para '{problema_contexto}' y resalta en **negrita** la precisión contextualizada).

INSTRUCCIONES DE FORMATO Y CONTENIDO (OBLIGATORIO):
1. FORMATO: Estructura toda la respuesta en Markdown limpio con tablas estándar. PROHIBIDO USAR CÓDIGO O ETIQUETAS HTML (no uses <table>, <tr>, <td>, <br>).
2. ESTÁNDAR DE APRENDIZAJE ÍNTEGRO: Copia el texto completo del estándar de ciclo tal cual figura en CNEB sin cortar ni resumir ni alterar ninguna palabra del ciclo correspondiente. Resalta en **negrita** únicamente el fragmento que se trabaja directamente en esta sesión.
3. DESEMPEÑO OFICIAL: Extrae el desempeño oficial del grado ({grado_seccion}) tal cual figura en el cneb, resaltando en **negrita** la precisión contextualizada al tema.
4. CRITERIOS DE EVALUACIÓN: Redacta de 2 a 3 criterios con la fórmula: Acción + Contenido + Condición.
5. ENFOQUE DUA: Incluye obligatoriamente la tabla con las 3 dimensiones: Múltiples formas de representación, Múltiples formas de acción/expresión y Múltiples formas de compromiso.
6. PROCESOS DIDÁCTICOS DEL ÁREA: En el momento del Desarrollo, conduce la clase utilizando obligatoriamente los procesos didácticos oficiales del área de {area_sel}, redactando en primera persona del plural (tiempo presente).
7. PAUSA ACTIVA OBLIGATORIA: Incluye dentro del Desarrollo un recuadro destacado de 2 minutos con ejercicios físicos o lúdicos de estiramiento.
8. INSTRUMENTO CON CALIFICACIÓN A, B, C: Genera una tabla de evaluación con columnas para estudiantes y criterios desglosados en niveles literales de primaria: A, B y C.

ESTRUCTURA DE SALIDA REQUERIDA:
# **SESIÓN DE APRENDIZAJE Nº {num_doc}**
## **{problema_contexto.upper()}**

• I. DATOS INFORMATIVOS:
| DATOS INFORMATIVOS | DETALLE / INFORMACIÓN |
| :--- | :--- |
| Institución Educativa | {ie_nombre} |
| Docente de Aula | {docente} |
| Grado y Sección | {grado_seccion} |
| Área Curricular | {area_sel} |
| Fecha | {fecha_sugerida} |
| Duración | {duracion_sesion} |

• II: PROPÓSITOS DE APRENDIZAJE Y EVIDENCIAS
(Genera una tabla markdown detallada con las siguientes columnas):
| Área, competencias y capacidades | Copia el desempeño completo resaltando en negrita la parte precisada (CNEB) | Criterios de evaluación (2 a 3 claros y medibles) |
| :--- | :--- | :--- |
| **{area_sel}**<br>• **{competencia_sel}**<br>• {capacidades_texto} | [Copia el desempeño oficial elegido resaltando en **negrita** la parte precisada] | 1. [Acción + Contenido + Condición]<br>2. [Criterio 2]<br>3. [Criterio 3] |

Debajo de la tabla, incluye de forma independiente y clara:
|Propósito | [Redacta en un párrafo corto qué aprenderán hoy los estudiantes y bajo qué contexto en lenguaje infantil y claro]|
| :--- | :--- |
|Evidencia de aprendizaje | [Define un producto o actuación tangible que realizarán los alumnos para demostrar su aprendizaje]|
| :--- | :--- |
|Instrumento de evaluación | [Escala valorativa / Lista de cotejo con niveles A, B, C] |
| :--- | :--- |
|Estándar de aprendizaje | [Copia el estándar de aprendizaje completo e íntegro sin cortar ni alterar ni resumir ninguna palabra del ciclo correspondiente según el CNEB: "{estandar_oficial}", resaltando en **negrita únicamente el fragmento que se trabaja directamente en la sesión**]|
| :--- | :--- |

• III. ENFOQUE DUA APLICADO:
| Dimensión | Estrategia aplicada en la sesión |
| :--- | :--- |
| **Múltiples formas de representación** | [Detalla cómo se presentará la información de forma visual, auditiva, concreta o textual] |
| **Múltiples formas de acción y expresión** | [Detalla las opciones diferenciadas que tendrán los alumnos para demostrar lo aprendido] |
| **Múltiples formas de compromiso** | [Explica cómo se motivará, conectará con sus intereses y mantendrá el foco de los estudiantes] |

• IV: ENFOQUES TRANSVERSALES
| ENFOQUE TRANSVERSAL | VALORES | ACTITUDES OBSERVABLES |

• V: COMPETENCIA TRANSVERSAL
| COMPETENCIA TRANSVERSAL | CAPACIDADES | DESEMPEÑOS PRECISADOS |

• VI: PREPARACIÓN DE LA SESIÓN
| ¿Qué necesitamos hacer antes de la sesión? | ¿Qué recursos o materiales se utilizarán en esta sesión? |

• VII: SECUENCIA DIDÁCTICA
#### **INICIO (Tiempo aproximado: {t_inicio})**
• **Actividad permanente:** Saludo cordial, control de asistencia, soporte socioemocional y oración del día.
• **Motivación y Saberes Previos:** [Plantea una dinámica lúdica breve, canción, imagen misteriosa o juego que active vivencias previas y capte la atención de los niños de {grado_seccion}].
• **Conflicto cognitivo:** [Pregunta retadora y abierta que los haga reflexionar y dudar constructivamente].
• **Presentación:** Comunicamos explícitamente el Propósito de la sesión y los Criterios con los que serán evaluados en lenguaje cercano.
• **Acuerdos:** Establecemos juntos 2 o 3 normas de convivencia clave para la jornada.

#### **DESARROLLO (Tiempo aproximado: {t_desarrollo})**
(Desarrolla esta sección aplicando los PROCESOS DIDÁCTICOS OFICIALES del área de {area_sel}: por ejemplo, si es Ciencia y Tecnología usa: Planteamiento del problema, Planteamiento de hipótesis, Elaboración del plan de acción, Recojo de datos y análisis de resultados, Estructuración del saber construido y Evaluación/Comunicación; si es Personal Social: Problematización, Análisis de la información y Toma de decisiones; si es Comunicación o Matemática usa sus respectivos procesos oficiales). Redacta en primera persona del plural de forma narrativa y viva las acciones del docente y las respuestas/participación activa de los niños.

> 🏃‍♂️ **PAUSA ACTIVA (2 minutos):** [Describe aquí una rutina breve de 2 minutos con ejercicios de respiración, estiramiento lúdico o juego corporal motor para recargar energía y recuperar la concentración de los niños].

(Continúa con el cierre de los procesos didácticos del área, la consolidación y la elaboración de la evidencia).

#### **CIERRE (Tiempo aproximado: {t_cierre})**
• **Sistematización:** Construimos junto a los estudiantes la idea fuerza o conclusión central en la pizarra o papelote.
• **Metacognición:** Formulamos 4 a 5 preguntas directas de autorreflexión:
  - ¿Qué aprendimos el día de hoy?
  - ¿Cómo lo aprendimos y qué pasos seguimos?
  - ¿Qué dificultades tuvimos y cómo las superamos?
  - ¿Para qué nos servirá lo aprendido en nuestra vida diaria?
• **Despedida:** Felicitamos calurosamente a los estudiantes por su participación y esfuerzo en la sesión.

• VII: INSTRUMENTO DE EVALUACIÓN (30 alumnos ficticios)
| Area: {area_sel} | Grado y Sección: {grado_seccion} | Fecha: {fecha_sugerida} |
| Competencia: {competencia_sel} | Capacidad: {capacidades_texto} | Evidencia: Evidencia de aprendizaje de la sesión |
"""

def generar_prompt_ficha_trabajo():
    return f"""
Actúa como: Especialista en Educación Primaria (CNEB - MINEDU Perú) y diseñador experto de material educativo impreso.
Elabora una FICHA DE TRABAJO / APLICACIÓN PARA EL ESTUDIANTE sobre {problema_contexto} para {grado_seccion} en el área de {area_sel}.

ESTRUCTURA DE SALIDA REQUERIDA (MARKDOWN PURA EN TABLAS):
# **FICHA DE TRABAJO DE {area_sel.upper()} N.º {num_doc}**
## **{problema_contexto.upper()}**

## **DATOS INFORMATIVOS**
| DATOS INFORMATIVOS | DETALLE / INFORMACIÓN |
| Institución Educativa | {ie_nombre} |
| Grado y Sección | {grado_seccion} |
| Área Curricular | {area_sel} |
| Docente de Aula | {docente} |
| Fecha | {fecha_sugerida} |
| Estudiante | __________________________________________________ |

## **PROPÓSITO DE HOY**
[Propósito amigable para el estudiante]

• SECCIÓN 1: "ME PREPARO Y DESCUBRO"
• SECCIÓN 2: "MANOS A LA OBRA / APLICO LO APRENDIDO"
• SECCIÓN 3: "MI RETO FINAL / MI COMPROMISO"

• TABLA II: AUTOEVALUACIÓN DE MIS LOGROS
"""

def generar_prompt_proyecto():
    val_titulo = f'"{titulo_opcional}"' if titulo_opcional.strip() else 'Crea un TÍTULO innovador y creativo para el proyecto basado en el problema.'
    info_feriados = f"Feriados o días no laborables indicados por el docente: {feriados_custom}" if feriados_custom.strip() else f"Identifica los feriados oficiales del calendario escolar peruano MINEDU que correspondan al período de fechas: {fechas_duracion}."

    return f"""
Actúa como un docente especialista de Primaria MINEDU Perú. Elabora un PROYECTO DE APRENDIZAJE completo.
PROHIBIDO usar símbolos #### o ##### y etiquetas HTML. Usa Markdown limpio y estructura strictly en TABLAS Y CUADROS.

A PARTIR DEL PROBLEMA DEL CONTEXTO DEL DOCENTE:
{problema_contexto}

CUADRO DE HORARIOS DE ÁREAS DEFINIDO POR EL DOCENTE EN LA PLATAFORMA (DE LUNES A VIERNES):
{tabla_horario_md}

FERIADOS SEÑALADOS DEL PERÍODO:
{info_feriados}

OBLIGATORIO - GENERACIÓN AUTOMÁTICA DE TÍTULO Y SITUACIÓN SIGNIFICATIVA:
1. Genera un TÍTULO del proyecto: {val_titulo}
2. Redacta la SITUACIÓN SIGNIFICATIVA COMPLETA estructurada en 3 párrafos.

ORDEN ESTRUCTURAL ESTRICTO DE SALIDA (Sigue exactamente esta secuencia):

1. ENCABEZADO Y TABLA I: DATOS INFORMATIVOS (Muestra exactamente: DRE/UGEL: {dre_ugel}, IE: {ie_nombre}, Director: {director}, Subdirector: {subdirector}, Docente: {docente}, Grado/Sección: {grado_seccion}, Duración: {fechas_duracion}).

2. SITUACIÓN SIGNIFICATIVA GENERADA (Ubicada OBLIGATORIAMENTE justo debajo de los Datos Informativos).

3. PLANIFICACIÓN DEL PROYECTO CON LOS ESTUDIANTES (Tabla: ¿Qué haremos?, ¿Qué sabemos?, ¿Qué queremos saber?, ¿Cómo lo haremos?, ¿Qué necesitamos?, ¿Cómo nos organizamos?).

4. MATRIZ DE PROPÓSITOS DE APRENDIZAJE (UN SOLO CUADRO UNIFICADO PARA TODAS LAS SEMANAS):
   🚨 REGLA CRÍTICA OBLIGATORIA DE TABLA ÚNICA (NO SEPARAR POR SEMANAS):
   - Presenta TODA esta matriz en UN SOLO CUADRO / UNA SOLA TABLA INTEGRADA Y CONTINUA para todo el proyecto ({duracion_semanas} semanas).
   - QUEDA TERMINANTEMENTE PROHIBIDO CORTAR, FRAGMENTAR O DIVIDIR LA MATRIZ EN CUADROS SEPARADOS POR CADA SEMANA (No hagas una tabla para la semana 1, otra tabla para la semana 2, etc.).
   - En este ÚNICO cuadro, organiza las filas por ÁREA y COMPETENCIA.
   
   🚨 REGLA CRÍTICA PARA LA COLUMNA "ACTIVIDADES SUGERIDAS" (DESGLOSE SEMANAL OBLIGATORIO):
   - EN ESTA COLUMNA ESTÁ ESTRICTAMENTE PROHIBIDO COLOCAR UNA SOLA ACTIVIDAD GENÉRICA.
   - Para cada área y competencia, DEBES colocar obligatoriamente las actividades sugeridas específicas a realizar en CADA UNA de las {duracion_semanas} semanas, usando viñetas desglosadas:
     • **Semana 1:** [Actividad sugerida de la semana 1]
     • **Semana 2:** [Actividad sugerida de la semana 2]
     • **Semana 3:** [Actividad sugerida de la semana 3]
     • **Semana 4:** [Actividad sugerida de la semana 4]
     (y Semana 5 si aplica).

   🚨 REGLA CRÍTICA DE CORRESPONDENCIA DIRECTA: UN CRITERIO DE EVALUACIÓN POR CADA ACTIVIDAD SUGERIDA:
   - EN LA COLUMNA DE CRITERIOS DE EVALUACIÓN, DEBES REDACTAR OBLIGATORIAMENTE UN CRITERIO DE EVALUACIÓN POR CADA ACTIVIDAD SUGERIDA DE CADA SEMANA (correspondencia exacta 1 a 1):
     • **Para la Actividad Sugerida 1 (Semana 1):** [Criterio de evaluación específico...]
     • **Para la Actividad Sugerida 2 (Semana 2):** [Criterio de evaluación específico...]
     • **Para la Actividad Sugerida 3 (Semana 3):** [Criterio de evaluación específico...]
     • **Para la Actividad Sugerida 4 (Semana 4):** [Criterio de evaluación específico...]
     (y Semana 5 si aplica).
     *(Fórmula de cada criterio: Verbo de acción + Contenido disciplinar + Condición/Contexto)*
   
   - Presenta la Matriz en sus 8 COLUMNAS EXACTAS dentro de la TABLA ÚNICA:
     | ÁREA | COMPETENCIA Y CAPACIDADES | ESTÁNDAR DE APRENDIZAJE | DESEMPEÑO PRECISADO | CRITERIOS DE EVALUACIÓN (POR CADA ACTIVIDAD SUGERIDA) | ACTIVIDADES SUGERIDAS (SEMANA A SEMANA) | EVIDENCIA | INSTRUMENTO DE EVALUACIÓN |
   - REGLA OBLIGATORIA DEL ESTÁNDAR: Copia el **ESTÁNDAR DE APRENDIZAJE EN SU TOTALIDAD Y DE MANERA ÍNTEGRA** tal cual figura en el CNEB oficial (RM N.º 649-2016-MINEDU) sin ningún corte ni resumen, y RESALTA EN **NEGRITA** (`**la parte específica movilizada en la actividad**`).
   - Copia el DESEMPEÑO ÍNTEGRO del CNEB con la parte trabajada en **negrita**.
   - REGLA OBLIGATORIA DE COBERTURA DE ÁREAS EN LA MATRIZ: Debes incluir OBLIGATORIAMENTE filas para TODAS Y CADA UNA DE LAS ÁREAS CURRICULARES SIN EXCEPCIÓN: Comunicación (3 comp.), Matemática (4 comp.), Personal Social, Ciencia y Tecnología, Educación Religiosa, Arte y Cultura, Educación Física y Tutoría / Competencias Transversales.

5. CUADRO DE HORARIOS DE ÁREAS POR DÍA DE LA SEMANA (LUNES A VIERNES) Y FERIADOS DEL PERÍODO:
   - Presenta el cuadro / tabla con la **DISTRIBUCIÓN DEL HORARIO SEMANAL DE ÁREAS** a utilizar de lunes a viernes en turno único:
{tabla_horario_md}
   - **INDICACIÓN DE FERIADOS EN LA PARTE DE ABAJO DE ESTE CUADRO:**
     Justo debajo de esta tabla de horarios, agrega un recuadro o texto destacado titulado:
     `📌 FERIADOS Y DÍAS NO LABORABLES DEL PERÍODO ({fechas_duracion}):`
     ({info_feriados})
     Indica la fecha exacta y la conmemoración/festividad de cada feriado comprendido en el proyecto. Si no hubiese ningún feriado en ese periodo, indícalo expresamente.

6. SECUENCIA DE ACTIVIDADES CON LOS DÍAS COMO COLUMNAS DE TABLA (PROGRAMACIÓN CRONOLÓGICA SEMANAL):
   - Presenta esta sección OBLIGATORIAMENTE AL TÉRMINO DEL CUADRO DE HORARIOS.
   - Para cada semana (Semana 1 a {duracion_semanas}), coloca el **TÍTULO DE LA SEMANA** y crea una TABLA OBLIGATORIA donde LAS COLUMNAS SEAN LOS DÍAS DE LA SEMANA:
     | LUNES | MARTES | MIÉRCOLES | JUEVES | VIERNES |

   🚨 REGLA ESTRICTA CONTRA LA OMISIÓN DE SESIONES (CERO RESÚMENES):
   En cada día de la semana DEBES generar exactamente las sesiones que el docente fijó en su horario:
{reglas_sesiones_diarias_md}

   ⚠️ ADVERTENCIA CRÍTICA:
   Si el Martes o Jueves tienen 2 áreas programadas, DEBES REDACTAR OBLIGATORIAMENTE LAS DOS SESIONES COMPLETAS:
   • Sesión 1 (90 min): **[Primera Área]**: [Competencia específica] - [Actividad en 1ª persona plural]
   • Sesión 2 (90 min): **[Segunda Área]**: [Competencia específica] - [Actividad en 1ª persona plural]
   ¡ESTÁ TOTALMENTE PROHIBIDO EMITIR SOLO UNA SESIÓN EN DÍAS DE DOS ÁREAS! El docente configuró dos áreas para esos días y ambas sesiones deben figurar obligatoriamente en cada casilla de martes y jueves.
   
   - REGLA DE FERIADOS: Si en el cronograma semanal coincide un día feriado de los indicados al pie del cuadro de horarios, en la columna correspondiente a ese día coloca claramente: **`FERIADO / DÍA NO LABORABLE: [Nombre del feriado]`**, sin programar sesiones curriculares dicho día.

7. TABLA DE ENFOQUES TRANSVERSALES.
8. PRODUCTO FINAL TANGIBLE DEL PROYECTO.
9. LISTA CLASIFICADA DE MATERIALES Y RECURSOS.
10. TABLA VIII: REFLEXIONES SOBRE LOS APRENDIZAJES (Tabla final obligatoria).
"""

def generar_prompt_unidad_sara():
    val_titulo = f'"{titulo_opcional}"' if titulo_opcional.strip() else 'Crea un TÍTULO motivador para la Unidad de Aprendizaje basado en el contexto/problema.'
    info_feriados = f"Feriados o días no laborables indicados por el docente: {feriados_custom}" if feriados_custom.strip() else f"Identifica los feriados oficiales del calendario escolar peruano MINEDU que correspondan al período de fechas: {fechas_duracion}."

    return f"""
Actúa como docente especialista de Primaria MINEDU Perú. Elabora una UNIDAD DE APRENDIZAJE completa y detallada (Modelo SARA).
PROHIBIDO usar símbolos #### o ##### y etiquetas HTML. Usa Markdown limpio y estructura strictly en TABLAS Y CUADROS.

ENTRADA PROVISTA POR EL DOCENTE (PROBLEMA DE CONTEXTO, SITUACIÓN SIGNIFICATIVA COMPLETA Y/O ACTIVIDADES PROPUESTAS):
{problema_contexto}

CUADRO DE HORARIOS DE ÁREAS DEFINIDO POR EL DOCENTE EN LA PLATAFORMA (DE LUNES A VIERNES):
{tabla_horario_md}

FERIADOS SEÑALADOS DEL PERÍODO:
{info_feriados}

REGLA DE PROCESAMIENTO DE LA SITUACIÓN SIGNIFICATIVA Y ACTIVIDADES:
1. SI EL DOCENTE INGRESÓ UNA SITUACIÓN SIGNIFICATIVA COMPLETA O ACTIVIDADES ESPECÍFICAS: Utiliza, respeta y adapta fielmente dicho texto e ideas dentro de la sección "II. SITUACIÓN (RETO)" y en la matriz curricular.
2. SI EL DOCENTE SOLO INGRESÓ UN PROBLEMA O INTERÉS DEL CONTEXTO BREVE: La IA debe GENERAR AUTOMÁTICAMENTE la Situación Significativa completa estructurada en 3 párrafos (Párrafo 1: Diagnóstico de la problemática local/nacional; Párrafo 2: Propuesta pedagógica e integración de áreas; Párrafo 3: Interrogantes retadoras y desafíos) y articular las actividades sugeridas correspondientes.

ORDEN ESTRUCTURAL ESTRICTO DE SALIDA (Sigue exactamente esta secuencia):

UNIDAD DE APRENDIZAJE N.º {num_doc}
{val_titulo}

I. DATOS GENERALES (Muestra exactamente: DRE/UGEL: {dre_ugel}, IE: {ie_nombre}, Director: {director}, Subdirector: {subdirector}, Docente: {docente}, Grado/Sección: {grado_seccion}, Fechas y Duración: {fechas_duracion}, Duración en Semanas: {duracion_semanas} semanas).

II. SITUACIÓN (RETO):
(Muestra la SITUACIÓN SIGNIFICATIVA provista por el docente o la generada automáticamente por la IA con sus 3 párrafos y retos justo debajo de los Datos Generales).

III. ENFOQUES TRANSVERSALES:
| ENFOQUE TRANSVERSAL | VALOR | ACTITUD |

IV. ACTIVIDADES PERTINENTES AL PROPÓSITO DE APRENDIZAJE:
(Presenta una lista ordenada de las grandes actividades pedagógicas planificadas por semana, respetando las propuestas por el docente si las incluyó).

V. PROPÓSITO DE APRENDIZAJE, CRITERIOS DE EVALUACIÓN Y ACTIVIDADES SUGERIDAS (MATRIZ DE APRENDIZAJES POR ÁREA):
   🚨 REGLA CRÍTICA OBLIGATORIA DE TABLA ÚNICA (UN SOLO CUADRO PARA TODA LA UNIDAD - NO SEPARAR POR SEMANAS):
   - Presenta TODA la matriz curricular en UN SOLO CUADRO / UNA SOLA TABLA INTEGRADA Y CONTINUA para toda la unidad ({duracion_semanas} semanas).
   - QUEDA TERMINANTEMENTE PROHIBIDO CORTAR, SEPARAR O FRAGMENTAR LA MATRIZ EN CUADROS INDIVIDUALES POR SEMANA (No pongas una tabla para la semana 1, otra tabla para la semana 2, otra para la semana 3, etc.).
   - En este ÚNICO cuadro, organiza las filas agrupando por ÁREA y COMPETENCIA.

   🚨 REGLA CRÍTICA OBLIGATORIA PARA LA COLUMNA "ACTIVIDADES SUGERIDAS" (DESGLOSE SEMANAL OBLIGATORIO):
   - EN LA COLUMNA DE ACTIVIDADES SUGERIDAS ESTÁ ESTRICTAMENTE PROHIBIDO COLOCAR UNA SOLA ACTIVIDAD GENÉRICA.
   - Para cada área y competencia, DEBES colocar obligatoriamente las actividades sugeridas específicas a realizar en CADA UNA de las {duracion_semanas} semanas, redactadas de forma clara y explícita usando viñetas desglosadas:
     • **Semana 1:** [Nombre o descripción de la actividad sugerida de la semana 1]
     • **Semana 2:** [Nombre o descripción de la actividad sugerida de la semana 2]
     • **Semana 3:** [Nombre o descripción de la actividad sugerida de la semana 3]
     • **Semana 4:** [Nombre o descripción de la actividad sugerida de la semana 4]
     (y **Semana 5:** [Actividad sugerida de la semana 5] si la unidad dura 5 semanas).

   🚨 REGLA CRÍTICA DE CORRESPONDENCIA DIRECTA: UN CRITERIO DE EVALUACIÓN POR CADA ACTIVIDAD SUGERIDA:
   - EN LA COLUMNA DE CRITERIOS DE EVALUACIÓN, DEBES FORMULAR OBLIGATORIAMENTE UN CRITERIO DE EVALUACIÓN ESPECÍFICO POR CADA ACTIVIDAD SUGERIDA DE CADA SEMANA, en estricta correspondencia 1 a 1:
     • **Para la Actividad Sugerida 1 (Semana 1):** [Criterio de evaluación específico para la actividad de la semana 1]
     • **Para la Actividad Sugerida 2 (Semana 2):** [Criterio de evaluación específico para la actividad de la semana 2]
     • **Para la Actividad Sugerida 3 (Semana 3):** [Criterio de evaluación específico para la actividad de la semana 3]
     • **Para la Actividad Sugerida 4 (Semana 4):** [Criterio de evaluación específico para la actividad de la semana 4]
     (y **Semana 5:** [Criterio específico para la actividad sugerida de la semana 5] si la unidad dura 5 semanas).
     *(Fórmula de cada criterio: Verbo de acción + Contenido disciplinar + Condición o contexto)*
   
   - Presenta la Matriz Curricular en sus 8 COLUMNAS EXACTAS dentro de la TABLA ÚNICA:
     | ÁREA | COMPETENCIA Y CAPACIDADES | ESTÁNDAR DE APRENDIZAJE | DESEMPEÑO PRECISADO | CRITERIOS DE EVALUACIÓN (POR CADA ACTIVIDAD SUGERIDA) | ACTIVIDADES SUGERIDAS (SEMANA A SEMANA) | EVIDENCIA | INSTRUMENTO DE EVALUACIÓN |
   
   - REGLA CRÍTICA OBLIGATORIA PARA MATEMÁTICA Y COMUNICACIÓN:
     1. En el área de MATEMÁTICA debes abordar e incluir OBLIGATORIAMENTE LAS 4 COMPETENCIAS del CNEB distribuida a lo largo de la unidad:
        - Resuelve problemas de cantidad.
        - Resuelve problemas de regularidad, equivalencia y cambio.
        - Resuelve problemas de forma, movimiento y localización.
        - Resuelve problemas de gestión de datos e incertidumbre.
     2. En el área de COMUNICACIÓN debes abordar e incluir OBLIGATORIAMENTE LAS 3 COMPETENCIAS del CNEB distribuida a lo largo de la unidad:
        - Se comunica oralmente en su lengua materna.
        - Lee diversos tipos de textos escritos en su lengua materna.
        - Escribe diversos tipos de textos en su lengua materna.

   - REGLA STRICTA Y ABSOLUTA PARA EL ESTÁNDAR DE APRENDIZAJE:
     1. El Estándar de Aprendizaje del ciclo correspondiente debe escribirse TAL CUAL figura de forma oficial en el CNEB  (RM N.º 649-2016-MINEDU).
     2. Queda STRICTAMENTE PROHIBIDO modificar, parafrasear, resumir, cortar u omitir cualquier parte del texto del estándar. Debe incluirse el texto completo e íntegro del estándar del ciclo.
     3. ÚNICAMENTE debes resaltar en NEGRITA (`**texto en negrita**`) el fragmento o porción específica del estándar que se está abordando o movilizando en esa actividad. El resto del texto del estándar debe permanecer en texto plano normal.

   - REGLA STRICTA Y ABSOLUTA PARA EL DESEMPEÑO:
     1. El Desempeño correspondiente al grado debe escribirse TAL CUAL figura de forma oficial en el Programa Curricular de Educación Primaria del CNEB.
     2. Queda STRICTAMENTE PROHIBIDO resumir, omitir o recortar el texto del desempeño. Debe redactarse de manera completa e íntegra.
     3. ÚNICAMENTE debes resaltar en NEGRITA (`**texto precisado**`) la precisión del desempeño o la porción específica que se está trabajando directamente en la actividad. El resto del desempeño debe permanecer en texto plano normal.
   
   - REGLA OBLIGATORIA DE COBERTURA DE ÁREAS EN LA MATRIZ: En la matriz debes incluir OBLIGATORIAMENTE filas para TODAS Y CADA UNA DE LAS ÁREAS CURRICULARES SIN EXCEPCIÓN: Comunicación (3 competencias), Matemática (4 competencias), Personal Social, Ciencia y Tecnología, Educación Religiosa, Arte y Cultura, Educación Física y Tutoría / Competencias Transversales.

VI. TUTORÍA Y EDUCACIÓN EDUCATIVA:
| DIMENSIÓN | SESIÓN | ¿QUÉ BUSCAMOS? |

VII. COMPETENCIAS TRANSVERSALES:
(Presenta obligatoriamente esta sección en un CUADRO / TABLA con las competencias transversales oficiales del CNEB, sus capacidades y desempeños precisados correspondientes a {grado_seccion}):
| COMPETENCIA TRANSVERSAL | CAPACIDADES | DESEMPEÑOS PRECISADOS |
| :--- | :--- | :--- |
| **Se desenvuelve en los entornos virtuales generados por las TIC** | • Personaliza entornos virtuales.<br>• Gestiona información del entorno virtual.<br>• Interactúa en entornos virtuales.<br>• Crea objetos virtuales en diversos formatos. | [Copia el desempeño oficial de esta competencia para {grado_seccion}, resaltando en negrita la precisión contextualizada a la unidad] |
| **Gestiona su aprendizaje de manera autónoma** | • Define metas de aprendizaje.<br>• Organiza acciones estratégicas para alcanzar sus metas de aprendizaje.<br>• Monitorea y ajusta su desempeño durante el proceso de aprendizaje. | [Copia el desempeño oficial de esta competencia para {grado_seccion}, resaltando en negrita la precisión contextualizada a la unidad] |

VIII. CUADRO DE HORARIOS DE ÁREAS POR DÍA DE LA SEMANA (LUNES A VIERNES) Y FERIADOS DEL PERÍODO:
   - Presenta el cuadro / tabla con la **DISTRIBUCIÓN DEL HORARIO SEMANAL DE ÁREAS** a utilizar de lunes a viernes en turno único:
{tabla_horario_md}
   - **INDICACIÓN DE FERIADOS EN LA PARTE DE ABAJO DE ESTE CUADRO:**
     Justo al pie de esta tabla de horarios, agrega un recuadro o detalle titulado:
     `📌 FERIADOS Y DÍAS NO LABORABLES DEL PERÍODO ({fechas_duracion}):`
     ({info_feriados})
     Indica las fechas y conmemoraciones de feriados en el periodo de la unidad. Si no hubiese feriados, déjalo constar expresamente.

IX. PROGRAMACIÓN DE ACTIVIDADES / SECUENCIA CRONOLÓGICA DE ACTIVIDADES SUGERIDAS (SEMANA A SEMANA):
   - Presenta esta sección OBLIGATORIAMENTE AL TÉRMINO DEL CUADRO DE HORARIOS.
   - Para cada semana (Semana 1 a {duracion_semanas}), coloca el **TÍTULO DE LA SEMANA** y crea una TABLA OBLIGATORIA donde LAS COLUMNAS SEAN LOS DÍAS DE LA SEMANA:
     | LUNES | MARTES | MIÉRCOLES | JUEVES | VIERNES |

   🚨 REGLA ESTRICTA CONTRA LA OMISIÓN DE SESIONES (CERO RESÚMENES):
   En cada día de la semana DEBES generar exactamente las sesiones que el docente fijó en su horario:
{reglas_sesiones_diarias_md}

   ⚠️ ADVERTENCIA CRÍTICA:
   Si el Martes o Jueves tienen 2 áreas programadas, DEBES REDACTAR OBLIGATORIAMENTE LAS DOS SESIONES COMPLETAS:
   • Sesión 1 (90 min): **Primera Área**:  (Actividad en 1ª persona plural)
   • Sesión 2 (90 min): **Segunda Área**: (Actividad en 1ª persona plural)
   ¡ESTÁ TOTALMENTE PROHIBIDO EMITIR SOLO UNA SESIÓN EN DÍAS DE DOS ÁREAS! El docente configuró dos áreas para esos días y ambas sesiones deben figurar obligatoriamente en cada casilla de martes y jueves.

   - REGLA DE FERIADOS: Si en algún día de la semana coincide un feriado señalado en la sección anterior, consigna en su casilla: **`FERIADO / DÍA NO LABORABLE: [Nombre del feriado]`**, omitiendo el desarrollo de sesiones en dicha fecha para mantener coherencia total.

X. MATERIALES BÁSICOS Y RECURSOS A UTILIZAR:
- Para el estudiante.
- Para el docente.

XI. REFLEXIONES SOBRE LOS APRENDIZAJES:
- Incluye la tabla o lista de preguntas de reflexión y metacognición del docente sobre el desarrollo de la unidad.
"""

# ==============================================================================
# EJECUCIÓN CON GOOGLE AI STUDIO (GEMINI API Y NANO BANANA)
# ==============================================================================
st.markdown("---")

if st.button(f"✨ Generar {tipo_documento}"):
    if not api_key:
        st.error("⚠️ Ingresa tu API Key de Google AI Studio en la barra lateral izquierda o en los Secrets.")
    elif not problema_contexto:
        st.warning("⚠️ Completa el campo del Tema, Problema o Situación Significativa.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            
            # SI SE SELECCIONA EL AFICHE DE NANO BANANA:
            if tipo_documento == "Afiche Educativo de la Sesión (Nano Banana)":
                st.session_state['tipo_doc_generado'] = tipo_documento
                with st.spinner("🎨 Nano Banana está diseñando la Lámina / Afiche Educativo Ilustrado en HD para tu sesión..."):
                    img_obj, img_bytes, err_detallado = generar_imagen_nanobanana(
                        client, 
                        tema=problema_contexto, 
                        grado=grado_seccion, 
                        area=area_sel
                    )
                    
                    if img_obj is not None:
                        st.session_state['imagen_nanobanana'] = img_obj
                        st.session_state['imagen_bytes'] = img_bytes
                        st.session_state['resultado_md'] = f"""
# 🖼️ **AFICHE EDUCATIVO DE LA SESIÓN (NANO BANANA AI)**
**Tema:** {problema_contexto} | **Área:** {area_sel} | **Grado:** {grado_seccion}  
**Institución Educativa:** {ie_nombre} | **Docente:** {docente}  

---
*El afiche ilustrado ha sido generado en alta resolución. Puedes observarlo en la vista previa y descargarlo directamente en formato JPG listo para imprimir o proyectar en el aula.*
"""
                        st.success("✅ ¡Afiche Educativo Ilustrado generado con éxito!")
                    else:
                        st.session_state['imagen_nanobanana'] = None
                        st.session_state['imagen_bytes'] = None
                        st.session_state['resultado_md'] = f"⚠️ No se pudo generar la imagen del afiche debido a una restricción de la API de Google AI Studio.\n\n**Detalle técnico:** {err_detallado}"
                        st.error(f"❌ Ocurrió un problema de la API de Google AI Studio al generar la imagen. Detalle técnico: {err_detallado}")

            # SI SE SELECCIONA OTRA HERRAMIENTA (PROYECTO, UNIDAD, SESIÓN, FICHA):
            else:
                if tipo_documento == "Sesión de Aprendizaje":
                    prompt_maestro = generar_prompt_sesion()
                    sys_inst = (
                        "Eres un Especialista Curricular y docente de Educación Primaria del MINEDU Perú. "
                        "Elaboras sesiones de aprendizaje oficiales completas aplicando el enfoque DUA, "
                        "procesos didácticos del área en el Desarrollo, pausa activa de 2 minutos, "
                        "estándar íntegro del CNEB con negrita en lo trabajado y evaluación con escala A, B y C. "
                        "Toda tu respuesta debe estar en formato Markdown limpio y en tablas, sin etiquetas HTML."
                    )
                elif tipo_documento == "Ficha de Aplicación / Trabajo (Para Alumnos)":
                    prompt_maestro = generar_prompt_ficha_trabajo()
                    sys_inst = "Eres un Especialista Curricular y Diseñador de Material Educativo de Educación Primaria del MINEDU Perú. Creas fichas de trabajo aplicando el proceso didáctico del área elegida. Muestras 'DATOS INFORMATIVOS' y 'PROPÓSITO DE HOY' obligatoriamente como SUBTÍTULOS FUERA DE LAS TABLAS. PROHIBIDO USAR ETIQUETAS HTML COMO <tr>, <td>, <th>, <table>, <tbody>."
                elif tipo_documento == "Proyecto de Aprendizaje":
                    prompt_maestro = generar_prompt_proyecto()
                    sys_inst = (
                        "Eres un Especialista Curricular de Educación Primaria del MINEDU Perú. "
                        "Elaboras Proyectos de Aprendizaje respetando estrictamente el Cuadro de Horarios Semanal configurado por el docente. "
                        "REGLA CRÍTICA DE MATRIZ DE APRENDIZAJES: Presenta la matriz de aprendizajes en UN SOLO CUADRO continuo para todo el proyecto, PROHIBIDO fragmentarla en tablas por semana. "
                        "REGLA CRÍTICA DE CORRESPONDENCIA 1 A 1: En la matriz de aprendizajes, es OBLIGATORIO desglosar las actividades sugeridas semana a semana (Semana 1, Semana 2, Semana 3, Semana 4) y redactar EXACTAMENTE UN CRITERIO DE EVALUACIÓN POR CADA ACTIVIDAD SUGERIDA. "
                        "ATENCIÓN CRÍTICA: En los días configurados con 2 áreas (como martes o jueves), es OBLIGATORIO generar 2 sesiones completas (Sesión 1 y Sesión 2). "
                        "ESTÁ ESTRICTAMENTE PROHIBIDO emitir solo 1 sesión en días de 2 áreas."
                    )
                else:
                    prompt_maestro = generar_prompt_unidad_sara()
                    sys_inst = (
                        "Eres un Especialista Curricular de Educación Primaria del MINEDU Perú. "
                        "Elaboras Unidades de Aprendizaje completas en formato Markdown. "
                        "REGLA CRÍTICA DE MATRIZ DE APRENDIZAJES (SECCIÓN V): Presenta la matriz de propósitos y aprendizajes en UN SOLO CUADRO O TABLA UNIFICADA Y CONTINUA para toda la unidad. QUEDA ESTRICTAMENTE PROHIBIDO separar o dividir la matriz en tablas individuales por cada semana. "
                        "REGLA CRÍTICA DE CORRESPONDENCIA 1 A 1 EN LA MATRIZ: En la columna de actividades sugeridas, desglosa obligatoriamente las actividades semana a semana (Semana 1, Semana 2, Semana 3, Semana 4, etc.), y en la columna de Criterios de Evaluación redacta OBLIGATORIAMENTE UN CRITERIO DE EVALUACIÓN POR CADA ACTIVIDAD SUGERIDA de cada semana. "
                        "REGLA CRÍTICA DE COMPETENCIAS TRANSVERSALES (SECCIÓN VII): Debes presentar las competencias transversales obligatoriamente en un CUADRO O TABLA con columnas: COMPETENCIA TRANSVERSAL | CAPACIDADES | DESEMPEÑOS PRECISADOS. "
                        "REGLA CRÍTICA PARA MATEMÁTICA Y COMUNICACIÓN: Debes incluir OBLIGATORIAMENTE las 4 competencias del área de Matemática y las 3 competencias del área de Comunicación a lo largo de la unidad. "
                        "REGLA CRÍTICA PARA EL ESTÁNDAR Y DESEMPEÑO: Debes copiar el texto completo e íntegro tanto del Estándar de Aprendizaje como del Desempeño oficial del CNEB (RM N.° 649-2016-MINEDU) para el grado/ciclo, sin modificar, resumir, alterar ni recortar ninguna palabra. "
                        "Resalta en NEGRITA (**texto**) únicamente el fragmento o precisión que se moviliza o evalúa en la actividad. El resto del texto del estándar y del desempeño debe permanecer exactamente en texto normal. "
                        "ATENCIÓN CRÍTICA PARA EL HORARIO: En los días configurados con 2 áreas (como martes y jueves), es OBLIGATORIO generar 2 sesiones completas (Sesión 1 y Sesión 2) en la tabla semanal. "
                        "QUEDA TERMINANTEMENTE PROHIBIDO poner solo 1 sesión en días que tienen 2 áreas programadas."
                    )
                    
                with st.spinner(f"🧠 Generando tu {tipo_documento} con Google Gemini ({model_choice})..."):
                    config = types.GenerateContentConfig(
                        system_instruction=sys_inst,
                        temperature=0.2
                    )
                    
                    # CASCADA AUTOMÁTICA BLINDADA CON LOS MODELOS VIGENTES:
                    modelos_a_probar = [model_choice]
                    for fallback in [
                        "gemini-3.5-flash-lite",
                        "gemini-3.5-flash",
                        "gemini-3.8-flash",
                        "gemini-2.5-flash",
                        "gemini-2.0-flash",
                        "gemini-1.5-flash",
                        "gemini-1.5-pro"
                    ]:
                        if fallback not in modelos_a_probar:
                            modelos_a_probar.append(fallback)
                    
                    response = None
                    modelo_exitoso = None
                    ultimo_err = None
                    
                    for mod in modelos_a_probar:
                        logrado = False
                        for intento in range(2):
                            try:
                                response = client.models.generate_content(
                                    model=mod,
                                    contents=prompt_maestro,
                                    config=config
                                )
                                if response and response.text:
                                    modelo_exitoso = mod
                                    logrado = True
                                    break
                            except Exception as m_err:
                                err_str_m = str(m_err)
                                ultimo_err = m_err
                                
                                # Si hay saturación (503), pausa y salta
                                if "503" in err_str_m or "UNAVAILABLE" in err_str_m or "high demand" in err_str_m.lower():
                                    if intento == 0:
                                        time.sleep(1.5)
                                        continue
                                    else:
                                        break
                                # Si el modelo fue retirado o no existe (404), salta de inmediato
                                elif "404" in err_str_m or "NOT_FOUND" in err_str_m or "no longer available" in err_str_m.lower() or "not supported" in err_str_m.lower() or "not found" in err_str_m.lower():
                                    break
                                elif "429" in err_str_m or "RESOURCE_EXHAUSTED" in err_str_m:
                                    time.sleep(2)
                                    break
                                else:
                                    break
                        if logrado:
                            break

                    if response is None or not response.text:
                        raise ultimo_err if ultimo_err else Exception("No se pudo obtener respuesta del modelo.")

                    st.session_state['resultado_md'] = response.text
                    st.session_state['tipo_doc_generado'] = tipo_documento
                    st.session_state['fname_clean'] = f"{tipo_documento.replace(' ', '_')}_N{num_doc}_{grado_seccion.replace(' ', '_')}.docx"
                    st.session_state['ie_nombre_generado'] = ie_nombre
                    st.session_state['imagen_nanobanana'] = None
                    st.session_state['imagen_bytes'] = None
                    
                    st.success(f"✅ ¡{tipo_documento} generado con éxito utilizando {modelo_exitoso}!")

        except Exception as e:
            err_str = str(e)
            if "503" in err_str or "UNAVAILABLE" in err_str or "high demand" in err_str.lower():
                st.warning("⚡ **Google AI Studio está experimentando una alta demanda momentánea (Error 503).**\n\nPor favor, espera unos 15 segundos y vuelve a presionar el botón Generar.")
            elif "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                st.warning("⏳ **Límite de velocidad por minuto alcanzado.** Por favor, espera 60 segundos y vuelve a presionar el botón Generar.")
            elif "404" in err_str or "NOT_FOUND" in err_str or "no longer available" in err_str.lower():
                st.error("⚠️ El modelo seleccionado no está disponible en tu cuenta. Por favor selecciona **gemini-3.5-flash-lite** o **gemini-3.5-flash** en el menú superior.")
            else:
                st.error(f"❌ Ocurrió un error con la API de Google AI Studio: {err_str}")

# ==============================================================================
# DESPLIEGUE DE VISTA PREVIA Y DESCARGA PERMANENTE
# ==============================================================================
if st.session_state['resultado_md'] is not None:
    st.markdown("---")
    
    tab_preview, tab_download = st.tabs(["📄 Vista Previa (Permanente)", "📥 Descargar Afiche / Documento"])
    
    with tab_preview:
        if st.session_state.get('imagen_nanobanana') is not None:
            st.markdown("### 🖼️ Afiche Educativo Ilustrado (Nano Banana AI)")
            st.image(st.session_state['imagen_nanobanana'], caption=f"Afiche para {grado_seccion} - {problema_contexto}", use_container_width=True)
            st.markdown("---")

        st.markdown(st.session_state['resultado_md'])
        
    with tab_download:
        if st.session_state.get('tipo_doc_generado') == "Afiche Educativo de la Sesión (Nano Banana)":
            st.markdown("### 🖼️ Descarga tu Afiche Educativo Ilustrado")
            if st.session_state.get('imagen_bytes') is not None:
                st.download_button(
                    label="💾 Descargar Afiche Ilustrado en Alta Calidad (.jpg)",
                    data=st.session_state['imagen_bytes'],
                    file_name=f"Afiche_NanoBanana_{grado_seccion.replace(' ', '_')}.jpg",
                    mime="image/jpeg",
                    use_container_width=True
                )
                st.success("✨ ¡Tu afiche en JPG está listo para imprimir o enviar por WhatsApp a los alumnos!")
            else:
                st.warning("⚠️ No se pudo generar la foto del afiche. Por favor verifica los permisos de tu API Key de Google AI Studio.")

        else:
            es_horizontal_doc = st.session_state['tipo_doc_generado'] in ["Proyecto de Aprendizaje", "Unidad de Aprendizaje (Modelo SARA)"]
            
            buffer_doc = markdown_to_docx(
                st.session_state['resultado_md'], 
                ie_nombre=st.session_state.get('ie_nombre_generado', ie_nombre),
                es_horizontal=es_horizontal_doc
            )
            
            st.download_button(
                label=f"💾 Descargar {st.session_state['tipo_doc_generado']} en Word (.docx)",
                data=buffer_doc,
                file_name=st.session_state['fname_clean'],
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.info("💡 **Nota:** El documento Word generado incluye los recuadros y tablas en tonos pasteles.")
