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
    page_title="PlanificaPrimaria - Plataforma para Docentes de Aula",
    page_icon="🍎",
    layout="wide"
)

st.markdown("""
<style>
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
    .stButton>button {
        background-color: #2563EB;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        width: 100%;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🍎 PlanificaPrimaria - Sistema para Docentes de Aula</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Plataforma Inteligente de Planificación Curricular para Educación Primaria (CNEB - MINEDU)</div>', unsafe_allow_html=True)

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

# ==============================================================================
# BARRA LATERAL (SIDEBAR) - LECTURA DE API KEY Y MODELOS
# ==============================================================================
st.sidebar.title("⚙️ Configuración")

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
st.sidebar.markdown("### 📋 Herramientas de Aula")
tipo_documento = st.sidebar.radio(
    "Selecciona la herramienta:",
    [
        "Sesión de Aprendizaje", 
        "Proyecto de Aprendizaje", 
        "Unidad de Aprendizaje (Modelo SARA)",
        "Ficha de Aplicación / Trabajo (Para Alumnos)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Alineamiento CNEB Perú:**
• RM N.° 649-2016-MINEDU
• Unidades y Proyectos en Orientación HORIZONTAL
• Columna explícita de ÁREA Curricular
• 2 Sesiones diarias (10 por semana)
• Tablas en Colores Pasteles Variados
""")

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
# CONVERTIDOR A WORD (.DOCX) CON SOPORTE PARA ORIENTACIÓN HORIZONTAL
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
        
        # Limpieza de etiquetas HTML indeseadas (<br>, <br/>, etc.)
        line_str = re.sub(r'<br\s*/?>', ' ', line_str)
        line_str = re.sub(r'</?[a-zA-Z0-9]+\s*/>', ' ', line_str)
        
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

    # GARANTIZAR QUE LA ÚLTIMA TABLA (EJ. TABLA DE REFLEXIONES) SE PROCESE E IMPRIMA EN WORD
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
    ie_nombre = st.text_input("Institución Educativa:", "N° 22303 'Santa Rosa de Lima'")
with c2:
    director = st.text_input("Director:", "Lic. Bernardo Francisco Salcedo Barrientos")
    subdirector = st.text_input("Subdirector(es):", "Mg. Mariela Velásquez Cárdenas / Mg. Frank Bernaola Pérez")
with c3:
    docente = st.text_input("Docente de Aula:", "Sara María Quiroz Rodríguez")
    grado_seccion = st.selectbox("Grado y Sección:", ["1er Grado A", "2do Grado A", "3er Grado A", "4to Grado A", "5to Grado A", "6to Grado A"], index=2)

if tipo_documento in ["Sesión de Aprendizaje", "Ficha de Aplicación / Trabajo (Para Alumnos)"]:
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        num_doc = st.text_input("N.° de Sesión:", "01")
    with f2:
        area_sel = st.selectbox("Área Curricular:", cneb.obtener_lista_areas(), index=0)
    with f3:
        fecha_sugerida = st.text_input("Fecha:", "05 de mayo de 2026")
    with f4:
        duracion_sesion = st.selectbox("Duración:", ["45 minutos", "90 minutos", "135 minutos"], index=1)
    
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

# CAMPO SIMPLIFICADO: El docente solo ingresa el Problema del Contexto
problema_contexto = st.text_area(
    "🚨 Problema o Interés del Contexto (Único dato requerido para que la IA cree el Título y la Situación Significativa automáticamente):",
    height=100,
    value="Poco hábito de recolección de residuos sólidos y acumulación de botellas de plástico en el patio durante el recreo por parte de los estudiantes de 3er grado."
)

