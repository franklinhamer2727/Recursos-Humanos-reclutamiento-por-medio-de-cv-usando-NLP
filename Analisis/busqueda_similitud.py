from diccionario_similitud import procesos_ejecucion
import nltk
import json
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

def leer_archivo(ruta_archivo):
    with open(ruta_archivo,'r') as archivo:
        contenido = archivo.read()
    return contenido

def separar_bloques(texto):
    informacion_personal = ["Personal information",
                            "Personal details",
                            "Personal Profile",
                            "Personal data",
                            "Personal details",
                            "Identity information",
                            "Confidential information",
                            "Private information",
                            "Sensitive information",
                            "Personal Dossier",
                            "Resume"]

    objetivos_profesionales = ["Professional objectives",
                               "Career aspirations",
                               "Professional goal",
                               "Occupational objectives" 
                               "Career goals",
                               "Professional ambitions",
                               "Professional summary",
                               "Professional overview",
                               "Work experience summary",
                               "Career Objective",
                               "Job target","Goal"]
    experiencia_laboral = ["Work experience",
                           "Laboral experience",
                           "Professional background",
                           "Career history",
                           "Professional experience",
                           "Professional Trainings",
                           "Job experience",
                           "Employment record",
                           "Employment history",
                           "Working Experience",
                           "Projects",
                           "Experience"]
    education = ["Education",
                 "Academic and Professional",
                 "academics","ACADEMICS",
                 "Academic background",
                 "Educational history",
                 "Academic record",
                 "Scholarly background",
                 "Educational qualifications",
                 "Educational credentials",
                 "Academic qualifications",
                 "Educational achievements",
                 "Academic Qualification",
                 "Educational Background",
                 "Academic degree",
                 "Educational degree",
                 "Qualification",
                "academic details",
                 "Educational details",
                 "Scholastics",
                 "Academic information",
                 "Schooling particulars"]
    habilidades = ["Technical and personal skills",
                   "Technical and personal competencies",
                   "Technical Skills",
                   "Technical and personal expertise",
                   "Abilities",
                   "Competencies",
                   "Personality Traits",
                   "Software Skill",
                   "Technical Proficiency",
                  "Skills"]
    logros_premios = ["Achievements and awards",
                      "Accomplishments and honors",
                      "Recognition and accolades"]

    actividades_extracurriculares = ["Extracurricular activities",
                                     "Extra Curricular Activities",
                                     "Additional activities",
                                     "Extra Curricular Activitis",
                                     "Extra Co-Curricutar Activities",
                                     "Non-academic involvement"]
    referencias = ["References",
                   "Referees",
                   "Recommendations",
                   "Other Information"]
    cv_titulos = [informacion_personal,objetivos_profesionales,experiencia_laboral,
                  education,habilidades,logros_premios,actividades_extracurriculares,referencias]
    cv_titulos_dict = {
    'informacion_personal': informacion_personal,
    'objetivos_profesionales': objetivos_profesionales,
    'experiencia_laboral': experiencia_laboral,
    'education':education,
    'habilidades':habilidades,
    'logros_premios':logros_premios,
    'actividades_extracurriculares':actividades_extracurriculares,
    'referencias'   :referencias
    }
    cadenas_cv = []
    cadenas_pos = []
    cadenas_name = []
    for cv_titulos in cv_titulos_dict.keys():
        for find in cv_titulos_dict[cv_titulos]:
            numero = texto.count(find.lower())
            if(numero!=0):
                pass
            if numero!=0 and numero <2:
                pos_texto = texto.find(find.lower())
                if pos_texto != -1:
                    cadenas_cv.append(find.lower())
                    cadenas_pos.append(pos_texto)
                    cadenas_name.append(cv_titulos)
                    break
    diccionario = {
        'cadenas_name': cadenas_name,
        'cadenas_cv': cadenas_cv,
        'cadenas_pos': cadenas_pos,
    }

    json_data = {}

    diccionario_ordenado = dict(sorted(zip( diccionario['cadenas_name'],diccionario['cadenas_pos']),key=lambda x: x[1]))
    name_bloque = 'Introduccion'
    posicion_inicial_text = 0
    count = 0
    for key, value  in list(diccionario_ordenado.items()):
        json_data[name_bloque] = texto[posicion_inicial_text:value]
        name_bloque = key
        posicion_inicial_text = value
        count +=1
    json_data[name_bloque] = texto[posicion_inicial_text:len(texto)]

    return json.dumps(json_data)


def convert_doc_to_json(link_doc):
    texto = leer_archivo(link_doc).lower()
    json_str = separar_bloques(texto)

    json_data = json.loads(json_str)
    return json_data
def tokenizacion_texto(texto):
    stop_words = stopwords.words('english')
    texto = texto.lower()
    tokens = word_tokenize(texto)
    text_filtrado = [word for word in tokens if not word in stop_words]
    return text_filtrado
def json_doc_postulante(json_postulante):
    json_postulante_habilidades = json_postulante['habilidades']
    json_postulante_experiencia = json_postulante['experiencia_laboral']
    tokenizado_habilidades = tokenizacion_texto(json_postulante_habilidades)
    tokenizado_expeciencia = tokenizacion_texto(json_postulante_experiencia)
    return tokenizado_habilidades, tokenizado_expeciencia



def procesar_archivos(ruta_txt):

    try:
        json_postulante = convert_doc_to_json(ruta_txt)
        tokenizado_habilidades, tokenizado_expeciencia = json_doc_postulante(json_postulante)
        return tokenizado_habilidades,tokenizado_expeciencia

    except Exception as e:
        print("Error al insertar datos:", e)
        return [], []




def procesar():
    palabras_cercanas_experiencia, palabras_cercanas_habilidades = procesos_ejecucion()
    ruta_txt = "../postulantes/txt/"
    tokenizado_expeciencia = None
    tokenizado_habilidades = None

    diccionario = {}
    resultados = []
    for i in os.listdir(ruta_txt):
        nombre = i.split('.')

        print(nombre[0])
        tokenizado_habilidades,tokenizado_expeciencia = procesar_archivos(os.path.join(ruta_txt, i))
        count_experiencia = 0
        count_habilidades = 0
        experiencia = []
        habilidades = []
        for i in range(len(palabras_cercanas_experiencia)):
            for key, value in palabras_cercanas_experiencia[i]:

                if key in tokenizado_expeciencia:
                    experiencia.append([value,key])
                    count_experiencia +=1


        for i in range(len(palabras_cercanas_habilidades)):
            for key, value in palabras_cercanas_habilidades[i]:

                if key in tokenizado_habilidades:
                    habilidades.append([value, key])
                    count_habilidades += 1

        diccionario[nombre[0]] ={"habilidades":habilidades,
                                 "experiencia":experiencia,
                                 "count_experiencia":count_experiencia,
                                "count_habilidades":count_habilidades}
    resultados.append(diccionario)
    return resultados



if __name__ == "__main__":
    r = procesar()
    print(r)