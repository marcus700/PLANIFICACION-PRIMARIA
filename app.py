import streamlit as st
from google import genai
from google.genai import types
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
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

# Modelos oficiales vigentes de Google AI Studio (Incluye Gemini 3.6 Flash)
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
• Nivel Educación Primaria (1.° a 6.° Grado)
• Salida editable en Word (.docx)
• Cuadro reservado para insignia de la I.E.
""")

# ==============================================================================
# CONVERTIDOR A WORD (.DOCX) CON CUADRO MANUAL PARA INSIGNIA
# ==============================================================================
def markdown_to_docx(md_text, ie_nombre="I.E. N° 22303"):
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    p_box = doc.add_paragraph()
    p_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_box = p_box.add_run(f"🖼️ [ PEGAR AQUÍ LA INSIGNIA / ESCUDO DE LA {ie_nombre.upper()} ]\n")
    run_box.font.size = Pt(10)
    run_box.font.italic = True
    run_box.font.color.rgb = RGBColor(107, 114, 128)

    lines = md_text.split('\n')
    in_table = False
    table_data = []
    
    for line in lines:
        line_str = line.strip()
        
        if line_str.startswith('|') and line_str.endswith('|'):
            in_table = True
            if re.match(r'^\|[\s\:\-\|]+\|$', line_str):
                continue
            cells = [c.strip() for c in line_str.split('|')[1:-1]]
            table_data.append(cells)
            continue
        elif in_table:
            if table_data:
                rows = len(table_data)
                cols = max(len(r) for r in table_data) if rows > 0 else 0
                if rows > 0 and cols > 0:
                    t = doc.add_table(rows=rows, cols=cols)
                    t.style = 'Table Grid'
                    for r_idx, row_cells in enumerate(table_data):
                        for c_idx, cell_value in enumerate(row_cells):
                            if c_idx < cols:
                                cell = t.cell(r_idx, c_idx)
                                cell.text = cell_value
                                if r_idx == 0:
                                    shading_elm = OxmlElement('w:shd')
                                    shading_elm.set(qn('w:val'), 'clear')
                                    shading_elm.set(qn('w:color'), 'auto')
                                    shading_elm.set(qn('w:fill'), '1E3A8A')
                                    cell._tc.get_or_add_tcPr().append(shading_elm)
                                    for paragraph in cell.paragraphs:
                                        for run in paragraph.runs:
                                            run.font.color.rgb = RGBColor(255, 255, 255)
                                            run.font.bold = True
            in_table = False
            table_data = []

        if line_str.startswith('# '):
            p = doc.add_paragraph()
            run = p.add_run(line_str[2:])
            run.font.size = Pt(16)
            run.font.bold = True
            run.font.color.rgb = RGBColor(30, 58, 138)
        elif line_str.startswith('## '):
            p = doc.add_paragraph()
            run = p.add_run(line_str[3:])
            run.font.size = Pt(14)
            run.font.bold = True
            run.font.color.rgb = RGBColor(30, 58, 138)
        elif line_str.startswith('### '):
            p = doc.add_paragraph()
            run = p.add_run(line_str[4:])
            run.font.size = Pt(12)
            run.font.bold = True
            run.font.color.rgb = RGBColor(55, 65, 81)
        elif line_str.startswith('• ') or line_str.startswith('- '):
            p = doc.add_paragraph(style='List Bullet')
            p.add_run(line_str[2:])
        elif line_str != "":
            p = doc.add_paragraph()
            p.add_run(line_str)
            
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
    f1, f2, f3 = st.columns(3)
    with f1:
        area_sel = st.selectbox("Área Curricular:", cneb.obtener_lista_areas(), index=0)
    with f2:
        tema_titulo = st.text_input("Título del Tema / Sesión:", "Leemos un afiche sobre el cuidado del agua")
    with f3:
        fecha_sugerida = st.text_input("Fecha:", "05 de mayo de 2026")
        duracion_semanas = 1
    
    situacion_significativa = st.text_area(
        "Propósito o Contexto de la Clase:",
        height=90,
        value="Los estudiantes del 3er grado necesitan comprender la estructura y función de los afiches para identificar información explícita e implícita sobre la conservación del agua en la escuela."
    )

elif tipo_documento == "Proyecto de Aprendizaje":
    f1, f2 = st.columns(2)
    with f1:
        tema_titulo = st.text_input("Título del Proyecto:", "Nos organizamos y celebramos con alegría nuestro aniversario escolar")
    with f2:
        fechas_duracion = st.text_input("Fechas / Duración:", "Del 11 de marzo al 12 de abril de 2026 (4 Semanas)")
        duracion_semanas = st.slider("Número de Semanas del Proyecto:", min_value=2, max_value=5, value=4)
        area_sel = "Multidisciplinar"

    situacion_significativa = st.text_area(
        "Situación Significativa del Proyecto:",
        height=100,
        value="Los estudiantes del 3er grado están próximos a celebrar el aniversario de su escuela. Se plantea el reto: ¿Cómo nos organizamos para celebrar nuestro aniversario cuidando el ambiente escolar? Los estudiantes elaborarán un periódico mural y organizarán un festival de talentos."
    )

else:  # Unidad SARA
    f1, f2 = st.columns(2)
    with f1:
        tema_titulo = st.text_input("Título de la Unidad SARA:", "Desarrollamos actividades ecoeficientes para mejorar nuestro ambiente escolar")
    with f2:
        fechas_duracion = st.text_input("Fechas / Duración:", "Del 01 de abril al 03 de mayo de 2026 (5 Semanas)")
        duracion_semanas = st.slider("Número de Semanas de la Unidad:", min_value=2, max_value=5, value=5)
        area_sel = "Multidisciplinar"

    situacion_significativa = st.text_area(
        "Situación Significativa de la Unidad SARA:",
        height=100,
        value="En la comunidad se evidencia aumento de residuos plásticos. Los niños se preguntan: ¿Qué acciones ecoeficientes podemos poner en práctica? Elaborarán tachos de reciclaje, carteles ecológicos y un huerto escolar."
    )

# ==============================================================================
# PROMPTS
# ==============================================================================
def generar_prompt_sesion():
    return f"""
