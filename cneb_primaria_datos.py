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
        "Construye su identidad": {
            "estandares": {
                "III_CICLO": (
                    "Construye su identidad al tomar conciencia de los aspectos que lo hacen único, "
                    "cuando se reconoce a sí mismo a partir de sus características físicas, habilidades y gustos. "
                    "Se da cuenta que es capaz de realizar tareas y aceptar retos. Disfruta de ser parte de su "
                    "familia, escuela y comunidad. Reconoce y expresa sus emociones y las regula a partir de la "
                    "interacción con sus compañeros y docente, y de las normas establecidas de manera conjunta. "
                    "Explica con razones sencillas por qué algunas acciones cotidianas causan malestar a él o a los "
                    "demás, y por qué otras producen bienestar a todos. Se reconoce como mujer o varón y explica "
                    "que ambos pueden realizar las mismas actividades. Muestra afecto a las personas que estima e "
                    "identifica a las personas que le hacen sentir protegido y seguro y recurre a ellas cuando las necesita."
                ),
                "IV_CICLO": (
                    "Construye su identidad al tomar conciencia de los aspectos que lo hacen único, cuando "
                    "se reconoce a sí mismo a partir de sus características físicas, cualidades, habilidades, "
                    "intereses y logros y valora su pertenencia familiar y escolar. Distingue sus diversas emociones "
                    "y comportamientos, menciona las causas y las consecuencias de estos y las regula usando estrategias "
                    "diversas. Explica con sus propios argumentos por qué considera buenas o malas determinadas acciones. "
                    "Se relaciona con las personas con igualdad, reconociendo que todos tienen diversas capacidades. "
                    "Desarrolla comportamientos que fortalecen las relaciones de amistad. Identifica situaciones que "
                    "afectan su privacidad o la de otros y busca ayuda cuando alguien no la respeta."
                ),
                "V_CICLO": (
                    "Construye su identidad al tomar conciencia de los aspectos que lo hacen único, cuando "
                    "se reconoce a sí mismo a partir de sus características personales, sus capacidades y limitaciones "
                    "reconociendo el papel de las familias en la formación de dichas características. Aprecia su "
                    "pertenencia cultural a un país diverso. Explica las causas y consecuencias de sus emociones, "
                    "y utiliza estrategias para regularlas. Manifiesta su punto de vista frente a situaciones de conflicto "
                    "moral, en función de cómo estas le afectan a él o a los demás. Examina sus acciones en situaciones "
                    "de conflicto moral que se presentan en la vida cotidiana y se plantea comportamientos que tomen en "
                    "cuenta principios éticos. Establece relaciones de igualdad entre hombres y mujeres, y explica su "
                    "importancia. Crea vínculos afectivos positivos y se sobrepone cuando estos cambian. Identifica "
                    "conductas para protegerse de situaciones que ponen en riesgo su integridad en relación a su sexualidad."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Expresa de diversas maneras algunas de sus características físicas, cualidades, gustos y preferencias, y las diferencia de las de los demás. Ejemplo: El estudiante, al realizar actividades individuales y colectivas, podría decir: 'Yo soy bueno dibujando y mi amiga es buena bailando'. O expresar que es capaz de realizar tareas: 'Yo barro'.",
                    "Compartes con sus compañeros las costumbres y actividades de su familia e institución educativa explicando su participación en ellas.",
                    "Describe, a través de diversas formas de representación, las emociones básicas (alegría, tristeza, miedo u otras) y explica las razones que las originan. Acepta e incorpora en sus acciones algunas normas básicas como límites que le brindan seguridad.",
                    "Autorregula sus emociones en interacción con sus compañeros, con apoyo del docente, al aplicar estrategias básicas de autorregulación (respiración).",
                    "Menciona acciones cotidianas que considera buenas o malas, a partir de sus propias experiencias.",
                    "Participa en juegos y otras actividades de la vida cotidiana sin hacer distinciones de género.",
                    "Identifica a las personas que le muestran afecto y lo hacen sentir protegido y seguro; recurre a ellas cuando las necesita."
                ],
                "2_GRADO": [
                    "Expresa sus características físicas, habilidades y gustos, y explica las razones de aquello que le agrada de sí mismo. Ejemplo: El estudiante podría decir: 'Me gustan mis manos porque con ellas puedo dibujar lindo'. Realiza actividades individuales y colectivas mostrando autonomía y asumiendo retos.",
                    "Expresa agrado al representar las manifestaciones culturales de su familia, institución educativa y comunidad.",
                    "Describe las emociones a partir de su experiencia y de lo que observa en los demás, y las regula teniendo en cuenta normas establecidas de manera conjunta. Aplica estrategias de autorregulación (respiración), con la guía del docente.",
                    "Identifica acciones que causan malestar o bienestar a sí mismo o a sus compañeros, y las explica con razones sencillas.",
                    "Explica las diferencias y similitudes entre las niñas y los niños, señalando que todos pueden realizar las mismas actividades tanto en la institución educativa como en la casa, y se relaciona de forma respetuosa con sus compañeros.",
                    "Dialoga con sus compañeros, con el apoyo del docente, sobre situaciones simuladas o personales en las que haya peligro de vulneración de su espacio personal. Explica qué puede hacer y a quiénes puede recurrir en esos casos."
                ],
                "3_GRADO": [
                    "Describe aquellas características personales, cualidades, habilidades y logros que hacen que se sienta orgulloso de sí mismo; se reconoce como una persona valiosa con características únicas.",
                    "Comparte las manifestaciones culturales, tradiciones y costumbres propias de su familia que hacen que se sienta orgulloso de su origen.",
                    "Describe sus emociones en situaciones cotidianas; reconoce sus causas y consecuencias. Aplica estrategias de autorregulación (ponerse en el lugar del otro, respiración y relajación).",
                    "Identifica situaciones y comportamientos que le causan agrado o desagrado, y explica de manera sencilla por qué.",
                    "Explica que los niños y las niñas pueden asumir las mismas responsabilidades y tareas, y que pueden establecer lazos de amistad basados en el respeto.",
                    "Reconoce a qué personas puede recurrir en situaciones de riesgo o en situaciones donde se vulnera su privacidad."
                ],
                "4_GRADO": [
                    "Describe sus características físicas, cualidades e intereses, y las fortalezas que le permiten lograr sus metas; manifiesta que estas lo hace una persona única y valiosa que forma parte de una comunidad familiar y escolar. Participa con seguridad y confianza en las tradiciones, costumbres y prácticas culturales que caracterizan a su familia e institución educativa, y muestra aprecio por ellas.",
                    "Relaciona sus diversas emociones con su comportamiento y el de sus compañeros; menciona las causas y consecuencias de estas y las regula mediante el uso de diferentes estrategias de autorregulación (ponerse en el lugar del otro, respiración y relajación).",
                    "Explica con argumentos sencillos por qué considera buenas o malas determinadas acciones o situaciones.",
                    "Se relaciona con niñas y niños con igualdad y respeto, reconoce que puede desarrollar diversas habilidades a partir de las experiencias vividas y realiza actividades que le permiten fortalecer sus relaciones de amistad.",
                    "Identifica situaciones que afectan su privacidad o que lo ponen en riesgo, y explica la importancia de buscar ayuda recurriendo a personas que le dan seguridad."
                ],
                "5_GRADO": [
                    "Explica sus características personales (cualidades, gustos, fortalezas y limitaciones), las cuales le permiten definir y fortalecer su identidad con relación a su familia.",
                    "Describe las prácticas culturales de su familia, institución educativa y comunidad señalando semejanzas y diferencias.",
                    "Describe sus emociones y explica sus causas y posibles consecuencias. Aplica estrategias de autorregulación (respiración, distanciamiento, relajación y visualización).",
                    "Explica las razones de por qué una acción es correcta o incorrecta, a partir de sus experiencias, y propone acciones que se me ajusten a las normas y a los principios éticos.",
                    "Se relaciona con sus compañeros con igualdad, respeto y cuidado del otro; rechaza cualquier manifestación de violencia de género (mensajes sexistas, lenguaje y trato ofensivo para la mujer, entre otros) en el aula, en la institución educativa y en su familia.",
                    "Describe situaciones que ponen en riesgo su integridad, así como las conductas para evitarlas o protegerse."
                ],
                "6_GRADO": [
                    "Explica las características personales (cualidades, gustos, fortalezas y limitaciones) que tiene por ser parte de una familia, así como la contribución de esta a su formación personal y a su proyecto de vida.",
                    "Explica diversas prácticas culturales de su familia, institución educativa y comunidad, y reconoce que aportan a la diversidad cultural del país.",
                    "Explica las causas y consecuencias de sus emociones y sentimientos, en sí mismo y en los demás, en situaciones reales e hipotéticas. Utiliza estrategias de autorregulación (respiración, distanciamiento, relajación y visualización) de acuerdo a la situación que se presenta.",
                    "Argumenta su postura en situaciones propias de su edad, reales o simuladas, que involucran un dilema moral, considerando cómo estas afectan a él o a los demás.",
                    "Evalúa sus acciones en situaciones de conflicto moral y se plantea comportamientos tomando en cuenta las normas sociales y los principios éticos.",
                    "Participa en diversas actividades con sus compañeros en situaciones de igualdad, cuidando y respetando su espacio personal, su cuerpo y el de los demás.",
                    "Propone conductas para protegerse en situaciones que ponen en riesgo su integridad con relación a su sexualidad."
                ]
            }
        },
        "Convive y participa democráticamente en la búsqueda del bien común": {
            "estandares": {
                "III_CICLO": (
                    "Convive y participa democráticamente cuando se relaciona con los demás respetando las diferencias "
                    "y cumpliendo con sus deberes. Conoce las costumbres y características de las personas de su localidad o región. "
                    "Construye de manera colectiva acuerdos y normas. Usa estrategias sencillas para resolver conflictos. "
                    "Realiza acciones específicas para el beneficio de todos a partir de la deliberación sobre asuntos de interés común "
                    "tomando como fuente sus experiencias previas."
                ),
                "IV_CICLO": (
                    "Convive y participa democráticamente cuando se relaciona con los demás respetando las diferencias, "
                    "expresando su desacuerdo frente a situaciones que vulneran la convivencia y cumpliendo con sus deberes. "
                    "Conoce las manifestaciones culturales de su localidad, región o país. Construye y evalúa acuerdos y normas "
                    "tomando en cuenta el punto de vista de los demás. Recurre al diálogo para manejar conflictos. Propone y realiza "
                    "acciones colectivas orientadas al bienestar común a partir de la deliberación sobre asuntos de interés público, "
                    "en la que se da cuenta que existen opiniones distintas a la suya."
                ),
                "V_CICLO": (
                    "Convive y participa democráticamente cuando se relaciona con los demás, respetando las diferencias, "
                    "los derechos de cada uno, cumpliendo y evaluando sus deberes. Se interesa por relacionarse con personas de "
                    "culturas distintas y conocer sus costumbres. Construye y evalúa normas de convivencia tomando en cuenta sus "
                    "derechos. Maneja conflictos utilizando el diálogo y la mediación con base en criterios de igualdad o equidad. "
                    "Propone, planifica y realiza acciones colectivas orientadas al bien común, la solidaridad, la protección de las "
                    "personas vulnerables y la defensa de sus derechos. Delibera sobre asuntos de interés público con argumentos "
                    "basados en fuentes y toma en cuenta la opinión de los demás."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Establece relaciones con sus compañeros respetando sus características físicas o culturales. Identifica sus derechos y cumple con sus deberes en el aula de acuerdo a su edad, para beneficio de todos.",
                    "Describe las características culturales que distinguen al pueblo de origen de sus familiares (bailes, comidas, vestimenta, etc.) y las comparte.",
                    "Participa en la elaboración de acuerdos y normas, y los cumple.",
                    "Utiliza estrategias para manejar sus conflictos en el aula con ayuda de un adulto; de esta manera, propicia el buen trato entre compañeros.",
                    "Delibera sobre asuntos de interés común enfatizando en los que se generan durante la convivencia diaria en el aula, para proponer y participar en actividades colectivas orientadas al bienestar de todos, a partir de la identificación de necesidades."
                ],
                "2_GRADO": [
                    "Comparte actividades con sus compañeros respetando sus diferencias y tratándolos con amabilidad y respeto. Cumple con sus deberes en el aula, para beneficio de todos y de acuerdo a su edad.",
                    "Describe las características culturales que distinguen a su localidad o región (bailes, comidas, vestimenta, etc.) y las comparte.",
                    "Participa en la elaboración de acuerdos y normas que reflejen el buen trato entre compañeros, y los cumple.",
                    "Utiliza estrategias para manejar sus conflictos en el aula con ayuda de un adulto; de esta manera, propicia el buen trato entre compañeros.",
                    "Delibera sobre asuntos de interés común enfatizando en los que se generan durante la convivencia diaria en el aula, para proponer y participar en actividades colectivas orientadas al reconocimiento y respeto de sus derechos como niños y niñas, a partir de situaciones cotidianas."
                ],
                "3_GRADO": [
                    "Muestra un trato respetuoso e inclusivo con sus compañeros de aula y expresa su desacuerdo en situaciones de maltrato en su institución educativa. Cumple con sus deberes.",
                    "Describe algunas manifestaciones culturales de su localidad o de su pueblo de origen. Se refiere a sí mismo como integrante de una localidad específica o de un pueblo originario.",
                    "Participa en la elaboración de acuerdos y normas de convivencia en el aula, teniendo en cuenta los deberes y derechos del niño, y escucha las propuestas de sus compañeros; explica la importancia de la participación de todos en dicha elaboración.",
                    "Interviene al observar un conflicto entre compañeros: recurre al diálogo o a un adulto cercano para que intervenga si es necesario.",
                    "Delibera sobre asuntos de interés público para proponer y participar en actividades colectivas orientadas al bien común (seguridad vial, entre otras), a partir de situaciones cotidianas, y reconoce que existen opiniones distintas a la suya."
                ],
                "4_GRADO": [
                    "Muestra un trato respetuoso e inclusivo con sus compañeros de aula y expresa su desacuerdo en situaciones reales e hipotéticas de maltrato y discriminación por razones de etnia, edad, género o discapacidad (niños, ancianos y personas con discapacidad). Cumple con sus deberes.",
                    "Explica algunas manifestaciones culturales de su localidad, región o país. Se refiere a sí mismo como integrante de una localidad específica o de un pueblo originario.",
                    "Participa en la elaboración de acuerdos y normas de convivencia en el aula, teniendo en cuenta los deberes y derechos del niño, y considera las propuestas de sus compañeros. Evalúa el cumplimiento de dichos acuerdos y normas, y propone cómo mejorarlo.",
                    "Propone alternativas de solución a los conflictos por los que atraviesa: recurre al diálogo y a la intervención de mediadores si lo cree necesario.",
                    "Delibera sobre asuntos de interés público (problemas de seguridad vial, delincuencia juvenil, incumplimiento de sus derechos, etc.) para proponer y participar en actividades colectivas orientadas al bien común, y reconoce que existen opiniones distintas a la suya."
                ],
                "5_GRADO": [
                    "Muestra un trato respetuoso e inclusivo con sus compañeros de aula y propone acciones para mejorar la convivencia a partir de la reflexión sobre conductas propias o de otros. Evalúa el cumplimiento de sus deberes.",
                    "Muestra interés por participar en actividades que le permitan relacionarse con sus compañeros y personas de distintas culturas para conocer sus costumbres.",
                    "Participa en la construcción consensuada de normas de convivencia del aula, teniendo en cuenta los deberes y derechos del niño, y evalúa su cumplimiento.",
                    "Utiliza el diálogo y la negociación para superar los conflictos. Explica que los conflictos se originan por no reconocer a los otros como sujetos con los mismos derechos y por falta de control de las emociones.",
                    "Propone, a partir de un diagnóstico y de la deliberación sobre asuntos públicos, acciones orientadas al bien común, la solidaridad, la protección de personas vulnerables y la defensa de sus derechos. Sustenta su posición basándose en fuentes."
                ],
                "6_GRADO": [
                    "Establece relaciones con sus compañeros sin discriminarlos. Propone acciones para mejorar la interacción entre compañeros, a partir de la reflexión sobre conductas propias o de otros, en las que se evidencian los prejuicios y estereotipos más comunes de su entorno (de género, raciales, entre otros). Evalúa el cumplimiento de sus deberes y los de sus compañeros, y propone cómo mejorarlo.",
                    "Se comunica por diversos medios con personas de una cultura distinta a la suya (afrodescendiente, tusán, nisei, entre otras), para aprender de ella.",
                    "Participa en la construcción consensuada de normas de convivencia del aula, teniendo en cuenta los deberes y derechos del niño, y evalúa su cumplimiento. Cumple con sus deberes y promueve que sus compañeros también lo hagan.",
                    "Recurre al diálogo o a mediadores para solucionar conflictos y buscar la igualdad o equidad; propone alternativas de solución.",
                    "Propone, a partir de un diagnóstico y de la deliberación sobre asuntos públicos, acciones orientadas al bien común, la solidaridad, la protección de personas vulnerables y la defensa de sus derechos, tomando en cuenta la opinión de los demás. Sustenta su posición basándose en fuentes."
                ]
            }
        },
        "Construye interpretaciones históricas": {
            "estandares": {
                "III_CICLO": (
                    "Construye interpretaciones históricas en las que describe los cambios ocurridos en su familia "
                    "y comunidad a partir de comparar el presente y el pasado, y de reconocer algunas causas y "
                    "consecuencias de estos cambios. Obtiene información sobre el pasado de diversos tipos de "
                    "fuentes, así como expresiones temporales propias de la vida cotidiana. Secuencia hechos o "
                    "acciones cotidianas ocurridos en periodos de tiempo cortos e identifica acciones simultáneas."
                ),
                "IV_CICLO": (
                    "Construye interpretaciones históricas en las que narra hechos y procesos relacionados a la "
                    "historia de su región, en los que incorpora más de una dimensión y reconoce diversas causas y "
                    "consecuencias. Utiliza información de diversas fuentes a partir de identificar las más "
                    "pertinentes para responder sus preguntas. Organiza secuencias para comprender cambios ocurridos "
                    "a través del tiempo, aplicando términos relacionados al tiempo."
                ),
                "V_CICLO": (
                    "Construye interpretaciones históricas en las que explica, de manera general, procesos históricos "
                    "peruanos, empleando algunas categorías temporales. Identifica las causas inmediatas y lejanas "
                    "que desencadenaron dichos procesos, así como las consecuencias cuyos efectos se ven de inmediato "
                    "o a largo plazo. Ordena cronológicamente procesos históricos peruanos y describe algunos cambios, "
                    "permanencias y simultaneidades producidos en ellos. Utiliza información de diversas fuentes "
                    "a partir de identificar su origen y distinguiendo algunas diferencias entre las versiones que dan "
                    "sobre los procesos históricos."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Obtiene información sobre sí mismo o sobre diversos hechos cotidianos del pasado, a partir del testimonio oral de dos o más personas, y de objetos en desuso, fotografías, etc.",
                    "Ordena hechos o acciones de su vida cotidiana usando expresiones que hagan referencia al paso del tiempo: ayer, hoy, mañana; antes, ahora; al inicio, al final; mucho tiempo, poco tiempo.",
                    "Describe acontecimientos de su historia personal y familiar, en los que compara el presente y el pasado; identifica alguna causa de los cambios."
                ],
                "2_GRADO": [
                    "Obtiene información de imágenes y objetos antiguos, testimonios de personas y expresiones temporales propias de la vida cotidiana, y reconoce que estos le brindan mayor información sobre su historia familiar y la de su comunidad.",
                    "Secuencia acciones o hechos cotidianos de su vida personal, familiar y de la comunidad, y reconoce aquellos que suceden de manera simultánea.",
                    "Describe acontecimientos de su historia y de la comunidad a partir de objetos, imágenes y testimonios de personas, en los que compara el presente y el pasado; identifica algunas causas y posibles consecuencias de los cambios."
                ],
                "3_GRADO": [
                    "Obtiene información acerca del proceso del poblamiento americano y de las primeras bandas a las primeras aldeas en el Perú, en textos cortos, así como en edificios antiguos o conjuntos arqueológicos de la localidad.",
                    "Explica la importancia de fuentes históricas, como textos, edificios antiguos o conjuntos arqueológicos de la localidad; identifica al autor o colectivo humano que las produjo.",
                    "Secuencia imágenes, objetos o hechos utilizando categorías temporales (antes, ahora y después; años, décadas y siglos); describe algunas características que muestran los cambios en diversos aspectos de la vida cotidiana y de la historia del poblamiento americano hasta el proceso de sedentarización.",
                    "Narra procesos históricos, como el poblamiento americano y el de la sedentarización; reconoce más de una causa y algunas consecuencias."
                ],
                "4_GRADO": [
                    "Identifica fuentes pertinentes que contengan la información que necesita para responder preguntas relacionadas con las principales sociedades prehispánicas y la Conquista.",
                    "Obtiene información sobre hechos concretos en fuentes de divulgación y difusión histórica (enciclopedias, páginas webs, libros de texto, videos, etc.), y la utiliza para responder preguntas con relación a las principales sociedades andinas, preincas e incas, y la Conquista.",
                    "Secuencia imágenes, objetos o hechos, y describe algunas características que muestran los cambios en diversos aspectos de la vida cotidiana y de las grandes etapas convencionales de la historia del Perú utilizando categorías temporales (años, décadas y siglos).",
                    "Explica hechos o procesos históricos claves de su región, de las principales sociedades andinas, preincas e incas, y la Conquista; reconoce las causas que los originaron y sus consecuencias teniendo en cuenta más de una dimensión (política, económica, ambiental, social, cultural, entre otras)."
                ],
                "5_GRADO": [
                    "Obtiene información sobre un hecho o proceso histórico, desde el Virreinato hasta el proceso de la Independencia del Perú, a partir de cuadros estadísticos, gráficos sencillos o investigaciones históricas.",
                    "Identifica en qué se diferencian las narraciones sobre un mismo acontecimiento del pasado relacionado con el Virreinato y el proceso de Independencia del Perú.",
                    "Secuencia cronológicamente las grandes etapas convencionales de la historia nacional y distingue qué las caracteriza.",
                    "Identifica cambios y permanencias con relación a la economía, la política y la sociedad entre el Virreinato y la actualidad.",
                    "Identifica algunas causas que tienen origen en acciones individuales y otras que se originan en acciones colectivas, con relación al Virreinato y al proceso de Independencia del Perú.",
                    "Explica el proceso de Independencia del Perú y Sudamérica; reconoce la participación de hombres y mujeres en dichos acontecimientos."
                ],
                "6_GRADO": [
                    "Selecciona fuentes que le proporcionan información sobre hechos y procesos históricos peruanos del siglo XIX y XX, y los ubica en el momento en que se produjeron.",
                    "Identifica las diferencias entre las versiones que las fuentes presentan sobre hechos o procesos históricos peruanos del siglo XIX y XX.",
                    "Secuencia distintos hechos de la historia local, regional y nacional del Perú de los siglos XIX y XX; identifica cambios, permanencias y simultaneidades.",
                    "Explica hechos o procesos históricos peruanos del siglo XIX y XX utilizando categorías temporales relacionadas con el tiempo histórico, e identifica algunas causas y consecuencias inmediatas y de largo plazo.",
                    "Explica hechos y procesos históricos peruanos del siglo XIX y XX; reconoce la participación de hombres y mujeres en ellos."
                ]
            }
        },
        "Gestiona responsablemente el espacio y el ambiente": {
            "estandares": {
                "III_CICLO": (
                    "Gestiona responsablemente el espacio y ambiente al desarrollar actividades sencillas frente "
                    "a los problemas y peligros que lo afectan. Explica de manera sencilla las relaciones directas "
                    "que se dan entre los elementos naturales y sociales de su espacio cotidiano. Utiliza puntos de "
                    "referencia para ubicarse, desplazarse y representar su espacio."
                ),
                "IV_CICLO": (
                    "Gestiona responsablemente el espacio y ambiente al realizar actividades específicas para su "
                    "cuidado a partir de reconocer las causas y consecuencias de los problemas ambientales. "
                    "Reconoce cómo sus acciones cotidianas impactan en el ambiente, en el calentamiento global y en su bienestar, "
                    "e identifica los lugares vulnerables y seguros de su escuela, frente a riesgos de desastres. Describe las "
                    "características de los espacios geográficos y el ambiente de su localidad o región. Utiliza representaciones "
                    "cartográficas sencillas, tomando en cuenta los puntos cardinales y otros elementos cartográficos, para ubicar "
                    "elementos del espacio."
                ),
                "V_CICLO": (
                    "Gestiona responsablemente el espacio y ambiente al realizar frecuentemente actividades para "
                    "su cuidado y al disminuir los factores de vulnerabilidad frente al cambio climático y a los "
                    "riesgos de desastres en su escuela. Utiliza distintas fuentes y herramientas cartográficas y "
                    "socioculturales para ubicar elementos en el espacio geográfico y el ambiente, y compara estos espacios "
                    "a diferentes escalas considerando la acción de los actores sociales. Explica las problemáticas "
                    "ambientales y territoriales a partir de sus causas, consecuencias y sus manifestaciones a diversas escalas."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Describe los elementos naturales y sociales del espacio donde realiza sus actividades cotidianas.",
                    "Se desplaza utilizando puntos de referencia y nociones espaciales ('delante de' - 'detrás de', 'debajo de' - 'encima de', 'al lado de', 'dentro de' - 'fuera de', 'cerca de' - 'lejos de', 'derecha-izquierda'...) para ubicarse en su espacio cotidiano.",
                    "Representa de diversas maneras su espacio cotidiano utilizando puntos de referencia.",
                    "Menciona los problemas ambientales que afectan a su espacio cotidiano (contaminación por basura y residuos) y los efectos de estos en su vida; participa de acciones sencillas orientadas al cuidado de su ambiente.",
                    "Reconoce y sigue las señales de evacuación y medidas de seguridad en la institución educativa ante peligros que lo afectan."
                ],
                "2_GRADO": [
                    "Brinda ejemplos de relaciones simples entre elementos naturales y sociales del espacio donde realiza sus actividades cotidianas y de otros espacios geográficos del Perú (Costa, Sierra, Selva y mar).",
                    "Se desplaza en su espacio cotidiano siguiendo instrucciones para localizar objetos, personas o continuar una ruta usando puntos de referencia. Ejemplo: El estudiante se desplaza desde la institución educativa hasta la plaza de la comunidad.",
                    "Representa su espacio cotidiano de diversas maneras (dibujos, croquis, maquetas, etc.) utilizando puntos de referencia.",
                    "Identifica las posibles causas y consecuencias de los problemas ambientales (contaminación de aire, suelo y del aire) que afectan su espacio cotidiano; participa de acciones sencillas orientadas al cuidado de su ambiente.",
                    "Practica y desarrolla actividades sencillas para prevenir accidentes y actuar en emergencias, en su aula y hogar, y conservar su ambiente: arrojar residuos sólidos en los tachos, cerrar el caño luego de usarlo, cuidar las plantas, etc."
                ],
                "3_GRADO": [
                    "Distingue los elementos naturales y sociales de su localidad y región; asocia recursos naturales con actividades económicas.",
                    "Identifica los elementos cartográficos que están presentes en planos y mapas, y los utiliza para ubicar elementos del espacio geográfico de su localidad.",
                    "Describe los problemas ambientales de su localidad y región; propone y realiza actividades orientadas a solucionarlos y a mejorar la conservación del ambiente desde su escuela, evaluando su efectividad a fin de llevarlas a cabo.",
                    "Identifica en su escuela los lugares seguros y vulnerables ante desastres de diversos tipos, y participa en actividades para la prevención (simulacros, señalización, etc.)."
                ],
                "4_GRADO": [
                    "Describe los espacios geográficos urbanos y rurales de su localidad y región, y de un área natural protegida; reconoce la relación entre los elementos naturales y sociales que los componen.",
                    "Identifica los elementos cartográficos que están presentes en planos y mapas, y los utiliza para ubicar elementos del espacio geográfico de su localidad y región.",
                    "Describe los problemas ambientales de su localidad y región e identifica las acciones cotidianas que los generan, así como sus consecuencias. A partir de ellas, propone y realiza actividades orientadas a la conservación del ambiente en su institución educativa, localidad y región.",
                    "Identifica y describe las principales áreas naturales protegidas de su localidad o región, e investiga sobre los beneficios y servicios ambientales que estas otorgan a los seres humanos, y sobre el impacto que estos tienen para su sostenibilidad.",
                    "Identifica los lugares seguros de su institución educativa ante desastres; propone actividades para la prevención (simulacros, señalización, etc.) y participa en ellas."
                ],
                "5_GRADO": [
                    "Describe las relaciones que se establecen entre los elementos naturales y sociales de un determinado espacio geográfico de su localidad o región, o de un área natural protegida, así como las características de la población que lo habita y las actividades económicas que esta realiza.",
                    "Identifica los elementos cartográficos presentes en planos y mapas que le permitan obtener información sobre los elementos del espacio geográfico y del ambiente.",
                    "Explica las características de una problemática ambiental, como la deforestación, la contaminación del mar, la desertificación y la pérdida de suelo, y las de una problemática territorial, como el caos en el transporte, a nivel local.",
                    "Explica los factores de vulnerabilidad ante desastres naturales en su institución educativa, localidad y región; propone y ejecuta acciones para reducirlos o adaptarse a ellos.",
                    "Explica el uso de recursos naturales renovables y no renovables que realiza su escuela, y planifica y ejecuta actividades orientadas a mejorar las prácticas de su escuela para la conservación del ambiente relacionadas al manejo y uso del agua, la energía, 3R y residuos sólidos, conservación de los ecosistemas, transporte, entre otros."
                ],
                "6_GRADO": [
                    "Compara los elementos naturales y sociales de los espacios geográficos de su localidad y región, y de un área natural protegida, y explica cómo los distintos actores sociales intervienen en su transformación de acuerdo a su función.",
                    "Utiliza diversas fuentes y herramientas cartográficas para obtener información y ubicar elementos en el espacio geográfico y el ambiente.",
                    "Explica los servicios ambientales que brindan las principales áreas naturales protegidas de su localidad o región, y propone y lleva a cabo soluciones prácticas para potenciar sus sostenibilidad.",
                    "Explica las causas y consecuencias de una problemática ambiental, del calentamiento global, y de una problemática territorial, como la expansión urbana versus la reducción de tierras de cultivo, a nivel local, regional y nacional.",
                    "Explica los factores de vulnerabilidad ante desastres, en su escuela y localidad, y aquellos factores de vulnerabilidad local frente a los efectos del cambio climático; propone y ejecuta acciones para reducirlos.",
                    "Explica el uso de recursos naturales renovables y no renovables, y los patrones de consumo de su comunidad, y planifica y ejecuta acciones orientadas a mejorar las prácticas para la conservación del ambiente, en su escuela y en su localidad relacionadas al manejo y uso del agua, la energía, 3R (reducir, reusar y reciclar) y residuos sólidos, conservación de los ecosistemas terrestres y marinos, transporte, entre otros,—teniendo en cuenta el desarrollo sostenible."
                ]
            }
        },
        "Gestiona responsablemente los recursos económicos": {
            "estandares": {
                "III_CICLO": (
                    "Gestiona responsablemente los recursos económicos al utilizar los bienes y servicios con los "
                    "que cuenta en su familia y en la escuela. Reconoce que las personas y las instituciones de su comunidad "
                    "desarrollan actividades económicas para satisfacer sus necesidades y que contribuyen a su bienestar."
                ),
                "IV_CICLO": (
                    "Gestiona responsablemente los recursos económicos al diferenciar entre necesidades y deseos, "
                    "y al usar los servicios públicos de su espacio cotidiano, reconociendo que tienen un costo. "
                    "Reconoce que los miembros de su comunidad se vinculan al desempeñar distintas actividades económicas "
                    "y que estas actividades inciden en su bienestar y en el de las otras personas."
                ),
                "V_CICLO": (
                    "Gestiona responsablemente los recursos económicos al utilizar el dinero y otros recursos "
                    "como consumidor informado y al realizar acciones de ahorro, inversión y cuidado de ellos. "
                    "Explica el papel de la publicidad frente a las decisiones de consumo y en la planificación de los presupuestos "
                    "personales y familiares, así como la importancia de cumplir con el pago de impuestos, tributos y deudas como medio "
                    "para el bienestar común. Explica los roles que cumplen las empresas y el Estado respecto a la satisfacción de las "
                    "necesidades económicas y financieras de las personas."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Explica las ocupaciones que desarrollan las personas de su espacio cotidiano y cómo atienden a sus necesidades y a las de la comunidad.",
                    "Utiliza responsablemente los recursos (pertenencias del estudiante) que le brindan su familia y la institución educativa, y reconoce que estos se agotan."
                ],
                "2_GRADO": [
                    "Explica que los recursos que se consumen en su hogar e institución educativa son producto de las actividades económicas que desarrollan las personas y las instituciones de su comunidad, para satisfacer sus necesidades y obtener bienestar; identifica acciones que le permiten el ahorro.",
                    "Explica que todo producto tiene un costo y que al obtenerlo se debe retribuir por ello (intercambio/dinero/trueque); propone acciones, de acuerdo a su edad, para el uso responsable de los productos en la institución educativa y en su familia."
                ],
                "3_GRADO": [
                    "Explica que el trabajo que realizan sus familiares y demás personas permite la obtención de dinero para la adquisición de ciertos bienes y servicios con la finalidad de satisfacer las necesidades de consumo.",
                    "Usa de manera responsable los recursos, dado que estos se agotan, y realiza acciones cotidianas de ahorro del uso de bienes y servicios que se consumen en su hogar y su institución educativa."
                ],
                "4_GRADO": [
                    "Describe los roles económicos que cumplen las personas de su comunidad e identifica las relaciones que se establecen entre ellas para satisfacer sus necesidades y generar bienestar en las demás.",
                    "Ejecuta acciones que contribuyen a su economía familiar diferenciando entre necesidades y deseos; utiliza responsablemente los servicios públicos de su espacio cotidiano y reconoce que tienen un costo y deben ser bien utilizados."
                ],
                "5_GRADO": [
                    "Explica el proceso económico, el funcionamiento del mercado y cómo las personas, las empresas y el Estado (los agentes económicos) cumplen distintos roles económicos, se organizan y producen bienes y servicios mediante el uso del dinero para la adquisición de estos.",
                    "Argumenta la importancia del ahorro y de la inversión de recursos, así como de la cultura de pago de las deudas contraídas.",
                    "Representa de diversas maneras cómo influye la publicidad en sus decisiones de consumo.",
                    "Argumenta la importancia de conocer los derechos del consumidor.",
                    "Elabora un plan de ahorro y explica cómo el uso del dinero afecta positiva o negativamente a las personas y a las familias."
                ],
                "6_GRADO": [
                    "Explica cómo el Estado promueve y garantiza los intercambios económicos en diferentes sectores y cómo las empresas producen bienes y servicios para contribuir al desarrollo sostenible de la sociedad.",
                    "Argumenta la importancia de cumplir con los compromisos de pago de deudas y responsabilidades tributarias para mejorar los bienes y servicios públicos.",
                    "Explica cuál es el rol de la publicidad y cómo influye en sus decisiones de consumo y en las de su familia.",
                    "Elabora un presupuesto personal y familiar; explica cómo el uso del dinero afecta positiva o negativamente a las personas y a las familias; y formula planes de ahorro e inversión personal y de aula, de acuerdo con metas trazadas y fines previstos.",
                    "Promueve actividades para fomentar el respeto de los derechos del consumidor, la responsabilidad socioambiental de las empresas, el ahorro personal y la cultura de pago de impuestos."
                ]
            }
        }
    },
    "Educación Física": {
        "Se desenvuelve de manera autónoma a través de su motricidad": {
            "estandares": {
                "III_CICLO": (
                    "Se desenvuelve de manera autónoma a través de su motricidad cuando comprende cómo usar su cuerpo "
                    "en las diferentes acciones que realiza utilizando su lado dominante y realiza movimientos coordinados "
                    "que le ayudan a sentirse seguro en la práctica de actividades físicas. Se orienta espacialmente en relación "
                    "a sí mismo y a otros puntos de referencia. Se expresa corporalmente con sus pares utilizando el ritmo, "
                    "gestos y movimientos como recursos para comunicar."
                ),
                "IV_CICLO": (
                    "Se desenvuelve de manera autónoma a través de su motricidad cuando comprende cómo usar su cuerpo "
                    "explorando la alternancia de sus lados corporales de acuerdo a su utilidad y ajustando la posición del cuerpo "
                    "en el espacio y en el tiempo en diferentes etapas de las acciones motrices, con una actitud positiva y una "
                    "voluntad de experimentar situaciones diversas. Experimenta nuevas posibilidades expresivas de su cuerpo y "
                    "las utiliza para relacionarse y comunicar ideas, emociones, sentimientos, pensamientos."
                ),
                "V_CICLO": (
                    "Se desenvuelve de manera autónoma a través de su motricidad cuando acepta sus posibilidades y "
                    "limitaciones según su desarrollo e imagen corporal. Realiza secuencias de movimientos coordinados aplicando "
                    "la alternancia de sus lados corporales de acuerdo a su utilidad. Produce con sus pares secuencias de "
                    "movimientos corporales, expresivos o rítmicos en relación a una intención."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Explora de manera autónoma las posibilidades de su cuerpo en diferentes acciones para mejorar sus movimientos (saltar, correr, lanzar) al mantener y/o recuperar el equilibrio en el espacio y con los objetos, cuando utiliza conscientemente distintas bases de sustentación; así, conoce en sí mismo su lado dominante.",
                    "Se orienta en un espacio y tiempo determinados, reconociendo su lado izquierdo y derecho, y a través de las nociones 'arriba-abajo', 'dentro-fuera', 'cerca-lejos', con relación a sí mismo y de acuerdo a sus intereses y necesidades.",
                    "Explora nuevos movimientos y gestos para representar objetos, personajes, estados de ánimo y ritmos sencillos de distintos orígenes: de la naturaleza, del propio cuerpo, de la música, etc.",
                    "Se expresa motrizmente para comunicar sus emociones (miedo, angustia, alegría, placer, torpeza, inhibición, rabia, entre otras) y representa en el juego acciones cotidianas de su familia y de la comunidad; así, afirma su identidad personal."
                ],
                "2_GRADO": [
                    "Explora de manera autónoma sus posibilidades de movimiento al realizar con seguridad y confianza habilidades motrices básicas, mediante movimientos coordinados según sus intereses, necesidades y posibilidades.",
                    "Se orienta en el espacio y tiempo con relación a sí mismo y a otros puntos de referencia; reconoce sus posibilidades de equilibrio con diferentes bases de sustentación en acciones lúdicas.",
                    "Resuelve situaciones motrices al utilizar su lenguaje corporal (gesto, contacto visual, actitud corporal, apariencia, etc.), verbal y sonoro, que lo ayudan a sentirse seguro, confiado y aceptado.",
                    "Utiliza su cuerpo y el movimiento para expresar ideas y emociones en la práctica de actividades lúdicas con diferentes tipos de ritmos y música, a fin de expresarse corporalmente y mediante el uso de diversos elementos."
                ],
                "3_GRADO": [
                    "Reconoce la izquierda y la derecha con relación a objetos y a sus pares, para mejorar sus posibilidades de movimiento en diferentes acciones lúdicas.",
                    "Se orienta en un espacio y tiempo determinados, con relación a sí mismo, a los objetos y a sus compañeros; coordina sus movimientos en situaciones lúdicas y regula su equilibrio al variar la base de sustentación y la altura de la superficie de apoyo, de esta manera, afianza sus habilidades motrices básicas.",
                    "Resuelve situaciones motrices al utilizar su lenguaje corporal (gestos, contacto visual, actitud corporal, apariencia, etc.), verbal y sonoro para comunicar actitudes, sensaciones, estados de ánimo y acciones que le posibilitan comunicarse mejor con los otros y disfrutar de las actividades lúdicas.",
                    "Vivencia el ritmo y se apropia de secuencias rítmicas corporales en situaciones de juego para expresarse corporalmente a través de la música."
                ],
                "4_GRADO": [
                    "Regula la posición del cuerpo en situaciones de equilibrio, con modificación del espacio, teniendo como referencia la trayectoria de objetos, los otros y sus propios desplazamientos, para afianzar sus habilidades motrices básicas.",
                    "Alterna sus lados corporales de acuerdo a su utilidad y/o necesidad y se orienta en el espacio y en el tiempo, con relación a sí mismo y a otros puntos de referencia en actividades lúdicas y predeportivas.",
                    "Utiliza su cuerpo (posturas, gestos y mímica) y diferentes movimientos para expresar formas, ideas, emociones, sentimientos y pensamientos en la actividad física.",
                    "Utiliza lenguaje corporal para expresar su forma particular de moverse, creando secuencias sencillas de movimientos relacionados con el ritmo, la música de su cultura y la historia de su región."
                ],
                "5_GRADO": [
                    "Aplica la alternancia de sus lados corporales de acuerdo a su preferencia, utilidad y/o necesidad, y anticipa las acciones motrices a realizar en un espacio y tiempo, para mejorar las posibilidades de respuesta en una actividad física.",
                    "Explora y regula su cuerpo para dar respuesta a las situaciones motrices en contextos lúdicos y predeportivos; así, pone en práctica las habilidades motrices relacionadas con la carrera, el salto y los lanzamientos.",
                    "Crea movimientos y desplazamientos rítmicos e incorpora las particularidades de su lenguaje corporal teniendo como base la música de su región, al asumir diferentes roles en la práctica de actividad física.",
                    "Valora en sí mismo y en sus pares nuevas formas de movimiento y gestos corporales; de esta manera, acepta la existencia de nuevas formas de movimiento y expresión para comunicar ideas y emociones en diferentes situaciones motrices."
                ],
                "6_GRADO": [
                    "Aplica la alternancia de sus lados corporales de acuerdo a su preferencia, utilidad y/o necesidad, y anticipa las acciones motrices a realizar en un espacio y tiempo, para mejorar las posibilidades de respuesta en una actividad física.",
                    "Regula su cuerpo para dar respuesta a las situaciones motrices en contextos lúdicos, predeportivos, etc.; de este modo, afianza las habilidades motrices específicas relacionadas con la carrera, el salto y los lanzamientos.",
                    "Expresa su forma particular de moverse, al asumir y adjudicar diferentes roles en la práctica de actividad física, aplicando su lenguaje corporal.",
                    "Crea con sus pares una secuencia de movimientos corporales, expresivos y/o rítmicos, de manera programada y estructurada; así, se expresa de diferentes formas y con diversos recursos, a través del cuerpo y el movimiento, para comunicar ideas y emociones."
                ]
            }
        },
        "Asume una vida saludable": {
            "estandares": {
                "III_CICLO": (
                    "Asume una vida saludable cuando diferencia los alimentos saludables de su dieta personal y familiar, "
                    "los momentos adecuados para ingerirlos y las posturas que lo ayudan al buen desempeño en la práctica de "
                    "actividades físicas, recreativas y de la vida cotidiana, reconociendo la importancia del autocuidado. "
                    "Participa regularmente en la práctica de actividades lúdicas identificando su ritmo cardiaco, respiración "
                    "y sudoración; utiliza prácticas de activación corporal y psicológica antes de la actividad lúdica."
                ),
                "IV_CICLO": (
                    "Asume una vida saludable cuando diferencia los alimentos de su dieta personal, familiar y de su "
                    "región que son saludables de los que no lo son. Previene riesgos relacionados con la postura e higiene "
                    "conociendo aquellas que favorecen y no favorecen su salud e identifica su fuerza, resistencia y velocidad "
                    "en la práctica de actividades lúdicas. Adapta su esfuerzo en la práctica de actividad física de acuerdo a "
                    "las características de la actividad y a sus posibilidades, aplicando conocimientos relacionados con el ritmo "
                    "cardiaco, la respiración y la sudoración. Realiza prácticas de activación corporal y psicológica, e incorpora "
                    "el autocuidado relacionado con los ritmos de actividad y descanso para mejorar el funcionamiento de su organismo."
                ),
                "V_CICLO": (
                    "Asume una vida saludable cuando utiliza instrumentos que miden la aptitud física y estado nutricional "
                    "e interpreta la información de los resultados obtenidos para mejorar su calidad de vida. Replantea sus hábitos "
                    "saludables, higiénicos y alimenticios tomando en cuenta los cambios físicos propios de la edad, evita la realización "
                    "de ejercicios y posturas contraindicadas para la salud en la práctica de actividad física. Incorpora prácticas "
                    "saludables para su organismo consumiendo alimentos adecuados a las características personales y evitando el consumo "
                    "de drogas. Propone ejercicios de activación y relajación antes, durante y después de la práctica y participa en "
                    "actividad física de distinta intensidad regulando su esfuerzo."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Describe los alimentos de su dieta familiar y las posturas que son beneficiosas para su salud en la vida cotidiana y en la práctica de actividades lúdicas.",
                    "Regula su esfuerzo al participar en actividades lúdicas e identifica en sí mismo y en otros la diferencia entre inspiración y espiración, en reposo y movimiento, en las actividades lúdicas.",
                    "Realiza con autonomía prácticas de cuidado personal al asearse, al vestirse, al adoptar posturas adecuadas en la práctica de actividades lúdicas y de la vida cotidiana. Ejemplo: El estudiante usa diversos medios de protección frente a la radiación solar.",
                    "Busca satisfacer sus necesidades corporales cuando tiene sed y resuelve las dificultades que le producen el cansancio, la incomodidad y la inactividad; evidencia su bienestar al realizar actividades lúdicas y se siente bien consigo mismo, con los otros y con su entorno."
                ],
                "2_GRADO": [
                    "Explica la importancia de la activación corporal (calentamiento) y psicológica (atención, concentración y motivación) antes de la actividad lúdica, e identifica los signos y síntomas relacionados con el ritmo cardiaco, la respiración agitada y la sudoración, que aparecen en el organismo al practicar actividades lúdicas.",
                    "Diferencia los alimentos saludables y nutritivos que forman parte de su dieta personal y familiar, y los momentos adecuados para ingerirlos; explica la importancia de hidratarse; conoce las posturas adecuadas en la práctica de actividad física y en la vida cotidiana, que le permiten mayor seguridad.",
                    "Incorpora prácticas de cuidado al asearse y vestirse; adopta posturas adecuadas en la práctica de actividades lúdicas y en la vida cotidiana, que le permiten la participación en el juego sin afectar su desempeño.",
                    "Regula su esfuerzo en la práctica de actividades lúdicas y reconoce la importancia del autocuidado para prevenir enfermedades."
                ],
                "3_GRADO": [
                    "Explica la importancia de la activación corporal (calentamiento) y psicológica (atención, concentración y motivación), que lo ayuda a estar predispuesto a la actividad.",
                    "Practica diferentes actividades lúdicas adaptando su esfuerzo y aplicando los conocimientos de los beneficios de la práctica de actividad física y de la salud relacionados con el ritmo cardiaco, la respiración y la sudoración.",
                    "Incorpora el autocuidado relacionado con los ritmos de actividad-descanso, para mejorar el funcionamiento de su organismo.",
                    "Identifica los alimentos propios de su región que forman parte de su dieta personal y familiar, y los clasifica en saludables o no, de acuerdo a la actividad física que realiza. Reconoce aquellos que son amigables con el ambiente (por el uso que se hacen de los recursos naturales, el empaquetado, etc.)."
                ],
                "4_GRADO": [
                    "Selecciona actividades para la activación corporal (calentamiento) y psicológica (atención, concentración y motivación) antes de la actividad, e identifica en sí mismo las variaciones en la frecuencia cardiaca y respiratoria con relación a los diferentes niveles de esfuerzo en la práctica de actividades lúdicas.",
                    "Selecciona e incorpora en su dieta personal y familiar los alimentos nutritivos y energéticos de la región que contribuyen a su bienestar.",
                    "Incorpora el autocuidado relacionado con los ritmos de actividad-descanso, hidratación y exposición a los rayos solares, para mejorar el funcionamiento de su organismo, y sustenta las razones de su importancia.",
                    "Adopta posturas adecuadas para prevenir problemas musculares y óseos e incorpora el autocuidado relacionado con los ritmos de actividad-descanso para mejorar el funcionamiento de su organismo y prevenir enfermedades."
                ],
                "5_GRADO": [
                    "Explica las condiciones que favorecen la aptitud física (Índice de Masa Corporal - IMC, consumo de alimentos favorables, cantidad y proporción necesarias) y las pruebas que la miden (resistencia, velocidad, flexibilidad y fuerza) para mejorar la calidad de vida, con relación a sus características personales.",
                    "Adapta sus prácticas de higiene a los cambios físicos propios de la edad; describe las prácticas alimenticias beneficiosas y perjudiciales para el organismo y el ambiente, y analiza la importancia de la alimentación con relación a su IMC.",
                    "Describe posturas y ejercicios contraindicados para la salud en la práctica de actividad física.",
                    "Realiza actividades de activación corporal, psicológica y de recuperación antes, durante y después de la práctica de actividad física; de esta manera, aplica los beneficios relacionados con la salud y planifica dietas saludables adaptadas a su edad y sus recursos."
                ],
                "6_GRADO": [
                    "Utiliza diferentes métodos de evaluación para determinar la aptitud física; asimismo, selecciona los que mejor se adecúen a sus posibilidades y utiliza la información que obtiene en beneficio de su salud.",
                    "Explica la relación entre los cambios físicos propios de la edad y la repercusión en la higiene, en la práctica de actividad física y en actividades de la vida cotidiana; practica actividad física y explica la importancia que tiene en su vida cotidiana.",
                    "Realiza actividad física y evita posturas y ejercicios contraindicados que perjudican su salud.",
                    "Muestra hábitos saludables y evita hábitos perjudiciales para su organismo, como el consumo de comida rápida, de alcohol, de tabaco, de drogas, desórdenes alimenticios, entre otros; proporciona el fundamento respectivo y desarrolla dietas saludables.",
                    "Explica la importancia de la vacunación y sus consecuencias en la salud."
                ]
            }
        },
        "Interactúa a través de sus habilidades sociomotrices": {
            "estandares": {
                "III_CICLO": (
                    "Interactúa a través de sus habilidades sociomotrices al aceptar al otro como compañero de juego "
                    "y busca el consenso sobre la manera de jugar para lograr el bienestar común y muestra una actitud de "
                    "respeto evitando juegos violentos y humillantes; expresa su posición ante un conflicto con intención de "
                    "resolverlo y escucha la posición de sus compañeros en los diferentes tipos de juegos. Resuelve "
                    "situaciones motrices a través de estrategias colectivas y participa en la construcción de reglas de juego "
                    "adaptadas a la situación y al entorno, para lograr un objetivo común en la práctica de actividades lúdicas."
                ),
                "IV_CICLO": (
                    "Interactúa a través de sus habilidades sociomotrices al tomar acuerdos sobre la manera de jugar "
                    "y los posibles cambios o conflictos que se den y propone adaptaciones o modificaciones para favorecer "
                    "la inclusión de sus compañeros en actividades lúdicas, aceptando al oponente como compañero de juego. "
                    "Adapta la estrategia de juego anticipando las intenciones de sus compañeros y oponentes para cumplir con los "
                    "objetivos planteados. Propone reglas y las modifica de acuerdo a las necesidades del contexto y los "
                    "intereses del grupo en la práctica de actividades físicas."
                ),
                "V_CICLO": (
                    "Interactúa a través de sus habilidades sociomotrices proactivamente con un sentido de cooperación "
                    "teniendo en cuenta las adaptaciones o modificaciones propuestas por el grupo en diferentes actividades físicas. "
                    "Hace uso de estrategias de cooperación y oposición seleccionando los diferentes elementos técnicos y tácticos "
                    "que se pueden dar en la práctica de actividades lúdicas y predeportivas, para resolver la situación de juego "
                    "que le dé un mejor resultado y que responda a las variaciones que se presentan en el entorno."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Asume roles y funciones de manera individual y dentro de un grupo; interactúa de forma espontánea en actividades lúdicas y disfruta de la compañía de sus pares para sentirse parte del grupo.",
                    "Participa en juegos cooperativos y de oposición en parejas y pequeños grupos; acepta al oponente como compañero de juego y las formas diferentes de jugar.",
                    "Propone soluciones a situaciones motrices y lúdicas, y llega a acuerdos con sus pares a fin de cumplir con los objetivos que surjan; respeta las reglas de juego propuestas (por ellos mismos, por el maestro o por las condiciones del entorno) en diferentes actividades lúdicas."
                ],
                "2_GRADO": [
                    "Participa en juegos cooperativos y de oposición en parejas y pequeños grupos; acepta al oponente como compañero de juego y llega a consensos sobre la manera de jugar.",
                    "Muestra una actitud de respeto en la práctica de actividades lúdicas y evita juegos bruscos, amenazas o apodos; acepta la participación de todos sus compañeros.",
                    "Resuelve de manera compartida situaciones producidas en los diferentes tipos de juegos (tradicionales, autóctonos, etc.) y adecúa las reglas para la inclusión de sus pares y el entorno, con el fin de lograr un desarrollo eficaz de la actividad."
                ],
                "3_GRADO": [
                    "Propone cambios en las condiciones de juego, si fuera necesario, para posibilitar la inclusión de sus pares; así, promueve el respeto y la participación, y busca un sentido de pertenencia al grupo en la práctica de diferentes actividades físicas.",
                    "Participa en juegos cooperativos y de oposición en parejas, pequeños y grandes grupos; acepta al oponente como compañero de juego y arriba a consensos sobre la manera de jugar y los posibles cambios que puedan producirse.",
                    "Genera estrategias colectivas en las actividades lúdicas según el rol de sus compañeros y el suyo propio, a partir de los resultados en el juego."
                ],
                "4_GRADO": [
                    "Propone normas y reglas en las actividades lúdicas y las modifica de acuerdo a las necesidades, el contexto y los intereses, con adaptaciones o modificaciones propuestas por el grupo, para favorecer la inclusión; muestra una actitud responsable y de respeto por el cumplimiento de los acuerdos establecidos.",
                    "Propone actividades lúdicas, como juegos populares y/o tradicionales, con adaptaciones o modificaciones propuestas por el grupo; acepta al oponente como compañero de juego y llega a consensos sobre la manera de jugar y los posibles cambios que puedan producirse.",
                    "Propone reglas y las modifica de acuerdo a las necesidades; adapta la estrategia de juego cuando prevé las intenciones de sus compañeros de equipo y oponentes, para cumplir con los objetivos planteados."
                ],
                "5_GRADO": [
                    "Emplea la resolución reflexiva y el diálogo como herramientas para solucionar problemas o conflictos surgidos con sus pares durante la práctica de actividades lúdicas y predeportivas diversas.",
                    "Realiza actividades lúdicas en las que interactúa con sus compañeros y oponentes como compañeros de juego; respeta las diferencias personales y asume roles y cambio de roles.",
                    "Propone, junto con sus pares, soluciones estratégicas oportunas, y toma en cuenta los aportes y las características de cada integrante del grupo al practicar juegos tradicionales, populares, autóctonos, predeportivos y en la naturaleza."
                ],
                "6_GRADO": [
                    "Participa en actividades físicas en la naturaleza, eventos predeportivos, juegos populares, entre otros, y toma decisiones en favor del grupo aunque vaya en contra de sus intereses personales, con un sentido solidario y de cooperación.",
                    "Modifica juegos y actividades para que se adecúen a las necesidades y posibilidades del grupo y a la lógica del juego deportivo.",
                    "Participa en actividades lúdicas, predeportivas y deportivas en las que pone en práctica diversas estrategias; adecúa normas de juego y la mejor solución táctica para dar respuesta a las variaciones que se presentan en el entorno."
                ]
            }
        }
    },
    "Comunicación": {
        "Se comunica oralmente en su lengua materna": {
            "estandares": {
                "III_CICLO": (
                    "Se comunica oralmente mediante diversos tipos de textos; identifica información explícita, "
                    "infiere e interpreta hechos y temas. Desarrolla sus ideas manteniéndose, por lo general, en el tema; "
                    "utiliza algunos conectores, así como vocabulario de uso frecuente. Su pronunciación es entendible y se "
                    "apoya en recursos no verbales y paraverbales. Reflexiona sobre textos escuchados a partir de sus conocimientos "
                    "y experiencia. Se expresa adecuándose a su propósito comunicativo, interlocutores y contexto. En un "
                    "intercambio, participa y responde en forma pertinente a lo que le dicen."
                ),
                "IV_CICLO": (
                    "Se comunica oralmente mediante diversos tipos de textos; identifica información explícita; "
                    "infiere e interpreta hechos, tema y propósito. Organiza y desarrolla sus ideas en torno a un tema y las "
                    "relaciona mediante el uso de algunos conectores y referentes, así como de un vocabulario variado. Se apoya "
                    "en recursos no verbales y paraverbales para enfatizar lo que dice. Reflexiona sobre textos escuchados a "
                    "partir de sus conocimientos y experiencia. Se expresa adecuándose a situaciones comunicativas formales e "
                    "informales. En un intercambio, comienza a adaptar lo que dice a las necesidades y puntos de vista de quien "
                    "lo escucha, a través de comentarios y preguntas relevantes."
                ),
                "V_CICLO": (
                    "Se comunica oralmente mediante diversos tipos de textos; infiere el tema, propósito, hechos y "
                    "conclusiones a partir de información explícita, e interpreta la intención del interlocutor en discursos "
                    "que contienen ironías. Se expresa adecuándose a situaciones comunicativas formales e informales. Organiza y "
                    "desarrolla sus ideas en torno a un tema y las relaciona mediante el uso de conectores y algunos referentes, "
                    "así como de un vocabulario variado y pertinente. Usa recursos no verbales y paraverbales para enfatizar "
                    "lo que dice. Reflexiona y evalúa los textos escuchados a partir de sus conocimientos y el contexto sociocultural. "
                    "En un intercambio, hace preguntas y contribuciones relevantes que responden a las ideas y puntos de vista "
                    "de otros, enriqueciendo el tema tratado."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Recupera información explícita de los textos orales que escucha (nombres de personas y personajes, hechos y lugares) y que presentan vocabulario de uso frecuente.",
                    "Dice de qué trata el texto y cuál es su propósito comunicativo; para ello, se apoya en la información recurrente del texto y en su experiencia.",
                    "Deduce características implícitas de personas, personajes, animales, objetos y lugares, o el significado de palabras y expresiones según el contexto (adivinanzas), así como relaciones lógicas entre las ideas del texto, como causa-efecto, que se pueden establecer fácilmente a partir de información explícita del mismo.",
                    "Explica acciones concretas de personas y personajes relacionando algunos recursos verbales y no verbales, a partir de su experiencia.",
                    "Adecúa su texto oral a la situación comunicativa, a sus interlocutores y al propósito comunicativo, utilizando recursos no verbales (gestos y movimientos corporales) y recurriendo a su experiencia.",
                    "Expresa oralmente ideas y emociones en torno a un tema, aunque en ocasiones puede salirse de este o reiterar información innecesariamente. Establece relaciones lógicas entre las ideas (en especial, de adición y secuencia), a través de algunos conectores. Incorpora un vocabulario de uso frecuente.",
                    "Emplea recursos no verbales (gestos y movimientos corporales) como apoyo durante el mensaje oral y en función del propósito comunicativo, en situaciones de comunicación no formal.",
                    "Participa en diversos intercambios orales formulando preguntas sobre lo que le interesa saber, dando respuestas o haciendo comentarios relacionados con el tema. Recurre a normas y modos de cortesía según el contexto sociocultural.",
                    "Opina como hablante y oyente sobre personas, personajes y hechos de los textos orales que escucha; da razones a partir del contexto en el que se desenvuelve y de su experiencia."
                ],
                "2_GRADO": [
                    "Recupera información explícita de los textos orales que escucha (nombres de personas y personajes, acciones, hechos, lugares y fechas) y que presentan vocabulario de uso frecuente.",
                    "Dice de qué trata el texto y cuál es su propósito comunicativo; para ello, se apoya en la información recurrente del texto y en su experiencia.",
                    "Deduce características implícitas de personas, personajes, animales, objetos, hechos y lugares, o el significado de palabras y expresiones según el contexto, así como relaciones lógicas entre las ideas del texto, como causa-efecto y semejanza-diferencia, a partir de información explícita del mismo.",
                    "Explica acciones concretas de personas y personajes relacionando recursos verbales y no verbales, a partir de su experiencia.",
                    "Adecúa su texto oral a la situación comunicativa y a sus interlocutores considerando el propósito comunicativo, utilizando recursos no verbales (gestos y movimientos corporales) y recurriendo a su experiencia y tipo textual.",
                    "Expresa oralmente ideas y emociones en torno a un tema, aunque en ocasiones puede reiterar información innecesariamente. Establece relaciones lógicas entre ellas (en especial, de adición, secuencia y causa), a través de algunos conectores. Incorpora un vocabulario de uso frecuente.",
                    "Emplea recursos no verbales (gestos y movimientos corporales) y paraverbales (pronunciación entendible) para apoyar lo que dice en situaciones de comunicación no formal.",
                    "Participa en diversos intercambios orales formulando preguntas sobre lo que le interesa saber, dando respuestas y haciendo comentarios relacionados con el tema. Recurre a normas y modos de cortesía según el contexto sociocultural.",
                    "Opina como hablante y oyente sobre personas, personajes y hechos de los textos orales que escucha; da razones a partir del contexto en el que se desenvuelve y de su experiencia."
                ],
                "3_GRADO": [
                    "Recupera información explícita de los textos orales que escucha, seleccionando datos específicos (nombres de personas y personajes, acciones, hechos, lugares y fechas), y que presentan vocabulario de uso frecuente y sinónimos.",
                    "Explica el tema, el propósito comunicativo, las emociones y los estados de ánimo de las personas y los personajes, así como las enseñanzas que se desprenden del texto; para ello, recurre a la información relevante del mismo.",
                    "Deduce algunas relaciones lógicas entre las ideas del texto oral, como las secuencias temporales, causa-efecto o semejanza-diferencia, así como las características de personas, personajes, animales, objetos, hechos y lugares, el significado de palabras según el contexto y expresiones con sentido figurado (adivinanzas, refranes), a partir de la información explícita e implícita del texto.",
                    "Explica las acciones y motivaciones de personas y personajes, así como el uso de adjetivaciones y personificaciones; para ello, relaciona recursos verbales, no verbales y paraverbales, a partir del texto oral y de su experiencia.",
                    "Adecúa su texto oral a la situación comunicativa, de acuerdo al propósito comunicativo, así como a las características más comunes del género discursivo. Distingue el registro formal del informal recurriendo a su experiencia y a algunas fuentes de información complementaria.",
                    "Expresa oralmente ideas y emociones en torno a un tema, y evita reiterar información innecesariamente. Ordena dichas ideas y las desarrolla para ampliar la información. Establece relaciones lógicas entre las ideas (en especial, de adición, secuencia y causa-efecto), a través de algunos referentes y conectores. Incorpora un vocabulario que incluye sinónimos y algunos términos propios de los campos del saber.",
                    "Emplea gestos y movimientos corporales que enfatizan lo que dice. Mantiene contacto visual con sus interlocutores. Se apoya en el volumen de su voz para transmitir emociones, caracterizar personajes o dar claridad a lo que dice.",
                    "Participa en diversos intercambios orales alternando roles de hablante y oyente, formulando preguntas, explicando sus respuestas y haciendo comentarios relevantes al tema. Recurre a normas y modos de cortesía según el contexto sociocultural.",
                    "Opina como hablante y oyente sobre ideas, hechos y temas de los textos orales, del ámbito escolar, social o de medios de comunicación, a partir de su experiencia y del contexto en que se desenvuelve."
                ],
                "4_GRADO": [
                    "Recupera información explícita de los textos orales que escucha, seleccionando datos específicos, y que presentan expresiones con sentido figurado, vocabulario que incluye sinónimos y términos propios de los campos del saber.",
                    "Explica el tema, el propósito comunicativo, las emociones y los estados de ánimo de personas y personajes; para ello, distingue lo relevante de lo complementario.",
                    "Deduce algunas relaciones lógicas entre las ideas del texto oral, como las secuencias temporales, causa-efecto o semejanza-diferencia, así como las características de personas, personajes, animales, objetos, hechos y lugares, el significado de palabras según el contexto y expresiones con sentido figurado (dichos populares, refranes, moralejas), a partir de la información explícita e implícita del texto.",
                    "Explica las motivaciones y los sentimientos de personas y personajes, así como el uso de comparaciones y personificaciones; para ello, relaciona recursos verbales, no verbales y paraverbales, a partir del texto oral y de su experiencia.",
                    "Adecúa su texto oral a la situación comunicativa, de acuerdo al propósito comunicativo, así como a las características más comunes del género discursivo. Distingue el registro formal del informal recurriendo a su experiencia y a algunas fuentes de información complementaria.",
                    "Expresa oralmente ideas y emociones en torno a un tema, de forma coherente y cohesionada. Ordena dichas ideas y las desarrolla para ampliar la información sin reiteraciones innecesarias. Establece relaciones lógicas entre las ideas (en especial, de causa-efecto y consecuencia), a través de algunos referentes y conectores. Incorpora un vocabulario que incluye sinónimos y algunos términos propios de los campos del saber.",
                    "Emplea gestos y movimientos corporales que enfatizan lo que dice. Mantiene contacto visual con sus interlocutores. Se apoya en el volumen y la entonación de su voz para transmitir emociones, caracterizar personajes o dar claridad a lo que dice.",
                    "Participa en diversos intercambios orales alternando roles de hablante y oyente, formulando preguntas, explicando sus respuestas y haciendo comentarios relevantes al tema. Recurre a normas y modos de cortesía según el contexto sociocultural.",
                    "Opina como hablante y oyente sobre ideas, hechos y temas de los textos orales, del ámbito escolar, social o de medios de comunicación, a partir de su experiencia y del contexto en que se desenvuelve."
                ],
                "5_GRADO": [
                    "Recupera información explícita de textos orales que escucha seleccionando datos específicos. Integra esta información cuando es dicha en distintos momentos en textos que incluyen expresiones con sentido figurado, y vocabulario que incluye sinónimos y términos propios de los campos del saber.",
                    "Explica el tema y el propósito comunicativo del texto oral. Distingue lo relevante de lo complementario clasificando y sintetizando la información. Establece conclusiones sobre lo comprendido; para ello, vincula el texto con su experiencia y el contexto sociocultural en que se desenvuelve.",
                    "Deduce relaciones lógicas (causa-efecto, semejanza-diferencia, etc.) entre las ideas del texto oral, a partir de información explícita e implícita del mismo. Señala las características y cualidades implícitas de personas, personajes, animales, objetos, hechos y lugares, y determina el significado de palabras según el contexto y de expresiones con sentido figurado (refranes, moralejas) cuando hay algunas pistas en el texto.",
                    "Explica las intenciones de sus interlocutores considerando recursos verbales, no verbales y paraverbales. Asimismo, los puntos de vista y las motivaciones de personas y personajes, así como figuras retóricas (por ejemplo, la hipérbole) considerando algunas características del tipo textual y género discursivo.",
                    "Adecúa su texto oral a la situación comunicativa considerando el propósito comunicativo y algunas características del género discursivo. Elige el registro formal e informal de acuerdo con sus interlocutores y el contexto; para ello, recurre a su experiencia y a algunas fuentes de información complementaria.",
                    "Expresa oralmente ideas y emociones de forma coherente y cohesionada. Ordena y jerarquiza las ideas en torno a un tema y las desarrolla para ampliar la información o mantener el hilo temático. Establece relaciones lógicas entre ellas (en especial, de causa-efecto, consecuencia y contraste), a través de algunos referentes y conectores. Incorpora un vocabulario que incluye sinónimos y algunos términos propios de los campos del saber.",
                    "Emplea gestos y movimientos corporales que enfatizan lo que dice. Mantiene la distancia física con sus interlocutores, así como el volumen, la entonación y el ritmo de su voz para transmitir emociones, caracterizar personajes o producir efectos en el público, como el suspenso y el entretenimiento.",
                    "Participa en diversos intercambios orales alternando los roles de hablante y oyente. Recurre a sus saberes previos y aporta nueva información para argumentar, explicar y complementar las ideas expuestas. Considera normas y modos de cortesía según el contexto sociocultural.",
                    "Opina como hablante y oyente sobre ideas, hechos y temas, de textos orales del ámbito escolar, social o de medios de comunicación. Justifica su posición sobre lo que dice el texto oral considerando su experiencia y el contexto en que se desenvuelve.",
                    "Evalúa la adecuación de textos orales a la situación comunicativa, así como la coherencia de ideas y la cohesión entre ellas; también, la utilidad de recursos verbales, no verbales y paraverbales de acuerdo al propósito comunicativo."
                ],
                "6_GRADO": [
                    "Recupera información explícita de textos orales que escucha seleccionando datos específicos. Integra esta información cuando es dicha en distintos momentos y por distintos interlocutores en textos que incluyen expresiones con sentido figurado, y vocabulario que incluye sinónimos y términos propios de los campos del saber.",
                    "Explica el tema y el propósito comunicativo del texto oral. Distingue lo relevante de lo complementario clasificando y sintetizando la información. Establece conclusiones sobre lo comprendido; para ello, vincula el texto con su experiencia y los contextos socioculturales en que se desenvuelve.",
                    "Deduce relaciones lógicas (causa-efecto, semejanza-diferencia, etc.) entre las ideas del texto oral, a partir de información explícita e implícita del mismo. Señala las características y cualidades implícitas de personas, personajes, animales, objetos, hechos y lugares, y determina el significado de palabras según el contexto y de expresiones con sentido figurado (expresiones irónicas) cuando hay algunas pistas en el texto.",
                    "Explica la intención de sus interlocutores considerando recursos verbales, no verbales y paraverbales. Asimismo, los puntos de vista y las motivaciones de personas y personajes, así como algunas figuras retóricas (por ejemplo, la hipérbole) considerando algunas características del tipo textual y género discursivo.",
                    "Adecúa su texto oral a la situación comunicativa considerando el propósito comunicativo y algunas características del género discursivo, manteniendo el registro formal e informal y adaptándose a sus interlocutores y al contexto; para ello, recurre a su experiencia y a algunas fuentes de información complementaria.",
                    "Expresa oralmente ideas y emociones de forma coherente y cohesionada. Ordena y jerarquiza las ideas en torno a un tema y las desarrolla para ampliar la información o mantener el hilo temático. Establece relaciones lógicas entre ellas (en especial, de causa-efecto, consecuencia y contraste), a través de algunos referentes y conectores. Incorpora un vocabulario que incluye sinónimos y algunos términos propios de los campos del saber.",
                    "Emplea gestos y movimientos corporales que enfatizan lo que dice. Mantiene la distancia física con sus interlocutores, así como el volumen, la entonación y el ritmo de su voz para transmitir emociones, caracterizar personajes o producir efectos en el público, como el suspenso y el entretenimiento.",
                    "Participa en diversos intercambios orales alternando los roles de hablante y oyente. Recurre a sus saberes previos, usa lo dicho por sus interlocutores y aporta nueva información relevante para argumentar, explicar y complementar ideas. Considera normas y modos de cortesía según el contexto sociocultural.",
                    "Opina como hablante y oyente sobre ideas, hechos y temas, de textos orales del ámbito escolar, social o de medios de comunicación. Justifica su posición sobre lo que dice el texto oral considerando su experiencia y los contextos socioculturales en que se desenvuelve.",
                    "Evalúa la adecuación de textos orales a la situación comunicativa, así como la coherencia de ideas y la cohesión entre ellas; también, la utilidad de recursos verbales, no verbales y paraverbales de acuerdo al propósito comunicativo."
                ]
            }
        },
        "Lee diversos tipos de textos escritos en su lengua materna": {
            "estandares": {
                "III_CICLO": (
                    "Lee diversos tipos de textos de estructura simple en los que predominan palabras conocidas "
                    "e ilustraciones que apoyan las ideas centrales. Obtiene información poco evidente distinguiéndola "
                    "de otra semejante y realiza inferencias locales a partir de información explícita. Interpreta el texto "
                    "considerando información recurrente para construir su sentido global. Opina sobre sucesos e ideas "
                    "importantes del texto a partir de su propia experiencia."
                ),
                "IV_CICLO": (
                    "Lee diversos tipos de textos que presentan estructura simple con algunos elementos complejos y con "
                    "vocabulario variado. Obtiene información poco evidente distinguiéndola de otras próximas y semejantes. "
                    "Realiza inferencias locales a partir de información explícita e implícita. Interpreta el texto "
                    "considerando información relevante para construir su sentido global. Reflexiona sobre sucesos e ideas "
                    "importantes del texto y explica la intención de los recursos textuales más comunes a partir de su "
                    "conocimiento y experiencia."
                ),
                "V_CICLO": (
                    "Lee diversos tipos de textos con varios elementos complejos en su estructura y con vocabulario "
                    "variado. Obtiene información e integra datos que están en distintas partes del texto. Realiza "
                    "inferencias locales a partir de información explícita e implícita. Interpreta el texto considerando "
                    "información relevante y complementaria para construir su sentido global. Reflexiona sobre aspectos "
                    "variados del texto a partir de su conocimiento y experiencia. Evalúa el uso del lenguaje, la intención "
                    "de los recursos textuales y el efecto del texto en el lector a partir de su conocimiento y del contexto sociocultural."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Identifica información explícita que es claramente distinguible de otra porque la relaciona con palabras conocidas o porque conoce el contenido del texto (por ejemplo, en una lista de cuentos con títulos que comienzan de diferente manera, el niño puede reconocer dónde dice 'Caperucita' porque comienza como el nombre de un compañero o lo ha leído en otros textos) y que se encuentra en lugares evidentes como el título, subtítulo, inicio, final, etc., en textos con ilustraciones. Establece la secuencia de los textos que lee (instrucciones, historias, noticias).",
                    "Deduce características de personajes, animales, objetos y lugares, así como relaciones lógicas de causa-efecto que se pueden establecer fácilmente a partir de información explícita del texto.",
                    "Predice de qué tratará el texto y cuál es su propósito comunicativo, a partir de algunos indicios, como título, ilustraciones, palabras conocidas o expresiones que se encuentran en los textos que le leen, que lee con ayuda o que lee por sí mismo.",
                    "Explica la relación del texto con la ilustración en textos que lee por sí mismo, que lee con ayuda del docente o que escucha leer.",
                    "Opina acerca de personas, personajes y hechos expresando sus preferencias. Elige o recomienda textos a partir de su experiencia, necesidades e intereses, con el fin de reflexionar sobre los textos que lee o escucha leer."
                ],
                "2_GRADO": [
                    "Identifica información explícita que se encuentra en distintas partes del texto. Distingue esta información de otra semejante (por ejemplo, distingue entre las características de dos personajes, elige entre dos datos de un animal, etc.) en diversos tipos de textos de estructura simple, con palabras conocidas e ilustraciones. Establece la secuencia de los textos que lee (instrucciones, historias, noticias).",
                    "Deduce características implícitas de personajes, animales, objetos y lugares; determina el significado de palabras según el contexto y hace comparaciones; asimismo, establece relaciones lógicas de causa-efecto, semejanza-diferencia y enseñanza y propósito, a partir de información explícita del texto.",
                    "Predice de qué tratará el texto y cuál es su propósito comunicativo, a partir de algunos indicios, como título, ilustraciones, silueta, formato, palabras, frases y expresiones que se encuentran en los textos que le leen o que lee por sí mismo.",
                    "Explica el tema y el propósito de los textos que lee por sí mismo, así como las relaciones texto-ilustración.",
                    "Opina acerca de personas, personajes y hechos expresando sus preferencias. Elige o recomienda textos a partir de su experiencia, necesidades e intereses, con el fin de reflexionar sobre los textos que lee."
                ],
                "3_GRADO": [
                    "Identifica información explícita que se encuentra en distintas partes del texto. Distingue información de otra próxima y semejante, en la que selecciona datos específicos (por ejemplo, el lugar de un hecho en una noticia), en diversos tipos de textos de estructura simple, con algunos elementos complejos (por ejemplo, sin referentes próximos, guiones de diálogo, ilustraciones), con palabras conocidas y, en ocasiones, con vocabulario variado, de acuerdo a las temáticas abordadas.",
                    "Deduce características implícitas de personajes, animales, objetos y lugares, y determina el significado de palabras según el contexto y hace comparaciones; así como el tema y destinatario. Establece relaciones lógicas de causa-efecto, semejanza-diferencia y enseñanza y propósito, a partir de la información explícita e implícita relevante del texto.",
                    "Predice de qué tratará el texto, a partir de algunos indicios como silueta del texto, palabras, frases, colores y dimensiones de las imágenes; asimismo, contrasta la información del texto que lee.",
                    "Explica el tema, el propósito, la enseñanza, las relaciones texto-ilustración, así como adjetivaciones y las motivaciones de personas y personajes.",
                    "Opina acerca del contenido del texto, explica el sentido de algunos recursos textuales (ilustraciones, tamaño de letra, etc.) y justifica sus preferencias cuando elige o recomienda textos a partir de su experiencia, necesidades e intereses, con el fin de reflexionar sobre los textos que lee."
                ],
                "4_GRADO": [
                    "Identifica información explícita y relevante que se encuentra en distintas partes del texto. Distingue esta información de otra semejante, en la que selecciona datos específicos, en diversos tipos de textos de estructura simple, con algunos elementos complejos, así como vocabulario variado, de acuerdo a las temáticas abordadas.",
                    "Deduce características implícitas de personajes, animales, objetos y lugares, y determina el significado de palabras y frases según el contexto, así como de expresiones con sentido figurado (refranes, comparaciones, etc.). Establece relaciones lógicas de intención-finalidad y tema y subtema, a partir de información relevante explícita e implícita.",
                    "Predice de qué tratará el texto, a partir de algunos indicios como subtítulos, colores y dimensiones de las imágenes, índice, tipografía, negritas, subrayado, etc.; asimismo, contrasta la información del texto que lee.",
                    "Explica el tema, el propósito, las motivaciones de personas y personajes, las comparaciones y personificaciones, así como las enseñanzas y los valores del texto, clasificando y sintetizando la información.",
                    "Opina acerca del contenido del texto, explica el sentido de algunos recursos textuales (uso de negritas, mayúsculas, índice, tipografía, subrayado, etc.), a partir de su experiencia y contexto, y justifica sus preferencias cuando elige o recomienda textos según sus necesidades, intereses y su relación con otros textos, con el fin de reflexionar sobre los textos que lee."
                ],
                "5_GRADO": [
                    "Identifica información explícita, relevante y complementaria que se encuentra en distintas partes del texto. Selecciona datos específicos e integra información explícita cuando se encuentra en distintas partes del texto con varios elementos complejos en su estructura, así como con vocabulario variado, de acuerdo a las temáticas abordadas.",
                    "Deduce características implícitas de personajes, seres, objetos, hechos y lugares, y determina el significado de palabras, según el contexto, y de expresiones con sentido figurado. Establece relaciones lógicas entre las ideas del texto escrito, como intención-finalidad, tema y subtemas, causa-efecto, semejanza-diferencia y enseñanza y propósito, a partir de información relevante explícita e implícita.",
                    "Predice de qué tratará el texto, a partir de algunos indicios como subtítulos, colores y dimensiones de las imágenes, índice, tipografía, negritas, subrayado, fotografías, reseñas, etc.; asimismo, contrasta la información del texto que lee.",
                    "Explica el tema, el propósito, los puntos de vista y las motivaciones de personas y personajes, las comparaciones e hipérboles, el problema central, las enseñanzas y los valores del texto, clasificando y sintetizando la información, para interpretar el sentido global del texto.",
                    "Opina sobre el contenido del texto, la organización textual, la intención de algunos recursos textuales (negritas, esquemas) y el efecto del texto en los lectores, a partir de su experiencia y del contexto sociocultural en que se desenvuelve.",
                    "Justifica la elección o recomendación de textos de su preferencia, de acuerdo a sus necesidades, intereses y la relación con otros textos leídos; sustenta su posición sobre los textos cuando los comparte con otros; y compara textos entre sí para indicar algunas similitudes y diferencias entre tipos textuales."
                ],
                "6_GRADO": [
                    "Identifica información explícita, relevante y complementaria que se encuentra en distintas partes del texto. Selecciona datos específicos e integra información explícita cuando se encuentra en distintas partes del texto, o al realizar una lectura intertextual de diversos tipos de textos con varios elementos complejos en su estructura, así como con vocabulario variado, de acuerdo a las temáticas abordadas.",
                    "Deduce características implícitas de seres, objetos, hechos y lugares, y determina el significado de palabras, según el contexto, y de expresiones con sentido figurado. Establece relaciones lógicas entre las ideas del texto escrito, como intención-finalidad, tema y subtemas, causa-efecto, semejanza-diferencia y enseñanza y propósito, a partir de información relevante y complementaria, y al realizar una lectura intertextual.",
                    "Predice de qué tratará el texto, a partir de algunos indicios como subtítulos, colores y dimensiones de las imágenes, índice, tipografía, negritas, subrayado, fotografías, reseñas (solapa, contratapa), notas del autor, biografía del autor o ilustrador, etc.; asimismo, contrasta la información del texto que lee.",
                    "Explica el tema, el propósito, los puntos de vista y las motivaciones de personas y personajes, las comparaciones e hipérboles, el problema central, las enseñanzas, los valores y la intención del autor, clasificando y sintetizando la información, y elabora conclusiones sobre el texto para interpretar su sentido global.",
                    "Opina sobre el contenido y la organización del texto, la intención de diversos recursos textuales, la intención del autor y el efecto que produce en los lectores, a partir de su experiencia y de los contextos socioculturales en que se desenvuelve.",
                    "Justifica la elección o recomendación de textos de su preferencia, de acuerdo a sus necesidades, intereses y la relación con otros textos leídos; sustenta su posición sobre los valores presentes en los textos, cuando los comparte con otros; y compara textos entre sí para indicar algunas similitudes y diferencias entre tipos textuales y géneros discursivos (por ejemplo: diferencias y semejanzas entre cuento y fábula)."
                ]
            }
        },
        "Escribe diversos tipos de textos en su lengua materna": {
            "estandares": {
                "III_CICLO": (
                    "Escribe diversos tipos de textos de forma reflexiva. Adecúa al propósito y el destinatario "
                    "a partir de su experiencia previa. Organiza y desarrolla lógicamente las ideas en torno a un tema. "
                    "Establece relaciones entre ideas a través del uso adecuado de algunos tipos de conectores y emplea "
                    "vocabulario de uso frecuente. Separa adecuadamente las palabras y utiliza algunos recursos ortográficos "
                    "básicos para darle claridad y sentido a su texto. Reflexiona sobre las ideas más importantes en el texto "
                    "que escribe y explica acerca del uso de algunos recursos ortográficos según la situación comunicativa."
                ),
                "IV_CICLO": (
                    "Escribe diversos tipos de textos de forma reflexiva. Adecúa su texto al destinatario, propósito "
                    "y el registro a partir de su experiencia previa y de alguna fuente de información. Organiza y "
                    "desarrolla lógicamente las ideas en torno a un tema. Establece relaciones entre ideas a través del uso "
                    "adecuado de algunos tipos de conectores y de referentes; emplea vocabulario variado. Utiliza recursos "
                    "ortográficos básicos para darle claridad y sentido a su texto. Reflexiona sobre la coherencia y cohesión "
                    "de las ideas en el texto que escribe, y explica acerca del uso de algunos recursos textuales para "
                    "reforzar sentidos y producir efectos en el lector según la situación comunicativa."
                ),
                "V_CICLO": (
                    "Escribe diversos tipos de textos de forma reflexiva. Adecúa su texto al destinatario, propósito "
                    "y el registro, a partir de su experiencia previa y de algunas fuentes de información complementarias. "
                    "Organiza y desarrolla lógicamente las ideas en torno a un tema y las estructura en párrafos. Establece "
                    "relaciones entre ideas a través del uso adecuado de algunos tipos de conectores y de referentes; emplea "
                    "vocabulario variado. Utiliza recursos ortográficos para separar expresiones, ideas y párrafos con la "
                    "intención de darle claridad y sentido a su texto. Reflexiona y evalúa de manera permanente la coherencia "
                    "y cohesión de las ideas en el texto que escribe, así como el uso del lenguaje para argumentar o reforzar "
                    "sentidos y producir efectos en el lector según la situación comunicativa."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Adecúa el texto a la situación comunicativa considerando el propósito comunicativo y el destinatario, recurriendo a su experiencia para escribir.",
                    "Escribe en nivel alfabético en torno a un tema, aunque en ocasiones puede salirse de este o reiterar información innecesariamente. Establece relaciones entre las ideas, sobre todo de adición, utilizando algunos conectores. Incorpora vocabulario de uso frecuente.",
                    "Revisa el texto con ayuda del docente, para determinar si se ajusta al propósito y destinatario, o si se mantiene o no dentro del tema, con el fin de mejorarlo."
                ],
                "2_GRADO": [
                    "Adecúa el texto a la situación comunicativa considerando el propósito comunicativo y el destinatario. Recurre a su experiencia previa para escribir.",
                    "Escribe textos en torno a un tema. Agrupa las ideas en oraciones y las desarrolla para ampliar la información, aunque en ocasiones puede reiterar información innecesariamente. Establece relaciones entre las ideas, como adición y secuencia, utilizando algunos conectores. Incorpora vocabulario de uso frecuente.",
                    "Utiliza recursos gramaticales y ortográficos (por ejemplo, las mayúsculas y el punto final) que contribuyen a dar sentido a su texto. Emplea fórmulas retóricas para marcar el inicio y el final en las narraciones que escribe; asimismo, elabora rimas y juegos verbales.",
                    "Revisa el texto con ayuda del docente, para determinar si se ajusta al propósito y destinatario, si existen contradicciones que afectan la coherencia entre las ideas, o si el uso de conectores asegura la cohesión entre ellas. También, revisa el uso de los recursos ortográficos empleados en su texto y verifica si falta alguno (como las mayúsculas), con el fin de mejorarlo."
                ],
                "3_GRADO": [
                    "Adecúa el texto a la situación comunicativa considerando el propósito comunicativo, el destinatario y las características más comunes del tipo textual. Distingue el registro formal del informal; para ello, recurre a su experiencia y a algunas fuentes de información complementaria.",
                    "Escribe textos de forma coherente y cohesionada. Ordena las ideas en torno a un tema y las desarrolla para ampliar la información, sin contradicciones, reiteraciones innecesarias o digresiones. Establece relaciones entre las ideas, como causa-efecto y secuencia, a través de algunos referentes y conectores. Incorpora un vocabulario que incluye sinónimos y algunos términos propios de los campos del saber.",
                    "Utiliza recursos gramaticales y ortográficos (por ejemplo, el punto seguido y los signos de admiración e interrogación) que contribuyen a dar sentido a su texto. Emplea algunas figuras retóricas (por ejemplo, las adjetivaciones) para caracterizar personas, personajes y escenarios, y elabora rimas y juegos verbales apelando al ritmo y la musicalidad de las palabras, con el fin de expresar sus experiencias y emociones.",
                    "Revisa el texto para determinar si se ajusta a la situación comunicativa, si existen contradicciones o reiteraciones innecesarias que afectan la coherencia entre las ideas, o si el uso de conectores y referentes asegura la cohesión entre ellas. También, revisa el uso de los recursos ortográficos empleados en su texto y verifica si falta alguno (como los signos de interrogación), con el fin de mejorarlo.",
                    "Explica el efecto de su texto en los lectores, luego de compartirlo con otros. También, revisa el uso de los recursos ortográficos empleados en su texto y algunos aspectos gramaticales."
                ],
                "4_GRADO": [
                    "Adecúa el texto a la situación comunicativa considerando el propósito comunicativo, el destinatario y las características más comunes del tipo textual. Distingue el registro formal del informal; para ello, recurre a su experiencia y a algunas fuentes de información complementaria.",
                    "Escribe textos de forma coherente y cohesionada. Ordena las ideas en torno a un tema y las desarrolla para ampliar la información, sin contradicciones, reiteraciones innecesarias o digresiones. Establece relaciones entre las ideas, como adición, causa-efecto y consecuencia, a través de algunos referentes y conectores. Incorpora un vocabulario que incluye sinónimos y algunos términos propios de los campos del saber.",
                    "Utiliza recursos gramaticales y ortográficos (por ejemplo, el punto seguido y las comas enumerativas) que contribuyen a dar sentido a su texto, e incorpora algunos recursos textuales (por ejemplo, el tamaño de la letra) para reforzar dicho sentido. Emplea comparaciones y adjetivaciones para caracterizar personas, personajes y escenarios, y elabora rimas y juegos verbales apelando al ritmo y la musicalidad de las palabras, con el fin de expresar sus experiencias y emociones.",
                    "Revisa el texto para determinar si se ajusta a la situación comunicativa, si existen contradicciones o reiteraciones innecesarias que afectan la coherencia entre las ideas, o si el uso de conectores y referentes asegura la cohesión entre ellas. También, revisa el uso de los recursos ortográficos que empleó en su texto y verifica si falta alguno (como el punto aparte), con el fin de mejorarlo.",
                    "Explica el efecto de su texto en los lectores considerando su propósito al momento de escribirlo. Asimismo, explica la importancia de los aspectos gramaticales y ortográficos más comunes."
                ],
                "5_GRADO": [
                    "Adecúa el texto a la situación comunicativa considerando el propósito comunicativo, el tipo textual, así como el formato y el soporte. Mantiene el registro formal e informal; para ello, se adapta a los destinatarios y selecciona algunas fuentes de información complementaria.",
                    "Escribe textos de forma coherente y cohesionada. Ordena las ideas en torno a un tema, las jerarquiza en subtemas de acuerdo a párrafos, y las desarrolla para ampliar la información, sin digresiones o vacíos. Establece relaciones entre las ideas, como causa-efecto, consecuencia y contraste, a través de algunos referentes y conectores. Incorpora de forma pertinente vocabulario que incluye sinónimos y algunos términos propios de los campos del saber.",
                    "Utiliza recursos gramaticales y ortográficos (por ejemplo, el punto aparte para separar párrafos) que contribuyen a dar sentido a su texto, e incorpora algunos recursos textuales (como uso de negritas o comillas) para reforzar dicho sentido. Emplea algunas figuras retóricas, (personificaciones y adjetivaciones) para caracterizar personas, personajes y escenarios, o para elaborar patrones rítmicos o versos libres, con el fin de expresar sus experiencias y emociones.",
                    "Evalúa de manera permanente el texto, para determinar si se ajusta a la situación comunicativa, si existen reiteraciones innecesarias o digresiones que afectan la coherencia entre las ideas, o si el uso de conectores y referentes asegura la cohesión entre ellas. También, evalúa la utilidad de los recursos ortográficos empleados y la pertinencia del vocabulario, para mejorar el texto y garantizar su sentido.",
                    "Evalúa el efecto de su texto en los lectores, a partir de los recursos textuales y estilísticos utilizados, y considerando su propósito al momento de escribirlo. Compara y contrasta los aspectos gramaticales y ortográficos más comunes cuando evalúa el texto."
                ],
                "6_GRADO": [
                    "Adecúa el texto a la situación comunicativa considerando el propósito comunicativo, el tipo textual y algunas características del género discursivo, así como el formato y el soporte. Mantiene el registro formal e informal; para ello, se adapta a los destinatarios y selecciona algunas fuentes de información complementaria.",
                    "Escribe textos de forma coherente y cohesionada. Ordena las ideas en torno a un tema, las jerarquiza en subtemas e ideas principales de acuerdo a párrafos, y las desarrolla para ampliar la información, sin digresiones o vacíos. Establece relaciones entre las ideas, como causa-efecto, consecuencia y contraste, a través de algunos referentes y conectores. Incorpora de forma pertinente vocabulario que incluye sinónimos y diversos términos propios de los campos del saber.",
                    "Utiliza recursos gramaticales y ortográficos (por ejemplo, el punto aparte para separar párrafos) que contribuyen a dar sentido a su texto, e incorpora algunos recursos textuales (como uso de negritas o comillas) para reforzar dicho sentido. Emplea algunas figuras retóricas (personificaciones e hipérboles) para caracterizar personas, personajes y escenarios, o para elaborar patrones rítmicos y versos libres, con el fin de producir efectos en el lector (el entretenimiento o el suspenso, por ejemplo).",
                    "Evalúa de manera permanente el texto, para determinar si se ajusta a la situación comunicativa, si existen digresiones o vacíos de información que afectan la coherencia entre las ideas, o si el uso de conectores y referentes asegura la cohesión entre ellas. También, evalúa la utilidad de los recursos ortográficos empleados y la pertinencia del vocabulario, para mejorar el texto y garantizar su sentido.",
                    "Evalúa el efecto de su texto en los lectores, a partir de los recursos textuales y estilísticos utilizados, y considerando su propósito al momento de escribirlo. Compara y contrasta los aspectos gramaticales y ortográficos más comunes, así como las características de tipos textuales, cuando evalúa el texto."
                ]
            }
        }
    },
    "Arte y Cultura": {
        "Aprecia de manera crítica manifestaciones artístico-culturales": {
            "estandares": {
                "III_CICLO": (
                    "Aprecia de manera crítica manifestaciones artístico-culturales al observar, escuchar y describir "
                    "las características visuales, táctiles, sonoras y kinestésicas de estas manifestaciones, describiendo "
                    "las sensaciones que le transmiten. Participa de conversaciones sobre los contextos donde se originan "
                    "manifestaciones artístico-culturales y reconoce que responden a características propias de un grupo "
                    "de personas, de tiempos y lugares diferentes. Expresa sus preferencias sobre manifestaciones artísticas "
                    "que observa o experimenta y conversa sobre los temas, las ideas y sentimientos que comunican."
                ),
                "IV_CICLO": (
                    "Aprecia de manera crítica manifestaciones artístico-culturales al observar, escuchar y describir "
                    "las características claves de una manifestación artístico-cultural, su forma, los medios que utiliza, "
                    "su temática; describe las ideas o sentimientos que comunica. Investiga los contextos donde se origina "
                    "e infiere información acerca del lugar, la época y la cultura donde fue creada. Integra la información "
                    "recogida y describe de qué manera una manifestación artístico-cultural comunica ideas, sentimientos e intenciones."
                ),
                "V_CICLO": (
                    "Aprecia de manera crítica manifestaciones artístico-culturales al interpretar las cualidades expresivas "
                    "de los elementos del arte, la estructura y los medios utilizados en una manifestación artístico-cultural "
                    "y explica cómo transmite mensajes, ideas y sentimientos. Investiga los contextos donde se originan "
                    "manifestaciones artístico-culturales tradicionales y contemporáneas e identifica cómo los cambios, las "
                    "tradiciones, las creencias y valores revelan la manera en que una determinada persona o sociedad ha vivido. "
                    "Genera hipótesis sobre el significado y las diversas intenciones que puede tener una manifestación creada "
                    "en contextos históricos y culturales diferentes."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Usa los sentidos para identificar, con la ayuda del docente, los elementos visuales, táctiles, sonoros y kinestésicos que hay en la naturaleza, el entorno y diversas manifestaciones artísticas de su contexto local.",
                    "Menciona y describe las experiencias que tiene con manifestaciones artísticas en su entorno familiar y en su comunidad. Ejemplo: El estudiante conversa sobre situaciones, eventos u ocasiones donde ha tenido oportunidad de vivir o experimentar la música (cuando su mamá le canta o cuando oye música para bailar en su casa, en fiestas o en celebraciones de su barrio).",
                    "Explica sus ideas y expresa sus emociones y sentimientos cuando entra en contacto con la naturaleza o manifestaciones artístico-culturales de su entorno."
                ],
                "2_GRADO": [
                    "Describe o registra líneas, formas, sonidos y movimientos que encuentra en la naturaleza, el entorno y en diversas manifestaciones artísticas, y los asocia con ideas y sentimientos. Ejemplo: El estudiante describe y compara diversos sonidos que escucha en el entorno (las bocinas de los carros, el silbido de un pájaro, el sonido de las hojas de los árboles) y explica cómo lo hacen sentir.",
                    "Mantiene conversaciones y hace registros sobre los contextos históricos y culturales de manifestaciones artístico-culturales con las que interactúa. Ejemplo: El estudiante conversa sobre las similitudes y diferencias entre las danzas peruanas que ha observado. Registra de manera visual y escrita cómo se lleva a cabo cada danza, la forma en que vesten los danzantes y con qué música o sonidos se acompañan.",
                    "Explica sus ideas y expresa los sentimientos que le generan las manifestaciones artístico-culturales, con base en sus observaciones y experiencias. Ejemplo: El estudiante comparte con sus compañeros lo que siente y piensa sobre los personajes de una obra de teatro, y lo asocia con el tema de la historia."
                ],
                "3_GRADO": [
                    "Identifica y describe los elementos básicos del arte que encuentra en su entorno y en manifestaciones artístico-culturales diversas. Reconoce que los elementos pueden transmitir múltiples sensaciones.",
                    "Especula sobre los procesos que el artista ha seguido para crear su obra e identifica los distintos usos y propósitos de manifestaciones artístico-culturales de su comunidad (ritual, recreativo, comercial, decorativo, utilitario, etc.).",
                    "Comenta sobre los posibles significados de una obra de arte, con base en lo observado y lo investigado acerca del autor, y emite una opinión personal sobre ella."
                ],
                "4_GRADO": [
                    "Describe y analiza los elementos del arte que identifica en el entorno y en manifestaciones artístico-culturales, e identifica los medios utilizados. Relaciona elementos con ideas, mensajes y sentimientos. Ejemplo: El estudiante describe qué instrumentos se usan en la música tradicional peruana que está escuchando, cómo es el sonido del tambor, el ritmo constante, qué sonidos le llaman la atención, qué le hace sentir, qué le hace pensar, entre otros.",
                    "Investiga el significado de los símbolos y características principales de manifestaciones artístico-culturales de diferentes lugares y tiempos, y comprende que cumplen diversos propósitos y comunican ideas sobre la cultura en la que fueron creados. Ejemplo: El estudiante investiga las formas y los propósitos de la cerámica Moche y cómo los motivos y diseños usados representan el carácter de los personajes o las figuras que allí aparecen.",
                    "Comenta sobre la manera en que los elementos, los procesos, los medios y las técnicas usadas comunican ideas, y genera hipótesis sobre el significado y la intención del artista."
                ],
                "5_GRADO": [
                    "Describe las características de manifestaciones artístico-culturales que observa, analiza sus elementos e interpreta las ideas y sentimientos que transmiten.",
                    "Identifica y describe los contextos de diversas manifestaciones artístico-culturales e identifica cómo el arte cumple diversas funciones (socializar, entretener, contar historias, celebrar) y ayuda a conocer las creencias, los valores o las actitudes de un artista o una sociedad. Ejemplo: El estudiante explica qué representa la danza Chuño Saruy para las comunidades que la realizan, por qué la hacen, de qué lugar es, entre otros.",
                    "Genera hipótesis sobre el significado y la intención de una manifestación artístico-cultural e incorpora la opinión de los demás para reformular sus puntos de vista sobre ella."
                ],
                "6_GRADO": [
                    "Describe y analiza las cualidades de los elementos visuales, táctiles, sonoros y kinestésicos que percibe en manifestaciones artístico-culturales, y establece relaciones entre sus hallazgos y las ideas y emociones que ellas le generan.",
                    "Investiga en diversas fuentes acerca del origen y las formas en que manifestaciones artístico-culturales tradicionales y contemporáneas transmiten las características de una sociedad.",
                    "Desarrolla y aplica criterios relevantes para evaluar una manifestación artística, con base en la información que maneja sobre su forma y contexto de creación, y ensaya una postura personal frente a ella. Ejemplo: El estudiante explica qué es un retablo y lo relaciona con eventos históricos sobre los que ha estudiado y explica qué partes del retablo son más efectivas en transmitir sus ideas. Explica cómo ha cambiado su reacción inicial frente al retablo, después de haberlo observado con detenimiento e indagado sobre el contexto en que fue creado."
                ]
            }
        },
        "Crea proyectos desde los lenguajes artísticos": {
            "estandares": {
                "III_CICLO": (
                    "Crea proyectos artísticos que demuestran habilidades artísticas iniciales para comunicar ideas, "
                    "sentimientos, observaciones y experiencias. Experimenta, selecciona y explora libremente las posibilidades "
                    "expresivas de los elementos, medios, materiales y técnicas de los diversos lenguajes del arte. "
                    "Explora ideas que surgen de su imaginación, sus experiencias o de sus observaciones y las concretiza "
                    "en trabajos de artes visuales, música, teatro o danza. Comparte sus experiencias y creaciones con sus "
                    "compañeros y su familia. Describe y dialoga sobre las características de sus propios trabajos y los "
                    "de sus compañeros y responde a preguntas sobre ellos."
                ),
                "IV_CICLO": (
                    "Crea proyectos artísticos en una variedad de lenguajes que comunican experiencias, ideas, sentimientos "
                    "y observaciones. Explora, selecciona y combina los elementos del arte y utiliza medios, materiales, "
                    "herramientas y técnicas de los diversos lenguajes del arte para expresar de diferentes maneras sus ideas "
                    "y resolver problemas creativos. Demuestra habilidad para planificar trabajos usando sus conocimientos del arte "
                    "y adecúa sus procesos para ajustarse a diferentes intenciones, que se basan en observaciones o problemas del "
                    "entorno natural, artístico y cultural. Comunica sus hallazgos, identificando elementos o técnicas o procesos "
                    "que ha usado para enriquecer sus creaciones y mejora sus trabajos a partir de retroalimentaciones. Planifica "
                    "cómo y qué necesita para compartir sus experiencias y descubrimientos hacia la comunidad educativa."
                ),
                "V_CICLO": (
                    "Crea proyectos artísticos individuales o colaborativos explorando formas alternativas de combinar "
                    "y usar elementos, medios, materiales y técnicas artísticas y tecnologías para la resolución de problemas "
                    "creativos. Genera ideas investigando una variedad de fuentes y manipulando los elementos de los diversos "
                    "lenguajes de las artes (danza, música, teatro, artes visuales) para evaluar cuáles se ajustan mejor a sus "
                    "intenciones. Planifica y produce trabajos que comunican ideas y experiencias personales y sociales e "
                    "incorpora influencias de su propia comunidad y de otras culturas. Registra sus procesos, identifica los "
                    "aspectos esenciales de sus trabajos y los va modificando para mejorarlos. Planifica los espacios de "
                    "presentación considerando sus intenciones y presenta sus descubrimientos y creaciones a una variedad de "
                    "audiencias. Evalúa si logra sus intenciones de manera efectiva."
                )
            },
            "desempenos": {
                "1_GRADO": [
                    "Experimenta con los medios, los materiales y las técnicas artísticas para crear efectos visuales, sonoros, vocales o kinestéticos en respuesta a estímulos del docente o con base en sus propias exploraciones. Ejemplo: El estudiante realiza movimientos según los ritmos que toca el profesor en un tambor, y altera o exagera sus movimientos cuando hay cambios de ritmo.",
                    "Explora ideas libremente a partir de su imaginación, sus experiencias u observaciones, y experimenta maneras en que los elementos del arte (movimientos, acciones, formas, colores o sonidos) pueden usarse o ser repetidos para comunicar una idea. Ejemplo: El estudiante realiza un trabajo de técnica mixta usando papeles y materiales de collage que el docente ha dispuesto sobre una mesa. Elige pedazos de papel de diferentes formas, colores y tamaños y los pega en una cartulina de manera libre. Agrega algunos retazos de tela en espacios que han quedado libres y hace varios puntos de colores con un plumón grueso, alrededor de cada pedazo de tela.",
                    "Presenta sus trabajos y creaciones y responde a preguntas sencillas sobre ellos; asimismo, describe las características de sus propios trabajos y los de sus compañeros."
                ],
                "2_GRADO": [
                    "Explora e improvisa maneras de usar los medios, los materiales y las técnicas artísticas, y descubre que pueden ser utilizados para expresar ideas y sentimientos. Ejemplo: El estudiante usa su imaginación para representar a los diversos personajes de una leyenda y experimenta con una variedad de movimientos corporales y tonos de voz.",
                    "Genera ideas a partir de intereses, de experiencias personales, de la observación de su entorno natural y social o de estímulos externos. Empieza a seleccionar y organizar elementos (movimientos, acciones o efectos visuales o sonoros) para presentar una idea de una manera en particular. Ejemplo: El estudiante realiza una lluvia de ideas para sonorizar un cuento y elige objetos cotidianos para crear efectos sonoros que puedan representar a los diversos personajes de la historia y las acciones o momentos más importantes.",
                    "Presenta sus trabajos y creaciones en forma individual y grupal, y describe de manera sencilla cómo los ha creado y organizado."
                ],
                "3_GRADO": [
                    "Improvisa y experimenta maneras de usar los elementos del arte y reconoce los efectos que puede lograr combinando diversos medios, materiales, herramientas y técnicas para comunicar ideas. Ejemplo: El estudiante realiza mezclas de color con témperas, para crear diferentes tonos de color que se parezcan más a su color de piel al hacer su autorretrato.",
                    "Planifica sus proyectos sobre la base de las maneras en que otros artistas han usado los elementos del arte y las técnicas (por ejemplo, en prácticas artísticas tradicionales de su comunidad) para comunicar sus propias experiencias o sentimientos. Improvisa, experimenta y combina diversos elementos, medios, materiales y técnicas para descubrir cómo puede comunicar una idea.",
                    "Describe la idea o temática específica desarrollada en sus procesos de improvisación y experimentación. Explica las técnicas que ha usado y las maneras en que siente que su trabajo es exitoso. Ejemplo: El estudiante explica por qué eligió estirar los brazos y desplazarse lentamente para representar el viento en una danza."
                ],
                "4_GRADO": [
                    "Combina y busca alternativas para usar elementos de los lenguajes artísticos, medios, materiales, herramientas, técnicas, recursos tecnológicos a su alcance, así como prácticas tradicionales de su comunidad, para expresar de diferentes maneras sus ideas.",
                    "Desarrolla sus ideas a partir de observaciones, experiencias y el trabajo artístico de otros, y selecciona elementos y materiales para componer una imagen de acuerdo a sus intenciones. Ejemplo: El estudiante crea una interpretación con base en un poema que ha leído. Experimenta con diversas fuentes sonoras usando objetos de su entorno, decide cuánto debe durar cada sonido y con qué ritmo lo debe tocar, de acuerdo al sentimiento que desea transmitir.",
                    "Planifica maneras de presentar sus trabajos para comunicar sus ideas efectivamente, donde asume un rol específico. Explica las razones por las que ha seleccionado medios, materiales, herramientas y técnicas específicas en sus trabajos y evalúa con criterios dados si logró su propósito."
                ],
                "5_GRADO": [
                    "Explora los elementos de los lenguajes de las artes visuales, la música, el teatro y la danza, y los aplica con fines expresivos y comunicativos. Prueba y propone formas de utilizar los medios, los materiales, las herramientas y las técnicas con fines expresivos y comunicativos.",
                    "Genera ideas a partir de estímulos y fuentes diversas (tradicionales, locales y globales) y planifica su trabajo artístico tomando en cuenta la información recogida. Manipula una serie de elementos, medios, técnicas, herramientas y materiales para desarrollar trabajos que comunican ideas a una audiencia específica. Ejemplo: El estudiante observa diversos cuentos ilustrados sobre Don Quijote de la Mancha para saber de qué maneras han sido representados los personajes principales. Luego, planifica cómo representará de manera dramática a uno de los personajes, con base en las imágenes vistas. Prueba con una serie de movimientos, gestos y tonos de voz frente a sus compañeros para elegir la mejor manera de transmitir las características  del      personaje      que      ha elegido. ",
                                    "Registra sus ideas y las influencias de sus creaciones y las presenta de diversas maneras. Asume roles en las diferentes	fases	del proyecto artístico y evalúa el impacto de sus acciones en el	resultado       de	sus creaciones      o presentaciones. "
                ],
                "6_GRADO": [
                   " Explora los elementos de los lenguajes de las artes visuales, la música, el teatro y la danza, y combina medios,	materiales, herramientas, técnicas y recursos tecnológicos con fines      expresivos y comunicativos. ",
                   " Realiza	creaciones individuales     y     colectivas, basadas en la observación y en el estudio del entorno natural, artístico y cultural local y global. Combina y propone formas de utilizar los elementos, materiales, técnicas  y recursos tecnológicos para resolver problemas   creativos planteados en su proyecto; incluye propuestas de artes integradas. ",
                   "Documenta la manera en que	sus	ideas	se	han desarrollado y cuáles han sido         sus	influencias. Planifica la manera en que desea mostrar el resultado de sus investigaciones y creaciones, y mejora su presentación a partir de su propia autoevaluación y la retroalimentación que recibe de otros. Evalúa el resultado de sus creaciones o presentaciones y describe cuáles eran sus intenciones y qué mensajes transmite. Ejemplo: El estudiante crea un trabajo de “arpillería” para representar conceptos básicos sobre la democracia (igualdad, libertad, mayoría, etc.) a través de diferentes escenas. Planifica de qué manera      presentará      sus bocetos	e ideas a sus compañeros.     Explica     los conceptos que eligió para crear su trabajo textil y responde a preguntas sobre los personajes y las acciones que	ha       representado. Recoge ideas y sugerencias para mejorar su trabajo final. "
                ]
            }
        }
    },
    "AREA_MATEMATICA": {
    "Resuelve problemas de cantidad": {
        "capacidades": [
            "Traduce cantidades a expresiones numéricas.",
            "Comunica su comprensión sobre los números y las operaciones.",
            "Usa estrategias y procedimientos de estimación y cálculo.",
            "Argumenta afirmaciones sobre las relaciones numéricas y las operaciones."
        ],
        "estandares": {
            "III_CICLO": (
                "Resuelve problemas referidos a acciones de juntar, separar, agregar, quitar, igualar y comparar cantidades; "
                "y las traduce a expresiones de adición y sustracción, doble y mitad. Expresa su comprensión del valor de "
                "posición en números de dos cifras y los representa mediante equivalencias entre unidades y decenas. Así también, "
                "expresa mediante representaciones su comprensión del doble y mitad de una cantidad; usa lenguaje numérico. "
                "Emplea estrategias diversas y procedimientos de cálculo y comparación de cantidades; mide y compara el tiempo y la "
                "masa, usando unidades no convencionales. Explica por qué debe sumar o restar en una situación y su proceso de resolución."
            ),
            "IV_CICLO": (
                "Resuelve problemas referidos a una o más acciones de agregar, quitar, igualar, repetir o repartir una cantidad, "
                "combinar dos colecciones de objetos, así como partir una unidad en partes iguales; traduciéndolas a expresiones aditivas "
                "y multiplicativas con números naturales y expresiones aditivas con fracciones usuales. Expresa su comprensión del valor "
                "posicional en números de hasta cuatro cifras y los representa mediante equivalencias, así también la comprensión de "
                "las nociones de multiplicación, sus propiedades conmutativa y asociativa y las nociones de división, la noción de fracción "
                "como parte – todo y las equivalencias entre fracciones usuales; usando lenguaje numérico y diversas representaciones. "
                "Emplea estrategias, el cálculo mental o escrito para operar de forma exacta y aproximada con números naturales; así también "
                "emplea estrategias para sumar, restar y encontrar equivalencias entre fracciones. Mide o estima la masa y el tiempo, "
                "seleccionando y usando unidades no convencionales y convencionales. Justifica sus procesos de resolución y sus "
                "afirmaciones sobre operaciones inversas con números naturales."
            ),
            "V_CICLO": (
                "Resuelve problemas referidos a una o más acciones de comparar, igualar, repetir o repartir cantidades, partir y repartir "
                "una cantidad en partes iguales; las traduce a expresiones aditivas, multiplicativas y la potenciación cuadrada y cúbica; "
                "así como a expresiones de adición, sustracción y multiplicación con fracciones y decimales (hasta el centésimo). Expresa su "
                "comprensión del sistema de numeración decimal con números naturales hasta seis cifras, de divisores y múltiplos, y del valor "
                "posicional de los números decimales hasta los centésimos; con lenguaje numérico y representaciones diversas. Representa "
                "de diversas formas su comprensión de la noción de fracción como operador y como cociente, así como las equivalencias entre "
                "decimales, fracciones o porcentajes usuales. Selecciona y emplea estrategias diversas, el cálculo mental o escrito para operar "
                "con números naturales, fracciones, decimales y porcentajes de manera exacta o aproximada; así como para hacer conversiones "
                "de unidades de medida de masa, tiempo y temperatura, y medir de manera exacta o aproximada usando la unidad pertinente. "
                "Justifica sus procesos de resolución así como sus afirmaciones sobre las relaciones entre las cuatro operaciones y sus propiedades, "
                "basándose en ejemplos y sus conocimientos matemáticos."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Establece relaciones entre datos y acciones de agregar, quitar y juntar cantidades, y las transforma en expresiones numéricas (modelo) de adición o sustracción con números naturales hasta 20.",
                "Expresa con diversas representaciones y lenguaje numérico (números, signos y expresiones verbales) su comprensión de la decena como grupo de diez unidades y de las operaciones de adición y sustracción con números hasta 20.",
                "Expresa con diversas representaciones y lenguaje numérico (números, signos y expresiones verbales) su comprensión del número como ordinal al ordenar objetos hasta el décimo lugar, del número como cardinal al determinar una cantidad de hasta 50 objetos y de la comparación y el orden entre dos cantidades.",
                "Emplea las siguientes estrategias y procedimientos: Estrategias heurísticas; Estrategias de cálculo mental, como la suma de cifras iguales, el conteo y las descomposiciones del 10; Procedimientos de cálculo, como las sumas y restas sin canjes; Estrategias de comparación, como la correspondencia uno a uno.",
                "Compara en forma vivencial y concreta la masa de los objetos usando otros objetos como referentes, y estima el tiempo usando unidades convencionales y referentes de actividades cotidianas (días de la semana, meses del año).",
                "Realiza afirmaciones sobre las diferentes formas de representar el número y las explica con ejemplos concretos.",
                "Realiza afirmaciones sobre los resultados que podría obtener al sumar o restar y las explica con apoyo de material concreto. Asimismo, explica los pasos que siguió en la resolución de un problema."
            ],
            "2_GRADO": [
                "Establece relaciones entre datos y una o más acciones de agregar, quitar, avanzar, retroceder, juntar, separar, comparar e igualar cantidades, y las transforma en expresiones numéricas (modelo) de adición o sustracción con números naturales de hasta dos cifras.",
                "Expresa con diversas representaciones y lenguaje numérico (números, signos y expresiones verbales) su comprensión de la decena como nueva unidad en el sistema de numeración decimal y el valor posicional de una cifra en números de hasta dos cifras.",
                "Expresa con diversas representaciones y lenguaje numérico (números, signos y expresiones verbales) su comprensión del número como ordinal al ordenar objetos hasta el vigésimo lugar, de la comparación entre números y de las operaciones de adición y sustracción, el doble y la mitad, con números de hasta dos cifras.",
                "Emplea estrategias y procedimientos como los siguientes: Estrategias heurísticas; Estrategias de cálculo mental, como las descomposiciones aditivas o el uso de analogías (70 + 20; 70 + 9, completar a la decena más cercana, usar dobles, sumar en vez de restar, uso de la conmutatividad); Procedimientos de cálculo, como sumas o restas con y sin canjes; Estrategias de comparación, que incluyen el uso del tablero cien y otros.",
                "Compara en forma vivencial y concreta la masa de objetos usando unidades no convencionales, y mide el tiempo usando unidades convencionales (días, horarios semanales).",
                "Realiza afirmaciones sobre la comparación de números naturales y de la decena, y las explica con material concreto.",
                "Realiza afirmaciones sobre por qué debe sumar o restar en un problema y las explica; así también, explica su proceso de resolución y los resultados obtenidos."
            ],
            "3_GRADO": [
                "Establece relaciones entre datos y una o más acciones de agregar, quitar, comparar, igualar, reiterar, agrupar, repartir cantidades y combinar colecciones diferentes de objetos, para transformarlas en expresiones numéricas (modelo) de adición, sustracción, multiplicación y división con números naturales de hasta tres cifras.",
                "Expresa con diversas representaciones y lenguaje numérico (números, signos y expresiones verbales) su comprensión sobre la centena como nueva unidad en el sistema de numeración decimal, sus equivalencias con decenas y unidades, el valor posicional de una cifra en números de tres cifras y la comparación y el orden de números.",
                "Expresa con diversas representaciones y lenguaje numérico (números, signos y expresiones verbales) su comprensión de la multiplicación y división con números naturales hasta 100, y la propiedad conmutativa de la adición.",
                "Emplea estrategias y procedimientos como los siguientes: Estrategias heurísticas; Estrategias de cálculo mental, como descomposiciones aditivas y multiplicativas, duplicar o dividir por 2, multiplicación y división por 10, completar a la centena más cercana y aproximaciones; Procedimientos de cálculo escrito, como sumas o restas con canjes y uso de la asociatividad.",
                "Mide y compara la masa de los objetos (kilogramo) y el tiempo (horas exactas) usando unidades convencionales y no convencionales.",
                "Realiza afirmaciones sobre la comparación de números naturales y la conformación de la centena, y las explica con material concreto.",
                "Realiza afirmaciones sobre el uso de la propiedad conmutativa y las explica con ejemplos concretos. Asimismo, explica por qué la sustracción es la operación inversa de la adición, por qué debe multiplicar o dividir en un problema, así como la relación inversa entre ambas operaciones; explica también su proceso de resolución y los resultados obtenidos."
            ],
            "4_GRADO": [
                "Establece relaciones entre datos y una o más acciones de agregar, quitar, comparar, igualar, reiterar, agrupar, repartir cantidades y combinar colecciones, para transformarlas en expresiones numéricas (modelo) de adición, sustracción, multiplicación y división con números naturales de hasta cuatro cifras.",
                "Establece relaciones entre datos y acciones de partir una unidad o una colección de objetos en partes iguales y las transforma en expresiones numéricas (modelo) de fracciones usuales, adición y sustracción de estas.",
                "Expresa con diversas representaciones y lenguaje numérico (números, signos y expresiones verbales) su comprensión de: La unidad de millar como unidad del sistema de numeración decimal, sus equivalencias entre unidades menores, el valor posicional de un dígito en números de cuatro cifras y la comparación y el orden de números; La multiplicación y división con números naturales, así como las propiedades conmutativa y asociativa de la multiplicación; La fracción como parte-todo (cantidad discreta o continua), así como equivalencias y operaciones de adición y sustracción entre fracciones usuales usando fracciones equivalentes.",
                "Emplea estrategias y procedimientos como los siguientes: Estrategias heurísticas; Estrategias de cálculo mental o escrito, como las descomposiciones aditivas y multiplicativas, doblar y dividir por 2 de forma reiterada, completar al millar más cercano, uso de la propiedad distributiva, redondeo a múltiplos de 10 y amplificación y simplificación de fracciones.",
                "Mide, estima y compara la masa (kilogramo, gramo) y el tiempo (año, hora, media hora y cuarto de hora) seleccionando unidades convencionales.",
                "Realiza afirmaciones sobre la conformación de la unidad de millar y las explica con material concreto.",
                "Realiza afirmaciones sobre las equivalencias entre fracciones y las explica con ejemplos concretos. Asimismo, explica la comparación entre fracciones, así como su proceso de resolución y los resultados obtenidos."
            ],
            "5_GRADO": [
                "Establece relaciones entre datos y una o más acciones de agregar, quitar, comparar, igualar, reiterar, agrupar y repartir cantidades, para transformarlas en expresiones numéricas (modelo) de adición, sustracción, multiplicación y división con números naturales, y de adición y sustracción con decimales.",
                "Establece relaciones entre datos y acciones de dividir la unidad o una cantidad en partes iguales, y las transforma en expresiones numéricas (modelo) de fracciones y de adición, sustracción y multiplicación de estas.",
                "Expresa con diversas representaciones y lenguaje numérico (números, signos y expresiones verbales) su comprensión de: El valor posicional de un dígito en números de hasta seis cifras, al hacer equivalencias entre decenas de millar, unidades de millar, centenas, decenas y unidades; así como del valor posicional de decimales hasta el décimo, su comparación y orden; Los múltiplos de un número natural y la relación entre las cuatro operaciones y sus propiedades (conmutativa, asociativa y distributiva); La fracción como parte de una cantidad discreta o continua y como operador; Las operaciones de adición y sustracción con números decimales y fracciones.",
                "Emplea estrategias y procedimientos como los siguientes: Estrategias heurísticas; Estrategias de cálculo: uso de la reversibilidad de las operaciones con números naturales, estimación de productos y cocientes, descomposición del dividendo, amplificación y simplificación de fracciones, redondeo de expresiones decimales y uso de la propiedad distributiva de la multiplicación respecto de la adición y división.",
                "Mide, estima y compara la masa de los objetos (kilogramo) y el tiempo (décadas y siglos) usando unidades convencionales (expresadas con naturales, fracciones y decimales); y usa multiplicaciones o divisiones por múltiplos de 10, así como equivalencias, para hacer conversiones de unidades de masa y tiempo.",
                "Realiza afirmaciones sobre las relaciones (orden y otras) entre números naturales, decimales y fracciones; así como sobre relaciones inversas entre operaciones, las cuales justifica con varios ejemplos y sus conocimientos matemáticos.",
                "Justifica su proceso de resolución y los resultados obtenidos."
            ],
            "6_GRADO": [
                "Establece relaciones entre datos y una o más acciones de comparar, igualar, reiterar y dividir cantidades, y las transforma en expresiones numéricas (modelo) de adición, sustracción, multiplicación y división de dos números naturales (obtiene como cociente un número decimal exacto), y en potencias cuadradas y cúbicas.",
                "Establece relaciones entre datos y acciones de dividir una o más unidades en partes iguales y las transforma en expresiones numéricas (modelo) de fracciones y adición, sustracción y multiplicación con expresiones fraccionarias y decimales (hasta el centésimo).",
                "Expresa con diversas representaciones y lenguaje numérico (números, signos y expresiones verbales) su comprensión de: El valor posicional de un dígito en números de hasta seis cifras y decimales hasta el centésimo, así como las unidades del sistema de numeración decimal; Los múltiplos y divisores de un número natural; las características de los números primos y compuestos; así como las propiedades de las operaciones y su relación inversa; La fracción como operador y como cociente; las equivalencias entre decimales, fracciones o porcentajes usuales; las operaciones de adición, sustracción y multiplicación con fracciones y decimales.",
                "Emplea estrategias y procedimientos como los siguientes: Estrategias heurísticas; Estrategias de cálculo, como el uso de la reversibilidad de las operaciones con números naturales, la amplificación y simplificación de fracciones, el redondeo de decimales y el uso de la propiedad distributiva; Procedimientos y recursos para realizar operaciones con números naturales, expresiones fraccionarias y decimales exactos, y calcular porcentajes usuales.",
                "Mide, estima y compara la masa de los objetos, el tiempo (minutos) y la temperatura usando la unidad de medida que conviene según el problema; emplea recursos y estrategias de cálculo para hacer conversiones de unidades de masa, tiempo y temperatura, expresadas con números naturales y expresiones decimales.",
                "Realiza afirmaciones sobre las relaciones (orden y otras) entre decimales, fracciones o porcentajes usuales, y las justifica con varios ejemplos y sus conocimientos matemáticos.",
                "Justifica su proceso de resolución y los resultados obtenidos."
            ]
        }
    },
    "Resuelve problemas de regularidad, equivalencia y cambio": {
        "capacidades": [
            "Traduce datos y condiciones a expresiones algebraicas y gráficas.",
            "Comunica su comprensión sobre las relaciones algebraicas.",
            "Usa estrategias y procedimientos para encontrar equivalencias y reglas generales.",
            "Argumenta afirmaciones sobre relaciones de cambio y equivalencia."
        ],
        "estandares": {
            "III_CICLO": (
                "Resuelve problemas que presentan equivalencias o regularidades, traduciéndolas a igualdades que contienen "
                "operaciones de adición o de sustracción y a patrones de repetición de dos criterios perceptuales y patrones aditivos. "
                "Expresa su comprensión de las equivalencias y de cómo es un patrón, usando material concreto y diversas representaciones. "
                "Emplea estrategias, la descomposición de números, cálculos sencillos para encontrar equivalencias, o para continuar y crear "
                "patrones. Explica las relaciones que encuentra en los patrones y lo que debe hacer para mantener el 'equilibrio' o la igualdad, "
                "con base en experiencias y ejemplos concretos."
            ),
            "IV_CICLO": (
                "Resuelve problemas que presentan dos equivalencias, regularidades o relación de cambio entre dos magnitudes y expresiones; "
                "traduciéndolas a igualdades que contienen operaciones aditivas o multiplicativas, a tablas de valores y a patrones de repetición "
                "que combinan criterios y patrones aditivos o multiplicativos. Expresa su comprensión de la regla de formación de un patrón y "
                "del signo igual para expresar equivalencias. Así también, describe la relación de cambio entre una magnitud y otra; usando "
                "lenguaje matemático y diversas representaciones. Emplea estrategias, la descomposición de números, el cálculo mental, para "
                "crear, continuar o completar patrones de repetición. Hace afirmaciones sobre patrones, la equivalencia entre expresiones y "
                "sus variaciones y las propiedades de la igualdad, las justifica con argumentos y ejemplos concretos."
            ),
            "V_CICLO": (
                "Resuelve problemas de equivalencias, regularidades o relaciones de cambio entre dos magnitudes o entre expresiones; "
                "traduciéndolas a ecuaciones que combinan las cuatro operaciones, a expresiones de desigualdad o a relaciones de "
                "proporcionalidad directa, y patrones de repetición que combinan criterios geométricos y cuya regla de formación se asocia a "
                "la posición de sus elementos. Expresa su comprensión del término general de un patrón, las condiciones de desigualdad "
                "expresadas con los signos > y <, así como de la relación proporcional como un cambio constante; usando lenguaje matemático "
                "y diversas representaciones. Emplea recursos, estrategias y propiedades de las igualdades para resolver ecuaciones o "
                "hallar valores que cumplen una condición de desigualdad o proporcionalidad; así como procedimientos para crear, continuar o "
                "completar patrones. Realiza afirmaciones a partir de sus experiencias concretas, sobre patrones y sus elementos no inmediatos; "
                "las justifica con ejemplos, procedimientos, y propiedades de la igualdad y desigualdad."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Establece relaciones de equivalencias entre dos grupos de hasta diez objetos y las trasforma en igualdades que contienen adiciones. Ejemplo: En un platillo de una balanza hay 2 pelotas rojas y 5 pelotas azules (del mismo tamaño) y en el otro platillo hay 3 pelotas amarillas y 4 pelotas rojas. El estudiante representa con una igualdad lo que observa en la balanza (2 + 5 = 3 + 4).",
                "Establece relaciones entre los datos que se repiten (objetos, colores, diseños, sonidos o movimientos) o entre cantidades que aumentan regularmente, y los transforma en patrones de repetición o en patrones aditivos.",
                "Describe, usando lenguaje cotidiano y representaciones concretas y dibujos, su comprensión de la equivalencia como equilibrio o igual valor entre dos colecciones o cantidades; asimismo, cómo se forma el patrón de repetición (de un criterio perceptual) y el patrón aditivo creciente hasta el 20 (de 1 en 1 y 2 en 2).",
                "Emplea estrategias heurísticas y estrategias de cálculo (como el conteo, el ensayo-error y la descomposición aditiva) para encontrar equivalencias o crear, continuar y completar patrones.",
                "Explica cómo continúa el patrón y lo que debe hacer para encontrar una equivalencia, así como su proceso de resolución. Ejemplo: En una balanza de platillos, se colocan 5 cubos en el lado izquierdo y 8 cubos en el lado derecho. ¿Cuántos cubos hay que poner del lado izquierdo para lograr el equilibrio de ambos lados?"
            ],
            "2_GRADO": [
                "Establece relaciones de equivalencias entre dos grupos de hasta veinte objetos y las trasforma en igualdades que contienen adiciones o sustracciones.",
                "Establece relaciones entre los datos que se repiten (objetos, colores, diseños, sonidos o movimientos) o entre cantidades que aumentan o disminuyen regularmente, y los transforma en patrones de repetición o patrones aditivos.",
                "Expresa, con lenguaje cotidiano y representaciones concretas o dibujos, su comprensión de la equivalencia como equilibrio o igualdad entre dos colecciones o cantidades.",
                "Describe, usando lenguaje cotidiano y representaciones concretas y dibujos, el patrón de repetición (con dos criterios perceptuales), y cómo aumentan o disminuyen los números en un patrón aditivo con números de hasta 2 cifras.",
                "Emplea estrategias heurísticas y estrategias de cálculo (el conteo o la descomposición aditiva) para encontrar equivalencias, mantener la igualdad ('equilibrio') o crear, continuar y completar patrones. Ejemplo: El estudiante podría decir: 'Si tú tienes tres frutas y yo cinco, ¿qué podemos hacer para que cada uno tenga el mismo número de frutas?'.",
                "Explica lo que debe hacer para mantener el 'equilibrio' o la igualdad, y cómo continúa el patrón y las semejanzas que encuentra en dos versiones del mismo patrón, con base en ejemplos concretos. Así también, explica su proceso de resolución. Ejemplo: El estudiante podría decir: 'El collar lleva dos hojas, tres frutos secos, una concha, una y otra vez; y los bloques van dos rojos, tres azules y uno blanco, una y otra vez; ambos se forman así: dos, luego tres, luego uno'."
            ],
            "3_GRADO": [
                "Establece relaciones de equivalencias entre dos grupos de hasta veinte objetos y las trasforma en igualdades que contienen adiciones, sustracciones o multiplicaciones.",
                "Establece relaciones entre los datos que se repiten (objetos, colores, diseños, sonidos o movimientos) o entre cantidades que aumentan o disminuyen regularmente, y los transforma en patrones de repetición (con criterios perceptuales o de cambio de posición) o patrones aditivos (con números de hasta 3 cifras).",
                "Describe, con algunas expresiones del lenguaje algebraico (igualdad, patrón, etc.) y representaciones, su comprensión de la igualdad como equivalencia entre dos colecciones o cantidades, así como que un patrón puede representarse de diferentes formas.",
                "Describe el cambio de una magnitud con respecto al paso del tiempo, apoyándose en tablas o dibujos. Ejemplo: El estudiante representa el mismo patrón de diferentes maneras: triángulo, rectángulo, triángulo como ABA, ABA, ABA.",
                "Emplea estrategias heurísticas y estrategias de cálculo (la descomposición aditiva y multiplicativa, agregar o quitar en ambos lados de la igualdad, relaciones inversas entre operaciones y otras), para encontrar equivalencias, mantener la igualdad ('equilibrio'), encontrar relaciones de cambio entre dos magnitudes o continuar, completar y crear patrones.",
                "Hace afirmaciones y explica lo que sucede al modificar las cantidades que intervienen en una relación de igualdad y cómo equiparar dos cantidades, así como lo que debe considerar para continuar o completar el patrón y las semejanzas que encuentra en dos versiones del mismo patrón, mediante ejemplos concretos. Así también, explica su proceso de resolución. Ejemplo: El estudiante podría decir: 'Si quito 2 kilos en este platillo de la balanza, se perderá el equilibrio'."
            ],
            "4_GRADO": [
                "Establece relaciones entre datos de hasta dos equivalencias y las trasforma en igualdades que contienen adiciones o sustracciones, o multiplicaciones o divisiones.",
                "Establece relaciones entre los datos de una regularidad y los transforma en patrones de repetición (que combinan criterios perceptuales y un criterio geométrico de simetría) o patrones aditivos o multiplicativos (con números de hasta 4 cifras).",
                "Expresa, usando lenguaje algebraico (ícono y operaciones) y diversas representaciones, su comprensión de la regla de formación de un patrón, de la igualdad (con un término desconocido) y del signo igual, distinguiéndolo de su uso en el resultado de una operación.",
                "Describe la relación de cambio de una magnitud con respecto de otra, apoyándose en tablas o dibujos.",
                "Emplea estrategias heurísticas o estrategias de cálculo (duplicar o repartir en cada lado de la igualdad, relación inversa entre operaciones), para encontrar equivalencias, completar, crear o continuar patrones, o para encontrar relaciones de cambio entre dos magnitudes.",
                "Hace afirmaciones sobre la equivalencia entre expresiones; para ello, usa nocionalmente las propiedades de la igualdad: uniformidad y cancelativa.",
                "Hace afirmaciones sobre las regularidades, las relaciones de cambio entre magnitudes, así como los números o elementos que siguen en un patrón, y las justifica con sus experiencias concretas. Así también, justifica sus procesos de resolución."
            ],
            "5_GRADO": [
                "Establece relaciones entre datos y valores desconocidos de una equivalencia y relaciones de variación entre los datos de dos magnitudes, y las transforma en ecuaciones simples (por ejemplo: x + a = b) con números naturales, o en tablas de proporcionalidad.",
                "Establece relaciones entre los datos de una regularidad y los transforma en un patrón de repetición (que combine un criterio geométrico de simetría o traslación y un criterio perceptual) o en un patrón aditivo de segundo orden (por ejemplo: 13 - 15 - 18 - 22 - 27 - …).",
                "Expresa, con lenguaje algebraico y diversas representaciones, su comprensión de la regla de formación de un patrón de segundo orden, así como de los símbolos o letras en la ecuación y de la proporcionalidad como un cambio constante.",
                "Emplea estrategias heurísticas, estrategias de cálculo y propiedades de la igualdad (uniformidad y cancelativa) para encontrar el valor de la incógnita en una ecuación, para hallar la regla de formación de un patrón o para encontrar valores de magnitudes proporcionales.",
                "Elabora afirmaciones sobre los elementos no inmediatos que continúan un patrón y las justifica con ejemplos y cálculos sencillos. Asimismo, justifica sus procesos de resolución mediante el uso de propiedades de igualdad y cálculos."
            ],
            "6_GRADO": [
                "Establece relaciones entre datos y valores desconocidos de una equivalencia, de no equivalencia ('desequilibrio') y de variación entre los datos de dos magnitudes, y las transforma en ecuaciones que contienen las cuatro operaciones, desigualdades con números naturales o decimales, o en proporcionalidad directa.",
                "Establece relaciones entre los datos de una regularidad y los transforma en patrones de repetición (con criterios geométricos de traslación y giros), patrones (con y sin configuraciones puntuales) cuya regla se asocia a la posición de sus elementos y patrones aditivos o multiplicativos.",
                "Expresa, con lenguaje algebraico y diversas representaciones, su comprensión del término general de un patrón (por ejemplo: 2, 5, 8, 11, 14...--> término general = triple de un número, menos 1), condiciones de desigualdad expresadas con los signos > y <, así como de la relación proporcional como un cambio constante.",
                "Emplea estrategias heurísticas y estrategias de cálculo para determinar la regla o el término general de un patrón, y propiedades de la igualdad (uniformidad y cancelativa) para resolver ecuaciones o hallar valores que cumplen una condición de desigualdad o de proporcionalidad.",
                "Elabora afirmaciones sobre los términos no inmediatos en un patrón y sobre lo que ocurre cuando modifica cantidades que intervienen en los miembros de una desigualdad, y las justifica con ejemplos, cálculos, propiedades de la igualdad o a través de sus conocimientos. Así también, justifica su proceso de resolución."
            ]
        }
    },
    "Resuelve problemas de forma, movimiento y localización": {
        "capacidades": [
            "Modela objetos con formas geométricas y sus transformaciones.",
            "Comunica su comprensión sobre las formas y relaciones geométricas.",
            "Usa estrategias y procedimientos para orientarse en el espacio.",
            "Argumenta afirmaciones sobre relaciones geométricas."
        ],
        "estandares": {
            "III_CICLO": (
                "Resuelve problemas en los que modela las características y datos de ubicación de los objetos del entorno a formas "
                "bidimensionales y tridimensionales, sus elementos, posición y desplazamientos. Describe estas formas mediante sus elementos: "
                "número de lados, esquinas, lados curvos y rectos; número de puntas caras, formas de sus caras, usando representaciones "
                "concretas y dibujos. Así también traza y describe desplazamientos y posiciones, en cuadriculados y puntos de referencia "
                "usando algunos términos del lenguaje geométrico. Emplea estrategias y procedimientos basados en la manipulación, para "
                "construir objetos y medir su longitud (ancho y largo) usando unidades no convencionales. Explica semejanzas y diferencias "
                "entre formas geométricas, así como su proceso de resolución."
            ),
            "IV_CICLO": (
                "Resuelve problemas en los que modela características y datos de ubicación de los objetos a formas bidimensionales y "
                "tridimensionales, sus elementos, propiedades, su movimiento y ubicación en el plano cartesiano. Describe con lenguaje "
                "geométrico, estas formas reconociendo ángulos rectos, número de lados y vértices del polígono, así como líneas paralelas y "
                "perpendiculares, identifica formas simétricas y realiza traslaciones, en cuadrículas. Así también elabora croquis, "
                "donde traza y describe desplazamientos y posiciones, usando puntos de referencia. Emplea estrategias y procedimientos para "
                "trasladar y construir formas a través de la composición y descomposición, y para medir la longitud, superficie y capacidad de "
                "los objetos, usando unidades convencionales y no convencionales, recursos e instrumentos de medición. Elabora afirmaciones sobre "
                "las figuras compuestas; así como relaciones entre una forma tridimensional y su desarrollo en el plano; las explica con ejemplos "
                "concretos y gráficos."
            ),
            "V_CICLO": (
                "Resuelve problemas en los que modela las características y la ubicación de objetos del entorno a formas bidimensionales y "
                "tridimensionales, sus propiedades, su ampliación, reducción o rotación. Describe y clasifica prismas rectos, cuadriláteros, "
                "triángulos, círculos, por sus elementos: vértices, lados, caras, ángulos, y por sus propiedades; usando lenguaje geométrico. "
                "Realiza giros en cuartos y medias vueltas, traslaciones, ampliación y reducción de formas bidimensionales, en el plano cartesiano. "
                "Describe recorridos y ubicaciones en planos. Emplea procedimientos e instrumentos para ampliar, reducir, girar y construir formas; "
                "así como para estimar o medir la longitud, superficie y capacidad de los objetos, seleccionando la unidad de medida convencional "
                "apropiada y realizando conversiones. Explica sus afirmaciones sobre relaciones entre elementos de las formas geométricas y sus "
                "atributos medibles, con ejemplos concretos y propiedades."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Establece relaciones entre las características de los objetos del entorno y las asocia y representa con formas geométricas tridimensionales y bidimensionales que conoce, así como con la medida cualitativa de su longitud.",
                "Establece relaciones entre los datos de ubicación y recorrido de objetos y personas del entorno, y los expresa con material concreto o bosquejos y desplazamientos, teniendo en cuenta su cuerpo como punto de referencia u objetos en las cuadrículas.",
                "Expresa con material concreto y dibujos su comprensión sobre algunos elementos de las formas tridimensionales (caras y vértices) y bidimensionales (lados, líneas rectas y curvas). Asimismo, describe si los objetos ruedan, se sostienen, no se sostienen o tienen puntas o esquinas usando lenguaje cotidiano y algunos términos geométricos.",
                "Expresa con material concreto su comprensión sobre la longitud como una de las propiedades que se puede medir en algunos objetos; asimismo, su comprensión sobre la medida de la longitud de objetos de manera cualitativa con representaciones concretas, y establece 'es más largo que' o 'es más corto que'.",
                "Expresa con material concreto y bosquejos los desplazamientos y posiciones de objetos o personas tomando como punto de referencia su propia posición; hace uso de expresiones como 'arriba', 'abajo', 'detrás de', 'encima de', 'debajo de', 'al lado', 'dentro', 'fuera', 'en el borde'.",
                "Emplea estrategias heurísticas, recursos y procedimientos de comparación para medir directamente la longitud de dos objetos con unidades no convencionales (dedos, manos, pies, pasos, brazos, y objetos como clips, lápices, palillos, etc.) y la visualización para construir objetos con material concreto.",
                "Hace afirmaciones sobre algunas propiedades físicas o semejanzas de los objetos y las prueba con ejemplos concretos. Así también, explica el proceso seguido. Ejemplo: El estudiante podría decir: 'Algunos objetos con puntas no ruedan', 'Estos dos objetos tienen la misma forma (pelota y canica)', etc."
            ],
            "2_GRADO": [
                "Establece relaciones entre las características de los objetos del entorno, las asocia y representa con formas geométricas tridimensionales (cuerpos que ruedan y no ruedan) y bidimensionales (cuadrado, rectángulo, círculo, triángulo), así como con las medidas de su longitud (largo y ancho).",
                "Establece relaciones entre los datos de ubicación y recorrido de objetos y personas del entorno, y los expresa con material concreto y bosquejos o gráficos, posiciones y desplazamientos, teniendo en cuenta puntos de referencia en las cuadrículas.",
                "Expresa con material concreto y dibujos su comprensión sobre algún elemento de las formas tridimensionales (número de puntas, número de caras, formas de sus caras) y bidimensionales (número de lados, vértices, lados curvos y rectos). Asimismo, describe si los objetos ruedan, se sostienen, no se sostienen o tienen puntas o esquinas usando lenguaje cotidiano y algunos términos geométricos.",
                "Expresa con material concreto su comprensión sobre la medida de la longitud al determinar cuántas veces es más largo un objeto con relación a otro. Expresa también que el objeto mantiene su longitud a pesar de sufrir transformaciones como romper, enrollar o flexionar (conservación de la longitud). Ejemplo: El estudiante, luego de enrollar y desenrollar sorbetes de diferentes tamaños, los ordena por su longitud, desde el más largo hasta el más corto, y viceversa.",
                "Expresa con material concreto, bosquejos o gráficos los desplazamientos y posiciones de objetos o personas con relación a un punto de referencia; hace uso de expresiones como 'sube', 'entra', 'hacia adelante', 'hacia arriba', 'a la derecha', 'por el borde', 'en frente de', etc., apoyándose con códigos de flechas.",
                "Emplea estrategias, recursos y procedimientos basados en la manipulación y visualización, para construir objetos y medir su longitud usando unidades no convencionales (manos, pasos, pies, etc.).",
                "Hace afirmaciones sobre las semejanzas y diferencias entre las formas geométricas, y las explica con ejemplos concretos y con base en sus conocimientos matemáticos. Asimismo, explica el proceso seguido. Ejemplo: El estudiante afirma que todas las figuras que tienen tres lados son triángulos o que una forma geométrica sigue siendo la misma aunque cambie de posición."
            ],
            "3_GRADO": [
                "Establece relaciones entre las características de los objetos del entorno, las asocia y representa con formas geométricas bidimensionales (figuras regulares o irregulares), sus elementos y con sus medidas de longitud y superficie; y con formas tridimensionales (cuerpos redondos y compuestos), sus elementos y su capacidad.",
                "Establece relaciones entre los datos de ubicación y recorrido de los objetos y personas del entorno, y los expresa en un gráfico, teniendo a los objetos fijos como puntos de referencia; asimismo, considera el eje de simetría de un objeto o una figura.",
                "Expresa con dibujos su comprensión sobre los elementos de las formas tridimensionales y bidimensionales (número de lados, vértices, eje de simetría).",
                "Expresa con material concreto su comprensión sobre las medidas de longitudes de un mismo objeto con diferentes unidades. Asimismo, su comprensión de la medida de la superficie de objetos planos de manera cualitativa con representaciones concretas, estableciendo 'es más extenso que', 'es menos extenso que' (superficie asociada a la noción de extensión) y su conservación.",
                "Expresa su comprensión sobre la capacidad como una de las propiedades que se puede medir en algunos recipientes, establece 'contiene más que', 'contiene menos que' e identifica que la cantidad contenida en un recipiente permanece invariante a pesar de que se distribuya en otros de distinta forma y tamaño (conservación de la capacidad).",
                "Expresa con gráficos los desplazamientos y posiciones de objetos o personas con relación a objetos fijos como puntos de referencia; hace uso de algunas expresiones del lenguaje geométrico.",
                "Emplea estrategias heurísticas y procedimientos como la composición y descomposición, el doblado, el recorte, la visualización y diversos recursos para construir formas y figuras simétricas (a partir de instrucciones escritas u orales). Asimismo, usa diversas estrategias para medir de manera exacta o aproximada (estimar) la longitud (centímetro, metro) y el contorno de una figura, y comparar la capacidad y superficie de los objetos empleando la unidad de medida, no convencional o convencional, según convenga, así como algunos instrumentos de medición.",
                "Hace afirmaciones sobre algunas relaciones entre elementos de las formas, su composición o descomposición, y las explica con ejemplos concretos o dibujos. Asimismo, explica el proceso seguido. Ejemplo: El estudiante podría decir: 'Todos los cuadrados se pueden formar con dos triángulos iguales'."
            ],
            "4_GRADO": [
                "Establece relaciones entre las características de objetos reales o imaginarios, los asocia y representa con formas bidimensionales (polígonos) y sus elementos, así como con su perímetro, medidas de longitud y superficie; y con formas tridimensionales (cubos y prismas de base cuadrangular), sus elementos y su capacidad.",
                "Establece relaciones entre los datos de ubicación y recorrido de los objetos, personas y lugares cercanos, así como la traslación de los objetos o figuras, y los expresa en gráficos o croquis teniendo a los objetos y lugares fijos como puntos de referencia.",
                "Expresa con dibujos su comprensión sobre los elementos de cubos y prismas de base cuadrangular: caras, vértices, aristas; también, su comprensión sobre los elementos de los polígonos: ángulos rectos, número de lados y vértices; así como su comprensión sobre líneas perpendiculares y paralelas usando lenguaje geométrico.",
                "Expresa con material concreto o gráficos su comprensión sobre el perímetro y la medida de capacidad de los recipientes para determinar cuántas veces se puede llenar uno con el otro. Asimismo, su comprensión sobre la medida de la superficie de objetos planos, de manera cualitativa y con representaciones concretas estableciendo 'es más extenso que', 'es menos extenso que' (superficie asociada a la noción de extensión) y su conservación.",
                "Expresa con gráficos o croquis los desplazamientos y posiciones de objetos, personas y lugares cercanos, así como sus traslaciones con relación a objetos fijos como puntos de referencia. Ejemplo: El estudiante podría dar instrucciones a partir de objetos del entorno para ubicar otros, o a partir de lugares del entorno para ubicarse o ubicar a otros.",
                "Emplea estrategias, recursos y procedimientos como la composición y descomposición, la visualización, así como el uso de las cuadrículas, para construir formas simétricas, ubicar objetos y trasladar figuras, usando recursos. Así también, usa diversas estrategias para medir, de manera exacta o aproximada (estimar), la medida de los ángulos respecto al ángulo recto, la longitud, el perímetro (metro y centímetro), la superficie (unidades patrón) y la capacidad (en litro y con fracciones) de los objetos, y hace conversiones de unidades de longitud. Emplea la unidad de medida, convencional o no convencional, según convenga, así como algunos instrumentos de medición (cinta métrica, regla, envases o recipientes).",
                "Hace afirmaciones sobre algunas relaciones entre elementos de las formas y su desarrollo en el plano, y explica sus semejanzas y diferencias mediante ejemplos concretos o dibujos con base en su exploración o visualización. Así también, explica el proceso seguido. Ejemplo: El estudiante podría decir: 'Un cubo se puede construir con una plantilla que contenga 6 cuadrados del mismo tamaño'."
            ],
            "5_GRADO": [
                "Establece relaciones entre las características de objetos reales o imaginarios, los asocia y representa con formas bidimensionales (cuadriláteros) y sus elementos, así como con su perímetro y medidas de la superficie; y con formas tridimensionales (prismas rectos), sus elementos y su capacidad.",
                "Establece relaciones entre los datos de ubicación y recorrido de los objetos, personas y lugares cercanos, y las expresa en un croquis teniendo en cuenta referencias como, por ejemplo, calles o avenidas.",
                "Establece relaciones entre los cambios de tamaño de los objetos con las ampliaciones, reducciones y reflexiones de una figura plana.",
                "Expresa con dibujos su comprensión sobre los elementos de prismas rectos y cuadriláteros (ángulos, vértices, bases), y propiedades (lados paralelos y perpendiculares) usando lenguaje geométrico.",
                "Expresa con gráficos su comprensión sobre el perímetro y la medida de longitud; además, sobre la medida de capacidad de los recipientes y la medida de la superficie de objetos planos como la porción de plano ocupado y recubrimiento de espacio, y su conservación.",
                "Expresa con un croquis los desplazamientos y posiciones de objetos o personas con relación a un sistema de referencia como, por ejemplo, calles o avenidas. Asimismo, describe los cambios de tamaño de los objetos mediante las ampliaciones, reducciones y reflexiones de una figura plana en el plano cartesiano.",
                "Emplea estrategias de cálculo, la visualización y los procedimientos de composición y descomposición para construir formas, ángulos, realizar ampliaciones, reducciones y reflexiones de las figuras, así como para hacer trazos en el plano cartesiano. Para ello, usa diversos recursos e instrumentos de dibujo. También, usa diversas estrategias para medir, de manera exacta o aproximada (estimar), la medida de ángulos, la longitud (perímetro, kilómetro, metro), la superficie (unidades patrón), la capacidad (en litros y en decimales) de los objetos; además, realiza conversiones de unidades de longitud mediante cálculos numéricos y usa la propiedad transitiva para ordenar objetos según su longitud. Emplea la unidad no convencional o convencional, según convenga, así como algunos instrumentos de medición.",
                "Plantea afirmaciones sobre las relaciones entre los objetos, entre los objetos y las formas geométricas, y entre las formas geométricas, así como su desarrollo en el plano, y las explica con argumentos basados en ejemplos concretos, gráficos y en sus conocimientos matemáticos con base en su exploración o visualización. Así también, explica el proceso seguido."
            ],
            "6_GRADO": [
                "Establece relaciones entre las características de objetos reales o imaginarios, los asocia y representa con formas bidimensionales (triángulos, cuadriláteros y círculos), sus elementos, perímetros y superficies ; y con formas tridimensionales (prismas rectos y cilindros), sus elementos y el volumen de los prismas rectos con base rectangular.",
                "Establece relaciones entre los datos de ubicación y recorrido de los objetos, personas o lugares, y las expresa en un croquis o plano sencillo teniendo en cuenta referencias como, por ejemplo, calles o avenidas.",
                "Establece relaciones entre los cambios de tamaño y ubicación de los objetos con las ampliaciones, reducciones y giros en el plano cartesiano. Ejemplo: El estudiante establece las coordenadas en las que se encuentra un lugar determinado.",
                "Expresa con dibujos su comprensión sobre los elementos y propiedades del prisma, triángulo, cuadrilátero y círculo usando lenguaje geométrico.",
                "Expresa con gráficos su comprensión sobre el perímetro, el volumen de un cuerpo sólido y el área como propiedades medibles de los objetos.",
                "Expresa con un croquis o plano sencillo los desplazamientos y posiciones de objetos o personas con relación a los puntos cardinales (sistema de referencia). Asimismo, describe los cambios de tamaño y ubicación de los objetos mediante ampliaciones, reducciones y giros en el plano cartesiano. Ejemplo: El estudiante nombra posiciones teniendo en cuenta sistemas de coordenadas presentes en los mapas.",
                "Emplea estrategias heurísticas, estrategias de cálculo, la visualización y los procedimientos de composición y descomposición para construir formas desde perspectivas, desarrollo de sólidos, realizar giros en el plano, así como para trazar recorridos. Usa diversas estrategias para construir ángulos, medir la longitud (cm) y la superficie (m2, cm2), y comparar el área de dos superficies o la capacidad de los objetos, de manera exacta o aproximada. Realiza cálculos numéricos para hacer conversiones de medidas (unidades de longitud). Emplea la unidad de medida no convencional o convencional, según convenga, así como instrumentos de dibujo (compás, transportador) y de medición, y diversos recursos.",
                "Plantea afirmaciones sobre las relaciones entre los objetos, entre los objetos y las formas geométricas, y entre las formas geométricas, así como su desarrollo en el plano cartesiano, entre el perímetro y la superficie de una forma geométrica, y las explica con argumentos basados en ejemplos concretos, gráficos, propiedades y en sus conocimientos matemáticos con base en su exploración o visualización, usando el razonamiento inductivo. Así también, explica el proceso seguido. Ejemplo: 'Dos rectángulos pueden tener diferente área pero el mismo perímetro', 'El área de un triángulo la puedo obtener dividiendo por la mitad el área de un paralelogramo'."
            ]
        }
    },
    "Resuelve problemas de gestión de datos e incertidumbre": {
        "capacidades": [
            "Representa datos con gráficos y medidas estadísticas o probabilísticas.",
            "Comunica su comprensión de los conceptos estadísticos y probabilísticos.",
            "Usa estrategias y procedimientos para recopilar y procesar datos.",
            "Sustenta conclusiones o decisiones con base en la información obtenida."
        ],
        "estandares": {
            "III_CICLO": (
                "Resuelve problemas relacionados con datos cualitativos en situaciones de su interés, recolecta datos a través "
                "de preguntas sencillas, los registra en listas o tablas de conteo simple (frecuencia) y los organiza en pictogramas "
                "horizontales y gráficos de barras simples. Lee la información contenida en estas tablas o gráficos identificando el "
                "dato o datos que tuvieron mayor o menor frecuencia y explica sus decisiones basándose en la información producida. "
                "Expresa la ocurrencia de sucesos cotidianos usando las nociones de posible o imposible y justifica su respuesta."
            ),
            "IV_CICLO": (
                "Resuelve problemas relacionados con datos cualitativos o cuantitativos (discretos) sobre un tema de estudio, "
                "recolecta datos a través de encuestas y entrevistas sencillas, registra en tablas de frecuencia simples y los representa "
                "en pictogramas, gráficos de barra simple con escala (múltiplos de diez). Interpreta información contenida en gráficos de "
                "barras simples y dobles y tablas de doble entrada, comparando frecuencias y usando el significado de la moda de un "
                "conjunto de datos; a partir de esta información, elabora algunas conclusiones y toma decisiones. Expresa la ocurrencia "
                "de sucesos cotidianos usando las nociones de seguro, más probable, menos probable, y justifica su respuesta."
            ),
            "V_CICLO": (
                "Resuelve problemas relacionados con temas de estudio, en los que reconoce variables cualitativas o cuantitativas discretas, "
                "recolecta datos a través de encuestas y de diversas fuentes de información. Selecciona tablas de doble entrada, gráficos "
                "de barras dobles y gráficos de líneas, seleccionando el más adecuado para representar los datos. Usa el significado de la "
                "moda para interpretar información contenida en gráficos y en diversas fuentes de información. Realiza experimentos "
                "aleatorios, reconoce sus posibles resultados y expresa la probabilidad de un evento relacionando el número de casos "
                "favorables y el total de casos posibles. Elabora y justifica predicciones, decisiones y conclusiones, basándose en la "
                "información obtenida en el análisis de datos o en la probabilidad de un evento."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Representa las características y el comportamiento de datos cualitativos (por ejemplo, color de los ojos: pardos, negros; plato favorito: cebiche, arroz con pollo, etc.) de una población, a través de pictogramas horizontales (el símbolo representa una unidad) y gráficos de barras verticales simples (sin escala), en situaciones cotidianas de su interés personal o de sus pares.",
                "Expresa la ocurrencia de acontecimientos cotidianos usando las nociones 'siempre', 'a veces' y 'nunca'.",
                "Lee la información contenida en tablas de frecuencia simple (conteo simple), pictogramas horizontales y gráficos de barras verticales simples; indica la mayor frecuencia y representa los datos con material concreto o gráfico.",
                "Recopila datos mediante preguntas sencillas y el empleo de procedimientos y recursos (material concreto y otros); los procesa y organiza en listas de datos o tablas de frecuencia simple (conteo simple) para describirlos.",
                "Toma decisiones sencillas y las explica a partir de la información obtenida."
            ],
            "2_GRADO": [
                "Representa las características y el comportamiento de datos cualitativos (por ejemplo, color de los ojos: pardos, negros; plato favorito: cebiche, arroz con pollo, etc.) de una población, a través de pictogramas horizontales (el símbolo representa una o dos unidades) y gráficos de barras verticales simples (sin escala), en situaciones cotidianas de su interés personal o de sus pares.",
                "Expresa la ocurrencia de acontecimientos cotidianos usando las nociones 'posible' e 'imposible'.",
                "Lee información contenida en tablas de frecuencia simple (conteo simple), pictogramas horizontales y gráficos de barras verticales simples; indica la mayor o menor frecuencia y compara los datos, los cuales representa con material concreto y gráfico.",
                "Recopila datos mediante preguntas y el empleo de procedimientos y recursos (material concreto y otros); los procesa y organiza en listas de datos o tablas de frecuencia simple (conteo simple) para describirlos.",
                "Toma decisiones sencillas y las explica a partir de la información obtenida."
            ],
            "3_GRADO": [
                "Representa las características y el comportamiento de datos cualitativos (por ejemplo, color de los ojos: pardos, negros; plato favorito: cebiche, arroz con pollo, etc.) y cuantitativos discretos (por ejemplo: número de hermanos: 3, 2; cantidad de goles: 2, 4, 5, etc.) de una población, a través de pictogramas verticales y horizontales (el símbolo representa más de una unidad) y gráficos de barras horizontales (simples y escala dada de 2 en 2, 5 en 5 y 10 en 10), en situaciones de su interés o un tema de estudio.",
                "Expresa la ocurrencia de acontecimientos cotidianos usando las nociones 'seguro', 'posible' e 'imposible'.",
                "Lee tablas de frecuencias simples (absolutas), gráficos de barras horizontales simples con escala y pictogramas de frecuencias con equivalencias, para interpretar la información explícita de los datos contenidos en diferentes formas de representación.",
                "Recopila datos mediante encuestas sencillas o entrevistas cortas con preguntas adecuadas empleando procedimientos y recursos; los procesa y organiza en listas de datos o tablas de frecuencia simple, para describirlos y analizarlos.",
                "Selecciona y emplea procedimientos y recursos como el recuento, el diagrama u otros, para determinar todos los posibles resultados de la ocurrencia de acontecimientos cotidianos.",
                "Predice la ocurrencia de un acontecimiento o suceso cotidiano. Así también, explica sus decisiones a partir de la información obtenida con base en el análisis de datos."
            ],
            "4_GRADO": [
                "Representa las características y el comportamiento de datos cualitativos (por ejemplo, color de ojos: pardos, negros; profesión: médico, abogado, etc.) y cuantitativos discretos (por ejemplo: número de hermanos: 3, 2; cantidad de goles: 2, 4, 5, etc.) de una población, a través de pictogramas verticales y horizontales (cada símbolo representa más de una unidad), gráficos de barras con escala dada (múltiplos de 10) y la moda como la mayor frecuencia, en situaciones de interés o un tema de estudio.",
                "Expresa su comprensión de la moda como la mayor frecuencia y la media aritmética como punto de equilibrio; así como todos los posibles resultados de la ocurrencia de sucesos cotidianos usando las nociones 'seguro', 'más probable' y 'menos probable'.",
                "Lee gráficos de barras con escala, tablas de doble entrada y pictogramas de frecuencias con equivalencias, para interpretar la información a partir de los datos contenidos en diferentes formas de representación y de la situación estudiada.",
                "Recopila datos mediante encuestas sencillas o entrevistas cortas con preguntas adecuadas empleando procedimientos y recursos; los procesa y organiza en listas de datos, tablas de doble entrada o tablas de frecuencia, para describirlos y analizarlos.",
                "Selecciona y emplea procedimientos y recursos como el recuento, el diagrama, las tablas de frecuencia u otros, para determinar la media aritmética como punto de equilibrio, la moda como la mayor frecuencia y todos los posibles resultados de la ocurrencia de sucesos cotidianos.",
                "Predice que la posibilidad de ocurrencia de un suceso es mayor que otro. Así también, explica sus decisiones y conclusiones a partir de la información obtenida con base en el análisis de datos."
            ],
            "5_GRADO": [
                "Representa las características de una población en estudio, las que asocia a variables cualitativas (por ejemplo, color de ojos: pardos, negros; profesión: médico, abogado, etc.) y cuantitativas discretas (por ejemplo, número de hermanos: 3, 2; cantidad de goles: 2, 4, 5, etc.), así como también el comportamiento del conjunto de datos, a través de pictogramas verticales y horizontales (cada símbolo representa más de una unidad), gráficos de barras con escala dada (múltiplos de 10), la moda como la mayor frecuencia y la media aritmética como punto de equilibrio.",
                "Expresa su comprensión de la moda como la mayor frecuencia y la media aritmética como punto de equilibrio; así como todos los posibles resultados de la ocurrencia de sucesos cotidianos usando las nociones 'seguro', 'más probable' y 'menos probable'.",
                "Lee gráficos de barras con escala, tablas de doble entrada y pictogramas de frecuencias con equivalencias, para interpretar la información del mismo conjunto de datos contenidos en diferentes formas de representación y de la situación estudiada.",
                "Recopila datos mediante encuestas sencillas o entrevistas cortas con preguntas adecuadas empleando procedimientos y recursos; los procesa y organiza en listas de datos, tablas de doble entrada o tablas de frecuencia, para describirlos y analizarlos.",
                "Selecciona y emplea procedimientos y recursos como el recuento, el diagrama, las tablas de frecuencia u otros, para determinar la media aritmética como punto de equilibrio, la moda como la mayor frecuencia y todos los posibles resultados de la ocurrencia de sucesos cotidianos.",
                "Predice la mayor o menor frecuencia de un conjunto de datos, o si la posibilidad de ocurrencia de un suceso es mayor que otro. Así también, explica sus decisiones y conclusiones a partir de la información obtenida con base en el análisis de datos."
            ],
            "6_GRADO": [
                "Representa las características de una población en estudio sobre situaciones de interés o aleatorias, asociándolas a variables cualitativas (por ejemplo: vóley, tenis) y cuantitativas discretas (por ejemplo: 3, 4, 5 hijos), así como también el comportamiento del conjunto de datos, a través de gráficos de barras dobles, gráficos de líneas, la moda y la media aritmética como reparto equitativo.",
                "Determina todos los posibles resultados de una situación aleatoria a través de su probabilidad como fracción.",
                "Expresa su comprensión de la moda como la mayor frecuencia y la media aritmética como reparto equitativo; así como todos los posibles resultados de una situación aleatoria en forma oral usando las nociones 'más probables' o 'menos probables', y numéricamente. Ejemplo: El estudiante podría decir: 'En dos de los cinco casos, el resultado es favorable: 2/5'.",
                "Lee tablas de doble entrada y gráficos de barras dobles, así como información proveniente de diversas fuentes (periódicos, revistas, entrevistas, experimentos, etc.), para interpretar la información que contienen considerando los datos, las condiciones de la situación y otra información que se tenga sobre las variables. También, advierte que hay tablas de doble entrada con datos incompletos, las completa y produce nueva información.",
                "Recopila datos mediante encuestas sencillas o entrevistas cortas con preguntas adecuadas empleando procedimientos y recursos; los procesa y organiza en tablas de doble entrada o tablas de frecuencia, para describirlos y analizarlos.",
                "Selecciona y emplea procedimientos y recursos como el recuento, el diagrama, las tablas de frecuencia u otros, para determinar la media aritmética como reparto equitativo, la moda, los casos favorables a un suceso y su probabilidad como fracción.",
                "Predice la tendencia de los datos o la ocurrencia de sucesos a partir del análisis de los resultados de una situación aleatoria. Así también, justifica sus decisiones y conclusiones a partir de la información obtenida con base en el análisis de datos."
            ]
        }
    }
},
"Ciencia y Tecnología": {
    "Indaga mediante métodos científicos para construir sus conocimientos": {
        "capacidades": [
            "Problematiza situaciones para hacer indagación.",
            "Diseña estrategias para hacer indagación.",
            "Genera y registra datos e información.",
            "Analiza datos e información.",
            "Evalúa y comunica el proceso y resultados de su indagación."
        ],
        "estandares": {
            "III_CICLO": (
                "Indaga al explorar objetos o fenómenos, al hacer preguntas, proponer posibles respuesta y actividades para obtener "
                "información sobre las características y relaciones que establece sobre estos. Sigue un procedimiento para observar, "
                "manipular, describir y comparar sus ensayos y los utiliza para elaborar conclusiones. Expresa en forma oral, escrita "
                "o gráfica lo realizado, aprendido y las dificultades de su indagación."
            ),
            "IV_CICLO": (
                "Indaga al establecer las causas de un hecho o fenómeno para formular preguntas y posibles respuestas sobre estos con "
                "base en sus experiencias. Propone estrategias para obtener información sobre el hecho o fenómeno y sus posibles causas, "
                "registra datos, los analiza estableciendo relaciones y evidencias de causalidad. Comunica en forma oral, escrita o gráfica "
                "sus procedimientos, dificultades, conclusiones y dudas."
            ),
            "V_CICLO": (
                "Indaga las causas o describe un objeto o fenómeno que identifica para formular preguntas e hipótesis en las que relaciona "
                "las variables que intervienen y que se pueden observar. Propone estrategias para observar o generar una situación "
                "controlada en la cual registra evidencias de cómo una variable independiente afecta a otra dependiente. Establece "
                "relaciones entre los datos, los interpreta y los contrasta con información confiable. Evalúa y comunica sus "
                "conclusiones y procedimientos."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Hace preguntas acerca de hechos, fenómenos u objetos naturales y tecnológicos que explora y observa en su entorno. Propone posibles respuestas con base en sus experiencias. Ejemplo: El estudiante observa cómo un caracol sube por el tronco de un árbol, y pregunta: '¿Por qué el caracol no se cae?'. Propone posibles respuestas, como: 'Tiene baba pegajosa como la goma'.",
                "Propone acciones que le permiten responder a la pregunta. Busca información, selecciona los materiales e instrumentos que necesitará para explorar y observar objetos, hechos o fenómenos y recoger datos. Ejemplo: El estudiante podría decir: 'Salgamos al patio a buscar otros caracoles; llevaremos lupas para mirarlos', 'Tengo un libro que trata sobre caracoles', etc.",
                "Obtiene datos a partir de la observación y exploración de objetos, hechos o fenómenos; y los registra en organizadores mediante dibujos o primeras formas de escritura. Ejemplo: El estudiante hace dibujos con detalles de las formas del caracol, del camino que recorrió, etc.",
                "Describe las características del hecho, fenómeno u objeto natural y tecnológico que registró, para comprobar si su respuesta es verdadera o no. Ejemplo: El estudiante describe los caracoles: forma, color, si tienen patas, qué estaban haciendo y lo que sucedió cuando se acercó a observarlos. Después de que el docente lea un texto sobre los caracoles, podrá comparar si lo que observó concuerda con lo que dice el texto, por qué, etc.",
                "Comunica las respuestas que dio a la pregunta, lo que aprendió, así como sus logros y dificultades, mediante diversas formas de expresión: gráficas, orales o a través de su nivel de escritura. Ejemplo: El estudiante comenta si los caracoles tenían patas, cómo era su cuerpo, así como las dificultades que tuvo para observarlos y lo que haría para estudiarlos mejor después de esta experiencia. Podría dibujar en una hoja lo que le pareció más importante y, además, comentar qué parte del trabajo y de lo aprendido le gustó más."
            ],
            "2_GRADO": [
                "Hace preguntas que buscan la descripción de las características de los hechos, fenómenos u objetos naturales y tecnológicos que explora y observa en su entorno. Propone posibles respuestas basándose en el reconocimiento de regularidades identificadas en su experiencia.",
                "Propone acciones que le permiten responder a la pregunta y las ordena secuencialmente; selecciona los materiales, instrumentos y herramientas necesarios para explorar, observar y recoger datos sobre los hechos, fenómenos u objetos naturales o tecnológicos.",
                "Obtiene y registra datos, a partir de las acciones que realizó para responder a la pregunta. Utiliza algunos organizadores de información o representa los datos mediante dibujos o sus primeras formas de escritura.",
                "Compara y establece si hay diferencia entre la respuesta que propuso y los datos o la información obtenida en su observación o experimentación. Elabora sus conclusiones.",
                "Comunica las respuestas que dio a la pregunta, lo que aprendió, así como sus logros y dificultades, mediante diversas formas de expresión: gráficas, orales o a través de su nivel de escritura."
            ],
            "3_GRADO": [
                "Hace preguntas sobre hechos, fenómenos u objetos naturales y tecnológicos que explora y observa en su entorno. Propone posibles respuestas con base en el reconocimiento de regularidades identificadas en situaciones similares. Ejemplo: El estudiante podría preguntar: '¿Por qué una vela encendida se derrite y no ocurre lo mismo con un mechero?'. Y podría responder: 'La cera se consume más rápido que el kerosene'.",
                "Propone un plan donde describe las acciones y los procedimientos que utilizará para responder a la pregunta. Selecciona los materiales e instrumentos que necesitará para su indagación, así como las fuentes de información que le permitan comprobar la respuesta.",
                "Obtiene datos cualitativos o cuantitativos al llevar a cabo el plan que propuso para responder la pregunta. Usa unidades de medida convencionales y no convencionales, registra los datos y los representa en organizadores. Ejemplo: Cuando el estudiante observa cómo se derriten unos cubos de hielo, puede medir la temperatura a la que están inicialmente y, luego, medir la temperatura del líquido, el tiempo que pasó para que se derritan, así como hacer una representación gráfica de lo sucedido.",
                "Establece relaciones que expliquen el fenómeno estudiado. Utiliza los datos obtenidos y los compara con la respuesta que propuso, así como con la información científica que posee. Elabora sus conclusiones. Ejemplo: Cuando el estudiante dice 'en un día caluroso, los cubos de hielo se derriten más rápido; y en un día frío, demoran en derretirse', utiliza los datos tomados para confirmar sus afirmaciones, así como los resúmenes que explican el tema.",
                "Comunica las conclusiones de su indagación y lo que aprendió usando conocimientos científicos, así como el procedimiento, los logros y las dificultades que tuvo durante su desarrollo. Propone algunas mejoras. Da a conocer su indagación en forma oral o escrita."
            ],
            "4_GRADO": [
                "Hace preguntas sobre hechos, fenómenos u objetos naturales o tecnológicos que explora. Elabora una posible explicación como respuesta, donde establece una relación entre los hechos y los factores que producen los cambios. Ejemplo: El estudiante podría preguntar: '¿Por qué algunos globos inflados se elevan y otros caen al suelo?'. Y, luego, responder: 'El aire que contienen tiene diferente peso y por eso unos caen al suelo mientras otros siguen elevándose'.",
                "Propone un plan donde describe las acciones y los procedimientos que utilizará para recoger información acerca de los factores relacionados con el problema en su indagación. Selecciona materiales, instrumentos y fuentes de información científica que le permiten comprobar la respuesta.",
                "Obtiene datos cualitativos o cuantitativos al llevar a cabo el plan que propuso para responder la pregunta. Usa unidades de medida convencionales y no convencionales, registra los datos y los representa en organizadores.",
                "Establece relaciones que expliquen el fenómeno estudiado. Utiliza los datos cualitativos y cuantitativos que obtuvo y los compara con la respuesta que propuso, así como con información científica. Elabora sus conclusiones.",
                "Comunica las conclusiones de su indagación y lo que aprendió usando conocimientos científicos, así como el procedimiento, los logros y las dificultades que tuvo durante su desarrollo. Propone algunas mejoras. Da a conocer su indagación en forma oral o escrita."
            ],
            "5_GRADO": [
                "Formula preguntas acerca de las variables que influyen en un hecho, fenómeno u objeto natural o tecnológico. Plantea hipótesis que expresan la relación causa-efecto y determina las variables involucradas. Ejemplo: El estudiante podría preguntar: '¿Qué le sucedería a una planta si la encerramos en una caja con un huequito por donde entre la luz?'. La hipótesis podría ser: 'Las plantas puestas en oscuridad mueren rápido y se les caen las hojas porque necesitan luz para vivir'.",
                "Propone un plan que le permita observar las variables involucradas, a fin de obtener datos para comprobar sus hipótesis. Selecciona materiales, instrumentos y fuentes que le brinden información científica. Considera el tiempo para el desarrollo del plan y las medidas de seguridad necesarias. Ejemplo: Si se está indagando sobre el comportamiento de las plantas y la luz, el estudiante podría decir: 'Necesitaremos una planta en un macetero y una caja de cartón para cubrirla. Haremos un huequito en la caja, la dejaremos cubierta por 5 días y anotaremos qué sucede. Buscaremos información en libros e internet'.",
                "Obtiene datos cualitativos o cuantitativos que evidencian la relación entre las variables que utiliza para responder la pregunta. Registra los datos y los representa en diferentes organizadores. Ejemplo: Al revisar diariamente lo que sucede con la planta cubierta por una caja con un huequito, el estudiante tomará nota para identificar si el color de las hojas se mantiene, si el tallo sigue en la misma dirección o si cambió, y hará resúmenes con la información que encontró en los libros e internet.",
                "Compara los datos cualitativos o cuantitativos para probar sus hipótesis y las contrasta con información científica. Elabora sus conclusiones. Ejemplo: El estudiante podría decir: 'Nuestra hipótesis es que las plantas puestas en la oscuridad mueren rápido y se les caen las hojas'; 'Experimentando, obtuvimos estos datos: a los \\'x\\' días las hojas de la planta cambiaron de color, a los \\'y\\' días el tallo de la planta se dobló hacia la fuente de luz'; 'Según los libros, el movimiento de las plantas hacia la luz se llama fototropismo positivo y su raíz tiene fototropismo negativo'.",
                "Comunica sus conclusiones y lo que aprendió usando conocimientos científicos. Evalúa si los procedimientos seguidos en su indagación ayudaron a comprobar sus hipótesis. Menciona las dificultades que tuvo y propone mejoras. Da a conocer su indagación en forma oral o escrita. Ejemplo: El estudiante podría decir: 'Las plantas buscan las fuentes de luz y a eso se le llama fototropismo positivo, por ello, se torció el tallo hacia la fuente de luz'; 'Las plantas no mueren en la oscuridad, pero el color de sus hojas sí cambia'; 'Tendríamos que haber contado con una planta igualita, pero expuesta a la luz, para compararlas'."
            ],
            "6_GRADO": [
                "Formula preguntas acerca de las variables que influyen en un hecho, fenómeno u objeto natural o tecnológico. Plantea hipótesis que expresan la relación causa-efecto y determina las variables involucradas.",
                "Propone un plan para observar las variables del problema de indagación y controlar aquellas que pueden modificar la experimentación, con la finalidad de obtener datos para comprobar sus hipótesis. Selecciona instrumentos, materiales y herramientas, así como fuentes que le brinden información científica. Considera el tiempo para el desarrollo del plan y las medidas de seguridad necesarias.",
                "Obtiene datos cualitativos o cuantitativos que evidencian la relación entre las variables que utiliza para responder la pregunta. Organiza los datos, hace cálculos de moda, proporcionalidad directa y otros, y los representa en diferentes organizadores.",
                "Utiliza los datos cualitativos o cuantitativos para probar sus hipótesis y las contrasta con información científica. Elabora sus conclusiones.",
                "Comunica sus conclusiones y lo que aprendió usando conocimientos científicos. Evalúa si los procedimientos seguidos en su indagación ayudaron a comprobar sus hipótesis. Menciona las dificultades que tuvo y propone mejoras. Da a conocer su indagación en forma oral o escrita."
            ]
        }
    },
    "Explica el mundo físico basándose en conocimientos sobre los seres vivos, materia y energía, biodiversidad, Tierra y universo": {
        "capacidades": [
            "Comprende y usa conocimientos sobre los seres vivos, materia y energía, biodiversidad, Tierra y universo.",
            "Evalúa las implicancias del saber y del quehacer científico y tecnológico."
        ],
        "estandares": {
            "III_CICLO": (
                "Explica, con base en sus observaciones y experiencias previas, las relaciones entre: las características de los "
                "materiales con los cambios que sufren por acción de la luz, del calor y del movimiento; la estructura de los "
                "seres vivos con sus funciones y su desarrollo; la Tierra, sus componentes y movimientos con los seres que lo habitan. "
                "Opina sobre los impactos del uso de objetos tecnológicos en relación a sus necesidades y estilo de vida."
            ),
            "IV_CICLO": (
                "Explica, con base en evidencias documentadas con respaldo científico, las relaciones que establece entre: las fuentes "
                "de energía o sus manifestaciones con los tipos de cambio que producen en los materiales; entre las fuerzas con el "
                "movimiento de los cuerpos; la estructura de los sistemas vivos con sus funciones y su agrupación en especies; la radiación "
                "del sol con las zonas climáticas de la Tierra y las adaptaciones de los seres vivos. Opina sobre los impactos de diversas "
                "tecnologías en la solución de problemas relacionados a necesidades y estilos de vida colectivas."
            ),
            "V_CICLO": (
                "Explica, con base en evidencia con respaldo científico, las relaciones entre: propiedades o funciones macroscópicas "
                "de los cuerpos, materiales o seres vivos con su estructura y movimiento microscópico; la reproducción sexual con la "
                "diversidad genética; los ecosistemas con la diversidad de especies; el relieve con la actividad interna de la Tierra. "
                "Relaciona el descubrimiento científico o la innovación tecnológica con sus impactos. Justifica su posición frente a "
                "situaciones controversiales sobre el uso de la tecnología y el saber científico."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Describe las características y necesidades de los seres vivos. Ejemplo: El estudiante describe qué necesitan los seres vivos para vivir: alimentos, oxígeno, etc.",
                "Relaciona las actividades cotidianas con el uso de la energía. Ejemplo: El estudiante relaciona el uso de gas en su cocina con la cocción de sus alimentos, o el uso de las pilas con el funcionamiento de sus juguetes.",
                "Propone una clasificación de los objetos según sus características. Ejemplo: El estudiante separa objetos que absorben agua de otros que no.",
                "Describe que el suelo está formado por seres vivos y no vivos. Ejemplo: El estudiante distingue lo que hay dentro del suelo: tierra, gusanos, rocas, objetos de plástico, etc.",
                "Justifica por qué el agua, el aire y el suelo son importantes para los seres vivos.",
                "Relaciona el comportamiento de los seres vivos con los cambios de clima. Ejemplo: El estudiante da razones de por qué cuando hace frío tenemos que abrigarnos más y cuando hace calor buscamos lugares frescos.",
                "Relaciona los objetos tecnológicos con su utilidad para satisfacer las necesidades de las personas y opina sobre cómo su uso impacta en ellos. Ejemplo: El estudiante menciona que para cocinar sus alimentos, su madre usa una cocina a gas o un fogón con leña, y cómo impacta en sus vidas."
            ],
            "2_GRADO": [
                "Relaciona las partes externas de los seres vivos con sus funciones. Ejemplo: El estudiante relaciona la función de los dientes (que sirven para masticar los alimentos antes de ingerirlos) con la buena salud.",
                "Compara las semejanzas externas de los progenitores y sus descendientes durante el desarrollo. Ejemplo: El estudiante compara las características que los renacuajos toman progresivamente hasta tener la forma de sus progenitores.",
                "Describe los cambios que experimentan los objetos debido a la luz o al calor que reciben. Ejemplo: El estudiante describe las causas por las que el hielo, la mantequilla o la cera se derriten cuando se calientan o les da la luz del sol.",
                "Justifica por qué los cambios que sufren los objetos dependen de sus características. Ejemplo: El estudiante da razones de por qué, con un golpe, un vaso de vidrio se rompe; mientras que uno de cartón, solo se deforma.",
                "Utiliza modelos para explicar las relaciones entre los seres vivos y sus características. Ejemplo: El estudiante diseña un modelo para explicar los componentes de una cadena alimenticia.",
                "Describe que el ciclo día-noche influye en los seres vivos. Ejemplo: El estudiante describe las características de los animales que duermen durante el día y se mantienen despiertos por la noche.",
                "Describe que en la Tierra se encuentran masas de agua, aire y material sólido. Ejemplo: El estudiante describe las características de las lagunas, los ríos, los cerros y las rocas, y cómo el viento fuerte puede mover algunos objetos.",
                "Describe el suelo como fuente esencial de nutrientes y sustrato para muchos seres vivos. Ejemplo: El estudiante describe que las plantas necesitan el suelo para crecer y que algunos animales se alimentan de ellas.",
                "Justifica por qué hay objetos tecnológicos que transforman los productos que consume o que usa en tareas específicas, y opina cómo estos objetos cambian su vida, la de su familia o el ambiente. Ejemplo: El estudiante justifica las ventajas de usar un molino para transformar los granos de maíz o trigo en harina, a fin de que sean utilizados en diferentes productos que consume en su vida diaria."
            ],
            "3_GRADO": [
                "Describe los órganos que conforman los sistemas de plantas y animales.",
                "Compara diversas especies y reconoce semejanzas y diferencias.",
                "Clasifica los materiales de acuerdo a sus características físicas (duros, blandos, frágiles, etc.).",
                "Relaciona el desplazamiento, el cambio de dirección o la modificación de la forma de los objetos por la aplicación de fuerzas sobre ellos. Ejemplo: El estudiante relaciona la deformación que sufre una pelota con la fuerza generada sobre ella cuando alguien la presiona con la planta de los pies.",
                "Compara las diferentes manifestaciones del clima a lo largo de un año y en las diferentes zonas en la superficie terrestre. Ejemplo: El estudiante diferencia las características de la época del año en que llueve y otra en que no.",
                "Describe cómo el hábitat proporciona a los organismos recursos para satisfacer sus necesidades básicas. Ejemplo: El estudiante describe cómo se alimentan los animales en la selva.",
                "Describe las interacciones entre los seres vivos y los no vivos en su hábitat. Ejemplo: El estudiante señala que los herbívoros comen pasto, que algunos animales se alimentan de herbívoros y que las plantas necesitan del suelo para vivir.",
                "Argumenta por qué la creación de objetos tecnológicos para satisfacer necesidades requiere de personas que tienen diferentes ocupaciones o especialidades, y opina sobre cómo el uso de los productos tecnológicos cambia la vida de las personas y el ambiente. Ejemplo: El estudiante explica que la producción de alimentos en conservas demanda la producción de materia prima, envases, planta procesadora, etc., para que las personas puedan consumirlos, y opina acerca de las ventajas y desventajas de esta clase de productos, en relación a la calidad de vida y del ambiente."
            ],
            "4_GRADO": [
                "Utiliza modelos para explicar las relaciones entre los órganos y sistemas con las funciones vitales en plantas y animales. Ejemplo: El estudiante utiliza un modelo para describir cómo el sistema digestivo transforma los alimentos en nutrientes que se distribuyen, a través de la sangre, por todo el organismo.",
                "Justifica por qué los individuos se reproducen con otros de su misma especie.",
                "Describe que los objetos pueden sufrir cambios reversibles e irreversibles por acción de la energía. Ejemplo: El estudiante describe por qué un cubo de hielo se disuelve por acción del calor del ambiente y por qué puede volver a ser un cubo de hielo al colocar el líquido en un refrigerador.",
                "Relaciona los cambios en el equilibrio, la posición y la forma de los objetos por las fuerzas aplicadas sobre ellos. Ejemplo: El estudiante da razones de por qué al tirar de un elástico, este se deforma, y cuando cesa esta acción, recupera su forma inicial.",
                "Describe cómo la energía se manifiesta de diferentes formas y puede usarse para diferentes propósitos. Ejemplo: El estudiante describe cómo la energía producida en una batería para un carro de juguete se manifiesta en movimiento, sonido y luz al poner en funcionamiento todos sus componentes.",
                "Describe el rol que cumplen los seres vivos en su hábitat. Ejemplo: El estudiante señala que las plantas son productores, la liebre es un consumidor y la lombriz es un descomponedor.",
                "Argumenta por qué las plantas y los animales poseen estructuras y comportamientos adaptados a su hábitat. Ejemplo: El estudiante da razones de por qué un camaleón se mimetiza con su ambiente o por qué los cactus tienen espinas en lugar de hojas.",
                "Describe las diferentes zonas climáticas y señala que se forman por la distribución de la energía del sol sobre la Tierra y su relieve.",
                "Argumenta por qué los diversos objetos tecnológicos son creados para satisfacer necesidades personales y colectivas. Ejemplo: El estudiante da razones de por qué los rayos X son empleados por los médicos en el diagnóstico de fracturas, así como las ventajas y desventajas de su uso.",
                "Opina sobre los cambios que la tecnología ha generado en la forma de vivir de las personas y en el ambiente. Ejemplo: El estudiante explica que gracias a la refrigeradora se pueden conservar los alimentos durante más tiempo, y cómo esto impacta sobre la calidad de vida y del ambiente."
            ],
            "5_GRADO": [
                "Describe las diferencias entre la célula animal y vegetal, y explica que ambas cumplen funciones básicas. Ejemplo: El estudiante describe por qué el cuerpo de un animal es suave en comparación con una planta, en función del tipo de células que poseen.",
                "Representa las diferentes formas de reproducción de los seres vivos.",
                "Describe la materia y señala que se compone de partículas pequeñas. Ejemplo: El estudiante señala que el vapor (moléculas) que sale del agua cuando hierve es la razón por la que disminuye el volumen inicial.",
                "Describe los ecosistemas y señala que se encuentran constituidos por componentes abióticos y bióticos que se interrelacionan.",
                "Describe el carácter dinámico de la estructura externa de la Tierra.",
                "Justifica que el quehacer tecnológico progresa con el paso del tiempo como resultado del avance científico para resolver problemas.",
                "Opina cómo el uso de los objetos tecnológicos impacta en el ambiente, con base en fuentes documentadas con respaldo científico. Ejemplo: El estudiante opina sobre cómo la demanda de muebles de madera promueve el desarrollo de maquinaria maderera, así como la deforestación, y qué alternativas existen desde la ciencia y tecnología para fomentar el desarrollo sostenible de esta industria."
            ],
            "6_GRADO": [
                "Describe los organismos y señala que pueden ser unicelulares o pluricelulares y que cada célula cumple funciones básicas o especializadas. Ejemplo: El estudiante señala que las bacterias necesitan un huésped para poder cumplir sus funciones básicas.",
                "Relaciona la reproducción sexual con la diversidad dentro de una especie.",
                "Relaciona los estados de los cuerpos con las fuerzas que predominan en sus moléculas (fuerzas de repulsión y cohesión) y sus átomos.",
                "Relaciona los cambios que sufren los materiales con el reordenamiento de sus componentes constituyentes. Ejemplo: El estudiante relaciona la ceniza, el humo y el vapor del agua con la combustión de madera.",
                "Interpreta la relación entre la temperatura y el movimiento molecular en los objetos. Ejemplo: El estudiante da razones de por qué cuando se calienta un objeto metálico como el aluminio, este cambia de tamaño.",
                "Justifica por qué la diversidad de especies da estabilidad a los ecosistemas. Ejemplo: El estudiante da razones de por qué cuando disminuye la cantidad de pasto por el friaje, la población de vizcachas se reduce, y cómo esto también afecta a la población de zorros.",
                "Relaciona los cambios del relieve terrestre con la estructura dinámica interna y externa de la Tierra.",
                "Argumenta que algunos objetos tecnológicos y conocimientos científicos han ayudado a formular nuevas teorías que propiciaron el cambio en la forma de pensar y el estilo de vida de las personas. Ejemplo: El estudiante da razones de cómo el uso del telescopio dio un nuevo lugar a la Tierra en el universo y de cómo con el microscopio se originó la teoría de los gérmenes como causantes de enfermedades.",
                "Defiende su punto de vista respecto al avance científico y tecnológico, y su impacto en la sociedad y el ambiente, con base en fuentes documentadas con respaldo científico. Ejemplo: El estudiante discute sus puntos de vista acerca de si la instalación de antenas de telefonía en zonas pobladas podría afectar la salud de los seres vivos."
            ]
        }
    },
    "Diseña y construye soluciones tecnológicas para resolver problemas de su entorno": {
        "capacidades": [
            "Determina una alternativa de solución tecnológica.",
            "Diseña la alternativa de solución tecnológica.",
            "Implementa y valida la alternativa de solución tecnológica.",
            "Evalúa y comunica el funcionamiento y los impactos de su alternativa de solución tecnológica."
        ],
        "estandares": {
            "III_CICLO": (
                "Diseña y construye soluciones tecnológicas al establecer las causas de un problema tecnológico y propone alternativas "
                "de solución. Representa una, incluyendo sus partes, a través de esquemas o dibujos y describe la secuencia de pasos "
                "para implementarla, usando herramientas y materiales seleccionados. Realiza ajustes en el proceso de construcción de "
                "la solución tecnológica. Describe el procedimiento y beneficios de la solución tecnológica; evalúa su funcionamiento "
                "según los requerimientos establecidos y propone mejoras."
            ),
            "IV_CICLO": (
                "Diseña y construye soluciones tecnológicas al establecer las posibles causas que generan problemas tecnológicos; propone "
                "alternativas de solución con conocimientos científicos. Representa una de ellas, incluyendo las partes o etapas, a "
                "través de esquemas o dibujos; establece características de forma, estructura y función y explica una secuencia de "
                "pasos para implementarla usando herramientas y materiales; verifica el funcionamiento de la solución tecnológica y "
                "realiza ajustes. Explica el procedimiento, conocimiento científico aplicado y beneficios de la solución tecnológica; "
                "evalúa su funcionamiento considerando los requerimientos establecidos y propone mejoras."
            ),
            "V_CICLO": (
                "Diseña y construye soluciones tecnológicas al identificar las causas que generan problemas tecnológicos y propone "
                "alternativas de solución con base en conocimientos científicos. Representa una de ellas incluyendo sus partes o "
                "etapas, a través de esquemas o dibujos estructurados. Establece características de forma, estructura y función y explica "
                "el procedimiento, los recursos de implementación; los ejecuta usando herramientas y materiales seleccionados; "
                "verifica el funcionamiento de la solución tecnológica detectando imprecisiones y realiza ajustes para mejorarlo. "
                "Explica el procedimiento, conocimiento científico aplicado y limitaciones de la solución tecnológica. Evalúa su "
                "funcionamiento a través de pruebas considerando los requerimientos establecidos y propone mejoras. Infiere impactos de la "
                "solución tecnológica."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Selecciona un problema tecnológico de su entorno. Explica su alternativa de solución con base en conocimientos previos o prácticas locales; considera los requerimientos que deberá cumplir y los recursos disponibles para construirla. Ejemplo: El estudiante propone retirar los residuos sólidos del jardín de la institución educativa; para ello, elaborará un rastrillo, con material reciclable, a fin de evitar tocar directamente los desechos con las manos.",
                "Representa su alternativa de solución tecnológica con dibujos y textos. Describe lo que hará para construirla. Ejemplo: El estudiante dibuja su rastrillo, señala sus partes y comenta qué acciones realizará para elaborarlo.",
                "Construye la alternativa de solución tecnológica manipulando materiales, instrumentos y herramientas; cumple las normas de seguridad y considera medidas de ecoeficiencia. Usa unidades de medida no convencionales. Realiza ensayos hasta que la alternativa funcione. Ejemplo: El estudiante elabora su rastrillo utilizando botellas descartables de medio litro, un palo de escoba en desuso o una rama larga y delgada, tijeras, cordel o soga; evita hacerse daño con dichas herramientas. Utiliza el grosor de sus dedos para estimar el ancho de cada diente del rastrillo y su mano para estimar el largo. Rastrilla una parte del jardín de la institución educativa y añade o quita dientes al rastrillo, según sea necesario, hasta que funcione.",
                "Realiza pruebas para verificar el funcionamiento de su alternativa de solución tecnológica con los requerimientos establecidos. Describe cómo la construyó, su uso, beneficios y los conocimientos previos o prácticas locales aplicadas. Comenta las dificultades que tuvo. Ejemplo: El estudiante rastrilla todo el jardín de la institución educativa para comprobar la durabilidad del rastrillo y, al finalizar, estima el desgaste de cada diente con el uso de su mano, a fin de predecir cuántas veces más podría rastrillar el jardín. Explica a sus compañeros cómo elaboró su rastrillo, de qué manera se utiliza, de dónde obtuvo las ideas para hacerlo, el impacto del mismo en el manejo de residuos sólidos en la institución educativa y los problemas que tuvo en el proceso de elaboración."
            ],
            "2_GRADO": [
                "Selecciona un problema tecnológico de su entorno y describe las causas que lo generan. Explica su alternativa de solución con base en conocimientos previos o prácticas locales; toma en cuenta los requerimientos que debe cumplir y los recursos disponibles para construirla.",
                "Representa su alternativa de solución tecnológica con dibujos y textos. Describe sus partes, la secuencia de pasos para su elaboración y selecciona herramientas, instrumentos y materiales según sus propiedades físicas.",
                "Construye su alternativa de solución tecnológica manipulando materiales, instrumentos y herramientas según su utilidad; cumple las normas de seguridad y considera medidas de ecoeficiencia. Usa unidades de medida convencionales. Realiza cambios o ajustes para cumplir los requerimientos o mejorar el funcionamiento de su alternativa de solución tecnológica.",
                "Realiza pruebas para verificar el funcionamiento de su alternativa de solución tecnológica con los requerimientos establecidos. Describe cómo la construyó, su uso, beneficios y funcionamiento, así como los conocimientos previos o prácticas locales aplicadas. Comenta las dificultades que tuvo."
            ],
            "3_GRADO": [
                "Determina el problema tecnológico y las causas que lo generan. Propone alternativas de solución con base en conocimientos científicos o prácticas locales, así como los requerimientos que debe cumplir y los recursos disponibles para construirlas. Ejemplo: El estudiante propone construir un sistema de riego para el jardín de la institución educativa usando material reciclable, a fin de que disminuya el consumo de agua, basándose en el conocimiento de las técnicas de regadío y en las formas de riego de jardines, parques o chacras observadas en su localidad.",
                "Representa su alternativa de solución tecnológica con dibujos y textos; describe sus partes, la secuencia de pasos para su implementación y selecciona herramientas, instrumentos y materiales según sus propiedades físicas. Ejemplo: El estudiante realiza gráficos de su sistema de riego, lo presenta y describe cómo será construido y cómo funcionará.",
                "Construye su alternativa de solución tecnológica manipulando materiales, instrumentos y herramientas según su utilidad; cumple las normas de seguridad y considera medidas de ecoeficiencia. Usa unidades de medida convencionales. Realiza cambios o ajustes para cumplir los requerimientos o mejorar el funcionamiento de su alternativa de solución tecnológica. Ejemplo: El estudiante construye su sistema de riego usando material reciclable (botellas descartables y mangueras) y herramientas (tijeras, cinta adhesiva, punzones, etc.), siguiendo las recomendaciones para su seguridad y la limpieza de la mesa de trabajo. Riega el jardín de la institución educativa utilizando el sistema de riego y realiza las modificaciones necesarias hasta que funcione y cumpla con los requerimientos establecidos.",
                "Realiza pruebas para verificar si la solución tecnológica cumple con los requerimientos establecidos. Explica cómo construyó su solución tecnológica, su funcionamiento, el conocimiento científico o prácticas locales aplicadas y las dificultades superadas. Ejemplo: El estudiante pone en funcionamiento su sistema de riego por dos meses (previamente, determina cuánto volumen de agua se usaba para regar el área correspondiente al jardín y realiza una lectura inicial del recibo de agua). Después de ese tiempo, compara los recibos de agua e indica si el consumo disminuyó. Finalmente, menciona qué materiales y herramientas utilizó para construir su sistema de riego, si fue fácil, de dónde obtuvo las ideas para su construcción, así como qué le gusto más y qué no le gustó."
            ],
            "4_GRADO": [
                "Determina el problema tecnológico y las causas que lo generan. Propone alternativas de solución con base en conocimientos científicos o prácticas locales, así como los requerimientos que debe cumplir y los recursos disponibles para construirlas.",
                "Representa su alternativa de solución tecnológica con dibujos y textos; describe sus partes o etapas, la secuencia de pasos, sus características, forma, estructura y función. Selecciona herramientas, instrumentos y materiales según sus propiedades físicas.",
                "Construye su alternativa de solución tecnológica manipulando materiales, instrumentos y herramientas según sus funciones; cumple las normas de seguridad y medidas de ecoeficiencia. Usa unidades de medida convencionales. Realiza cambios o ajustes para cumplir los requerimientos o mejorar el funcionamiento de su alternativa de solución tecnológica.",
                "Realiza pruebas para verificar si la solución tecnológica cumple con los requerimientos establecidos. Explica cómo construyó su alternativa de solución tecnológica, su funcionamiento, el conocimiento científico o las prácticas locales aplicadas, las dificultades superadas y los beneficios e inconvenientes de su uso."
            ],
            "5_GRADO": [
                "Determina el problema tecnológico, las causas que lo generan y su alternativa de solución, con base en conocimientos científicos o prácticas locales; asimismo, los requerimientos que debe cumplir y los recursos disponibles para construirla. Ejemplo: Ante la necesidad de conservar el refrigerio caliente, el estudiante propone elaborar un envase que permita mantener las bebidas calientes por 2 horas. Considera los principios de conservación del calor en los cuerpos y las formas de conservación del calor en los alimentos utilizados por sus familiares o la comunidad. Usa materiales reciclables.",
                "Representa su alternativa de solución tecnológica con dibujos y textos; describe sus partes o etapas, la secuencia de pasos, características de forma, estructura y función. Selecciona herramientas, instrumentos y materiales según sus propiedades físicas. Considera el tiempo para desarrollarla y las medidas de seguridad necesarias, así como medidas de ecoeficiencia. Ejemplo: El estudiante dibuja el envase para mantener las bebidas calientes; describe las partes que tendrá y sus características: tamaño, forma, material del que estará hecho; expone cómo lo elaborará y hace un listado de las herramientas que utilizará (papel de aluminio, poliestireno expandido, lana, botellas descartables, pegamento, tijeras, etc.).",
                "Construye su alternativa de solución tecnológica manipulando los materiales, instrumentos y herramientas según sus funciones; cumple las normas de seguridad. Usa unidades de medida convencionales. Verifica el funcionamiento de cada parte o etapa de la solución tecnológica y realiza cambios o ajustes para cumplir los requerimientos establecidos. Ejemplo: El estudiante elabora el envase para mantener las bebidas calientes utilizando botellas de plástico descartables, papel de aluminio, poliestireno, lana, pegamento, tijeras, etc.; determina el tamaño del envase en centímetros y su capacidad en mililitros; maneja las herramientas e instrumentos con los cuidados del caso. Pone a prueba el envase elaborado y lo compara con otro diferente de las mismas dimensiones, vierte agua caliente, mide la temperatura inicial del líquido de ambos envases y los cierra. Vuelve a tomar la temperatura después de 30 minutos y compara las medidas encontradas, para determinar si el envase elaborado conserva mejor el agua caliente que el otro. Si la diferencia de la temperatura de los líquidos de los dos envases no es amplia, realizará los ajustes necesarios, como aumentar las capas de papel aluminio o lana que envuelven el envase elaborado.",
                "Realiza pruebas para verificar si la solución tecnológica cumple con los requerimientos establecidos. Explica cómo construyó su solución tecnológica, su funcionamiento, el conocimiento científico o las prácticas locales aplicadas, las dificultades superadas y los beneficios e inconvenientes de su uso. Ejemplo: El estudiante pone a prueba nuevamente el envase elaborado. Vierte agua caliente, toma la temperatura inicial y después de 2 horas toma la temperatura final. Si nota que la temperatura inicial del agua solo ha descendido en un 50%, determina que su prototipo cumple el requerimiento establecido. Demuestra a sus compañeros el funcionamiento de su envase mientras comenta cómo lo hizo y explica los inconvenientes que tuvo que superar hasta llegar a la versión final."
            ],
            "6_GRADO": [
                "Determina el problema tecnológico, las causas que lo generan y su alternativa de solución, con base en conocimientos científicos o prácticas locales; asimismo, los requerimientos que debe cumplir y los recursos disponibles para construirla.",
                "Representa su alternativa de solución tecnológica con dibujos y textos; describe sus partes o etapas, la secuencia de pasos y las características: dimensiones, forma, estructura y función. Selecciona herramientas, instrumentos y materiales según sus propiedades físicas; incluye los recursos a utilizar y los posibles costos. Considera el tiempo para desarrollarla y las medidas de seguridad necesarias.",
                "Construye su alternativa de solución tecnológica manipulando los materiales, instrumentos y herramientas según sus funciones; cumple las normas de seguridad y considera medidas de ecoeficiencia. Usa unidades de medida convencionales. Verifica el funcionamiento de cada parte o etapa de la solución tecnológica; detecta imprecisiones en las dimensiones y procedimientos, o errores en la selección de materiales; y realiza ajustes o cambios necesarios para cumplir los requerimientos establecidos.",
                "Realiza pruebas para verificar si la solución tecnológica cumple con los requerimientos establecidos. Explica cómo construyó su solución tecnológica, su funcionamiento, el conocimiento científico o las prácticas locales aplicadas, las dificultades superadas y los beneficios e inconvenientes de su uso. Infiere posibles impactos positivos o negativos de la solución tecnológica en diferentes contextos."
            ]
        }
    }
},

