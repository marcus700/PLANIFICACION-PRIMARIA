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
import cneb_primaria_datos as cneb

# ==============================================================================
# CONFIGURACIÓN DE LA PÁGINA STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="PLANIFIC APRIMARIA - PLATAFORMA PARA DOCENTE DE AULA",
    page_icon="🍎",
    layout="wide"
)

st.markdown("""
<style>
    /* Ocultar la barra superior predeterminada de Streamlit */
    header {visibility: hidden !important;}
    div[data-testid="stHeader"] {display: none !important;}
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    
    /* Ocultar el banner e icono inferior de 'Gestionar la aplicación' */
    div[data-testid="stDecoration"] {display: none !important;}
    div[data-testid="stStatusWidget"] {display: none !important;}
    div[data-testid="stViewerBadge"] {display: none !important;}
    .viewerBadge_container__1613n {display: none !important;}
    .stDeployButton {display: none !important;}
    
    /* Ajustar espacios para diseño limpio */
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 1rem !important;
    }
    
    /* Estilos del encabezado principal */
    .main-header {
        font-size: 2.3rem;
        color: #1E3A8A;
        text-align: center;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 1.5rem;
    }

    /* ESTILOS EXCLUSIVOS Y LLAMATIVOS PARA LOS BOTONES DE HERRAMIENTAS */
    div.st-key-btn_proyecto > button {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        padding: 0.85rem 1rem !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4) !important;
    }
    div.st-key-btn_proyecto > button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        transform: translateY(-2px);
    }

    div.st-key-btn_unidad > button {
        background: linear-gradient(135deg, #8B5CF6 0%, #7C3AED 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        padding: 0.85rem 1rem !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4) !important;
    }
    div.st-key-btn_unidad > button:hover {
        background: linear-gradient(135deg, #7C3AED 0%, #6D28D9 100%) !important;
        transform: translateY(-2px);
    }

    div.st-key-btn_sesion > button {
        background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        padding: 0.85rem 1rem !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4) !important;
    }
    div.st-key-btn_sesion > button:hover {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        transform: translateY(-2px);
    }

    div.st-key-btn_ficha > button {
        background: linear-gradient(135deg, #F97316 0%, #D97706 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        padding: 0.85rem 1rem !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(249, 115, 22, 0.4) !important;
    }
    div.st-key-btn_ficha > button:hover {
        background: linear-gradient(135deg, #EA580C 0%, #B45309 100%) !important;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🍎 PlanificaPrimaria - Sistema para Docentes de Aula</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Plataforma Inteligente de Planificación Curricular para Educación Primaria (CNEB - MINEDU)</div>', unsafe_allow_html=True)

# ==============================================================================
# CONTROL DE ACCESO MEDIANTE CONTRASEÑA
# ==============================================================================
def check_password():
    """Retorna True si el usuario ingresó la contraseña correcta."""
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
            # Verifica contraseña desde Secrets o usa la predeterminada "docente2026"
            target_pwd = st.secrets.get("APP_PASSWORD", "docente2026")
            if pwd_input == target_pwd:
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Contraseña incorrecta. Inténtalo de nuevo.")
    return False

# Si la contraseña no es correcta, detiene la ejecución aquí
if not check_password():
    st.stop()

# ==============================================================================
# INICIALIZACIÓN DE MEMORIA PERSISTENTE (st.session_state)
# ==============================================================================
if 'resultado_md' not in st.session_state:
    st.session_state['resultado_md'] = None
if 'tipo_doc_generado' not in st.session_state:
    st.session_state['tipo_doc_generado'] = None
if 'fname_clean' not in st.session_state:
    st.session_state['fname_clean'] = None
if 'ie_nombre_generado' not in st.session_state:
    st.session_state['ie_nombre_generado'] = None
if 'tipo_documento' not in st.session_state:
    st.session_state['tipo_documento'] = "Proyecto de Aprendizaje"

# ==============================================================================
# BARRA LATERAL (SIDEBAR) - CONFIGURACIÓN Y API KEY
# ==============================================================================
st.sidebar.title("⚙️ Configuración")

# Botón para cerrar sesión
if st.sidebar.button("🔒 Cerrar Sesión"):
    st.session_state["password_correct"] = False
    st.rerun()

st.sidebar.markdown("---")

# Detección inteligente de la API Key (Desde Secrets o Entrada Manual)
if "GEMINI_API_KEY" in st.secrets and st.secrets["GEMINI_API_KEY"]:
    api_key = st.secrets["GEMINI_API_KEY"]
    st.sidebar.success("🔑 API Key activada desde el servidor.")
else:
    api_key = st.sidebar.text_input(
        "🔑 Google AI Studio API Key:", 
        type="password", 
        help="Consigue tu clave gratuita en https://aistudio.google.com/app/apikey"
    )

# Modelos oficiales vigentes de Google AI Studio
model_choice = st.sidebar.selectbox(
    "Modelo de Gemini:", 
    ["gemini-3.6-flash", "gemini-3.5-flash", "gemini-2.5-flash", "gemini-2.0-flash"]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Alineamiento CNEB Perú:**
• RM N.° 649-2016-MINEDU
• Estándares y Desempeños CNEB Íntegros
• Turno Único: 2 a 3 Sesiones diarias de 90 min
• Nivel Educación Primaria (1.° a 6.° Grado)
• Tablas en Colores Pasteles Variados
""")

# ==============================================================================
# SELECCIÓN DE HERRAMIENTAS DE AULA EN LA PÁGINA PRINCIPAL (ORDEN Y COLORES LLAMATIVOS)
# ==============================================================================
st.markdown("### 📋 Selecciona la Herramienta de Aula que deseas elaborar:")

col_b1, col_b2, col_b3, col_b4 = st.columns(4)

with col_b1:
    if st.button("🚀 Proyecto de Aprendizaje", key="btn_proyecto", use_container_width=True):
        st.session_state['tipo_documento'] = "Proyecto de Aprendizaje"
        st.rerun()

with col_b2:
    if st.button("📘 Unidad de Aprendizaje", key="btn_unidad", use_container_width=True):
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

tipo_documento = st.session_state['tipo_documento']