# Título Opcional
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
        t_inicio, t_desarrollo, t_cierre = "15 min", "65 min", "10 min"

    val_titulo = f'"{titulo_opcional}"' if titulo_opcional.strip() else 'Crea un TÍTULO corto y motivador basado en el problema.'

    return f"""
Actúa como: Especialista en CNEB MINEDU Perú, experto en planificación de Educación Primaria de Aula.
Elabora una Sesión de Aprendizaje completa y estructurada strictly en CUADROS/TABLAS.

A PARTIR DEL PROBLEMA DEL CONTEXTO:
{problema_contexto}
Instrucción de Título: {val_titulo}
Instrucción de Situación Significativa: Redacta una Situación Significativa estructurada a partir del problema.

ENCABEZADO DE SALIDA OBLIGATORIO:
# **SESIÓN DE APRENDIZAJE N.º {num_doc}**
## **[INSERTAR AQUÍ EL TÍTULO GENERADO]**

DATOS: Grado: {grado_seccion} | Área: {area_sel} | Fecha: {fecha_sugerida} | Duración Total: {duracion_sesion} | IE: {ie_nombre} | Docente: {docente}

REGLAS OBLIGATORIAS DE ESTÁNDAR, COMPETENCIA Y DESEMPEÑO DEL CNEB:
1. **COLUMNA DE ÁREA:** Incluye la columna **ÁREA** explícitamente en las tablas.
2. **UNA SOLA COMPETENCIA:** Coloca ÚNICAMENTE la competencia específica que se aborda en la actividad (NO listes todas las competencias del área).
3. **COLUMNA DEDICADA PARA EL ESTÁNDAR:** En la Tabla II, el **ESTÁNDAR DE APRENDIZAJE** debe tener su propia COLUMNA DEDICADA, copiando el texto oficial del CNEB de manera ÍNTEGRA Y LITERAL, y RESALTANDO EN **NEGRITA** (`**la parte específica del estándar que se moviliza en la sesión**`).
4. **DESEMPEÑO ÍNTEGRO Y PRECISADO:** Copia el desempeño oficial del CNEB de manera ÍNTEGRA y RESALTA EN **NEGRITA** (`**la parte específica del desempeño que se evalúa en la sesión**`).
5. PROHIBIDO UTILIZAR símbolos de almohadillas como #### o ##### o ###### para títulos.
6. NO UTILICES etiquetas HTML como <br> o <br/>. Usa únicamente saltos de línea normales.
7. ESTRUCTURA EN TABLAS/CUADROS OBLIGATORIOS:
   - Tabla I: DATOS INFORMATIVOS
   - Tabla II: PROPÓSITOS DE APRENDIZAJE Y EVIDENCIAS. Columnas estrictas: 
     ÁREA | COMPETENCIA TRABAJADA (Solo una) Y CAPACIDADES | ESTÁNDAR DE APRENDIZAJE (Columna dedicada con CNEB completo y parte trabajada en **negrita**) | DESEMPEÑO PRECISADO (CNEB completo con parte trabajada en **negrita**) | CRITERIOS DE EVALUACIÓN | PROPÓSITO DE LA SESIÓN | EVIDENCIA DE APRENDIZAJE | INSTRUMENTO DE EVALUACIÓN.
   - Tabla III: ENFOQUES TRANSVERSALES
   - Tabla IV: COMPETENCIA TRANSVERSAL ("Gestiona su aprendizaje de manera autónoma")
   - Tabla V: META DE APRENDIZAJE
   - Tabla VI: PREPARACIÓN DE LA SESIÓN
   - Tabla VII: ESCALA DE VALORACIÓN (Cuadro para 10 estudiantes ficticios peruanos)

8. FORMATO DE LOS MOMENTOS Y PROCESOS DE LA SESIÓN:
   - Resalta en **NEGRITA** los títulos principales (**INICIO ({t_inicio})**, **DESARROLLO ({t_desarrollo})**, **CIERRE ({t_cierre})**) y cada uno de los procesos pedagógicos/didácticos.
   - Cada actividad, pregunta o consigna DEBE INICIAR OBLIGATORIAMENTE CON SU SUBTÍTULO EN NEGRITA Y LUEGO VIÑETA (`•`).
   - Redacción de actividades en PRIMERA PERSONA DEL PLURAL Y TIEMPO PRESENTE ("Saludamos a los niños", "Preguntamos a los estudiantes").
"""

def generar_prompt_ficha_trabajo():
    val_titulo = f'"{titulo_opcional}"' if titulo_opcional.strip() else 'Crea un TÍTULO corto y motivador basado en el problema.'

    return f"""
Actúa como un Docente de Primaria experto del MINEDU Perú.
Crea una FICHA DE APLICACIÓN / TRABAJO PARA EL ESTUDIANTE lista para imprimir.
PROHIBIDO usar símbolos #### o ##### y etiquetas HTML. Usa Markdown limpio y cuadros.

A PARTIR DEL PROBLEMA DEL CONTEXTO:
{problema_contexto}
Instrucción de Título: {val_titulo}

ENCABEZADO DE SALIDA OBLIGATORIO:
# **FICHA DE TRABAJO N.º {num_doc}**
## **[INSERTAR AQUÍ EL TÍTULO GENERADO]**

DATOS DE LA FICHA:
• Institución Educativa: {ie_nombre}
• Grado y Sección: {grado_seccion}
• Área: {area_sel}
• Estudiante: _____________________________________ Fecha: {fecha_sugerida}

ESTRUCTURA DE LA FICHA EN MARKDOWN (INCLUIR TABLAS PARA EJERCICIOS Y AUTOEVALUACIÓN):
1. Encabezado llamativo en un cuadro con título de la ficha y propósito para el niño.
2. Breve texto/resumen ilustrativo o caso práctico adaptado a niños de {grado_seccion}.
3. Sección 1: "Comprendo lo que leí / lo que aprendí" (3 preguntas).
4. Sección 2: "Aplico lo aprendido" (3 actividades prácticas en tablas/cuadros).
5. Sección 3: "Reto Creativo / Mi Compromiso".
6. Tabla de Autoevaluación para el niño.
"""

