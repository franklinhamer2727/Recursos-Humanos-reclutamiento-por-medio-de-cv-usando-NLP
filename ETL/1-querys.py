from conexion_db import conexion_collection
import sys
import os
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))
import time
from dotenv import load_dotenv
import json
from TecnicasNLP.tokenizacion import  procesamiento_tokenizacion, word2vec_oraciones, procesamiento_tokenizacion_spacy

load_dotenv()
db_host = os.getenv("IP_CONEXION")
db_user = os.getenv("USUARIO_CONEXION")
db_pass = os.getenv("CONTRASENA_CONEXION")
db_name = os.getenv("DB_NAME")
col_collection = os.getenv("DB_COLLECTION")
col_collection_ = os.getenv("DB_COLLECTION_FILTRO")
expedientes_laborales =[]
expedientes_habilidades = []
expedientes_objetivos_profesionales = []
expedientes_educacion = []
expedientes_logros_premios = []
expedientes_actividades_extracurriculares = []


expedientes_laborales_oraciones =[]
expedientes_habilidades_oraciones = []
expedientes_objetivos_profesionales_oraciones = []
expedientes_educacion_oraciones = []
expedientes_logros_premios_oraciones = []
expedientes_actividades_extracurriculares_oraciones = []


oraciones_limpias_laborales =[]
oraciones_limpias_habilidades = []
oraciones_limpias_objetivos_profesionales = []
oraciones_limpias_educacion = []
oraciones_limpias_logros_premios = []
oraciones_limpias_actividades_extracurriculares = []
def consulta_collection():

    collection, db, client = conexion_collection(col_collection, db_name)
    """
    registros_claves = collection.find({
        "experiencia_laboral": {"$exists":True,"$ne":""},
        "habilidades": {"$exists":True,"$ne":""},
    })"""
    registros_claves = collection.find()
    for registro in registros_claves:
        registro['_id'] = str(registro['_id'])
        # Tipos de datos

        objetivos_profesionales = registro.get("objetivos_profesionales")
        experiencia_laboral = registro.get("experiencia_laboral")
        education = registro.get("education")
        habilidades = registro.get("habilidades")
        logros_premios = registro.get("logros_premios")
        actividades_extracurriculares = registro.get("actividades_extracurriculares")

        ## Creacion de arrays
        expedientes_objetivos_profesionales.append(objetivos_profesionales)
        expedientes_laborales.append(experiencia_laboral)
        expedientes_educacion.append(education)
        expedientes_habilidades.append(habilidades)
        expedientes_logros_premios.append(logros_premios)
        expedientes_actividades_extracurriculares.append(actividades_extracurriculares)
    client.close()
def split_document(expediente):
    oraciones_expediente = expediente.split(".")
    return oraciones_expediente

def split_documento_coma(expediente):
    oraciones_expediente = expediente.split(",")
    return oraciones_expediente
def union_expedientes(expediente_laboral):
    expedientes_laborales_oraciones.extend(expediente_laboral)
    return expedientes_laborales_oraciones

def creacion_modelo_laboral():
    for expediente_laboral in expedientes_laborales:
        oraciones_expediente_laboral = split_document(expediente_laboral)
        expedientes_laborales_oraciones = union_expedientes(oraciones_expediente_laboral)
    oraciones_limpias_laborales = procesamiento_tokenizacion(expedientes_laborales_oraciones)
    model = word2vec_oraciones(oraciones_limpias_laborales)
    return model

def creacion_modelo_habilidades():
    for habilidades in expedientes_habilidades:
        oraciones_habilidades = split_document(habilidades)
        expedientes_habilidades_oraciones = union_expedientes(oraciones_habilidades)
    oraciones_limpias_habilidades = procesamiento_tokenizacion(expedientes_habilidades_oraciones)
    model = word2vec_oraciones(oraciones_limpias_habilidades)
    return model


if __name__ == "__main__":
    tiempos_creacion_modelos = {}
    consulta_collection()

    # Crear y guardar el modelo laboral
    start_time = time.time()
    model_laboral = creacion_modelo_laboral()
    model_laboral.save("experiencia_laboral.model")
    end_time = time.time()
    tiempos_creacion_modelos['experiencia_laboral'] = end_time - start_time

    # Crear y guardar el modelo de habilidades
    start_time = time.time()
    model_habilidades = creacion_modelo_habilidades()
    model_habilidades.save("habilidades.model")
    end_time = time.time()
    tiempos_creacion_modelos['habilidades'] = end_time - start_time
    