Actúa como: Especialista en CNEB MINEDU Perú, experto en planificación de Educación Primaria de Aula.
Elabora una Sesión de Aprendizaje completa según el modelo CNEB.

DATOS: Grado: {grado_seccion} | Área: {area_sel} | Tema: {tema_titulo} | Fecha: {fecha_sugerida} | IE: {ie_nombre} | Docente: {docente}
Contexto: {situacion_significativa}

REGLAS OBLIGATORIAS:
1. Cuadros/Tablas para: Datos Informativos, Propósitos CNEB, Enfoques Transversales, Competencia Transversal, Metas de Aprendizaje, Preparación, Momentos y Escala de Valoración.
2. Redacción de actividades en PRIMERA PERSONA DEL PLURAL Y TIEMPO PRESENTE ("Saludamos", "Preguntamos", "Repartimos").
3. Procesos Pedagógicos en INICIO (20 min): Problematización, Propósito, Motivación, Saberes Previos, Criterios y Normas.
4. Procesos Didácticos Específicos del Área {area_sel} en DESARROLLO (60 min).
5. CIERRE (10 min): Metacognición y Reflexión.
6. ESCALA DE VALORACIÓN: Tabla final para 10 estudiantes ficticios peruanos.
"""

def generar_prompt_ficha_trabajo():
    return f"""
Actúa como un Docente de Primaria experto del MINEDU Perú.
Crea una FICHA DE APLICACIÓN / TRABAJO PARA EL ESTUDIANTE lista para imprimir.

DATOS DE LA FICHA:
• Institución Educativa: {ie_nombre}
• Grado y Sección: {grado_seccion}
• Área: {area_sel}
• Tema: {tema_titulo}
• Estudiante: _____________________________________ Fecha: {fecha_sugerida}

ESTRUCTURA DE LA FICHA EN MARKDOWN:
1. Encabezado llamativo con título de la ficha y propósito para el niño.
2. Breve texto/resumen ilustrativo o caso práctico adaptado a niños de {grado_seccion}.
3. Sección 1: "Comprendo lo que leí / lo que aprendí" (3 preguntas de respuesta libre o verdadero/falso).
4. Sección 2: "Aplico lo aprendido" (3 actividades prácticas: unir con líneas, marcar la opción correcta, completar tablas o esquemas).
5. Sección 3: "Reto Creativo / Mi Compromiso" (Una actividad de dibujo o redacción personal corta).
6. Sección de Autoevaluación para el niño (*Caritas o semáforo de aprendizaje* con 2 criterios sencillos).
"""

def generar_prompt_proyecto():
    return f"""
Actúa como un docente especialista de Primaria MINEDU Perú. Elabora un PROYECTO DE APRENDIZAJE completo.
DATOS: IE: {ie_nombre} | Docente: {docente} | Grado: {grado_seccion} | Duración: {fechas_duracion} | Título: "{tema_titulo}"
Situación Significativa: {situacion_significativa}

