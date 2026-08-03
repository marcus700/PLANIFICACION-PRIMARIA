# cneb_primaria_datos.py
"""
Base de Datos Oficial del Currículo Nacional de la Educación Básica (CNEB)
Nivel Educación Primaria - RM N.º 649-2016-MINEDU / Ministerio de Educación del Perú.
Contiene Áreas Curriculares, Competencias, Capacidades, Estándares por Ciclo (III, IV, V)
y Desempeños por Grado (1.° a 6.°).
"""

def obtener_ciclo_por_grado(grado: str) -> str:
    """Devuelve el ciclo (III, IV o V) según el grado ingresado."""
    g = str(grado).lower()
    if "1" in g or "2" in g:
        return "III CICLO"
    elif "3" in g or "4" in g:
        return "IV CICLO"
    elif "5" in g or "6" in g:
        return "V CICLO"
    return "IV CICLO"


CNEB_PRIMARIA = {
    "Personal Social": {
        "competencias": [
            {
                "nombre": "CONSTRUYE SU IDENTIDAD",
                "capacidades": [
                    "Se valora a sí mismo.",
                    "Autorregula sus emociones.",
                    "Reflexiona y argumenta éticamente.",
                    "Vive su sexualidad de manera integral y responsable de acuerdo a su etapa de desarrollo y madurez."
                ],
                "estandares": {
                    "III CICLO": "Construye su identidad al tomar conciencia de los aspectos que lo hacen único, cuando se reconoce a sí mismo a partir de sus características físicas, habilidades y gustos. Se da cuenta que es capaz de realizar tareas y aceptar retos. Disfruta de ser parte de su familia, escuela y comunidad. Reconoce y expresa sus emociones y las regula a partir de la interacción con sus compañeros y docente, y de las normas establecidas de manera conjunta. Explica con razones sencillas por qué algunas acciones cotidianas causan malestar a él o a los demás, y por qué otras producen bienestar a todos. Se reconoce como mujer o varón y explica que ambos pueden realizar las mismas actividades. Muestra afecto a las personas que estima e identifica a las personas que le hacen sentir protegido y seguro y recurre a ellas cuando las necesita.",
                    "IV CICLO": "Construye su identidad al tomar conciencia de los aspectos que lo hacen único, cuando se reconoce a sí mismo a partir de sus características físicas, cualidades, habilidades, intereses y logros y valora su pertenencia familiar y escolar. Distingue sus diversas emociones y comportamientos, menciona las causas y las consecuencias de estos y las regula usando estrategias diversas. Explica con sus propios argumentos por qué considera buenas o malas determinadas acciones. Se relaciona con las personas con igualdad, reconociendo que todos tienen diversas capacidades. Desarrolla comportamientos que fortalecen las relaciones de amistad. Identifica situaciones que afectan su privacidad o la de otros y busca ayuda cuando alguien no la respeta.",
                    "V CICLO": "Construye su identidad al tomar conciencia de los aspectos que lo hacen único, cuando se reconoce a sí mismo a partir de sus características personales, sus capacidades y limitaciones reconociendo el papel de las familias en la formación de dichas características. Aprecia su pertenencia cultural a un país diverso. Explica las causas y consecuencias de sus emociones, y utiliza estrategias para regularlas. Manifiesta su punto de vista frente a situaciones de conflicto moral, en función de cómo estas le afectan a él o a los demás. Examina sus acciones en situaciones de conflicto moral que se presentan en la vida cotidiana y se plantea comportamientos que tomen en cuenta principios éticos. Establece relaciones de igualdad entre hombres y mujeres, y explica su importancia. Crea vínculos afectivos positivos y se sobrepone cuando estos cambian. Identifica conductas para protegerse de situaciones que ponen en riesgo su integridad en relación a su sexualidad."
                },
                "desempenos": {
                    "1° GRADO": [
                        "Expresa de diversas maneras algunas de sus características físicas, cualidades, gustos y preferencias, y las diferencia de las de los demás.",
                        "Comparte con sus compañeros las costumbres y actividades de su familia e institución educativa explicando su participación en ellas.",
                        "Describe, a través de diversas formas de representación, las emociones básicas (alegría, tristeza, miedo u otras) y explica las razones que las originan.",
                        "Autorregula sus emociones en interacción con sus compañeros, con apoyo del docente, al aplicar estrategias básicas de autorregulación.",
                        "Menciona acciones cotidianas que considera buenas o malas, a partir de sus propias experiencias.",
                        "Participa en juegos y otras actividades de la vida cotidiana sin hacer distinciones de género.",
                        "Identifica a las personas que le muestran afecto y lo hacen sentir protegido y seguro; recurre a ellas cuando las necesita."
                    ],
                    "2° GRADO": [
                        "Expresa sus características físicas, habilidades y gustos, y explica las razones de aquello que le agrada de sí mismo.",
                        "Expresa agrado al representar las manifestaciones culturales de su familia, institución educativa y comunidad.",
                        "Describe las emociones a partir de su experiencia y de lo que observa en los demás, y las regula teniendo en cuenta normas establecidas de manera conjunta.",
                        "Identifica acciones que causan malestar o bienestar a sí mismo o a sus compañeros, y las explica con razones sencillas.",
                        "Explica las diferencias y similitudes entre las niñas y los niños, señalando que todos pueden realizar las mismas actividades tanto en la IE como en la casa.",
                        "Dialoga con sus compañeros, con el apoyo del docente, sobre situaciones simuladas o personales en las que haya peligro de vulneración de su espacio personal."
                    ],
                    "3° GRADO": [
                        "Describe aquellas características personales, cualidades, habilidades y logros que hacen que se sienta orgulloso de sí mismo; se reconoce como una persona valiosa con características únicas.",
                        "Comparte las manifestaciones culturales, tradiciones y costumbres propias de su familia que hacen que se sienta orgulloso de su origen.",
                        "Describe sus emociones en situaciones cotidianas; reconoce sus causas y consecuencias. Aplica estrategias de autorregulación.",
                        "Identifica situaciones y comportamientos que le causan agrado o desagrado, y explica de manera sencilla por qué.",
                        "Explica que los niños y las niñas pueden asumir las mismas responsabilidades y tareas, y que pueden establecer lazos de amistad basados en el respeto.",
                        "Reconoce a qué personas puede recurrir en situaciones de riesgo o en situaciones donde se vulnera su privacidad."
                    ],
                    "4° GRADO": [
                        "Describe sus características físicas, cualidades e intereses, y las fortalezas que le permiten lograr sus metas; manifiesta que estas lo hacen una persona única y valiosa.",
                        "Relaciona sus diversas emociones con su comportamiento y el de sus compañeros; menciona causas y consecuencias y las regula.",
                        "Explica con argumentos sencillos por qué considera buenas o malas determinadas acciones o situaciones.",
                        "Se relaciona con niñas y niños con igualdad y respeto, reconoce que puede desarrollar diversas habilidades.",
                        "Identifica situaciones que afectan su privacidad o lo ponen en riesgo, y explica la importancia de buscar ayuda."
                    ],
                    "5° GRADO": [
                        "Explica sus características personales (cualidades, gustos, fortalezas y limitaciones) para definir y fortalecer su identidad.",
                        "Describe sus emociones y explica sus causas y posibles consecuencias. Aplica estrategias de autorregulación.",
                        "Explica las razones de por qué una acción es correcta o incorrecta a partir de sus experiencias y principios éticos.",
                        "Se relaciona con sus compañeros con igualdad, respeto y cuidado del otro; rechaza cualquier manifestación de violencia de género.",
                        "Describe situaciones que ponen en riesgo su integridad, así como las conductas para evitarlas o protegerse."
                    ],
                    "6° GRADO": [
                        "Explica las características personales que tiene por ser parte de una familia, así como la contribución de esta a su formación y proyecto de vida.",
                        "Explica las causas y consecuencias de sus emociones y sentimientos en sí mismo y en los demás. Utiliza estrategias de autorregulación.",
                        "Argumenta su postura en situaciones propias de su edad, reales o simuladas, que involucran un dilema moral.",
                        "Evalúa sus acciones en situaciones de conflicto moral y se plantea comportamientos tomando en cuenta normas sociales y éticas.",
                        "Propone conductas para protegerse en situaciones que ponen en riesgo su integridad en relación a su sexualidad."
                    ]
                }
            },
            {
                "nombre": "CONVIVE Y PARTICIPA DEMOCRÁTICAMENTE EN LA BÚSQUEDA DEL BIEN COMÚN",
                "capacidades": [
                    "Interactúa con todas las personas.",
                    "Construye normas y asume acuerdos y leyes.",
                    "Maneja conflictos de manera constructiva.",
                    "Delibera sobre asuntos públicos.",
                    "Participa en acciones que promueven el bienestar común."
                ],
                "estandares": {
                    "III CICLO": "Convive y participa democráticamente cuando se relaciona con los demás respetando las diferencias y cumpliendo con sus deberes. Conoce las costumbres y características de las personas de su localidad o región. Construye de manera colectiva acuerdos y normas. Usa estrategias sencillas para resolver conflictos. Realiza acciones específicas para el beneficio de todos a partir de la deliberación sobre asuntos de interés común tomando como fuente sus experiencias previas.",
                    "IV CICLO": "Convive y participa democráticamente cuando se relaciona con los demás respetando las diferencias, expresando su desacuerdo frente a situaciones que vulneran la convivencia y cumpliendo con sus deberes. Conoce las manifestaciones culturales de su localidad, región o país. Construye y evalúa acuerdos y normas tomando en cuenta el punto de vista de los demás. Recurre al diálogo para manejar conflictos. Propone y realiza acciones colectivas orientadas al bienestar común a partir de la deliberación sobre asuntos de interés público, en la que se da cuenta que existen opiniones distintas a la suya.",
                    "V CICLO": "Convive y participa democráticamente cuando se relaciona con los demás, respetando las diferencias, los derechos de cada uno, cumpliendo y evaluando sus deberes. Se interesa por relacionarse con personas de culturas distintas y conocer sus costumbres. Construye y evalúa normas de convivencia tomando en cuenta sus derechos. Maneja conflictos utilizando el diálogo y la mediación con base en criterios de igualdad o equidad. Propone, planifica y realiza acciones colectivas orientadas al bien común, la solidaridad, la protección de las personas vulnerables y la defensa de sus derechos. Delibera sobre asuntos de interés público con argumentos basados en fuentes y toma en cuenta la opinión de los demás."
                },
                "desempenos": {
                    "1° GRADO": [
                        "Establece relaciones con sus compañeros respetando sus características físicas o culturales. Identifica sus derechos y cumple sus deberes.",
                        "Describe las características culturales que distinguen al pueblo de origen de sus familiares y las comparte.",
                        "Participa en la elaboración de acuerdos y normas, y los cumple.",
                        "Utiliza estrategias para manejar sus conflictos en el aula con ayuda de un adulto.",
                        "Delibera sobre asuntos de interés común enfatizando en los que se generan durante la convivencia diaria."
                    ],
                    "2° GRADO": [
                        "Comparte actividades con sus compañeros respetando sus diferencias y tratándolos con amabilidad y respeto.",
                        "Describe las características culturales que distinguen a su localidad o región y las comparte.",
                        "Participa en la elaboración de acuerdos y normas que reflejen el buen trato entre compañeros, y los cumple.",
                        "Utiliza estrategias para manejar sus conflictos en el aula con ayuda de un adulto.",
                        "Delibera sobre asuntos de interés común enfatizando en la convivencia diaria para proponer actividades colectivas."
                    ],
                    "3° GRADO": [
                        "Muestra un trato respetuoso e inclusivo con sus compañeros de aula y expresa su desacuerdo en situaciones de maltrato. Cumple con sus deberes.",
                        "Describe algunas manifestaciones culturales de su localidad o de su pueblo de origen.",
                        "Participa en la elaboración de acuerdos y normas de convivencia en el aula, teniendo en cuenta los deberes y derechos del niño.",
                        "Interviene al observar un conflicto entre compañeros: recurre al diálogo o a un adulto cercano.",
                        "Delibera sobre asuntos de interés público para proponer y participar en actividades colectivas orientadas al bien común."
                    ],
                    "4° GRADO": [
                        "Muestra un trato respetuoso e inclusivo con sus compañeros y expresa su desacuerdo en situaciones de maltrato y discriminación.",
                        "Explica algunas manifestaciones culturales de su localidad, región o país.",
                        "Participa en la elaboración de acuerdos y normas de convivencia en el aula, teniendo en cuenta deberes y derechos del niño. Evalúa su cumplimiento.",
                        "Propone alternativas de solución a los conflictos por los que atravesa: recurre al diálogo y a mediadores.",
                        "Delibera sobre asuntos de interés público (seguridad vial, delincuencia juvenil, incumplimiento de derechos) para proponer acciones colectivas."
                    ],
                    "5° GRADO": [
                        "Muestra un trato respetuoso e inclusivo y propone acciones para mejorar la convivencia a partir de la reflexión sobre conductas propias o de otros.",
                        "Muestra interés por participar en actividades que le permitan relacionarse con sus compañeros y personas de distintas culturas.",
                        "Participa en la construcción consensuada de normas de convivencia del aula, teniendo en cuenta los deberes y derechos del niño.",
                        "Utiliza el diálogo y la negociación para superar los conflictos.",
                        "Propone, a partir de un diagnóstico y de la deliberación sobre asuntos públicos, acciones orientadas al bien común y la solidaridad."
                    ],
                    "6° GRADO": [
                        "Establece relaciones con sus compañeros sin discriminarlos. Propone acciones para mejorar la interacción a partir de la reflexión sobre prejuicios.",
                        "Se comunica por diversos medios con personas de una cultura distinta a la suya para aprender de ella.",
                        "Participa en la construcción consensuada de normas de convivencia del aula, teniendo en cuenta los deberes y derechos del niño. Cumple sus deberes.",
                        "Recurre al diálogo o a mediadores para solucionar conflictos y buscar la igualdad o equidad.",
                        "Propone, a partir de un diagnóstico y de la deliberación sobre asuntos públicos, acciones orientadas al bien común sustentando su posición en fuentes."
                    ]
                }
            },
            {
                "nombre": "CONSTRUYE INTERPRETACIONES HISTÓRICAS",
                "capacidades": [
                    "Interpreta críticamente fuentes diversas.",
                    "Comprende el tiempo histórico.",
                    "Elabora explicaciones sobre procesos históricos."
                ],
                "estandares": {
                    "III CICLO": "Construye interpretaciones históricas en las que describe los cambios ocurridos en su familia y comunidad a partir de comparar el presente y el pasado, y de reconocer algunas causas y consecuencias de estos cambios. Obtiene información sobre el pasado de diversos tipos de fuentes. Secuencia hechos o acciones cotidianas e identifica acciones simultáneas.",
                    "IV CICLO": "Construye interpretaciones históricas en las que narra hechos y procesos relacionados a la historia de su región, en los que incorpora más de una dimensión y reconoce diversas causas y consecuencias. Utiliza información de diversas fuentes. Organiza secuencias para comprender cambios ocurridos a través del tiempo.",
                    "V CICLO": "Construye interpretaciones históricas en las que explica, de manera general, procesos históricos peruanos, empleando categorías temporales. Identifica las causas inmediatas y lejanas que desencadenaron dichos procesos, así como sus consecuencias. Ordena cronológicamente procesos históricos y describe cambios, permanencias y simultaneidades."
                },
                "desempenos": {
                    "1° GRADO": ["Obtiene información sobre sí mismo o sobre hechos del pasado a partir de testimonios orales, objetos y fotografías.", "Ordena hechos de su vida cotidiana usando expresiones de tiempo (ayer, hoy, mañana, antes, ahora).", "Describe acontecimientos de su historia personal y familiar comparando presente y pasado."],
                    "2° GRADO": ["Obtiene información de imágenes y objetos antiguos y testimonios de personas.", "Secuencia acciones o hechos cotidianos de su vida personal y familiar e identifica simultaneidades.", "Describe acontecimientos de su historia y comunidad identificando causas y consecuencias."],
                    "3° GRADO": ["Obtiene información del poblamiento americano y primeras aldeas en el Perú.", "Explica la importancia de fuentes históricas como textos o conjuntos arqueológicos de la localidad.", "Secuencia imágenes, objetos o hechos utilizando categorías temporales (antes, ahora, años, décadas)."],
                    "4° GRADO": ["Identifica fuentes pertinentes sobre sociedades prehispánicas, incas y la Conquista.", "Obtiene información en fuentes de divulgación histórica sobre sociedades andinas.", "Secuencia imágenes y describe cambios en la vida cotidiana y etapas de la historia del Perú."],
                    "5° GRADO": ["Obtiene información sobre el Virreinato e Independencia del Perú en cuadros o gráficos.", "Identifica diferencias entre narraciones sobre un mismo hecho histórico.", "Secuencia cronológicamente las etapas de la historia nacional y explica el proceso de Independencia."],
                    "6° GRADO": ["Selecciona fuentes sobre hechos del siglo XIX y XX en el Perú y los ubica en el tiempo.", "Identifica diferencias en las versiones que presentan diversas fuentes históricas.", "Explica procesos históricos del siglo XIX y XX usando categorías temporales y analizando causas y consecuencias."]
                }
            },
            {
                "nombre": "GESTIONA RESPONSABLEMENTE EL ESPACIO Y EL AMBIENTE",
                "capacidades": [
                    "Comprende las relaciones entre los elementos naturales y sociales.",
                    "Maneja fuentes de información para comprender el espacio geográfico y el ambiente.",
                    "Genera acciones para conservar el ambiente local y global."
                ],
                "estandares": {
                    "III CICLO": "Gestiona responsablemente el espacio y ambiente al desarrollar actividades sencillas frente a los problemas y peligros que lo afectan. Explica relaciones sencillas entre elementos naturales y sociales. Utiliza puntos de referencia para ubicarse y desplazarse.",
                    "IV CICLO": "Gestiona responsablemente el espacio y ambiente al realizar actividades específicas para su cuidado a partir de reconocer causas y consecuencias de problemas ambientales. Reconoce el impacto de sus acciones, identifica zonas seguras y vulnerables. Utiliza representaciones cartográficas sencillas.",
                    "V CICLO": "Gestiona responsablemente el espacio y ambiente al realizar actividades para su cuidado y disminuir factores de vulnerabilidad frente al cambio climático y desastres. Utiliza herramientas cartográficas para ubicar elementos geográficos. Explica problemáticas ambientales y territoriales."
                },
                "desempenos": {
                    "1° GRADO": ["Describe elementos naturales y sociales de su espacio cotidiano.", "Se desplaza usando puntos de referencia y nociones espaciales.", "Menciona problemas ambientales (basura) y participa en acciones sencillas de cuidado.", "Sigue señales de evacuación ante peligros."],
                    "2° GRADO": ["Brinda ejemplos de relaciones entre elementos naturales y sociales de su espacio.", "Se desplaza siguiendo instrucciones para localizar objetos o personas.", "Identifica causas y consecuencias de la contaminación del aire, agua y suelo.", "Practica actividades de prevención de accidentes en el aula y hogar."],
                    "3° GRADO": ["Distingue elementos naturales y sociales de su localidad y asocia recursos a actividades económicas.", "Identifica elementos en planos y mapas para ubicar lugares de su localidad.", "Describe problemas ambientales de su localidad y propone actividades de conservación desde su escuela.", "Identifica lugares seguros y vulnerables en la escuela ante desastres."],
                    "4° GRADO": ["Describe espacios geográficos urbanos y rurales y áreas naturales protegidas.", "Utiliza planos y mapas para ubicar elementos de su localidad y región.", "Describe problemas ambientales cotidianos y propone acciones de conservación.", "Identifica lugares seguros en la IE y participa en simulacros."],
                    "5° GRADO": ["Describe relaciones entre elementos naturales y sociales de un espacio geográfico.", "Obtiene información en planos y mapas sobre el espacio y ambiente.", "Explica problemáticas ambientales como deforestación, contaminación del mar o caos vehicular.", "Explica factores de vulnerabilidad ante desastres y ejecuta acciones para reducirlos."],
                    "6° GRADO": ["Compara elementos naturales y sociales de su localidad y región y la acción de actores sociales.", "Utiliza herramientas cartográficas para obtener información y ubicar elementos.", "Explica servicios ambientales de áreas naturales protegidas y propone soluciones sostenibles.", "Explica vulnerabilidades frente al cambio climático y ejecuta acciones de adaptación."]
                }
            },
            {
                "nombre": "GESTIONA RESPONSABLEMENTE LOS RECURSOS ECONÓMICOS",
                "capacidades": [
                    "Comprende las relaciones entre los elementos del sistema económico y financiero.",
                    "Toma decisiones económicas y financieras."
                ],
                "estandares": {
                    "III CICLO": "Gestiona responsablemente los recursos económicos al utilizar los bienes y servicios con los que cuenta en su familia y escuela. Reconoce que las actividades económicas satisfacen necesidades y contribuyen al bienestar.",
                    "IV CICLO": "Gestiona responsablemente los recursos económicos al diferenciar entre necesidades y deseos, y usar servicios públicos reconociendo que tienen un costo. Reconoce la vinculación entre actividades económicas y bienestar social.",
                    "V CICLO": "Gestiona responsablemente los recursos económicos al utilizar el dinero como consumidor informado y realizar acciones de ahorro. Explica el papel de la publicidad, el presupuesto familiar, el pago de tributos y las funciones del Estado y empresas."
                },
                "desempenos": {
                    "1° GRADO": ["Explica las ocupaciones de las personas de su entorno y cómo atienden necesidades.", "Utiliza responsablemente sus pertenencias y reconoce que los recursos se agotan."],
                    "2° GRADO": ["Explica que los recursos del hogar e IE provienen de actividades económicas.", "Explica que los productos tienen un costo y propone acciones para su uso responsable."],
                    "3° GRADO": ["Explica que el trabajo familiar permite obtener dinero para adquirir bienes y servicios.", "Usa responsablemente los recursos y realiza acciones de ahorro en el hogar e IE."],
                    "4° GRADO": ["Describe roles económicos de su comunidad e interrelaciones para satisfacer necesidades.", "Ejecuta acciones de economía familiar diferenciando necesidades y deseos."],
                    "5° GRADO": ["Explica el funcionamiento del mercado y el rol de personas, empresas y el Estado.", "Argumenta la importancia del ahorro, la inversión y el pago puntual de deudas.", "Representa cómo influye la publicidad en las decisiones de consumo."],
                    "6° GRADO": ["Explica cómo el Estado y empresas producen bienes/servicios para el desarrollo sostenible.", "Argumenta la importancia del cumplimiento de compromisos tributarios.", "Elabora un presupuesto personal/familiar y formula planes de ahorro e inversión."]
                }
            }
        ]
    },

    "Comunicación": {
        "competencias": [
            {
                "nombre": "SE COMUNICA ORALMENTE EN SU LENGUA MATERNA",
                "capacidades": [
                    "Obtiene información del texto oral.",
                    "Infiere e interpreta información del texto oral.",
                    "Adecúa, organiza y desarrolla las ideas de forma coherente y cohesionada.",
                    "Utiliza recursos no verbales y paraverbales de forma estratégica.",
                    "Interactúa estratégicamente con distintos interlocutores.",
                    "Reflexiona y evalúa la forma, el contenido y contexto del texto oral."
                ],
                "estandares": {
                    "III CICLO": "Se comunica oralmente mediante diversos tipos de textos; identifica información explícita, infiere e interpreta hechos y temas. Desarrolla sus ideas manteniéndose en el tema, usa conectores y vocabulario frecuente. Su pronunciación es entendible y se apoya en gestos. Participa y responde en forma pertinente.",
                    "IV CICLO": "Se comunica oralmente mediante diversos tipos de textos; identifica información explícita, infiere hechos, tema y propósito. Organiza y desarrolla ideas en torno a un tema con conectores y referentes. Se apoya en recursos no verbales y paraverbales. Adapta su discurso a situaciones formales e informales.",
                    "V CICLO": "Se comunica oralmente mediante diversos tipos de textos; infiere tema, propósito, hechos y conclusiones. Se expresa adecuándose a situaciones formales e informales. Organiza y jerarquiza ideas con vocabulario variado. Evalúa los textos escuchados e interactúa haciendo aportes relevantes."
                },
                "desempenos": {
                    "1° GRADO": ["Recupera información explícita de textos orales sencillos que escucha.", "Dice de qué trata el texto y su propósito con apoyo de lenguaje gráfico.", "Deduce características de personajes y palabras según el contexto.", "Expresa oralmente ideas y emociones apoyándose en gestos."],
                    "2° GRADO": ["Recupera información explícita (nombres, fechas, acciones) de textos orales.", "Deduce características implícitas de personajes, objetos y relaciones de causa-efecto.", "Adecúa su texto oral al propósito y usa conectores de adición y secuencia."],
                    "3° GRADO": ["Recupera datos específicos de textos orales y explica el tema y propósito.", "Deduce relaciones lógicas entre ideas (causa-efecto, secuencia temporal).", "Expresa ideas de forma coherente, evitando reiteraciones innecesarias."],
                    "4° GRADO": ["Recupera información explícita con vocabulario variado y sentido figurado.", "Explica el tema, propósito e intenciones, distinguiendo lo relevante de lo secundario.", "Distingue el registro formal e informal en situaciones comunicativas."],
                    "5° GRADO": ["Integra información explícita dicha en distintos momentos del texto oral.", "Deduce relaciones lógicas e intenciones del hablante a partir de pistas.", "Organiza y jerarquiza ideas de forma coherente y cohesionada."],
                    "6° GRADO": ["Selecciona e integra datos explícitos de diversos interlocutores.", "Deduce relaciones lógicas avanzadas e intenciones en textos con ironías.", "Mantiene el registro formal o informal adaptándose a sus interlocutores y contexto."]
                }
            },
            {
                "nombre": "LEE DIVERSOS TIPOS DE TEXTOS ESCRITOS EN SU LENGUA MATERNA",
                "capacidades": [
                    "Obtiene información del texto escrito.",
                    "Infiere e interpreta información del texto.",
                    "Reflexiona y evalúa la forma, el contenido y contexto del texto."
                ],
                "estandares": {
                    "III CICLO": "Lee diversos tipos de textos de estructura simple en los que predominan palabras conocidas e ilustraciones. Obtiene información poco evidente y realiza inferencias locales. Interpreta el sentido global y opina a partir de su experiencia.",
                    "IV CICLO": "Lee diversos tipos de textos de estructura simple con algunos elementos complejos y vocabulario variado. Obtiene información próxima o semejante. Realiza inferencias e interpreta información relevante para construir el sentido global.",
                    "V CICLO": "Lee diversos tipos de textos con varios elementos complejos y vocabulario variado. Integra datos que están en distintas partes del texto. Interpreta información relevante y complementaria. Evalúa el uso del lenguaje y la intención del autor."
                },
                "desempenos": {
                    "1° GRADO": ["Identifica información explícita que es claramente distinguible en textos con ilustraciones.", "Deduce características de personajes y relaciones de causa-efecto sencillas.", "Predice de qué tratará el texto a partir del título, imágenes y palabras conocidas.", "Opina sobre personas o hechos del texto a partir de su experiencia."],
                    "2° GRADO": ["Identifica información explícita ubicada en distintas partes del texto.", "Deduce características implícitas de personajes y significado de palabras por el contexto.", "Predice el contenido usando indicios como silueta, título e ilustraciones.", "Explica el tema, propósito y relaciones texto-ilustración."],
                    "3° GRADO": ["Identifica información explícita distinguiéndola de otra próxima y semejante.", "Deduce causas-efectos, enseñanzas y motivaciones de personajes.", "Predice el contenido a partir de silueta, tipografía y dimensiones de imágenes.", "Opina sobre el contenido y explica el sentido de recursos como tamaño de letra."],
                    "4° GRADO": ["Identifica información explícita y relevante en textos con algunos elementos complejos.", "Deduce el significado de palabras, frases con sentido figurado y comparaciones.", "Predice de qué tratará el texto contrastando la información que lee.", "Opina sobre el uso de negritas, mayúsculas e índice en el texto."],
                    "5° GRADO": ["Identifica información explícita, relevante y complementaria en distintas partes del texto.", "Deduce relaciones de intención-finalidad, causa-efecto, tema y subtemas.", "Predice de qué tratará el texto a partir de subtítulos, esquemas y notas.", "Opina sobre la organización textual, recursos gráficos y efecto en el lector."],
                    "6° GRADO": ["Selecciona e integra información explícita en textos complejos o en lectura intertextual.", "Deduce características implícitas, sentido figurado y relaciones de causa-efecto avanzadas.", "Explica el tema, el propósito, motivaciones de personajes y conclusiones globales.", "Opina sobre la intención del autor, postura y evalúa la estructura del texto."]
                }
            },
            {
                "nombre": "ESCRIBE DIVERSOS TIPOS DE TEXTOS EN SU LENGUA MATERNA",
                "capacidades": [
                    "Adecúa el texto a la situación comunicativa.",
                    "Organiza y desarrolla las ideas de forma coherente y cohesionada.",
                    "Utiliza convenciones del lenguaje escrito de forma pertinente.",
                    "Reflexiona y evalúa la forma, el contenido y contexto del texto escrito."
                ],
                "estandares": {
                    "III CICLO": "Escribe diversos tipos de textos de forma reflexiva. Adecúa al propósito y destinatario. Organiza ideas en torno a un tema usando conectores y vocabulario frecuente. Utiliza recursos ortográficos básicos y revisa su texto para mejorarlo.",
                    "IV CICLO": "Escribe diversos tipos de textos de forma reflexiva. Adecúa el texto al destinatario, propósito y registro. Organiza ideas en torno a un tema con conectores y referentes. Usa ortografía básica y reflexiona sobre la coherencia de su texto.",
                    "V CICLO": "Escribe diversos tipos de textos de forma reflexiva. Adecúa el texto al destinatario y propósito, organizando ideas en párrafos. Utiliza conectores, referentes y recursos ortográficos para dar claridad. Evalúa la coherencia y cohesión de su escrito."
                },
                "desempenos": {
                    "1° GRADO": ["Adecúa el texto a la situación comunicativa y al propósito a partir de su experiencia.", "Escribe en nivel alfabético en torno a un tema, usando algunos conectores.", "Revisa el texto con ayuda del docente para determinar si se ajusta al propósito."],
                    "2° GRADO": ["Adecúa el texto a la situación comunicativa considerando el destinatario.", "Agrupa ideas en oraciones en torno a un tema, utilizando conectores de adición y secuencia.", "Utiliza mayúsculas y punto final para dar sentido a su texto.", "Revisa el escrito con ayuda docente para mejorar la coherencia."],
                    "3° GRADO": ["Adecúa el texto al propósito, destinatario y tipo textual; distingue registro formal/informal.", "Escribe textos de forma coherente y cohesionada sin contradicciones ni repeticiones.", "Utiliza punto seguido y signos de interrogación/admiración adecuadamente.", "Revisa el texto para verificar si se ajusta a la situación e identificar vacíos."],
                    "4° GRADO": ["Adecúa el texto a la situación comunicativa y características del género discursivo.", "Organiza ideas en torno a un tema sin digresiones, usando conectores y referentes.", "Utiliza punto seguido y coma enumerativa para dar claridad.", "Revisa el texto para asegurar la cohesión y el ajuste al propósito."],
                    "5° GRADO": ["Adecúa el texto al propósito, tipo textual, formato y soporte en registro formal/informal.", "Organiza y jerarquiza ideas en subtemas y párrafos de forma coherente.", "Utiliza punto aparte, comillas y negritas para estructurar el escrito.", "Evalúa de manera permanente si el texto responde al propósito y corrige errores."],
                    "6° GRADO": ["Adecúa el texto a la situación comunicativa, género discursivo, formato y soporte.", "Jerarquiza ideas en subtemas e ideas principales organizadas en párrafos.", "Utiliza recursos ortográficos avanzados (punto aparte, conectores de contraste) para dar sentido.", "Evalúa la cohesión, coherencia y adecuación de su escrito para asegurar su calidad."]
                }
            }
        ]
    },

    "Matemática": {
        "competencias": [
            {
                "nombre": "RESUELVE PROBLEMAS DE CANTIDAD",
                "capacidades": [
                    "Traduce cantidades a expresiones numéricas.",
                    "Comunica su comprensión sobre los números y las operaciones.",
                    "Usa estrategias y procedimientos de estimación y cálculo.",
                    "Argumenta afirmaciones sobre las relaciones numéricas y las operaciones."
                ],
                "estandares": {
                    "III CICLO": "Resuelve problemas referidos a acciones de juntar, separar, agregar, quitar, igualar y comparar cantidades; las traduce a adición, sustracción, doble y mitad. Expresa comprensión de la decena y valor posicional hasta 2 cifras. Emplea estrategias y mide masa/tiempo con unidades no convencionales.",
                    "IV CICLO": "Resuelve problemas de agregar, quitar, igualar, repetir o repartir cantidades, combinar colecciones y partir unidades. Traduce a adición, sustracción, multiplicación, división y fracciones usuales. Expresa comprensión de la centena y millar. Opera con cálculo mental o escrito.",
                    "V CICLO": "Resuelve problemas de comparar, igualar, repartir cantidades y potenciamiento. Traduce a 4 operaciones con naturales, fracciones y decimales. Comprende el sistema decimal hasta 6 cifras, divisores, múltiplos y porcentajes. Realiza conversiones de medida."
                },
                "desempenos": {
                    "1° GRADO": ["Transforma acciones de juntar/quitar en adiciones y sustracciones hasta 20.", "Comprende la decena como grupo de 10 y representa ordinales hasta el décimo.", "Emplea estrategias de conteo, cálculo mental y comparación uno a uno.", "Compara la masa de objetos y el tiempo de manera vivencial."],
                    "2° GRADO": ["Transforma acciones de avanzar, retroceder, juntar, igualar en operaciones hasta dos cifras.", "Comprende la decena y valor posicional en números de 2 cifras.", "Emplea estrategias como descomposiciones aditivas y uso de dobles.", "Mide el tiempo usando días u horarios semanales."],
                    "3° GRADO": ["Transforma acciones de agregar, juntar, multiplicar y dividir en operaciones hasta 3 cifras.", "Comprende la centena, valor posicional, orden y la propiedad conmutativa.", "Emplea estrategias de cálculo mental (duplicar, multiplicar por 10) y escrito con canjes.", "Mide la masa en kilogramos y el tiempo en horas exactas."],
                    "4° GRADO": ["Transforma acciones en expresiones de 4 cifras, multiplicaciones, divisiones y fracciones.", "Comprende la unidad de millar, fracciones equivalentes y operaciones aditivas de fracciones.", "Emplea cálculo mental o escrito (descomposiciones, doble/mitad) y redondeo.", "Mide masa (kg, g) y tiempo (año, hora, media hora)."],
                    "5° GRADO": ["Transforma problemas en adición, sustracción, multiplicación, división con naturales y decimales.", "Comprende valor posicional hasta 6 cifras, decimales al décimo, múltiplos e infracción como operador.", "Emplea estrategias de reversibilidad, simplificación de fracciones y propiedad distributiva.", "Mide masa (kg) y tiempo (décadas, siglos) con unidades convencionales."],
                    "6° GRADO": ["Transforma problemas en 4 operaciones con naturales, decimales, fracciones y potencias.", "Comprende decimales al centésimo, números primos, compuestos, fracción operador y cociente.", "Emplea estrategias avanzadas de cálculo, simplificación, redondeo y porcentajes.", "Realiza conversiones de unidades de masa, tiempo y temperatura."]
                }
            },
            {
                "nombre": "RESUELVE PROBLEMAS DE REGULARIDAD, EQUIVALENCIA Y CAMBIO",
                "capacidades": [
                    "Traduce datos y condiciones a expresiones algebraicas y gráficas.",
                    "Comunica su comprensión sobre las relaciones algebraicas.",
                    "Usa estrategias y procedimientos para encontrar equivalencias y reglas generales.",
                    "Argumenta afirmaciones sobre relaciones de cambio y equivalencia."
                ],
                "estandares": {
                    "III CICLO": "Resuelve problemas de equivalencias o regularidades, traduciéndolas a igualdades con adición/sustracción y patrones de repetición o aditivos. Expresa equivalencias con material concreto. Explica cómo mantener el equilibrio.",
                    "IV CICLO": "Resuelve problemas con dos equivalencias o cambio entre magnitudes, traduciendo a operaciones aditivas/multiplicativas, tablas y patrones. Expresa comprensión de la regla de formación y signo igual.",
                    "V CICLO": "Resuelve problemas de equivalencia y cambio traduciéndolos a ecuaciones, desigualdades, proporcionalidad directa y patrones geométricos/posicionales. Emplea propiedades de la igualdad (uniformidad y cancelativa)."
                },
                "desempenos": {
                    "1° GRADO": ["Transforma equivalencias de hasta 10 objetos en igualdades aditivas (ej. 2+5=3+4).", "Crea y continua patrones de repetición o aditivos crecientes hasta 20.", "Explica cómo continúa un patrón o cómo mantener la equivalencia."],
                    "2° GRADO": ["Transforma equivalencias de hasta 20 objetos en igualdades aditivas o sustracciones.", "Crea y continua patrones aditivos con números de hasta 2 cifras.", "Emplea estrategias para mantener la igualdad o 'equilibrio' en balanzas."],
                    "3° GRADO": ["Transforma equivalencias en igualdades con adición, sustracción o multiplicación.", "Crea patrones de repetición con cambio de posición o patrones aditivos.", "Describe el cambio de una magnitud respecto al tiempo usando tablas o gráficos."],
                    "4° GRADO": ["Transforma equivalencias en igualdades con las 4 operaciones.", "Crea y continua patrones aditivos o multiplicativos con números de hasta 4 cifras.", "Aplica nocionalmente las propiedades de la igualdad (uniformidad y cancelativa)."],
                    "5° GRADO": ["Transforma relaciones de equivalencia y cambio en ecuaciones simples (x + a = b) o tablas de proporcionalidad.", "Crea patrones aditivos de segundo orden o con criterios geométricos.", "Emplea la propiedad distributiva, uniformidad y cancelativa para resolver ecuaciones."],
                    "6° GRADO": ["Transforma equivalencias y cambios en ecuaciones con 4 operaciones, desigualdades o proporcionalidad directa.", "Determina la regla o término general de un patrón numérico o geométrico.", "Justifica sus procesos al resolver ecuaciones y relaciones de proporcionalidad."]
                }
            },
            {
                "nombre": "RESUELVE PROBLEMAS DE FORMA, MOVIMIENTO Y LOCALIZACIÓN",
                "capacidades": [
                    "Modela objetos con formas geométricas y sus transformaciones.",
                    "Comunica su comprensión sobre las formas y relaciones geométricas.",
                    "Usa estrategias y procedimientos para orientarse en el espacio.",
                    "Argumenta afirmaciones sobre relaciones geométricas."
                ],
                "estandares": {
                    "III CICLO": "Modela características de objetos a formas 2D y 3D, elementos y desplazamientos. Describe lados, vértices y caras. Traza recorridos en cuadrículas y mide longitud con unidades no convencionales.",
                    "IV CICLO": "Modela objetos a formas 2D, 3D, simetría y ubicación en cuadrículas/planos. Describe ángulos rectos, paralelismo y dibujo de croquis. Mide longitud, superficie y capacidad con unidades convencionales.",
                    "V CICLO": "Modela formas 2D, 3D, ampliación, reducción, rotación y ubicación en plano cartesiano. Clasifica prismas, cuadriláteros y círculos. Realiza conversiones de unidades y explica relaciones de área/perímetro."
                },
                "desempenos": {
                    "1° GRADO": ["Representa objetos del entorno con formas tridimensionales y bidimensionales básicas.", "Expresa desplazamientos usando nociones arriba-abajo, delante-detrás, dentro-fuera.", "Mide la longitud de objetos usando unidades no convencionales (manos, pasos, clips)."],
                    "2° GRADO": ["Identifica objetos que ruedan y no ruedan y los asocia a formas 2D y 3D.", "Expresa posiciones usando puntos de referencia en cuadrículas (derecha, izquierda, borde).", "Compara la longitud de dos objetos de manera cualitativa."],
                    "3° GRADO": ["Representa objetos con formas 2D (regulares e irregulares) y 3D (redondos y compuestos).", "Considera el eje de simetría al ubicar o reproducir figuras.", "Mide la longitud en centímetros y metros y estima superficies de forma cualitativa."],
                    "4° GRADO": ["Representa objetos con polígonos, cubos y prismas de base cuadrangular.", "Describe ángulos rectos, líneas paralelas y perpendiculares.", "Mide perímetro, superficie y capacidad en litros usando instrumentos."],
                    "5° GRADO": ["Representa objetos con cuadriláteros, prismas rectos, perímetro y área.", "Describe giros, traslaciones, ampliaciones y reducciones en el plano cartesiano.", "Emplea estrategias para calcular área y volumen y hacer trazados geométricos."],
                    "6° GRADO": ["Representa objetos con triángulos, cuadriláteros, círculos, prismas rectos y cilindros.", "Ubica posiciones y trayectorias usando coordenadas y puntos cardinales en planos sencillos.", "Realiza conversiones de unidades de longitud (m, cm) y superficie (m2, cm2)."]
                }
            },
            {
                "nombre": "RESUELVE PROBLEMAS DE GESTIÓN DE DATOS E INCERTIDUMBRE",
                "capacidades": [
                    "Representa datos con gráficos y medidas estadísticas o probabilísticas.",
                    "Comunica su comprensión de los conceptos estadísticos y probabilísticos.",
                    "Usa estrategias y procedimientos para recopilar y procesar datos.",
                    "Sustenta conclusiones o decisiones con base en la información obtenida."
                ],
                "estandares": {
                    "III CICLO": "Resuelve problemas de datos cualitativos, recolecta datos con preguntas sencillas y los representa en pictogramas y gráficos de barras simples. Lee e identifica la mayor frecuencia. Usa nociones de posible e imposible.",
                    "IV CICLO": "Resuelve problemas cualitativos o cuantitativos discretos. Representa en pictogramas con escala y barras dobles/simples. Interpreta usando la moda. Expresa ocurrencia con seguro, más probable o menos probable.",
                    "V CICLO": "Resuelve problemas con datos cualitativos/cuantitativos discretos. Representa en barras dobles, líneas y tablas de doble entrada. Interpreta con la moda, media aritmética y expresa probabilidad de sucesos."
                },
                "desempenos": {
                    "1° GRADO": ["Representa datos cualitativos en pictogramas horizontales y barras simples sin escala.", "Expresa la ocurrencia de sucesos con 'siempre', 'a veces', 'nunca'.", "Recopila datos mediante preguntas sencillas e indica la mayor frecuencia."],
                    "2° GRADO": ["Representa datos en pictogramas donde el símbolo vale 1 o 2 unidades.", "Expresa ocurrencias con 'posible' e 'imposible'.", "Compara datos en tablas de frecuencia simple indicando mayor y menor frecuencia."],
                    "3° GRADO": ["Representa datos cuantitativos discretos en barras con escala (2 en 2, 5 en 5, 10 en 10).", "Expresa la ocurrencia de sucesos con 'seguro', 'posible' e 'imposible'.", "Recopila datos mediante encuestas cortas y determina la moda."],
                    "4° GRADO": ["Representa datos en barras con escala y determina la moda y media como punto de equilibrio.", "Expresa la probabilidad con 'seguro', 'más probable' y 'menos probable'.", "Interpreta información en tablas de doble entrada y gráficos de barras dobles."],
                    "5° GRADO": ["Representa datos en barras con escala, pictogramas y determina la media aritmética.", "Expresa la ocurrencia de sucesos con probabilidades cualitativas.", "Recopila datos mediante encuestas y determina conclusiones basadas en la moda."],
                    "6° GRADO": ["Representa datos en gráficos de barras dobles, líneas, moda y media aritmética como reparto equitativo.", "Determina todos los posibles resultados de una situación aleatoria como fracción.", "Produce nueva información interpretando fuentes diversas y advirtiendo datos incompletos."]
                }
            }
        ]
    },

    "Ciencia y Tecnología": {
        "competencias": [
            {
                "nombre": "INDAGA MEDIANTE MÉTODOS CIENTÍFICOS PARA CONSTRUIR SUS CONOCIMIENTOS",
                "capacidades": [
                    "Problematiza situaciones para hacer indagación.",
                    "Diseña estrategias para hacer indagación.",
                    "Genera y registra datos e información.",
                    "Analiza datos e información.",
                    "Evalúa y comunica el proceso y resultados de su indagación."
                ],
                "estandares": {
                    "III CICLO": "Indaga al explorar objetos o fenómenos, hacer preguntas y proponer posibles respuestas. Sigue procedimientos para observar, manipular y comparar, elaborando conclusiones sencillas que comunica de forma oral o gráfica.",
                    "IV CICLO": "Indaga al establecer causas de un hecho para formular preguntas e hipótesis. Propone estrategias para obtener datos, los registra, analiza relaciones de causalidad y comunica sus procedimientos y conclusiones.",
                    "V CICLO": "Indaga formulando preguntas e hipótesis relacionando variables dependiente e independiente. Diseña situaciones controladas, registra datos, los contrasta con información científica confiable y evalúa sus conclusiones."
                },
                "desempenos": {
                    "1° GRADO": ["Hace preguntas sobre hechos u objetos de su entorno y propone posibles respuestas.", "Propone acciones para responder preguntas y selecciona materiales para explorar.", "Obtiene datos mediante la observación y los registra con dibujos.", "Comunica lo aprendido, logros y dificultades."],
                    "2° GRADO": ["Hace preguntas sobre características de objetos y propone explicaciones basadas en regularidades.", "Ordena acciones de su plan de indagación y selecciona materiales.", "Obtiene y registra datos en organizadores o dibujos.", "Compara la respuesta inicial con los datos obtenidos."],
                    "3° GRADO": ["Hace preguntas sobre hechos naturales y propone posibles respuestas con base en patrones.", "Describe un plan de acción para responder la pregunta y selecciona herramientas.", "Obtiene datos cualitativos/cuantitativos midiendo con unidades convencionales.", "Compara sus datos con información científica y elabora conclusiones."],
                    "4° GRADO": ["Formula preguntas sobre hechos y elabora una explicación relacionando causas y factores.", "Diseña un plan de indagación indicando procedimientos y fuentes científicas.", "Obtiene datos con instrumentos y los representa en tablas o gráficos.", "Evalúa si sus procedimientos ayudaron a comprobar la hipótesis."],
                    "5° GRADO": ["Formula preguntas e hipótesis relacionando variables causa-efecto.", "Diseña un plan con medidas de seguridad, tiempo e instrumentos para medir variables.", "Registra datos en organizadores y los contrasta con información científica confiable.", "Comunica sus conclusiones evaluando los errores del proceso."],
                    "6° GRADO": ["Plantea hipótesis controlando variables en una experimentación.", "Selecciona fuentes científicas, instrumentos y herramientas para su plan de indagación.", "Organiza datos, hace cálculos estadísticos (moda) y los contrasta con teorías científicas.", "Evalúa la validez de su indagación y propone mejoras al diseño."]
                }
            },
            {
                "nombre": "EXPLICA EL MUNDO FÍSICO BASÁNDOSE EN CONOCIMIENTOS SOBRE LOS SERES VIVOS, MATERIA Y ENERGÍA, BIODIVERSIDAD, TIERRA Y UNIVERSO",
                "capacidades": [
                    "Comprende y usa conocimientos sobre los seres vivos, materia y energía, biodiversidad, Tierra y universo.",
                    "Evalúa las implicancias del saber y del quehacer científico y tecnológico."
                ],
                "estandares": {
                    "III CICLO": "Explica con base en sus observaciones la relación entre materiales y cambios por luz/calor, estructura de seres vivos y sus funciones, componentes de la Tierra y opina sobre objetos tecnológicos.",
                    "IV CICLO": "Explica con base en evidencia científica la relación entre fuentes de energía y cambios, fuerzas y movimiento, estructura de sistemas vivos y su clasificación, radiación solar y climas.",
                    "V CICLO": "Explica con evidencia científica las relaciones entre propiedades de la materia y estructura microscópica, reproducción sexual y genética, ecosistemas y biodiversidad, y justifica su posición sobre el uso de la tecnología."
                },
                "desempenos": {
                    "1° GRADO": ["Describe las necesidades de los seres vivos (agua, aire, alimento).", "Relaciona las actividades cotidianas con el uso de la energía.", "Justifica la importancia del agua, aire y suelo para la vida.", "Relaciona los objetos tecnológicos con su utilidad para satisfacer necesidades."],
                    "2° GRADO": ["Relaciona las partes externas de seres vivos con sus funciones (ej. dientes).", "Describe los cambios en objetos por acción del calor o luz.", "Utiliza modelos para explicar la cadena alimenticia.", "Describe que la Tierra tiene agua, aire y material sólido."],
                    "3° GRADO": ["Describe los órganos que conforman los sistemas en plantas y animales.", "Clasifica materiales por propiedades físicas (duro, blando, frágil).", "Relaciona fuerzas con el movimiento o deformación de cuerpos.", "Describe las interacciones de los seres vivos en su hábitat."],
                    "4° GRADO": ["Explica la función de relación, nutrición y reproducción en plantas y animales.", "Describe cambios reversibles e irreversibles en la materia por energía.", "Describe el rol de productores, consumidores y descomponedores.", "Explica la formación de zonas climáticas en la Tierra por el Sol."],
                    "5° GRADO": ["Describe la estructura de la célula animal y vegetal y sus funciones básicas.", "Describe la estructura de los ecosistemas (factores bióticos y abióticos).", "Explica que el progreso tecnológico responde a necesidades humanas e impactos ambientales.", "Opina con respaldo científico sobre el uso de tecnologías."],
                    "6° GRADO": ["Explica organismos unicelulares y pluricelulares y especialización celular.", "Relaciona la reproducción sexual con la diversidad de especies.", "Relaciona estados de agregación de la materia con fuerzas moleculares.", "Justifica por qué la diversidad de especies da estabilidad a los ecosistemas."]
                }
            },
            {
                "nombre": "DISEÑA Y CONSTRUYE SOLUCIONES TECNOLÓGICAS PARA RESOLVER PROBLEMAS DE SU ENTORNO",
                "capacidades": [
                    "Determina una alternativa de solución tecnológica.",
                    "Diseña la alternativa de solución tecnológica.",
                    "Implementa y valida la alternativa de solución tecnológica.",
                    "Evalúa y comunica el funcionamiento y los impactos de su alternativa de solución tecnológica."
                ],
                "estandares": {
                    "III CICLO": "Diseña y construye soluciones tecnológicas estableciendo causas de un problema. Representa con dibujos, describe pasos, usa herramientas, realiza ajustes y evalúa el funcionamiento.",
                    "IV CICLO": "Diseña soluciones tecnológicas con base en conocimientos científicos. Representa etapas, determina características de forma/función, verifica el funcionamiento y propone mejoras.",
                    "V CICLO": "Diseña soluciones tecnológicas identificando causas con base científica. Representa esquemas estructurados, ejecuta con herramientas seleccionadas, detecta imprecisiones y evalúa limitaciones e impactos."
                },
                "desempenos": {
                    "1° GRADO": ["Selecciona un problema tecnológico sencillo y propone una solución con material reciclable.", "Representa su idea con dibujos y texto indicando sus partes.", "Construye el prototipo manipulando materiales con seguridad.", "Realiza pruebas sencillas y explica cómo funciona."],
                    "2° GRADO": ["Describe las causas de un problema tecnológico y propone una solución.", "Representa la solución seleccionando herramientas según sus propiedades físicas.", "Construye la solución realizando ajustes si no funciona.", "Explica el proceso de construcción y dificultades superadas."],
                    "3° GRADO": ["Determina un problema tecnológico y propone alternativas con conocimientos locales o científicos.", "Representa la solución con dibujos, detallando la secuencia de pasos.", "Construye la alternativa usando herramientas y cumpliendo normas de ecoeficiencia.", "Prueba si la solución cumple con los requerimientos y propone mejoras."],
                    "4° GRADO": ["Determina las causas de un problema y propone soluciones tecnológicas.", "Describe partes, etapas, forma, estructura y función de la alternativa.", "Construye la alternativa verificando el funcionamiento de cada parte.", "Explica los conocimientos científicos aplicados y los beneficios del prototipo."],
                    "5° GRADO": ["Determina un problema tecnológico, sus causas y propone soluciones con sustento científico.", "Representa el prototipo en esquemas considerando tiempo, recursos y seguridad.", "Verifica el funcionamiento de cada etapa y realiza ajustes en las dimensiones.", "Evalúa si el prototipo cumple los requerimientos a través de pruebas repetidas."],
                    "6° GRADO": ["Determina el problema tecnológico considerando requerimientos, recursos y costos.", "Representa la solución con esquemas estructurados incluyendo dimensiones y materiales.", "Construye la solución detectando errores en la selección de materiales o dimensiones.", "Realiza pruebas para verificar requerimientos e infiere impactos positivos o negativos."]
                }
            }
        ]
    },

    "Arte y Cultura": {
        "competencias": [
            {
                "nombre": "APRECIA DE MANERA CRÍTICA MANIFESTACIONES ARTÍSTICO CULTURALES",
                "capacidades": [
                    "Percibe manifestaciones artístico-culturales.",
                    "Contextualiza manifestaciones artístico-culturales.",
                    "Reflexiona creativa y críticamente sobre manifestaciones artístico-culturales."
                ],
                "estandares": {
                    "III CICLO": "Aprecia manifestaciones artístico-culturales al describir sus elementos visuales, sonoros y táctiles y las sensaciones que transmiten. Reconoce que expresan características de personas y lugares.",
                    "IV CICLO": "Aprecia manifestaciones artístico-culturales describiendo sus elementos, forma y medios. Investiga el contexto donde se originaron y explica cómo comunican ideas y sentimientos.",
                    "V CICLO": "Aprecia manifestaciones artístico-culturales interpretando elementos y estructura. Investiga contextos tradicionales y contemporáneos y genera hipótesis sobre sus significados e intenciones."
                },
                "desempenos": {
                    "1° GRADO": ["Usa los sentidos para identificar elementos visuales, sonoros y táctiles en el arte.", "Describe lo que siente al observar o escuchar manifestaciones artísticas.", "Explica sus ideas sobre manifestaciones artísticas de su entorno."],
                    "2° GRADO": ["Describe líneas, formas, sonidos y movimientos en la naturaleza y el arte.", "Conversa sobre los contextos donde se producen manifestaciones artísticas.", "Explica los sentimientos que le generan obras de arte a partir de sus vivencias."],
                    "3° GRADO": ["Identifica elementos básicos del arte (color, forma, sonido) y sensaciones que transmiten.", "Especula sobre los procesos que el artista siguió para crear su obra.", "Comenta sobre los posibles significados de una manifestación artística."],
                    "4° GRADO": ["Describe y analiza elementos del arte e instrumentos usados en manifestaciones culturales.", "Investiga el significado de símbolos en manifestaciones de diferentes lugares.", "Genera hipótesis sobre la intención del artista y el mensaje de la obra."],
                    "5° GRADO": ["Describe las características de manifestaciones artísticas e interpreta su mensaje.", "Identifica cómo el arte cumple funciones como entretener, socializar o contar historias.", "Genera hipótesis sobre intenciones del artista e integra opiniones de otros."],
                    "6° GRADO": ["Analiza cualidades de elementos en el arte y las relaciones con las emociones que generan.", "Investiga el origen y evolución de manifestaciones artísticas tradicionales y contemporáneas.", "Desarrolla criterios para evaluar obras de arte con base en su contexto de creación."]
                }
            },
            {
                "nombre": "CREA PROYECTOS DESDE LOS LENGUAJES ARTÍSTICOS",
                "capacidades": [
                    "Explora y experimenta los lenguajes del arte.",
                    "Aplica procesos creativos.",
                    "Evalúa y comunica sus procesos y proyectos."
                ],
                "estandares": {
                    "III CICLO": "Crea proyectos artísticos explorando elementos y técnicas (música, teatro, artes visuales, danza). Concretiza ideas de su imaginación y comparte sus creaciones con otros.",
                    "IV CICLO": "Crea proyectos artísticos combinando elementos del arte y usando diversos medios y técnicas. Planifica trabajos para resolver problemas creativos y los mejora con retroalimentación.",
                    "V CICLO": "Crea proyectos artísticos individuales o colaborativos usando diversas técnicas y tecnologías. Genera ideas investigando fuentes, planifica la presentación y evalúa la efectividad del mensaje."
                },
                "desempenos": {
                    "1° GRADO": ["Experimenta con materiales y técnicas visuales, sonoras o corporales.", "Explora ideas libremente para comunicar una vivencia o emoción.", "Presenta sus creaciones y responde preguntas sencillas sobre ellas."],
                    "2° GRADO": ["Explora formas de usar medios y materiales para expresar ideas.", "Organiza elementos (sonidos, movimientos, colores) para presentar una idea específica.", "Presenta sus creaciones individuales o grupales explicando cómo las hizo."],
                    "3° GRADO": ["Improvisa y combina medios, herramientas y materiales para lograr efectos expresivos.", "Planifica sus proyectos basándose en cómo otros artistas usaron las técnicas.", "Explica las técnicas elegidas y por qué considera exitosa su creación."],
                    "4° GRADO": ["Combina elementos de los lenguajes artísticos con recursos tecnológicos a su alcance.", "Desarrolla ideas a partir de observaciones y compone imágenes según su intención.", "Planifica la presentación de sus trabajos asumiendo un rol específico."],
                    "5° GRADO": ["Explora elementos de danza, música, teatro y artes visuales con fines comunicativos.", "Genera ideas desde fuentes culturales tradicionales o locales para su proyecto.", "Registra el proceso de creación y evalúa el impacto de su presentación."],
                    "6° GRADO": ["Combina materiales, técnicas y tecnologías para resolver problemas creativos.", "Realiza creaciones individuales y colectivas estudiando el entorno natural y cultural.", "Documenta su proceso creativo, recoge sugerencias y mejora el resultado final."]
                }
            }
        ]
    },

    "Educación Religiosa": {
        "competencias": [
            {
                "nombre": "CONSTRUYE SU IDENTIDAD COMO PERSONA HUMANA, AMADA POR DIOS, DIGNA, LIBRE Y TRASCENDENTE, COMPRENDIENDO LA DOCTRINA DE SU PROPIA RELIGIÓN, ABIERTO AL DIÁLOGO CON LAS QUE LE SON CERCANAS",
                "capacidades": [
                    "Conoce a Dios y asume su identidad religiosa y espiritual como persona digna, libre y trascendente.",
                    "Cultiva y valora las manifestaciones religiosas de su entorno argumentando su fe de manera comprensible y respetuosa."
                ],
                "estandares": {
                    "III CICLO": "Descubre el amor de Dios en la creación y lo relaciona con el amor familiar. Explica el Plan de Salvación y vive en fraternidad respetando otras expresiones religiosas.",
                    "IV CICLO": "Describe el amor de Dios en la Creación y el Evangelio. Construye su identidad como hijo de Dios y participa en la comunidad de fe con respeto y tolerancia.",
                    "V CICLO": "Comprende el amor de Dios respetando la dignidad humana. Explica el Plan de Salvación y demuestra su fe con obras de caridad y diálogo fraterno."
                },
                "desempenos": {
                    "1° GRADO": ["Identifica que Dios manifiesta su amor en la Creación y en su familia.", "Comprende hechos de la Historia de la Salvación.", "Se relaciona con su prójimo con respeto y fraternidad.", "Reconoce lo bueno y malo de sus acciones imitando a Jesús."],
                    "2° GRADO": ["Descubre que Dios nos creó a su imagen y semejanza.", "Explica hechos principales de la Biblia y los relaciona con su entorno.", "Participa en celebraciones religiosas de su comunidad.", "Asume compromisos de cambio para imitar a Jesús."],
                    "3° GRADO": ["Identifica la acción de Dios en la Historia de la Salvación.", "Conoce el mensaje de Dios en las Sagradas Escrituras.", "Respeta a compañeros que profesan credos diferentes.", "Se compromete a una convivencia cristiana basada en el diálogo."],
                    "4° GRADO": ["Relaciona sus experiencias con la Historia de la Salvación.", "Se reconoce como hijo amado de Dios mediante las Escrituras.", "Participa en la Iglesia como comunidad de fe y amor.", "Promueve el respeto, tolerancia y amor fraterno."],
                    "5° GRADO": ["Explica el amor de Dios en la Creación y se compromete a cuidarla.", "Demuestra su amor a Dios realizando acciones de solidaridad.", "Promueve la convivencia armónica en su entorno escolar."],
                    "6° GRADO": ["Comprende el amor de Dios promoviendo la libertad y dignidad humana.", "Demuestra su fe atendiendo las necesidades del prójimo.", "Fomenta en todo lugar el diálogo y la comprensión fraterna."]
                }
            },
            {
                "nombre": "ASUME LA EXPERIENCIA DEL ENCUENTRO PERSONAL Y COMUNITARIO CON DIOS EN SU PROYECTO DE VIDA EN COHERENCIA CON SU CREENCIA RELIGIOSA",
                "capacidades": [
                    "Transforma su entorno desde el encuentro personal y comunitario con Dios y desde la fe que profesa.",
                    "Actúa coherentemente en razón de su fe según los principios de su conciencia moral en situaciones concretas de la vida."
                ],
                "estandares": {
                    "III CICLO": "Expresa coherencia en sus acciones cotidianas descubriendo a Dios. Practica virtudes evangélicas y agradece por lo creado.",
                    "IV CICLO": "Expresa coherencia entre lo que cree, dice y hace a la luz del Evangelio y de los santos. Celebra su fe y asume el cuidado de lo creado.",
                    "V CICLO": "Expresa coherencia en su proyecto de vida a la luz del mensaje bíblico. Transforma su entorno y participa activamente en su comunidad de fe."
                },
                "desempenos": {
                    "1° GRADO": ["Descubre el amor de Dios en su vida cotidiana.", "Practica la oración constante como medio de diálogo con Dios.", "Agradece a Dios por la creación y los dones recibidos."],
                    "2° GRADO": ["Expresa el amor de Dios siguiendo el ejemplo de Jesús.", "Participa en momentos de oración en la escuela y hogar.", "Agradece a Dios asumiendo el compromiso de cuidar la naturaleza."],
                    "3° GRADO": ["Muestra su fe mediante acciones concretas en la convivencia.", "Participa en espacios de oración personal y comunitaria.", "Muestra compromiso en el cuidado del prójimo y la naturaleza."],
                    "4° GRADO": ["Aplica las enseñanzas de la Biblia y los santos en sus acciones diarias.", "Interioriza la presencia de Dios celebrando su fe con gratitud.", "Motiva a otros a cuidar la naturaleza como creación divina."],
                    "5° GRADO": ["Acepta las enseñanzas de Jesús para transformar su comportamiento.", "Participa en su comunidad eclesial activamente.", "Promueve acciones de cambio para una convivencia justa."],
                    "6° GRADO": ["Cultiva la oración y reflexión para fortalecer su fe.", "Actúa con liderazgo promoviendo la justicia y la solidaridad.", "Propone acciones comunitarias a imagen de Jesucristo."]
                }
            }
        ]
    },

    "Educación Física": {
        "competencias": [
            {
                "nombre": "SE DESENVUELVE DE MANERA AUTÓNOMA A TRAVÉS DE SU MOTRICIDAD",
                "capacidades": [
                    "Comprende su cuerpo.",
                    "Se expresa corporalmente."
                ],
                "estandares": {
                    "III CICLO": "Se desenvuelve de manera autónoma al comprender cómo usar su cuerpo en acciones motrices con lado dominante. Se orienta en el espacio y se expresa corporalmente con ritmo y gestos.",
                    "IV CICLO": "Se desenvuelve de manera autónoma explorando la alternancia de lados corporales y regulando el cuerpo en el espacio/tiempo. Experimenta posibilidades expresivas.",
                    "V CICLO": "Se desenvuelve de manera autónoma aceptando sus posibilidades y limitaciones. Crea secuencias de movimiento coordinadas y expresivas con intención."
                },
                "desempenos": {
                    "1° GRADO": ["Explora posibilidades de movimiento (saltar, correr, lanzar) manteniendo equilibrio.", "Reconoce su lado derecho e izquierdo en nociones espaciales.", "Explora gestos y ritmos sencillos para comunicar emociones."],
                    "2° GRADO": ["Realiza habilidades motrices básicas mediante movimientos coordinados.", "Reconoce sus posibilidades de equilibrio en acciones lúdicas.", "Utiliza su cuerpo para expresar emociones en juegos rítmicos."],
                    "3° GRADO": ["Reconoce derecha e izquierda con relación a objetos y compañeros.", "Coordina movimientos en situaciones lúdicas y regula el equilibrio.", "Vivencia ritmos corporales mediante la música."],
                    "4° GRADO": ["Regula la posición del cuerpo en situaciones de equilibrio dinámico.", "Alterna lados corporales en actividades lúdicas y predeportivas.", "Crea secuencias de movimientos usando lenguaje corporal."],
                    "5° GRADO": ["Aplica la alternancia de lados corporales anticipando acciones motrices.", "Regula su cuerpo en carreras, saltos y lanzamientos predeportivos.", "Crea movimientos rítmicos basados en la música de su región."],
                    "6° GRADO": ["Anticipa acciones motrices evaluando espacio y tiempo en juegos.", "Afianza habilidades motrices específicas en contextos predeportivos.", "Crea con sus pares secuencias de movimiento expresivas estructuradas."]
                }
            },
            {
                "nombre": "ASUME UNA VIDA SALUDABLE",
                "capacidades": [
                    "Comprende las relaciones entre la actividad física, alimentación, postura e higiene personal y del ambiente, y la salud.",
                    "Incorpora prácticas que mejoran su calidad de vida."
                ],
                "estandares": {
                    "III CICLO": "Diferencia alimentos saludables, reconoce momentos de hidratación, posturas adecuadas y participa en actividades lúdicas identificando ritmo cardiaco y respiración.",
                    "IV CICLO": "Diferencia alimentos de la región, previene riesgos posturales, aplica calentamiento corporal antes de jugar e incorpora ritmos de actividad y descanso.",
                    "V CICLO": "Evalúa su aptitud física e IMC, adapta hábitos alimenticios, evita ejercicios contraindicados y realiza ejercicios de activación y relajación."
                },
                "desempenos": {
                    "1° GRADO": ["Describe alimentos saludables de su dieta familiar.", "Regula el esfuerzo reconociendo inspiración y espiración.", "Adopta posturas adecuadas y hábitos de higiene."],
                    "2° GRADO": ["Explica la importancia del calentamiento antes de jugar.", "Diferencia alimentos nutritivos e importancia de la hidratación.", "Adopta posturas correctas en juegos y actividades cotidianas."],
                    "3° GRADO": ["Aplica activación corporal y psicológica antes del juego.", "Adapta el esfuerzo según los cambios en su ritmo cardiaco.", "Clasifica alimentos de su región en saludables o no."],
                    "4° GRADO": ["Selecciona ejercicios de activación e identifica frecuencia cardiaca.", "Incorpora en su dieta alimentos energéticos de la región.", "Adopta posturas para prevenir problemas musculares y óseos."],
                    "5° GRADO": ["Explica factores de la aptitud física e IMC.", "Describe posturas y ejercicios contraindicados para la salud.", "Realiza la activación y recuperación antes y después del ejercicio."],
                    "6° GRADO": ["Utiliza pruebas para evaluar su aptitud física y salud.", "Evita posturas y ejercicios perjudiciales.", "Desarrolla hábitos saludables rechazando sustancias nocivas."]
                }
            },
            {
                "nombre": "INTERACTÚA A TRAVÉS DE SUS HABILIDADES SOCIOMOTRICES",
                "capacidades": [
                    "Se relaciona utilizando sus habilidades sociomotrices.",
                    "Crea y aplica estrategias y tácticas de juego."
                ],
                "estandares": {
                    "III CICLO": "Interactúa en juegos aceptando al compañero, evitando violencia y buscando el bien común. Aplica estrategias colectivas y reglas adaptadas.",
                    "IV CICLO": "Interactúa tomando acuerdos, proponiendo adaptaciones para la inclusión de todos. Adapta estrategias de juego anticipando intenciones.",
                    "V CICLO": "Interactúa proactivamente con sentido de cooperación. Selecciona tácticas de juego en actividades lúdicas y predeportivas."
                },
                "desempenos": {
                    "1° GRADO": ["Asume roles dentro del equipo e interactúa espontáneamente.", "Participa en juegos cooperativos respetando al oponente.", "Llega a acuerdos para cumplir objetivos lúdicos."],
                    "2° GRADO": ["Muestra respeto en el juego evitando expresiones bruscas o apodos.", "Adecúa reglas para la inclusión de sus compañeros.", "Resuelve colectivamente situaciones de conflicto en el juego."],
                    "3° GRADO": ["Propone cambios en reglas para garantizar la inclusión de sus pares.", "Genera estrategias grupales en actividades lúdicas.", "Llega a consensos sobre la manera de jugar."],
                    "4° GRADO": ["Modifica normas de juego según necesidades e intereses del grupo.", "Propone estrategias previendo intenciones de los oponentes.", "Promueve la inclusión y el cumplimiento de acuerdos."],
                    "5° GRADO": ["Aplica el diálogo para solucionar conflictos durante los juegos.", "Asume cambio de roles y respeta diferencias individuales.", "Propone soluciones tácticas en juegos tradicionales y predeportivos."],
                    "6° GRADO": ["Toma decisiones colectivas solidarias en actividades en la naturaleza.", "Modifica reglas de juego para adaptarlas a la lógica deportiva.", "Aplica estrategias ofensivas y defensivas en deportes escolares."]
                }
            }
        ]
    },

    "Enfoques Transversales": [
        {
            "nombre": "Enfoque de Derechos",
            "valores": "Conciencia de derechos, Libertad y responsabilidad, Diálogo y concertación",
            "actitudes": "Disposición a conocer, reconocer y valorar los derechos individuales y colectivos que tenemos las personas en el ámbito privado y público."
        },
        {
            "nombre": "Enfoque Inclusivo o de Atención a la diversidad",
            "valores": "Respeto por las diferencias, Equidad en la enseñanza, Confianza en la persona",
            "actitudes": "Reconocimiento al valor inherente de cada persona y de sus derechos, por encima de cualquier diferencia."
        },
        {
            "nombre": "Enfoque Intercultural",
            "valores": "Respeto a la identidad cultural, Justicia, Diálogo intercultural",
            "actitudes": "Reconocimiento al valor de las diversas identidades culturales y relaciones de pertenencia de los estudiantes."
        },
        {
            "nombre": "Enfoque Igualdad de Género",
            "valores": "Igualdad y Dignidad, Justicia, Empatía",
            "actitudes": "Reconocimiento al valor inherente de cada persona, por encima de cualquier diferencia de género."
        },
        {
            "nombre": "Enfoque Ambiental",
            "valores": "Solidaridad planetaria y equidad intergeneracional, Justicia y solidaridad, Respeto a toda forma de vida",
            "actitudes": "Disposición para colaborar con el bienestar y la calidad de vida de las generaciones presentes y futuras, así como con la naturaleza asumiendo el cuidado del planeta."
        },
        {
            "nombre": "Enfoque Orientación al bien común",
            "valores": "Equidad y justicia, Solidaridad, Empatía, Responsabilidad",
            "actitudes": "Disposición a valorar y proteger los bienes comunes y compartidos de un colectivo."
        },
        {
            "nombre": "Enfoque Búsqueda de la Excelencia",
            "valores": "Flexibilidad y apertura, Superación personal",
            "actitudes": "Disposición para adaptarse a los cambios, modificando si fuera necesario la propia conducta para alcanzar determinados objetivos."
        }
    ]
}


