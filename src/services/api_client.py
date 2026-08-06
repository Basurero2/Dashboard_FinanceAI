import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://150.230.77.225:8080/api/v1")

def obtener_analisis_financiero(token: str = None):
    endpoint = f"{API_BASE_URL}/analisis/predict"
    
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.post(endpoint, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"⚠️ Respuesta del servidor ({response.status_code}). Cargando mock data...")
            return _obtener_datos_mock()
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error de conexión ({e}). Cargando mock data...")
        return _obtener_datos_mock()

def _obtener_datos_mock():
    return {
        "perfilFinanciero": "RIESGOSO",
        "probabilidad_num": 94.43,
        "probabilidad": "94.43%",
        "nivel_endeudamiento": "12.4%",
        "porcentaje_ahorro": "Alta",
        "resumenGastos": {
            "alimentacion": 850.0,
            "entretenimiento": 199.0,
            "transporte": 180.5,
            "otros servicios": 320.0
        },
        "gastosPorMedioPago": {
            "Tarjeta de Crédito": 1049.0,
            "Tarjeta de Débito": 320.5,
            "Efectivo": 180.0
        },
        "recomendaciones": [
            "Para aumentar el score del perfil, se recomienda incrementar el ingreso mensual de modo que supere la línea de crédito asignada o solicitar un ajuste en el límite de crédito."
        ]
    }