"Educación  Religiosa": {
    "Construye su identidad como persona humana, amada por Dios, digna, libre y trascendente, comprendiendo la doctrina de su propia religión, abierto al diálogo con las que le son cercanas": {
        "capacidades": [
            "Conoce a Dios y asume su identidad religiosa y espiritual como persona digna, libre y trascendente.",
            "Cultiva y valora las manifestaciones religiosas de su entorno argumentando su fe de manera comprensible y respetuosa."
        ],
        "estandares": {
            "III_CICLO": (
                "Descubre el amor de Dios en la creación y lo relaciona con el amor que recibe de las personas que lo rodean. "
                "Explica la presencia de Dios en el Plan de Salvación y la relación que Él establece con el ser humano. Convive de "
                "manera fraterna con el prójimo respetando las diferentes expresiones religiosas. Asume las consecuencias de sus "
                "acciones con responsabilidad, comprometiéndose a ser mejor persona, a ejemplo de Jesucristo."
            ),
            "IV_CICLO": (
                "Describe el amor de Dios presente en la creación y en el Plan de Salvación. Construye su identidad como hijo de Dios "
                "desde el mensaje de Jesús presente en el Evangelio. Participa en la Iglesia como comunidad de fe y de amor, respetando "
                "la dignidad humana y las diversas manifestaciones religiosas. Fomenta una convivencia armónica basada en el diálogo, "
                "el respeto, la tolerancia y el amor fraterno."
            ),
            "V_CICLO": (
                "Comprende el amor de Dios desde la creación respetando la dignidad y la libertad de la persona humana. Explica la "
                "acción de Dios presente en el Plan de Salvación. Demuestra su amor a Dios y al prójimo participando en su comunidad "
                "y realizando obras de caridad que le ayudan en su crecimiento personal y espiritual. Fomenta una convivencia cristiana "
                "basada en el diálogo, el respeto, la tolerancia y el amor fraterno fortaleciendo su identidad como hijo de Dios."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Identifica que Dios manifiesta su amor en la Creación y lo relaciona con el amor que recibe de sus padres, docentes y amigos.",
                "Comprende los principales hechos de la Historia de la Salvación y los relaciona con su familia y su institución educativa.",
                "Se relaciona con su prójimo de manera fraterna y respeta las expresiones de fe de los demás.",
                "Reconoce lo bueno y lo malo de sus acciones, y asume actitudes de cambio para imitar a Jesús."
            ],
            "2_GRADO": [
                "Descubre que Dios nos creó, por amor, a su imagen y semejanza, y valora sus características personales como hijo de Dios.",
                "Explica los principales hechos de la Historia de la Salvación y los relaciona con su entorno.",
                "Establece relaciones fraternas y respetuosas con los demás en diferentes escenarios, y participa en celebraciones religiosas de su comunidad.",
                "Discrimina lo bueno y lo malo de sus acciones, y asume actitudes de cambio y compromiso para imitar a Jesús."
            ],
            "3_GRADO": [
                "Identifica la acción de Dios en diversos acontecimientos de la Historia de la Salvación.",
                "Conoce a Dios Padre, que se manifiesta en las Sagradas Escrituras, y acepta el mensaje que le da a conocer para vivir en armonía con Él y con los demás.",
                "Expresa su fe al participar en su comunidad y respeta a sus compañeros y a los que profesan diferentes credos.",
                "Se compromete a una convivencia cristiana basada en el diálogo y el respeto mutuo."
            ],
            "4_GRADO": [
                "Relaciona sus experiencias de vida con los acontecimientos de la Historia de la Salvación como manifestación del amor de Dios.",
                "Conoce a Dios Padre y se reconoce como hijo amado según las Sagradas Escrituras para vivir en armonía con su entorno.",
                "Participa en la Iglesia como comunidad de fe y amor, y respeta la integridad de las personas y las diversas manifestaciones religiosas.",
                "Promueve la convivencia cristiana basada en el diálogo, el respeto, la comprensión y el amor fraterno."
            ],
            "5_GRADO": [
                "Explica el amor de Dios presente en la Creación y se compromete a cuidarla.",
                "Reconoce el amor de Dios presente en la Historia de la Salvación respetándose a sí mismo y a los demás.",
                "Expresa su amor a Dios y al prójimo realizando acciones que fomentan el respeto por la vida humana.",
                "Promueve la convivencia armónica en su entorno más cercano y fortalece su identidad como hijo de Dios."
            ],
            "6_GRADO": [
                "Comprende el amor de Dios desde el cuidado de la Creación y respeta la dignidad y la libertad de la persona humana.",
                "Comprende la acción de Dios revelada en la Historia de la Salvación y en su propia historia, que respeta la dignidad y la libertad de la persona humana.",
                "Demuestra su amor a Dios atendiendo las necesidades del prójimo y fortalece así su crecimiento personal y espiritual.",
                "Fomenta en toda ocasión y lugar una convivencia cristiana basada en el diálogo, el respeto, la comprensión y el amor fraterno."
            ]
        }
    },
    "Asume la experiencia del encuentro personal y comunitario con Dios en su proyecto de vida en coherencia con su creencia religiosa": {
        "capacidades": [
            "Transforma su entorno desde el encuentro personal y comunitario con Dios y desde la fe que profesa.",
            "Actúa coherentemente en razón de su fe según los principios de su conciencia moral en situaciones concretas de la vida."
        ],
        "estandares": {
            "III_CICLO": (
                "Expresa coherencia en sus acciones cotidianas descubriendo el amor de Dios. Comprende su dimensión religiosa, "
                "espiritual y trascendente que le permite poner en practicar actitudes evangélicas. Interioriza la presencia de Dios en su "
                "entorno más cercano desarrollando virtudes evangélicas. Asume actitudes de agradecimiento a Dios respetando lo creado."
            ),
            "IV_CICLO": (
                "Expresa coherencia entre lo que cree, dice y hace en su diario vivir a la luz de las enseñanzas bíblicas y de los santos. "
                "Comprende su dimensión religiosa, espiritual y trascendente que le permita establecer propósitos de cambio a la luz del Evangelio. "
                "Interioriza la presencia de Dios en su vida personal y en su entorno más cercano, celebrando su fe con gratitud. Asume su rol "
                "protagónico respetando y cuidando lo creado."
            ),
            "V_CICLO": (
                "Expresa coherencia entre lo que cree, dice y hace en su proyecto de vida personal, a la luz del mensaje bíblico. Comprende "
                "su dimensión espiritual y religiosa que le permita cooperar en la transformación de sí mismo y de su entorno a la luz del "
                "Evangelio. Reflexiona el encuentro personal y comunitario con Dios en diversos contextos, con acciones orientadas a la "
                "construcción de una comunidad de fe guiada por las enseñanzas de Jesucristo. Asume las enseñanzas de Jesucristo y de la Iglesia "
                "desempeñando su rol protagónico en la transformación de la sociedad."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Descubre el amor de Dios con diversas acciones en su familia, institución educativa y entorno.",
                "Muestra en forma oral, gráfica y corporal el amor a su amigo Jesús.",
                "Practica el silencio y la oración como medios para comunicarse con Dios.",
                "Agradece a Dios por la Creación y por todos los dones recibidos."
            ],
            "2_GRADO": [
                "Expresa el amor de Dios con diversas acciones, siguiendo el ejemplo de su amigo Jesús, en su familia, institución educativa y entorno.",
                "Expresa en forma oral, gráfica, escrita y corporal el amor a su amigo Jesús.",
                "Practica el silencio y la oración en celebraciones de fe para comunicarse con Dios.",
                "Agradece a Dios por la naturaleza, la vida y los dones recibidos asumiendo un compromiso de cuidado y respeto."
            ],
            "3_GRADO": [
                "Muestra su fe mediante acciones concretas en la convivencia cotidiana, en coherencia con relatos bíblicos y la vida de los santos.",
                "Descubre el amor de Dios proponiendo acciones para mejorar la relación con su familia y la institución educativa.",
                "Participa en momentos de encuentro con Dios, personal y comunitariamente, y celebra su fe con gratitud.",
                "Participa responsablemente en el cuidado de sí mismo, del prójimo y de la naturaleza como creación de Dios."
            ],
            "4_GRADO": [
                "Expresa su fe mediante acciones concretas en la convivencia diaria; para ello, aplica las enseñanzas bíblicas y de los santos.",
                "Reconoce el amor de Dios asumiendo acciones para mejorar la relación con su familia, institución educativa y comunidad.",
                "Interioriza la acción de Dios en su vida personal y en su entorno, y celebra su fe con confianza y gratitud.",
                "Participa activamente y motiva a los demás en el respeto y cuidado de sí mismos, del prójimo y de la naturaleza como creación de Dios."
            ],
            "5_GRADO": [
                "Relaciona el amor de Dios con sus experiencias de vida, para actuar con coherencia.",
                "Acepta las enseñanzas de Jesucristo, para asumir cambios de comportamiento al interactuar con los demás.",
                "Participa en espacios de encuentro personal y comunitario con Dios y fortalece así su fe como miembro activo de su familia, Iglesia y comunidad.",
                "Participa proactivamente en acciones de cambio a imagen de Jesucristo, para alcanzar una convivencia justa y fraterna con los demás."
            ],
            "6_GRADO": [
                "Expresa el amor de Dios desde sus vivencias, coherentes con su fe, en su entorno familiar y comunitario.",
                "Reconoce que las enseñanzas de Jesucristo le permiten desarrollar actitudes de cambio a nivel personal y comunitario.",
                "Cultiva el encuentro personal y comunitario con Dios mediante la búsqueda de espacios de oración y reflexión que lo ayuden a fortalecer su fe como miembro activo de su familia, Iglesia y comunidad desde las enseñanzas de Jesucristo.",
                "Actúa con liderazgo realizando y proponiendo acciones a imagen de Jesucristo, para alcanzar una convivencia justa, fraterna y solidaria con los demás."
            ]
        }
    }
},