# ==============================================================================
# FUNCIONES AUXILIARES DE CONSULTA
# ==============================================================================

def obtener_lista_areas():
    """Devuelve la lista con los nombres de todas las áreas curriculares."""
    return [area for area in CNEB_PRIMARIA.keys() if area != "Enfoques Transversales"]

def obtener_competencias(area: str):
    """Devuelve los nombres de las competencias asociadas a un área curricular."""
    if area in CNEB_PRIMARIA and "competencias" in CNEB_PRIMARIA[area]:
        return [c["nombre"] for c in CNEB_PRIMARIA[area]["competencias"]]
    return []

def obtener_capacidades(area: str, competencia_nombre: str):
    """Devuelve las capacidades asociadas a una competencia de un área."""
    if area in CNEB_PRIMARIA and "competencias" in CNEB_PRIMARIA[area]:
        for c in CNEB_PRIMARIA[area]["competencias"]:
            if c["nombre"].strip().upper() == competencia_nombre.strip().upper():
                return c.get("capacidades", [])
    return []

def obtener_estandar(area: str, competencia_nombre: str, grado_o_ciclo: str):
    """Devuelve el texto completo del estándar de aprendizaje según ciclo o grado."""
    ciclo = obtener_ciclo_por_grado(grado_o_ciclo) if ("grado" in grado_o_ciclo.lower() or "°" in grado_o_ciclo) else grado_o_ciclo.upper()
    if area in CNEB_PRIMARIA and "competencias" in CNEB_PRIMARIA[area]:
        for c in CNEB_PRIMARIA[area]["competencias"]:
            if c["nombre"].strip().upper() == competencia_nombre.strip().upper():
                return c.get("estandares", {}).get(ciclo, "Estándar no disponible para el ciclo especificado.")
    return "Estándar no encontrado."

def obtener_desempenos(area: str, competencia_nombre: str, grado: str):
    """Devuelve los desempeños para un grado determinado (ej. '3° GRADO' o '3')."""
    grado_clean = str(grado).upper().strip()
    if "°" not in grado_clean and "GRADO" not in grado_clean:
        grado_clean = f"{grado_clean}° GRADO"
    elif "GRADO" not in grado_clean:
        grado_clean = f"{grado_clean} GRADO"

    if area in CNEB_PRIMARIA and "competencias" in CNEB_PRIMARIA[area]:
        for c in CNEB_PRIMARIA[area]["competencias"]:
            if c["nombre"].strip().upper() == competencia_nombre.strip().upper():
                return c.get("desempenos", {}).get(grado_clean, ["Desempeño no disponible para el grado seleccionado."])
    return []

def obtener_enfoques_transversales():
    """Devuelve la lista completa de enfoques transversales, valores y actitudes."""
    return CNEB_PRIMARIA.get("Enfoques Transversales", [])