# Banner indicador de la herramienta seleccionada
COLOR_MAP = {
    "Proyecto de Aprendizaje": "#059669",
    "Unidad de Aprendizaje": "#7C3AED",
    "Sesión de Aprendizaje": "#2563EB",
    "Ficha de Aplicación / Trabajo (Para Alumnos)": "#D97706"
}
banner_color = COLOR_MAP.get(tipo_documento, "#059669")

st.markdown(f"""
<div style="background-color: {banner_color}; color: white; padding: 0.6rem 1rem; border-radius: 8px; font-weight: bold; font-size: 1.1rem; margin-top: 0.8rem; margin-bottom: 1.2rem; text-align: center;">
    📍 Herramienta Seleccionada: {tipo_documento.upper()}
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# PROCESADOR DE TEXTO ENRIQUECIDO PARA WORD (SOPORTE DE NEGRITAS **)
# ==============================================================================
def add_formatted_text(paragraph, text):
    """Agrega texto a un párrafo en Word respetando las marcas de negrita **texto**"""
    parts = re.split(r'(\*\*.*?\*\*)', text)
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            run = paragraph.add_run(part[2:-2])
            run.font.bold = True
        else:
            paragraph.add_run(part)

# ==============================================================================
# CONVERTIDOR A WORD (.DOCX) CON PROCESAMIENTO GARANTIZADO DE LA ÚLTIMA TABLA
# ==============================================================================
def markdown_to_docx(md_text, ie_nombre="I.E. N° 22303", es_horizontal=False):
    doc = docx.Document()
    
    # Paleta de colores pasteles rotativos para los encabezados de tablas
    PASTEL_COLORS = [
        'D9E1F2',  # Azul Pastel
        'E2EFDA',  # Verde Menta Pastel
        'FFF2CC',  # Amarillo Pastel
        'E8D8F8',  # Lavanda Pastel
        'E0F2FE',  # Celeste Pastel
        'FCE4D6'   # Rosa/Coral Pastel
    ]
    table_count = 0
    
    # Configurar Márgenes y Orientación (Horizontal para Unidades y Proyectos)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
        if es_horizontal:
            section.orientation = WD_ORIENT.LANDSCAPE
            section.page_width = Inches(11.69)   # A4 Horizontal
            section.page_height = Inches(8.27)
        else:
            section.orientation = WD_ORIENT.PORTRAIT
            section.page_width = Inches(8.27)    # A4 Vertical
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
                        p_cell.text = ""  # Limpiar
                        add_formatted_text(p_cell, cell_value)
                        
                        # APLICAR COLOR PASTEL EN EL ENCABEZADO
                        if r_idx == 0:
                            shading_elm = OxmlElement('w:shd')
                            shading_elm.set(qn('w:val'), 'clear')
                            shading_elm.set(qn('w:color'), 'auto')
                            shading_elm.set(qn('w:fill'), color_hex)
                            cell._tc.get_or_add_tcPr().append(shading_elm)
                            for paragraph in cell.paragraphs:
                                for run in paragraph.runs:
                                    run.font.color.rgb = RGBColor(30, 58, 138)  # Azul Marino
                                    run.font.bold = True

    for line in lines:
        line_str = line.strip()
        
        # Limpieza de etiquetas HTML indeseadas (<br>, <br/>, <tr>, <td>, <th>, etc.)
        line_str = re.sub(r'<br\s*/?>', ' ', line_str)
        line_str = re.sub(r'</?[a-zA-Z0-9]+\s*/>', ' ', line_str)
        line_str = re.sub(r'</?(table|tr|td|th|thead|tbody)[^>]*>', ' ', line_str, flags=re.IGNORECASE)
        
        # Procesamiento de Tablas Markdown
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

        # DETECCIÓN Y ELIMINACIÓN DE CUALQUIER NIVEL DE ALMOHADILLAS (#, ##, ###, ####, #####)
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

        # Procesamiento de Viñetas
        if line_str.startswith('• ') or line_str.startswith('- '):
            p = doc.add_paragraph(style='List Bullet')
            clean_bullet = line_str[2:].strip()
            add_formatted_text(p, clean_bullet)
        elif line_str != "":
            p = doc.add_paragraph()
            add_formatted_text(p, line_str)

    # GARANTIZAR QUE LA ÚLTIMA TABLA SE PROCESE E IMPRIMA EN WORD
    if in_table and table_data:
        table_count += 1
        header_color = PASTEL_COLORS[(table_count - 1) % len(PASTEL_COLORS)]
        render_table(table_data, header_color)
        in_table = False
        table_data = []
            
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer


# ==============================================================================
# FORMULARIO DE DATOS DE AULA
# ==============================================================================
st.subheader(f"📝 Configuración de Datos: {tipo_documento}")

c1, c2, c3 = st.columns(3)
with c1:
    dre_ugel = st.text_input("DRE / UGEL:", "Ica / Ica")
    ie_nombre = st.text_input("Institución Educativa:", "N°")
with c2:
    director = st.text_input("Director:", " ")
    subdirector = st.text_input("Subdirector(es):", " ")
with c3:
    docente = st.text_input("Docente de Aula:", " ")
    grado_seccion = st.selectbox("Grado y Sección:", ["1er Grado A", "2do Grado A", "3er Grado A", "4to Grado A", "5to Grado A", "6to Grado A"], index=2)

if tipo_documento in ["Sesión de Aprendizaje", "Ficha de Aplicación / Trabajo (Para Alumnos)"]:
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        num_doc = st.text_input("N.° de Documento / Sesión / Ficha:", "01")
    with f2:
        area_sel = st.selectbox("Área Curricular:", cneb.obtener_lista_areas(), index=0)
    with f3:
        fecha_sugerida = st.text_input("Fecha:", "05 de mayo de 2026")
    with f4:
        duracion_sesion = st.selectbox("Duración de la Sesión:", ["45 minutos", "90 minutos", "135 minutos"], index=1)
    
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

# CAMPO DE TEMA/PROBLEMA SEGÚN EL TIPO DE DOCUMENTO
if tipo_documento in ["Sesión de Aprendizaje", "Ficha de Aplicación / Trabajo (Para Alumnos)"]:
    problema_contexto = st.text_input(
        "📌 Tema / Título de la Actividad o Ficha de Trabajo:",
        value="Mis derechos y deberes"
    )
    titulo_opcional = ""
else:
    problema_contexto = st.text_area(
        "🚨 Problema o Interés del Contexto (Único dato requerido para que la IA cree el Título y la Situación Significativa automáticamente):",
        height=100,
        value="Poco hábito de recolección de residuos sólidos y acumulación de botellas de plástico en el patio durante el recreo por parte de los estudiantes de 3er grado."
    )
    titulo_opcional = st.text_input("Título Opcional (Déjalo en blanco si deseas que la IA cree un título creativo automático a partir del problema):", value="")

# ==============================================================================
# PROMPTS MAESTROS ALINEADOS AL CNEB COMPLETO
# ==============================================================================
def generar_prompt_sesion():
    if "45" in duracion_sesion:
        t_inicio, t_desarrollo, t_cierre = "10 min", "30 min", "5 min"
    elif "135" in duracion_sesion:
        t_inicio, t_desarrollo, t_cierre = "20 min", "100 min", "15 min"
    else:
        t_inicio, t_desarrollo, t_cierre = "20 min", "60 min", "10 min"

    return f"""
Actúa como: Un Especialista en Currículo Nacional de Educación Básica (CNEB) del MINEDU, experto en planificación pedagógica de nivel Primaria.
Tu objetivo: Elaborar una sesión de aprendizaje completa siguiendo estrictamente el formato y estructura del modelo proporcionado.

Datos para la sesión (Configuración):
• Grado y Sección: {grado_seccion}
• Área Curricular: {area_sel}
• Tema/Título de la sesión: {problema_contexto}
• Fecha sugerida: {fecha_sugerida}
• DRE / UGEL: {dre_ugel}
• Institución Educativa: {ie_nombre}
• Director: {director}
• Subdirector(es): {subdirector}
• Docente de Aula: {docente}
• Duración Total: {duracion_sesion}

________________________________________
INSTRUCCIONES DE FORMATO Y CONTENIDO (OBLIGATORIO):
• Estructura de Cuadros: Utiliza exactamente los mismos cuadros del modelo (Datos Informativos, Propósitos, Enfoques, Metas, Preparación, Momentos de la sesión y Escala de Valoración). NO INCLUYAS NINGUNA SITUACIÓN SIGNIFICATIVA.
• Alineación CNEB: Selecciona la Competencia, Capacidades y Desempeños (precisados si es necesario) directamente del Programa Curricular de Educación Primaria del MINEDU correspondiente al grado ({grado_seccion}). Para el Estándar de Aprendizaje del CNEB, escríbelo EN SU TOTALIDAD Y DE MANERA ÍNTEGRA sin ningún corte, resumen ni omisión, resaltando en **negrita** únicamente el fragmento trabajado.
• Criterios de Evaluación: Deben redactarse bajo la estructura implícita de ACCIÓN + CONTENIDO + CONDICIÓN, pero que no figure dicha estructura o etiqueta explícita en su redacción (Ejemplo: "Reconoce las acciones que contaminan el ambiente mediante la observación de imágenes").
• Redacción de Actividades: Las actividades en los momentos de Inicio, Desarrollo y Cierre deben estar redactadas en PRIMERA PERSONA DEL PLURAL Y TIEMPO PRESENTE (Ejemplo: "Saludamos a los estudiantes", "Preguntamos a los niños", "Repartimos las fichas").
• Procesos Didácticos y pedagógicos por Área: Debes aplicar rigurosamente los procesos del área seleccionada:

Procesos Pedagógicos Comunes a Todas las Áreas:
A.- MOMENTO: INICIO DE LA SESIÓN ({t_inicio})
• Estos procesos son fundamentales para cualquier sesión de aprendizaje y el docente debe promoverlos de manera continua:
- Problematización: Plantear situaciones o desafíos que generen interés y un conflicto cognitivo en los estudiantes, llevándolos a cuestionarse y a querer aprender.
- Propósito y Organización: Comunicar a los estudiantes el objetivo de la sesión, las competencias que se desarrollarán y cómo será el proceso de trabajo.
- Motivación/Interés: Mantener el interés de los estudiantes a lo largo de toda la sesión a través de actividades lúdicas, materiales novedosos o temáticas relevantes para ellos.
- Saberes Previos: Activar los conocimientos y experiencias que los estudiantes ya poseen sobre el tema, conectándolos con el nuevo aprendizaje.
- Criterios de evaluación: Se mencionan a los estudiantes los criterios que van a ser observados durante la sesión de aprendizaje.
- Normas de convivencia: Formulación de normas que se van a utilizar en la sesión.
- Gestión y Acompañamiento del Desarrollo de las Competencias: El docente acompaña al estudiante en su proceso de aprendizaje, brindándole retroalimentación, resolviendo dudas y ajustando la enseñanza según las necesidades observadas.
- Evaluación: Recoger y valorar información sobre el nivel de desarrollo de las competencias de los estudiantes, tanto durante el proceso (formativa) como al final (sumativa), para tomar decisiones que mejoren el aprendizaje (Se dan en el momento del desarrollo de las sesiones).

Procesos Didácticos por Área Curricular:
B.- MOMENTO DEL DESARROLLO DE LA SESIÓN ({t_desarrollo})
1. Matemática (Enfoque Centrado en la Resolución de Problemas):
   - Comprensión del Problema: Los estudiantes leen atentamente el problema para identificar los datos, las condiciones y lo que se les pide resolver. Pueden usar técnicas como el parafraseo o la realización de preguntas.
   - Búsqueda de Estrategias: Proponen y seleccionan diversas formas de solucionar el problema, como hacer un diagrama, usar material concreto, plantear una operación, etc.
   - Representación: Plasman la situación de manera concreta (con materiales), pictórica (dibujos, esquemas) o simbólica (números, operaciones).
   - Formalización: A partir de lo trabajado, el docente guía a los estudiantes para que identifiquen y nombren los conceptos, propiedades o procedimientos matemáticos involucrados.
   - Reflexión: Los estudiantes analizan el proceso seguido, verifican sus resultados y reflexiona sobre qué les funcionó, qué dificultades tuvieron y cómo lo superaron.
   - Transferencia: Aplican lo aprendido en la resolución de nuevos problemas o situaciones similares, tanto dentro como fuera de la escuela.

2. Comunicación (Enfoque Comunicativo):
   Los procesos didácticos varían si se trabaja la oralidad, la lectura o la escritura:
   • Para la Comprensión de Textos (Lectura):
     - Antes de la Lectura: Se activan los saberes previos, se formulan hipótesis sobre el contenido a partir del título o las imágenes y se define el propósito de la lectura.
     - Durante la Lectura: Se realiza la lectura (individual, en voz alta, silenciosa), se formulan preguntas, se hacen predicciones y se aclara el vocabulario.
     - Después de la Lectura: Se contrasta la hipótesis inicial, se resume el texto, se formulan opiniones y se reflexiona sobre el contenido y la forma del texto.
   • Para la Producción de Textos (Escritura):
     - Planificación: Se define el propósito, el destinatario, el tipo de texto y el tema. Se generan ideas y se organizan en un esquema o plan de escritura.
     - Textualización (o Escritura): Se redacta el primer borrador del texto, respetando la estructura y el lenguaje planificados.
     - Revisión: Se lee el borrador para identificar errores y aspectos a mejorar (coherencia, cohesión, ortografía, gramática). Se puede hacer de forma individual o con compañeros.
     - Edición y Publicación: Se reescribe el texto incorporando las correcciones y se comparte o publica según el propósito definido.

3. Personal Social (Enfoque de Desarrollo Personal y Ciudadanía Activa):
   - Problematización: Se presenta una situación real o simulada (un caso, una noticia, un dilema moral) que genere un conflicto y motive al análisis.
   - Análisis de Información: Los estudiantes buscan, leen y analizan información de diversas fuentes (textos, videos, testimonios) para comprender mejor la situación problemática.
   - Acuerdo o Toma de Decisiones: A partir del análisis, los estudiantes deliberan, dialogan, argumentan sus puntos de vista y toman una postura o llegan a consensos para actuar frente a la situación.

4. Ciencia y Tecnología (Enfoque de Indagación Científica):
   - Planteamiento del Problema: A partir de una observación o experiencia, los estudiantes formulan una pregunta que pueda ser investigada.
   - Planteamiento de la Hipótesis: Proponen una posible respuesta o explicación al problema planteado.
   - Elaboración del Plan de Acción: Diseñan los pasos que seguirán para comprobar su hipótesis: qué materiales usarán, qué medirán, cómo registrarán los datos.
   - Recojo y Análisis de Datos: Ejecutan el plan, experimentan, observan y registran la información obtenida en tablas, gráficos, etc.
   - Estructuración del Saber Construido: Comparan los resultados con su hipótesis inicial, la aceptan o la rechazan, y construyen una conclusión basada en las evidencias.
   - Evaluación y Comunicación: Comunican sus hallazgos y conclusiones (de forma oral, escrita, gráfica) y reflexionan sobre el proceso de indagación realizado.

5. Arte y Cultura (Enfoque Multicultural e Interdisciplinario):
   - Explorar y Experimentar: Los estudiantes interactúan libremente con diversos materiales y lenguajes artísticos (danza, música, teatro, artes visuales) para descubrir sus posibilidades expresivas.
   - Aplicar Procesos Creativos: Planifican y desarrollan sus propios proyectos artísticos, tomando decisiones sobre los elementos y técnicas a utilizar para comunicar sus ideas y sentimientos.
   - Evaluar y Socializar sus Procesos y Proyectos: Reflexionan sobre sus creaciones y las de sus compañeros, y las presentan a una audiencia, explicando sus intenciones y el proceso seguido.

6. Educación Física (Enfoque de la Corporeidad):
   - Se organiza de la siguiente manera:
     • Actividad fisiológica: Se realizan juegos y actividades de calentamiento para preparar el cuerpo para la actividad principal.
     • Actividades centrales de la sesión: Orientadas al desarrollo de habilidades motrices, la expresión corporal o la práctica de juegos y deportes (Actividad básica, Actividad avanzada, Actividad de aplicación).
     • Momento de cierre: Vuelta a la Calma (Relajación), Metacognición, Retroalimentación, Despedida.

7. Educación Religiosa (Enfoque Humanista Cristiano):
   Se basa en el método VER - JUZGAR - ACTUAR - CELEBRAR:
   - VER: Se parte de una experiencia de la vida cotidiana de los estudiantes, un acontecimiento o una realidad que los interpela.
   - JUZGAR: Se ilumina esa realidad con la Palabra de Dios y las enseñanzas de la Iglesia, buscando un mensaje que dé sentido a la experiencia.
   - ACTUAR: Se invita a los estudiantes a asumir un compromiso personal y comunitario coherente con la reflexión realizada.
   - CELEBRAR: Se finaliza con un momento de oración, canto o un gesto simbólico para expresar la fe y agradecer la experiencia vivida.

Procesos Pedagógicos Recurrentes: Asegúrese de incluir en la sesión: Problematización, Propósito y organización, Motivación, Saberes previos, Gestión y acompañamiento, y Evaluación.

________________________________________
ESTRUCTURA DE SALIDA REQUERIDA (OBLIGATORIA EN CUADROS/TABLAS MARKDOWN Y SIN SITUACIÓN SIGNIFICATIVA):

# **SESIÓN DE APRENDIZAJE N.º {num_doc}**
## **{problema_contexto.upper()}**

• TABLA I: DATOS INFORMATIVOS (ESTRICTAMENTE EN 2 COLUMNAS: COLUMNA 1 = CONCEPTO/DATO, COLUMNA 2 = VALOR/RESPUESTA):
| DATOS INFORMATIVOS | DETALLE / INFORMACIÓN |
| DRE / UGEL | {dre_ugel} |
| Institución Educativa | {ie_nombre} |
| Director | {director} |
| Subdirector(es) | {subdirector} |
| Docente de Aula | {docente} |
| Grado y Sección | {grado_seccion} |
| Área Curricular | {area_sel} |
| Fecha | {fecha_sugerida} |
| Duración | {duracion_sesion} |

• TABLA II: PROPÓSITOS DE APRENDIZAJE Y EVIDENCIAS
| ÁREA | COMPETENCIA Y CAPACIDADES | ESTÁNDAR DE APRENDIZAJE (CNEB completo en su totalidad con parte trabajada en **negrita**) | DESEMPEÑOS PRECISADOS (CNEB) | CRITERIOS DE EVALUACIÓN | PROPÓSITO DE LA SESIÓN | EVIDENCIA DE APRENDIZAJE | INSTRUMENTO DE EVALUACIÓN |

• TABLA III: ENFOQUES TRANSVERSALES
| ENFOQUE TRANSVERSAL | VALORES | ACTITUDES OBSERVABLES |

• TABLA IV: COMPETENCIA TRANSVERSAL
| COMPETENCIA TRANSVERSAL | CAPACIDADES | DESEMPEÑOS PRECISADOS |
| "Gestiona su aprendizaje de manera autónoma" | Define metas de aprendizaje / Organiza acciones estratégicas | Muestra autonomía al realizar sus tareas pedagógicas. |

• TABLA V: META DE APRENDIZAJE
| META DE APRENDIZAJE ({grado_seccion}) | DESCRIPCIÓN DE LA META |
| Protección de la vida / Habilidades para la vida | [Inserte meta del grado correspondiente] |

• TABLA VI: PREPARACIÓN DE LA SESIÓN
| ¿Qué necesitamos hacer antes de la sesión? | ¿Qué recursos o materiales se utilizarán en esta sesión? |

• MOMENTOS DE LA SESIÓN (REDACTADO EN 1ra PERSONA DEL PLURAL Y TIEMPO PRESENTE):
- **INICIO ({t_inicio})**: Motivación, Saberes previos, Problematización, Propósito y Criterios, Normas de convivencia.
- **DESARROLLO ({t_desarrollo})**: Aplicar detalladamente los procesos didácticos específicos del área ({area_sel}).
- **CIERRE ({t_cierre})**: Metacognición y Reflexión final.

• TABLA VII: ESCALA DE VALORACIÓN
(Crea una tabla completa con exactamente 30 estudiantes ficticios con nombres y apellidos peruanos, y evalúa 3 Criterios de Evaluación con las columnas: N.°, Apellidos y Nombres, Criterio 1 [Inicio, En proceso, Lo logró], Criterio 2 [Inicio, En proceso, Lo logró], Criterio 3 [Inicio, En proceso, Lo logró], Observaciones).
"""

def generar_prompt_ficha_trabajo():
    return f"""
Actúa como: Especialista en Educación Primaria (CNEB - MINEDU Perú) y diseñador experto de material educativo impreso para estudiantes de primaria.
Tu objetivo: Elaborar una FICHA DE TRABAJO / APLICACIÓN PARA EL ESTUDIANTE altamente didáctica, motivadora, visualmente ordenada en cuadros/tablas y lista para imprimir.

DATOS DE CONFIGURACIÓN DE LA FICHA:
• Grado y Sección: {grado_seccion}
• Área Curricular: {area_sel}
• Tema / Título de la Ficha: {problema_contexto}
• Fecha: {fecha_sugerida}
• Institución Educativa: {ie_nombre}
• Docente de Aula: {docente}

________________________________________
INSTRUCCIONES DE ESTILO Y DISEÑO (OBLIGATORIO):
1. Adaptación al Grado: Utiliza un lenguaje directo, claro, motivador e instrucciones sencillas adaptadas al nivel lector de {grado_seccion}.
2. Formato en Cuadros/Tablas MARKDOWN PURAS: Organiza los ejercicios y actividades en tablas Markdown puras usando tuberías (|). 
3. PROHIBIDO ROTUNDAMENTE usar etiquetas HTML de tablas como <table>, <tr>, <td>, <th>, <tbody>, <thead> o <br>. Toda la información, tableros posicionales o cuadros matemáticos deben generarse únicamente mediante sintaxis de tablas Markdown de texto (| C | D | U |).
4. NO uses símbolos de almohadillas excesivos (#### o #####). Usa solo Markdown limpio (#, ##, **negrita**, listas • y tablas |).
5. REGLA DE SUBTÍTULOS OBLIGATORIOS FUERA DE LAS TABLAS: 
   - Las palabras "DATOS INFORMATIVOS" deben colocarse FUERA DE CUALQUIER TABLA como un SUBTÍTULO PRINCIPAL (`## **DATOS INFORMATIVOS**`).
   - Las palabras "PROPÓSITO DE HOY" deben colocarse FUERA DE CUALQUIER TABLA como otro SUBTÍTULO PRINCIPAL (`## **PROPÓSITO DE HOY**`).

________________________________________
APLICACIÓN ESTRICTA DEL PROCESO DIDÁCTICO SEGÚN EL ÁREA SELECCIONADA ({area_sel}):
La estructura central de la ficha DEBE seguir obligatoriamente los pasos del proceso didáctico del CNEB del área elegida:

• Si el área es MATEMÁTICA (Enfoque de Resolución de Problemas):
  - Sección 1: Comprensión del problema (Texto del problema cotidiano + preguntas para identificar datos).
  - Sección 2: Búsqueda de estrategias y representación (Cuadro Markdown para representar con dibujo/esquema y cuadro Markdown para la operación o tablero posicional).
  - Sección 3: Formalización y Transferencia (Conclusión rápida + Un nuevo reto matemático similar).

• Si el área es COMUNICACIÓN - LECTURA (Enfoque Comunicativo):
  - Sección 1: Antes de la lectura (Predicciones a partir del título/imagen y propósito lector).
  - Sección 2: Durante la lectura (Lectura corta y adaptada al grado).
  - Sección 3: Después de la lectura (Preguntas explícitas, inferenciales y de opinión/reflexión en cuadros).

• Si el área es COMUNICACIÓN - ESCRITURA (Enfoque Comunicativo):
  - Sección 1: Planificación (Cuadro: ¿Qué escribiré?, ¿Para quién?, ¿Para qué?).
  - Sección 2: Textualización (Espacio estructurado para escribir el primer borrador).
  - Sección 3: Revisión (Lista de cotejo amigable para que el estudiante revise su texto).

• Si el área es PERSONAL SOCIAL (Enfoque de Ciudadanía Activa / Desarrollo Personal):
  - Sección 1: Problematización (Lectura de un caso o noticia corta con dilema/situación).
  - Sección 2: Análisis de la información (Preguntas de reflexión y comparación de posturas).
  - Sección 3: Toma de decisiones / Mi compromiso (Cuadro para redactar su compromiso personal).

• Si el área es CIENCIA Y TECNOLOGÍA (Enfoque de Indagación Científica):
  - Sección 1: Planteamiento del problema e Hipótesis (Pregunta investigable + Mi respuesta previa).
  - Sección 2: Plan de acción y Recojo de datos (Tabla para registrar experimento, observaciones o lectura).
  - Sección 3: Conclusión (Comprobación de hipótesis y qué aprendí hoy).

• Si el área es ARTE Y CULTURA (Enfoque Multicultural):
  - Sección 1: Exploración (Observación de una manifestación o prueba de materiales).
  - Sección 2: Proceso Creativo (Pasos para realizar la actividad artística o boceto).
  - Sección 3: Reflexión (Preguntas sobre lo que sintió y transmitió con su obra).

• Si el área es EDUCACIÓN RELIGIOSA (Método Ver-Juzgar-Actuar-Celebrar):
  - Sección 1: VER (Situación de la vida diaria).
  - Sección 2: JUZGAR (Cita bíblica o mensaje bíblico corto adaptado).
  - Sección 3: ACTUAR Y CELEBRAR (Compromiso cristiano + Oración final corta).

• Si el área es EDUCACIÓN FÍSICA / TUTORÍA:
  - Sección 1: Identificación (Situación sobre hábitos saludables, emociones o habilidades).
  - Sección 2: Práctica / Aplicación (Ficha de registro de actividad o reflexiones).
  - Sección 3: Autocuidado y Compromiso.

________________________________________
ESTRUCTURA DE SALIDA REQUERIDA (OBLIGATORIA EN MARKDOWN PURA Y TABLAS SIN ETIQUETAS HTML):

# **FICHA DE TRABAJO DE {area_sel.upper()} N.º {num_doc}**
## **{problema_contexto.upper()}**

## **DATOS INFORMATIVOS**
• TABLA I: DATOS DE LA FICHA (EN 2 COLUMNAS):
| DATOS INFORMATIVOS | DETALLE / INFORMACIÓN |
| Institución Educativa | {ie_nombre} |
| Grado y Sección | {grado_seccion} |
| Área Curricular | {area_sel} |
| Docente de Aula | {docente} |
| Fecha | {fecha_sugerida} |
| Estudiante | __________________________________________________ |

## **PROPÓSITO DE HOY**
[Escribe aquí en una frase o párrafo corto, sencillo y directo qué aprenderá y logrará el estudiante el día de hoy].

• SECCIÓN 1: "ME PREPARO Y DESCUBRO"
(Aplica el 1er momento del proceso didáctico del área de {area_sel}).

• SECCIÓN 2: "MANOS A LA OBRA / APLICO LO APRENDIDO"
(Aplica el 2do momento del proceso didáctico con tablas de ejercicios, casilleros para responder, marcar o completar usando únicamente tablas Markdown con |).

• SECCIÓN 3: "MI RETO FINAL / MI COMPROMISO"
(Aplica el momento final del proceso didáctico con una actividad desafiante o compromiso).

• TABLA II: AUTOEVALUACIÓN DE MIS LOGROS
| Criterios para evaluar mi trabajo | ¡Lo logré! 😀 | Estoy en proceso 😐 | Necesito ayuda 😕 |
| [Criterio 1 adaptado al niño de {grado_seccion}] | | | |
| [Criterio 2 adaptado al niño de {grado_seccion}] | | | |
| [Criterio 3 adaptado al niño de {grado_seccion}] | | | |
"""

def generar_prompt_proyecto():
    val_titulo = f'"{titulo_opcional}"' if titulo_opcional.strip() else 'Crea un TÍTULO innovador y creativo para el proyecto basado en el problema.'

    return f"""
Actúa como un docente especialista de Primaria MINEDU Perú. Elabora un PROYECTO DE APRENDIZAJE completo.
PROHIBIDO usar símbolos #### o ##### y etiquetas HTML. Usa Markdown limpio y estructura strictly en TABLAS Y CUADROS.

A PARTIR DEL PROBLEMA DEL CONTEXTO DEL DOCENTE:
{problema_contexto}

OBLIGATORIO - GENERACIÓN AUTOMÁTICA DE TÍTULO Y SITUACIÓN SIGNIFICATIVA:
1. Genera un TÍTULO del proyecto: {val_titulo}
2. Redacta la SITUACIÓN SIGNIFICATIVA COMPLETA estructurada en 3 párrafos.

ORDEN ESTRUCTURAL ESTRICTO DE SALIDA (Sigue exactamente esta secuencia):

1. ENCABEZADO Y TABLA I: DATOS INFORMATIVOS (Muestra exactamente: DRE/UGEL: {dre_ugel}, IE: {ie_nombre}, Director: {director}, Subdirector: {subdirector}, Docente: {docente}, Grado/Sección: {grado_seccion}, Duración: {fechas_duracion}).

2. SITUACIÓN SIGNIFICATIVA GENERADA (Ubicada OBLIGATORIAMENTE justo debajo de los Datos Informativos).

3. PLANIFICACIÓN DEL PROYECTO CON LOS ESTUDIANTES (Tabla: ¿Qué haremos?, ¿Qué sabemos?, ¿Qué queremos saber?, ¿Cómo lo haremos?, ¿Qué necesitamos?, ¿Cómo nos organizamos?).

4. MATRIZ DE PROPÓSITOS DE APRENDIZAJE POR SEMANA (SECCIÓN CONTINUA COMPLETA DESDE LA SEMANA 1 HASTA LA SEMANA {duracion_semanas}):
   - Para CADA una de las {duracion_semanas} semanas, coloca el **TÍTULO CREATIVO DE LA ACTIVIDAD DE LA SEMANA** (Ejemplo: SEMANA 1: "Investigamos los problemas ambientales de nuestro colegio").
   - Debajo del título de la semana, presenta la Matriz de Propósitos en sus 8 COLUMNAS EXACTAS:
     | ÁREA | ACTIVIDAD | COMPETENCIA Y CAPACIDADES | ESTÁNDAR DE APRENDIZAJE | DESEMPEÑO PRECISADO | CRITERIOS DE EVALUACIÓN | EVIDENCIA | INSTRUMENTO DE EVALUACIÓN |
   - REGLA OBLIGATORIA DEL ESTÁNDAR: Copia el **ESTÁNDAR DE APRENDIZAJE EN SU TOTALIDAD Y DE MANERA ÍNTEGRA** tal cual figura en el CNEB oficial (RM N.º 649-2016-MINEDU) sin ningún corte ni resumen, y RESALTA EN **NEGRITA** (`**la parte específica movilizada en la actividad**`).
   - Copia el DESEMPEÑO ÍNTEGRO del CNEB con la parte trabajada en **negrita**.
   - REGLA OBLIGATORIA DE COBERTURA DE ÁREAS EN LA MATRIZ: En cada una de las {duracion_semanas} semanas, debes incluir OBLIGATORIAMENTE filas para TODAS Y CADA UNA DE LAS ÁREAS CURRICULARES SIN EXCEPCIÓN: Comunicación (3 comp.), Matemática (4 comp.), Personal Social, Ciencia y Tecnología, Educación Religiosa, Arte y Cultura, Educación Física y Tutoría / Competencias Transversales.

5. SECUENCIA DE ACTIVIDADES CON LOS DÍAS COMO COLUMNAS DE TABLA (2 A 3 SESIONES DIARIAS DE 90 MINUTOS EN TURNO ÚNICO - 10 A 15 SESIONES POR SEMANA):
   - Presenta esta sección OBLIGATORIAMENTE AL TÉRMINO DE TODA LA MATRIZ DE PROPÓSITOS.
   - Para cada semana (Semana 1 a {duracion_semanas}), coloca el **TÍTULO DE LA SEMANA** y crea una TABLA OBLIGATORIA donde LAS COLUMNAS SEAN LOS DÍAS DE LA SEMANA:
     | LUNES | MARTES | MIÉRCOLES | JUEVES | VIERNES |
   - En cada casillero diario, programa de 2 a 3 sesiones de 90 minutos en turno único (sin dividir en mañana/tarde), indicando el **ÁREA CURRICULAR DESTACADA**:
     • Sesión 1 (90 min): **[ÁREA]**: [Competencia específica] - [Actividad en 1ª persona plural]
     • Sesión 2 (90 min): **[ÁREA]**: [Competencia específica] - [Actividad en 1ª persona plural]
     • Sesión 3 (90 min, si aplica): **[ÁREA]**: [Competencia específica] - [Actividad en 1ª persona plural]
   - REGLA OBLIGATORIA DE ÁREAS EN LA SECUENCIA DE ACTIVIDADES: En la tabla semanal de actividades, DEBES DISTRIBUIR Y CONSIDERAR OBLIGATORIAMENTE TODAS Y CADA UNA DE LAS ÁREAS CURRICULARES EN CADA SEMANA SIN EXCEPCIÓN (Comunicación, Matemática, Personal Social, Ciencia y Tecnología, Religión, Arte, Educación Física y Tutoría).

6. TABLA DE ENFOQUES TRANSVERSALES.
7. PRODUCTO FINAL TANGIBLE DEL PROYECTO.
8. LISTA CLASIFICADA DE MATERIALES Y RECURSOS.
9. TABLA VIII: REFLEXIONES SOBRE LOS APRENDIZAJES (Tabla final obligatoria).
"""

def generar_prompt_unidad_sara():
    val_titulo = f'"{titulo_opcional}"' if titulo_opcional.strip() else 'Crea un TÍTULO motivador para la Unidad SARA basado en el problema.'

    return f"""
Actúa como docente especialista de Primaria MINEDU Perú. Elabora una UNIDAD DE APRENDIZAJE (Modelo SARA).
PROHIBIDO usar símbolos #### o ##### y etiquetas HTML. Usa Markdown limpio y estructura estrictamente en TABLAS Y CUADROS.

A PARTIR DEL PROBLEMA DEL CONTEXTO DEL DOCENTE:
{problema_contexto}

OBLIGATORIO - GENERACIÓN AUTOMÁTICA DE TÍTULO Y SITUACIÓN SIGNIFICATIVA:
1. Genera un TÍTULO de la unidad: {val_titulo}
2. Redacta la SITUACIÓN SIGNIFICATIVA COMPLETA estructurada en 3 párrafos.

ORDEN ESTRUCTURAL ESTRICTO DE SALIDA (Sigue exactamente esta secuencia):

I. TABLA I: DATOS INFORMATIVOS (Muestra exactamente: DRE/UGEL: {dre_ugel}, IE: {ie_nombre}, Director: {director}, Subdirector: {subdirector}, Docente: {docente}, Grado/Sección: {grado_seccion}, Duración: {fechas_duracion}).

II. SITUACIÓN SIGNIFICATIVA GENERADA (Ubicada OBLIGATORIAMENTE justo debajo de los Datos Informativos).

III. MATRIZ DE APRENDIZAJES POR ÁREA (SECCIÓN CONTINUA COMPLETA DESDE LA SEMANA 1 HASTA LA SEMANA {duracion_semanas}):
    - Para CADA una de las {duracion_semanas} semanas, coloca el **TÍTULO CREATIVO DE LA ACTIVIDAD DE LA SEMANA** (Ejemplo: SEMANA 1: "Desarrollamos hábitos de limpieza en nuestro entorno").
    - Debajo del título de la semana, presenta la Matriz de Aprendizajes en sus 8 COLUMNAS EXACTAS:
      | ÁREA | ACTIVIDAD | COMPETENCIA Y CAPACIDADES | ESTÁNDAR DE APRENDIZAJE | DESEMPEÑO PRECISADO | CRITERIOS DE EVALUACIÓN | EVIDENCIA | INSTRUMENTO DE EVALUACIÓN |
    - REGLA OBLIGATORIA DEL ESTÁNDAR: Copia el **ESTÁNDAR DE APRENDIZAJE EN SU TOTALIDAD Y DE MANERA ÍNTEGRA** tal cual figura en el CNEB oficial (RM N.º 649-2016-MINEDU) sin ningún corte ni resumen, y RESALTA EN **NEGRITA** (`**la parte específica movilizada en la actividad**`).
    - Copia el DESEMPEÑO ÍNTEGRO del CNEB con la parte trabajada en **negrita**.
    - REGLA OBLIGATORIA DE COBERTURA DE ÁREAS EN LA MATRIZ: En cada una de las {duracion_semanas} semanas, debes incluir OBLIGATORIAMENTE filas para TODAS Y CADA UNA DE LAS ÁREAS CURRICULARES SIN EXCEPCIÓN: Comunicación (3 comp.), Matemática (4 comp.), Personal Social, Ciencia y Tecnología, Educación Religiosa, Arte y Cultura, Educación Física y Tutoría / Competencias Transversales.

IV. SECUENCIA DE ACTIVIDADES PROPUESTAS (SECCIÓN COMPLETA DESDE LA SEMANA 1 HASTA LA SEMANA {duracion_semanas}):
    - Presenta esta sección OBLIGATORIAMENTE AL TÉRMINO DE TODA LA MATRIZ DE APRENDIZAJES.
    - Para cada semana (Semana 1 a {duracion_semanas}), coloca el **TÍTULO DE LA SEMANA** y crea una TABLA OBLIGATORIA donde LAS COLUMNAS SEAN LOS DÍAS DE LA SEMANA:
      | LUNES | MARTES | MIÉRCOLES | JUEVES | VIERNES |
    - En cada casillero diario, programa de 2 a 3 sesiones de 90 minutos en turno único (sin dividir en mañana/tarde), indicando el **ÁREA CURRICULAR DESTACADA**:
      • Sesión 1 (90 min): **[ÁREA]**: [Competencia específica] - [Actividad en 1ª persona plural]
      • Sesión 2 (90 min): **[ÁREA]**: [Competencia específica] - [Actividad en 1ª persona plural]
      • Sesión 3 (90 min, si aplica): **[ÁREA]**: [Competencia específica] - [Actividad en 1ª persona plural]
    - REGLA OBLIGATORIA DE ÁREAS EN LA SECUENCIA DE ACTIVIDADES: En la tabla semanal de actividades, DEBES DISTRIBUIR Y CONSIDERAR OBLIGATORIAMENTE TODAS Y CADA UNA DE LAS ÁREAS CURRICULARES EN CADA SEMANA SIN EXCEPCIÓN.
    - Cierra respondiendo a: ¿Qué productos lograré en esta experiencia?

V. TABLA DE ENFOQUES TRANSVERSALES.
VI. PRODUCTO DE LA UNIDAD.
VII. LISTA CLASIFICADA DE MATERIALES Y RECURSOS.
VIII. TABLA VIII: REFLEXIONES SOBRE LOS APRENDIZAJES (Tabla final obligatoria).
"""

# ==============================================================================
# EJECUCIÓN CON GOOGLE AI STUDIO (GEMINI API)
# ==============================================================================
st.markdown("---")

if st.button(f"✨ Generar {tipo_documento} en Word"):
    if not api_key:
        st.error("⚠️ Ingresa tu API Key de Google AI Studio en la barra lateral izquierda o en los Secrets.")
    elif not problema_contexto:
        st.warning("⚠️ Completa el campo del Tema o Problema del Contexto.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            
            if tipo_documento == "Sesión de Aprendizaje":
                prompt_maestro = generar_prompt_sesion()
                sys_inst = "Eres un Especialista Curricular de Educación Primaria del MINEDU Perú. Creas sesiones de aprendizaje en tablas sin incluir situación significativa, incluyendo datos informativos en 2 columnas, propósitos de aprendizaje, enfoques, competencia transversal, meta de aprendizaje, preparación, momentos con procesos didácticos del área en 1ra persona plural tiempo presente, y escala de valoración con 30 estudiantes ficticios."
            elif tipo_documento == "Ficha de Aplicación / Trabajo (Para Alumnos)":
                prompt_maestro = generar_prompt_ficha_trabajo()
                sys_inst = "Eres un Especialista Curricular y Diseñador de Material Educativo de Educación Primaria del MINEDU Perú. Creas fichas de trabajo aplicando el proceso didáctico del área elegida. Muestras 'DATOS INFORMATIVOS' y 'PROPÓSITO DE HOY' obligatoriamente como SUBTÍTULOS FUERA DE LAS TABLAS. PROHIBIDO USAR ETIQUETAS HTML COMO <tr>, <td>, <th>, <table>, <tbody>."
            elif tipo_documento == "Proyecto de Aprendizaje":
                prompt_maestro = generar_prompt_proyecto()
                sys_inst = "Eres un Especialista Curricular de Educación Primaria del MINEDU Perú."
            else:
                prompt_maestro = generar_prompt_unidad_sara()
                sys_inst = "Eres un Especialista Curricular de Educación Primaria del MINEDU Perú."
                
            with st.spinner(f"🧠 Google Gemini ({model_choice}) está procesando y generando tu {tipo_documento} para {grado_seccion}..."):
                
                config = types.GenerateContentConfig(
                    system_instruction=sys_inst,
                    temperature=0.2
                )
                
                try:
                    response = client.models.generate_content(
                        model=model_choice,
                        contents=prompt_maestro,
                        config=config
                    )
                except Exception as model_err:
                    err_text = str(model_err)
                    if "404" in err_text or "NOT_FOUND" in err_text:
                        response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            contents=prompt_maestro,
                            config=config
                        )
                    else:
                        raise model_err
                
                # GUARDAR RESULTADO EN SESSION STATE (MEMORIA PERMANENTE)
                st.session_state['resultado_md'] = response.text
                st.session_state['tipo_doc_generado'] = tipo_documento
                st.session_state['fname_clean'] = f"{tipo_documento.replace(' ', '_')}_N{num_doc}_{grado_seccion.replace(' ', '_')}.docx"
                st.session_state['ie_nombre_generado'] = ie_nombre
                
                st.success(f"✅ ¡{tipo_documento} generado con éxito y guardado en memoria!")

        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                st.warning("⏳ **Límite de velocidad alcanzado.** Por favor, espera 60 segundos y vuelve a intentarlo o cambia de modelo en la barra lateral.")
            elif "404" in err_str or "NOT_FOUND" in err_str:
                st.error("⚠️ El modelo seleccionado no está disponible. Por favor selecciona **gemini-2.0-flash** o **gemini-2.5-flash** en la barra lateral.")
            else:
                st.error(f"❌ Ocurrió un error con la API de Google AI Studio: {err_str}")

# ==============================================================================
# DESPLIEGUE DE VISTA PREVIA Y DESCARGA PERMANENTE
# ==============================================================================
if st.session_state['resultado_md'] is not None:
    st.markdown("---")
    
    tab_preview, tab_download = st.tabs(["📄 Vista Previa (Permanente)", "📥 Descargar Word (.docx)"])
    
    with tab_preview:
        st.markdown(st.session_state['resultado_md'])
        
    with tab_download:
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
        st.info("💡 **Nota:** La vista previa en pantalla permanecerá visible. El documento Word generado incluye la estructura oficial solicitada en tablas.")