def generar_prompt_proyecto():
    val_titulo = f'"{titulo_opcional}"' if titulo_opcional.strip() else 'Crea un TÍTULO innovador y creativo para el proyecto basado en el problema.'

    return f"""
Actúa como un docente especialista de Primaria MINEDU Perú. Elabora un PROYECTO DE APRENDIZAJE completo.
PROHIBIDO usar símbolos #### o ##### y etiquetas HTML. Usa Markdown limpio y estructura estrictamente en TABLAS Y CUADROS.

A PARTIR DEL PROBLEMA DEL CONTEXTO DEL DOCENTE:
{problema_contexto}

OBLIGATORIO - GENERACIÓN AUTOMÁTICA DE TÍTULO Y SITUACIÓN SIGNIFICATIVA:
1. Genera un TÍTULO del proyecto: {val_titulo}
2. Redacta la SITUACIÓN SIGNIFICATIVA COMPLETA estructurada en 3 párrafos.

ENCABEZADO DE SALIDA OBLIGATORIO:
# **PROYECTO DE APRENDIZAJE N.º {num_doc}**
## **[INSERTAR AQUÍ EL TÍTULO GENERADO]**

ESTRUCTURA DEL PROYECTO DE APRENDIZAJE:
1. Tabla de Datos Informativos.
2. Situación Significativa Generada.
3. Planificación del Proyecto (Tabla para el estudiante: ¿Qué haremos?, ¿Qué sabemos?, ¿Qué queremos saber?, ¿Cómo lo haremos?, ¿Qué necesitamos?, ¿Cómo nos organizamos?).
4. Propósitos de Aprendizaje por cada una de las {duracion_semanas} semanas:
   - En la Matriz de Aprendizajes, incluye OBLIGATORIAMENTE las siguientes columnas:
     ÁREA | ACTIVIDAD | COMPETENCIA TRABAJADA (Solo una) Y CAPACIDADES | ESTÁNDAR DE APRENDIZAJE (Columna dedicada con CNEB completo y parte movilizada en **negrita**) | DESEMPEÑO PRECISADO (CNEB completo con parte trabajada en **negrita**) | CRITERIOS DE EVALUACIÓN | EVIDENCIA | INSTRUMENTO.
   - Cobertura Curricular Obligatoria: Distribuye las **4 competencias de Matemática**, las **3 competencias de Comunicación**, **Educación Religiosa**, **Arte y Cultura**, **Educación Física** y **Competencias Transversales**.
5. Tabla de Enfoques Transversales.
6. Producto Final Tangible del Proyecto.
7. SECUENCIA DE ACTIVIDADES CON LOS DÍAS COMO COLUMNAS DE TABLA (2 SESIONES DIARIAS - 10 SESIONES POR SEMANA):
   - Para cada semana (Semana 1 a {duracion_semanas}), crea una TABLA OBLIGATORIA donde LAS COLUMNAS SEAN LOS DÍAS DE LA SEMANA:
     | LUNES | MARTES | MIÉRCOLES | JUEVES | VIERNES |
   - En cada casillero diario, indica de forma obligatoria el **ÁREA CURRICULAR DESTACADA**:
     • Fila 1 (Sesión 1 / Mañana): **[ÁREA]**: [Competencia específica] - [Actividad en 1ª persona plural]
     • Fila 2 (Sesión 2 / Tarde): **[ÁREA]**: [Competencia específica] - [Actividad en 1ª persona plural]
8. Lista Clasificada de Materiales y Recursos.
9. Tabla de Reflexiones sobre los aprendizajes (Estructurada obligatoriamente en Cuadro/Tabla final).
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

ENCABEZADO DE SALIDA OBLIGATORIO:
# **UNIDAD DE APRENDIZAJE N.º {num_doc}**
## **[INSERTAR AQUÍ EL TÍTULO GENERADO]**

ESTRUCTURA DE LA UNIDAD DE APRENDIZAJE SARA:
I. Tabla de Datos Informativos.
II. Situación Significativa Generada.
III. Matriz de Aprendizajes por Área:
    - Incluye OBLIGATORIAMENTE las siguientes columnas en la tabla:
      ÁREA | ACTIVIDAD en 1ra persona plural | COMPETENCIA TRABAJADA (Solo una) Y CAPACIDADES | ESTÁNDAR DE APRENDIZAJE (Columna dedicada con CNEB completo y parte movilizada en **negrita**) | DESEMPEÑO PRECISADO (CNEB completo con parte trabajada en **negrita**) | CRITERIOS DE EVALUACIÓN | EVIDENCIA | LISTA DE COTEJO.
    - Cobertura Curricular Obligatoria: Integra las **4 competencias de Matemática**, las **3 competencias de Comunicación**, **Educación Religiosa**, **Arte y Cultura**, **Educación Física** y **Competencias Transversales**.
IV. Tabla de Enfoques Transversales.
V. Producto de la Unidad.
VI. ACTIVIDADES PROPUESTAS CON LOS DÍAS COMO COLUMNAS DE TABLA (2 SESIONES DIARIAS - 10 SESIONES POR SEMANA):
    - Para cada semana (Semana 1 a {duracion_semanas}), crea una TABLA OBLIGATORIA donde LAS COLUMNAS SEAN LOS DÍAS DE LA SEMANA:
      | LUNES | MARTES | MIÉRCOLES | JUEVES | VIERNES |
    - En cada casillero diario, indica de forma obligatoria el **ÁREA CURRICULAR DESTACADA**:
      • Fila 1 (Sesión 1): **[ÁREA]**: [Competencia específica] - [Actividad en 1ª persona plural]
      • Fila 2 (Sesión 2): **[ÁREA]**: [Competencia específica] - [Actividad en 1ª persona plural]
    - Cierra respondiendo a: ¿Qué productos lograré en esta experiencia?
VII. Lista Clasificada de Materiales y Recursos.
VIII. Tabla de Reflexiones sobre los Aprendizajes (Estructurada obligatoriamente en Cuadro/Tabla final).
"""