"Educación física" : {
    "Se desenvuelve de manera autónoma a través de su motricidad": {
        "capacidades": [
            "Comprende su cuerpo.",
            "Se expresa corporalmente."
        ],
        "estandares": {
            "III_CICLO": (
                "Se desenvuelve de manera autónoma a través de su motricidad cuando comprende cómo usar su cuerpo "
                "en las diferentes acciones que realiza utilizando su lado dominante y realiza movimientos coordinados "
                "que le ayudan a sentirse seguro en la práctica de actividades físicas. Se orienta espacialmente en relación "
                "a sí mismo y a otros puntos de referencia. Se expresa corporalmente con sus pares utilizando el ritmo, "
                "gestos y movimientos como recursos para comunicar."
            ),
            "IV_CICLO": (
                "Se desenvuelve de manera autónoma a través de su motricidad cuando comprende cómo usar su cuerpo "
                "explorando la alternancia de sus lados corporales de acuerdo a su utilidad y ajustando la posición del cuerpo "
                "en el espacio y en el tiempo en diferentes etapas de las acciones motrices, con una actitud positiva y una "
                "voluntad de experimentar situaciones diversas. Experimenta nuevas posibilidades expresivas de su cuerpo y "
                "las utiliza para relacionarse y comunicar ideas, emociones, sentimientos, pensamientos."
            ),
            "V_CICLO": (
                "Se desenvuelve de manera autónoma a través de su motricidad cuando acepta sus posibilidades y "
                "limitaciones según su desarrollo e imagen corporal. Realiza secuencias de movimientos coordinados aplicando "
                "la alternancia de sus lados corporales de acuerdo a su utilidad. Produce con sus pares secuencias de "
                "movimientos corporales, expresivos o rítmicos en relación a una intención."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Explora de manera autónoma las posibilidades de su cuerpo en diferentes acciones para mejorar sus movimientos (saltar, correr, lanzar) al mantener y/o recuperar el equilibrio en el espacio y con los objetos, cuando utiliza conscientemente distintas bases de sustentación; así, conoce en sí mismo su lado dominante.",
                "Se orienta en un espacio y tiempo determinados, reconociendo su lado izquierdo y derecho, y a través de las nociones 'arriba-abajo', 'dentro-fuera', 'cerca-lejos', con relación a sí mismo y de acuerdo a sus intereses y necesidades.",
                "Explora nuevos movimientos y gestos para representar objetos, personajes, estados de ánimo y ritmos sencillos de distintos orígenes: de la naturaleza, del propio cuerpo, de la música, etc.",
                "Se expresa motrizmente para comunicar sus emociones (miedo, angustia, alegría, placer, torpeza, inhibición, rabia, entre otras) y representa en el juego acciones cotidianas de su familia y de la comunidad; así, afirma su identidad personal."
            ],
            "2_GRADO": [
                "Explora de manera autónoma sus posibilidades de movimiento al realizar con seguridad y confianza habilidades motrices básicas, mediante movimientos coordinados según sus intereses, necesidades y posibilidades.",
                "Se orienta en el espacio y tiempo con relación a sí mismo y a otros puntos de referencia; reconoce sus posibilidades de equilibrio con diferentes bases de sustentación en acciones lúdicas.",
                "Resuelve situaciones motrices al utilizar su lenguaje corporal (gesto, contacto visual, actitud corporal, apariencia, etc.), verbal y sonoro, que lo ayudan a sentirse seguro, confiado y aceptado.",
                "Utiliza su cuerpo y el movimiento para expresar ideas y emociones en la práctica de actividades lúdicas con diferentes tipos de ritmos y música, a fin de expresarse corporalmente y mediante el uso de diversos elementos."
            ],
            "3_GRADO": [
                "Reconoce la izquierda y la derecha con relación a objetos y a sus pares, para mejorar sus posibilidades de movimiento en diferentes acciones lúdicas.",
                "Se orienta en un espacio y tiempo determinados, con relación a sí mismo, a los objetos y a sus compañeros; coordina sus movimientos en situaciones lúdicas y regula su equilibrio al variar la base de sustentación y la altura de la superficie de apoyo, de esta manera, afianza sus habilidades motrices básicas.",
                "Resuelve situaciones motrices al utilizar su lenguaje corporal (gestos, contacto visual, actitud corporal, apariencia, etc.), verbal y sonoro para comunicar actitudes, sensaciones, estados de ánimo y acciones que le posibilitan comunicarse mejor con los otros y disfrutar de las actividades lúdicas.",
                "Vivencia el ritmo y se apropia de secuencias rítmicas corporales en situaciones de juego para expresarse corporalmente a través de la música."
            ],
            "4_GRADO": [
                "Regula la posición del cuerpo en situaciones de equilibrio, con modificación del espacio, teniendo como referencia la trayectoria de objetos, los otros y sus propios desplazamientos, para afianzar sus habilidades motrices básicas.",
                "Alterna sus lados corporales de acuerdo a su utilidad y/o necesidad y se orienta en el espacio y en el tiempo, con relación a sí mismo y a otros puntos de referencia en actividades lúdicas y predeportivas.",
                "Utiliza su cuerpo (posturas, gestos y mímica) y diferentes movimientos para expresar formas, ideas, emociones, sentimientos y pensamientos en la actividad física.",
                "Utiliza lenguaje corporal para expresar su forma particular de moverse, creando secuencias sencillas de movimientos relacionados con el ritmo, la música de su cultura y la historia de su región."
            ],
            "5_GRADO": [
                "Aplica la alternancia de sus lados corporales de acuerdo a su preferencia, utilidad y/o necesidad, y anticipa las acciones motrices a realizar en un espacio y tiempo, para mejorar las posibilidades de respuesta en una actividad física.",
                "Explora y regula su cuerpo para dar respuesta a las situaciones motrices en contextos lúdicos y predeportivos; así, pone en práctica las habilidades motrices relacionadas con la carrera, el salto y los lanzamientos.",
                "Crea movimientos y desplazamientos rítmicos e incorpora las particularidades de su lenguaje corporal teniendo como base la música de su región, al asumir diferentes roles en la práctica de actividad física.",
                "Valora en sí mismo y en sus pares nuevas formas de movimiento y gestos corporales; de esta manera, acepta la existencia de nuevas formas de movimiento y expresión para comunicar ideas y emociones en diferentes situaciones motrices."
            ],
            "6_GRADO": [
                "Aplica la alternancia de sus lados corporales de acuerdo a su preferencia, utilidad y/o necesidad, y anticipa las acciones motrices a realizar en un espacio y tiempo, para mejorar las posibilidades de respuesta en una actividad física.",
                "Regula su cuerpo para dar respuesta a las situaciones motrices en contextos lúdicos, predeportivos, etc.; de este modo, afianza las habilidades motrices específicas relacionadas con la carrera, el salto y los lanzamientos.",
                "Expresa su forma particular de moverse, al asumir y adjudicar diferentes roles en la práctica de actividad física, aplicando su lenguaje corporal.",
                "Crea con sus pares una secuencia de movimientos corporales, expresivos y/o rítmicos, de manera programada y estructurada; así, se expresa de diferentes formas y con diversos recursos, a través del cuerpo y el movimiento, para comunicar ideas y emociones."
            ]
        }
    },
    "Asume una vida saludable": {
        "capacidades": [
            "Comprende las relaciones entre la actividad física, alimentación, postura e higiene personal y del ambiente, y la salud.",
            "Incorpora prácticas que mejoran su calidad de vida."
        ],
        "estandares": {
            "III_CICLO": (
                "Asume una vida saludable cuando diferencia los alimentos saludables de su dieta personal y familiar, "
                "los momentos adecuados para ingerirlos y las posturas que lo ayudan al buen desempeño en la práctica de "
                "actividades físicas, recreativas y de la vida cotidiana, reconociendo la importancia del autocuidado. "
                "Participa regularmente en la práctica de actividades lúdicas identificando su ritmo cardiaco, respiración "
                "y sudoración; utiliza prácticas de activación corporal y psicológica antes de la actividad lúdica."
            ),
            "IV_CICLO": (
                "Asume una vida saludable cuando diferencia los alimentos de su dieta personal, familiar y de su "
                "región que son saludables de los que no lo son. Previene riesgos relacionados con la postura e higiene "
                "conociendo aquellas que favorecen y no favorecen su salud e identifica su fuerza, resistencia y velocidad "
                "en la práctica de actividades lúdicas. Adapta su esfuerzo en la práctica de actividad física de acuerdo a "
                "las características de la actividad y a sus posibilidades, aplicando conocimientos relacionados con el ritmo "
                "cardiaco, la respiración y la sudoración. Realiza prácticas de activación corporal y psicológica, e incorpora "
                "el autocuidado relacionado con los ritmos de actividad y descanso para mejorar el funcionamiento de su organismo."
            ),
            "V_CICLO": (
                "Asume una vida saludable cuando utiliza instrumentos que miden la aptitud física y estado nutricional "
                "e interpreta la información de los resultados obtenidos para mejorar su calidad de vida. Replantea sus hábitos "
                "saludables, higiénicos y alimenticios tomando en cuenta los cambios físicos propios de la edad, evita la realización "
                "de ejercicios y posturas contraindicadas para la salud en la práctica de actividad física. Incorpora prácticas "
                "saludables para su organismo consumiendo alimentos adecuados a las características personales y evitando el consumo "
                "de drogas. Propone ejercicios de activación y relajación antes, durante y después de la práctica y participa en "
                "actividad física de distinta intensidad regulando su esfuerzo."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Describe los alimentos de su dieta familiar y las posturas que son beneficiosas para su salud en la vida cotidiana y en la práctica de actividades lúdicas.",
                "Regula su esfuerzo al participar en actividades lúdicas e identifica en sí mismo y en otros la diferencia entre inspiración y espiración, en reposo y movimiento, en las actividades lúdicas.",
                "Realiza con autonomía prácticas de cuidado personal al asearse, al vestirse, al adoptar posturas adecuadas en la práctica de actividades lúdicas y de la vida cotidiana. Ejemplo: El estudiante usa diversos medios de protección frente a la radiación solar.",
                "Busca satisfacer sus necesidades corporales cuando tiene sed y resuelve las dificultades que le producen el cansancio, la incomodidad y la inactividad; evidencia su bienestar al realizar actividades lúdicas y se siente bien consigo mismo, con los otros y con su entorno."
            ],
            "2_GRADO": [
                "Explica la importancia de la activación corporal (calentamiento) y psicológica (atención, concentración y motivación) antes de la actividad lúdica, e identifica los signos y síntomas relacionados con el ritmo cardiaco, la respiración agitada y la sudoración, que aparecen en el organismo al practicar actividades lúdicas.",
                "Diferencia los alimentos saludables y nutritivos que forman parte de su dieta personal y familiar, y los momentos adecuados para ingerirlos; explica la importancia de hidratarse; conoce las posturas adecuadas en la práctica de actividad física y en la vida cotidiana, que le permiten mayor seguridad.",
                "Incorpora prácticas de cuidado al asearse y vestirse; adopta posturas adecuadas en la práctica de actividades lúdicas y en la vida cotidiana, que le permiten la participación en el juego sin afectar su desempeño.",
                "Regula su esfuerzo en la práctica de actividades lúdicas y reconoce la importancia del autocuidado para prevenir enfermedades."
            ],
            "3_GRADO": [
                "Explica la importancia de la activación corporal (calentamiento) y psicológica (atención, concentración y motivación), que lo ayuda a estar predispuesto a la actividad.",
                "Practica diferentes actividades lúdicas adaptando su esfuerzo y aplicando los conocimientos de los beneficios de la práctica de actividad física y de la salud relacionados con el ritmo cardiaco, la respiración y la sudoración.",
                "Incorpora el autocuidado relacionado con los ritmos de actividad-descanso, para mejorar el funcionamiento de su organismo.",
                "Identifica los alimentos propios de su región que forman parte de su dieta personal y familiar, y los clasifica en saludables o no, de acuerdo a la actividad física que realiza. Reconoce aquellos que son amigables con el ambiente (por el uso que se hacen de los recursos naturales, el empaquetado, etc.)."
            ],
            "4_GRADO": [
                "Selecciona actividades para la activación corporal (calentamiento) y psicológica (atención, concentración y motivación) antes de la actividad, e identifica en sí mismo las variaciones en la frecuencia cardiaca y respiratoria con relación a los diferentes niveles de esfuerzo en la práctica de actividades lúdicas.",
                "Selecciona e incorpora en su dieta personal y familiar los alimentos nutritivos y energéticos de la región que contribuyen a su bienestar.",
                "Incorpora el autocuidado relacionado con los ritmos de actividad-descanso, hidratación y exposición a los rayos solares, para mejorar el funcionamiento de su organismo, y sustenta las razones de su importancia.",
                "Adopta posturas adecuadas para prevenir problemas musculares y óseos e incorpora el autocuidado relacionado con los ritmos de actividad-descanso para mejorar el funcionamiento de su organismo y prevenir enfermedades."
            ],
            "5_GRADO": [
                "Explica las condiciones que favorecen la aptitud física (Índice de Masa Corporal - IMC, consumo de alimentos favorables, cantidad y proporción necesarias) y las pruebas que la miden (resistencia, velocidad, flexibilidad y fuerza) para mejorar la calidad de vida, con relación a sus características personales.",
                "Adapta sus prácticas de higiene a los cambios físicos propios de la edad; describe las prácticas alimenticias beneficiosas y perjudiciales para el organismo y el ambiente, y analiza la importancia de la alimentación con relación a su IMC.",
                "Describe posturas y ejercicios contraindicados para la salud en la práctica de actividad física.",
                "Realiza actividades de activación corporal, psicológica y de recuperación antes, durante y después de la práctica de actividad física; de esta manera, aplica los beneficios relacionados con la salud y planifica dietas saludables adaptadas a su edad y sus recursos."
            ],
            "6_GRADO": [
                "Utiliza diferentes métodos de evaluación para determinar la aptitud física; asimismo, selecciona los que mejor se adecúen a sus posibilidades y utiliza la información que obtiene en beneficio de su salud.",
                "Explica la relación entre los cambios físicos propios de la edad y la repercusión en la higiene, en la práctica de actividad física y en actividades de la vida cotidiana; practica actividad física y explica la importancia que tiene en su vida cotidiana.",
                "Realiza actividad física y evita posturas y ejercicios contraindicados que perjudican su salud.",
                "Muestra hábitos saludables y evita hábitos perjudiciales para su organismo, como el consumo de comida rápida, de alcohol, de tabaco, de drogas, desórdenes alimenticios, entre otros; proporciona el fundamento respectivo y desarrolla dietas saludables.",
                "Explica la importancia de la vacunación y sus consecuencias en la salud."
            ]
        }
    },
    "Interactúa a través de sus habilidades sociomotrices": {
        "capacidades": [
            "Se relaciona utilizando sus habilidades sociomotrices.",
            "Crea y aplica estrategias y tácticas de juego."
        ],
        "estandares": {
            "III_CICLO": (
                "Interactúa a través de sus habilidades sociomotrices al aceptar al otro como compañero de juego "
                "y busca el consenso sobre la manera de jugar para lograr el bienestar común y muestra una actitud de "
                "respeto evitando juegos violentos y humillantes; expresa su posición ante un conflicto con intención de "
                "resolverlo y escucha la posición de sus compañeros en los diferentes tipos de juegos. Resuelve "
                "situaciones motrices a través de estrategias colectivas y participa en la construcción de reglas de juego "
                "adaptadas a la situación y al entorno, para lograr un objetivo común en la práctica de actividades lúdicas."
            ),
            "IV_CICLO": (
                "Interactúa a través de sus habilidades sociomotrices al tomar acuerdos sobre la manera de jugar "
                "y los posibles cambios o conflictos que se den y propone adaptaciones o modificaciones para favorecer "
                "la inclusión de sus compañeros en actividades lúdicas, aceptando al oponente como compañero de juego. "
                "Adapta la estrategia de juego anticipando las intenciones de sus compañeros y oponentes para cumplir con los "
                "objetivos planteados. Propone reglas y las modifica de acuerdo a las necesidades del contexto y los "
                "intereses del grupo en la práctica de actividades físicas."
            ),
            "V_CICLO": (
                "Interactúa a través de sus habilidades sociomotrices proactivamente con un sentido de cooperación "
                "teniendo en cuenta las adaptaciones o modificaciones propuestas por el grupo en diferentes actividades físicas. "
                "Hace uso de estrategias de cooperación y oposición seleccionando los diferentes elementos técnicos y tácticos "
                "que se pueden dar en la práctica de actividades lúdicas y predeportivas, para resolver la situación de juego "
                "que le dé un mejor resultado y que responda a las variaciones que se presentan en el entorno."
            )
        },
        "desempenos": {
            "1_GRADO": [
                "Asume roles y funciones de manera individual y dentro de un grupo; interactúa de forma espontánea en actividades lúdicas y disfruta de la compañía de sus pares para sentirse parte del grupo.",
                "Participa en juegos cooperativos y de oposición en parejas y pequeños grupos; acepta al oponente como compañero de juego y las formas diferentes de jugar.",
                "Propone soluciones a situaciones motrices y lúdicas, y llega a acuerdos con sus pares a fin de cumplir con los objetivos que surjan; respeta las reglas de juego propuestas (por ellos mismos, por el maestro o por las condiciones del entorno) en diferentes actividades lúdicas."
            ],
            "2_GRADO": [
                "Participa en juegos cooperativos y de oposición en parejas y pequeños grupos; acepta al oponente como compañero de juego y llega a consensos sobre la manera de jugar.",
                "Muestra una actitud de respeto en la práctica de actividades lúdicas y evita juegos bruscos, amenazas o apodos; acepta la participación de todos sus compañeros.",
                "Resuelve de manera compartida situaciones producidas en los diferentes tipos de juegos (tradicionales, autóctonos, etc.) y adecúa las reglas para la inclusión de sus pares y el entorno, con el fin de lograr un desarrollo eficaz de la actividad."
            ],
            "3_GRADO": [
                "Propone cambios en las condiciones de juego, si fuera necesario, para posibilitar la inclusión de sus pares; así, promueve el respeto y la participación, y busca un sentido de pertenencia al grupo en la práctica de diferentes actividades físicas.",
                "Participa en juegos cooperativos y de oposición en parejas, pequeños y grandes grupos; acepta al oponente como compañero de juego y arriba a consensos sobre la manera de jugar y los posibles cambios que puedan producirse.",
                "Genera estrategias colectivas en las actividades lúdicas según el rol de sus compañeros y el suyo propio, a partir de los resultados en el juego."
            ],
            "4_GRADO": [
                "Propone normas y reglas en las actividades lúdicas y las modifica de acuerdo a las necesidades, el contexto y los intereses, con adaptaciones o modificaciones propuestas por el grupo, para favorecer la inclusión; muestra una actitud responsable y de respeto por el cumplimiento de los acuerdos establecidos.",
                "Propone actividades lúdicas, como juegos populares y/o tradicionales, con adaptaciones o modificaciones propuestas por el grupo; acepta al oponente como compañero de juego y llega a consensos sobre la manera de jugar y los posibles cambios que puedan producirse.",
                "Propone reglas y las modifica de acuerdo a las necesidades; adapta la estrategia de juego cuando prevé las intenciones de sus compañeros de equipo y oponentes, para cumplir con los objetivos planteados."
            ],
            "5_GRADO": [
                "Emplea la resolución reflexiva y el diálogo como herramientas para solucionar problemas o conflictos surgidos con sus pares durante la práctica de actividades lúdicas y predeportivas diversas.",
                "Realiza actividades lúdicas en las que interactúa con sus compañeros y oponentes como compañeros de juego; respeta las diferencias personales y asume roles y cambio de roles.",
                "Propone, junto con sus pares, soluciones estratégicas oportunas, y toma en cuenta los aportes y las características de cada integrante del grupo al practicar juegos tradicionales, populares, autóctonos, predeportivos y en la naturaleza."
            ],
            "6_GRADO": [
                "Participa en actividades físicas en la naturaleza, eventos predeportivos, juegos populares, entre otros, y toma decisiones en favor del grupo aunque vaya en contra de sus intereses personales, con un sentido solidario y de cooperación.",
                "Modifica juegos y actividades para que se adecúen a las necesidades y posibilidades del grupo y a la lógica del juego deportivo.",
                "Participa en actividades lúdicas, predeportivas y deportivas en las que pone en práctica diversas estrategias; adecúa normas de juego y la mejor solución táctica para dar respuesta a las variaciones que se presentan en el entorno."
            ]
        }
    }
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


 