Estructura:
1. Datos Informativos (Tabla)
2. Situación Significativa
3. Planificación del Proyecto (Tabla para el estudiante: ¿Qué haremos?, ¿Qué sabemos?, ¿Qué queremos saber?, ¿Cómo lo haremos?, ¿Qué necesitamos?, ¿Cómo nos organizamos?)
4. Propósitos de Aprendizaje por cada una de las {duracion_semanas} semanas (Tablas completas por semana para todas las áreas con estándar completo, desempeño en negrita, criterios, evidencia e instrumento).
5. Enfoques Transversales (Tabla)
6. Producto Final Tangible
7. Secuencia de Actividades diarias por semana (Lunes a Viernes en 1ra persona plural)
8. Materiales y Recursos (Clasificados)
9. Reflexiones sobre los aprendizajes
"""

def generar_prompt_unidad_sara():
    return f"""
Actúa como docente especialista de Primaria MINEDU Perú. Elabora una UNIDAD DE APRENDIZAJE (Modelo SARA).
DATOS: IE: {ie_nombre} | Docente: {docente} | Grado: {grado_seccion} | Duración: {fechas_duracion} | Título: "{tema_titulo}"
Situación Significativa: {situacion_significativa}

Estructura:
I. Datos Informativos (Tabla)
II. Situación Significativa
III. Matriz de Aprendizajes por Área (Tabla por área con estándar completo en fila superior, columnas: Actividad en 1ra persona plural, Competencia/Capacidad, Desempeño con negrita, Criterios de Evaluación Acción+Contenido+Condición, Evidencia, Lista de cotejo).
IV. Enfoques Transversales (Tabla)
V. Producto de la Unidad
VI. Actividades Propuestas semanales (Lunes a Viernes) cerrando con la pregunta: ¿Qué productos lograré en esta experiencia?
VII. Materiales y Recursos
VIII. Reflexiones sobre los Aprendizajes
"""

# ==============================================================================
# EJECUCIÓN CON GOOGLE AI STUDIO (GEMINI API)
# ==============================================================================
st.markdown("---")

if st.button(f"✨ Generar {tipo_documento} en Word"):
    if not api_key:
        st.error("⚠️ Ingresa tu API Key de Google AI Studio en la barra lateral izquierda o en los Secrets.")
    elif not situacion_significativa or not tema_titulo:
        st.warning("⚠️ Completa los campos obligatorios del formulario.")
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
                
            with st.spinner(f"🧠 Google Gemini ({model_choice}) está generando tu {tipo_documento} para {grado_seccion}..."):
                
                config = types.GenerateContentConfig(
                    system_instruction="Eres un Especialista Curricular de Educación Primaria de Aula del MINEDU Perú. Generas documentos pedagógicos impecables en Markdown con tablas perfeccionadas.",
                    temperature=0.2
                )
                
                # Intentar primero con el modelo seleccionado por el usuario
                try:
                    response = client.models.generate_content(
                        model=model_choice,
                        contents=prompt_maestro,
                        config=config
                    )
                except Exception as model_err:
                    err_text = str(model_err)
                    # Respaldo automático si el modelo seleccionado no responde o se agota cuota
                    if "404" in err_text or "NOT_FOUND" in err_text:
                        response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            contents=prompt_maestro,
                            config=config
                        )
                    else:
                        raise model_err
                
                resultado_md = response.text
                
                st.success(f"✅ ¡{tipo_documento} generado con éxito!")
                
                tab_preview, tab_download = st.tabs(["📄 Vista Previa", "📥 Descargar Word (.docx)"])
                
                with tab_preview:
                    st.markdown(resultado_md)
                    
                with tab_download:
                    fname_clean = f"{tipo_documento.replace(' ', '_')}_{grado_seccion.replace(' ', '_')}.docx"
                    buffer_doc = markdown_to_docx(resultado_md, ie_nombre=ie_nombre)
                    
                    st.download_button(
                        label=f"💾 Descargar {tipo_documento} en Word (.docx)",
                        data=buffer_doc,
                        file_name=fname_clean,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                    st.info(f"💡 **Nota:** El archivo Word descargado incluye el cuadro `🖼️ [ PEGAR AQUÍ LA INSIGNIA / ESCUDO DE LA {ie_nombre.upper()} ]` en la parte superior para que el docente pegue manualmente la insignia de su colegio.")

        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                st.warning("⏳ **Límite de velocidad del plan gratuito alcanzado.**\n\nPor favor, **espera 60 segundos** y vuelve a hacer clic en el botón de generación, o cambia el **Modelo de Gemini** en la barra lateral por otro modelo disponible.")
            elif "404" in err_str or "NOT_FOUND" in err_str:
                st.error("⚠️ El modelo seleccionado no está disponible para tu cuenta de Google AI. Por favor selecciona **gemini-2.0-flash** o **gemini-3.6-flash** en la barra lateral.")
            else:
                st.error(f"❌ Ocurrió un error con la API de Google AI Studio: {err_str}")