# ==============================================================================
# EJECUCIÓN CON GOOGLE AI STUDIO (GEMINI API)
# ==============================================================================
st.markdown("---")

if st.button(f"✨ Generar {tipo_documento} en Word"):
    if not api_key:
        st.error("⚠️ Ingresa tu API Key de Google AI Studio en la barra lateral izquierda o en los Secrets.")
    elif not problema_contexto:
        st.warning("⚠️ Completa el campo del Problema o Interés del Contexto.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            
            if tipo_documento == "Sesión de Aprendizaje":
                prompt_maestro = generar_prompt_sesion()
            elif tipo_documento == "Ficha de Aplicación / Trabajo (Para Alumnos)":
                prompt_maestro = generar_prompt_ficha_trabajo()
            elif tipo_documento == "Proyecto de Aprendizaje":
                prompt_maestro = generar_prompt_proyecto()
            else:
                prompt_maestro = generar_prompt_unidad_sara()
                
            with st.spinner(f"🧠 Google Gemini ({model_choice}) está analizando el problema, organizando la columna ÁREA, Estándares en columna dedicada, días en columnas y aplicando colores pasteles para {grado_seccion}..."):
                
                config = types.GenerateContentConfig(
                    system_instruction="Eres un Especialista Curricular de Educación Primaria de Aula del MINEDU Perú. Muestras la columna ÁREA de forma explícita, incluyes Educación Física, transcribes Estándares y Desempeños del CNEB en negrita, colocas una sola competencia por actividad, organizas los días en columnas y aplicas tonos pasteles en todas las tablas sin omitir la tabla final de reflexiones.",
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
                st.warning("⏳ **Límite de velocidad del plan gratuito alcanzado.**\n\nPor favor, **espera 60 segundos** y vuelve a hacer clic en el botón de generación, o cambia el **Modelo de Gemini** en la barra lateral por otro modelo disponible.")
            elif "404" in err_str or "NOT_FOUND" in err_str:
                st.error("⚠️ El modelo seleccionado no está disponible para tu cuenta de Google AI. Por favor selecciona **gemini-2.0-flash** o **gemini-3.6-flash** en la barra lateral.")
            else:
                st.error(f"❌ Ocurrió un error con la API de Google AI Studio: {err_str}")

# ==============================================================================
# DESPLIEGUE DE VISTA PREVIA Y DESCARGA PERMANENTE (NUNCA DESAPARECE)
# ==============================================================================
if st.session_state['resultado_md'] is not None:
    st.markdown("---")
    
    tab_preview, tab_download = st.tabs(["📄 Vista Previa (Permanente)", "📥 Descargar Word (.docx)"])
    
    with tab_preview:
        st.markdown(st.session_state['resultado_md'])
        
    with tab_download:
        # Determinar si el documento debe ser HORIZONTAL (Unidades y Proyectos) o VERTICAL (Sesiones y Fichas)
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
        st.info("💡 **Nota:** La vista previa en pantalla permanecerá visible de forma continua y el archivo Word descargado incluye la orientación HORIZONTAL para Unidades y Proyectos, garantizando la impresión completa de todas las tablas.")
