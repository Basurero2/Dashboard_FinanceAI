import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://150.230.77.225:8080/api/v1")

def obtener_analisis_predict(token: str = None):
    """
    Endpoint: POST /api/v1/analisis/predict
    """
    endpoint = f"{API_BASE_URL}/analisis/predict"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.post(endpoint, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass
    
    # Mock Data alineada exactamente a los esquemas OpenAPI
    return {
        "perfilFinanciero": "EN_OBSERVACION",
        "probabilidad": 0.82,
        "resumenGastos": {
            "alimentacion": 650.0,
            "transporte": 360.0,
            "entretenimiento": 210.0,
            "servicios": 180.0
        },
        "recomendaciones": [
            "Monitorear los gastos recurrentes de entretenimiento para evitar sobrepasar tu capacidad mensual.",
            "Aumentar la reserva financiera mensual destina al menos un 10% adicional al ahorro."
        ],
        "ingreso_mensual": 4500.0,
        "nivel_endeudamiento": 32.0,
        "frecuencia_ahorro": "Alta"
    }

def obtener_historial_usuario(user_id: int = 1, token: str = None):
    """
    Endpoint: GET /api/v1/analisis/usuario/{userId}
    """
    endpoint = f"{API_BASE_URL}/analisis/usuario/{user_id}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(endpoint, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass

    # Mock Data para el gráfico de línea temporal de diagnósticos anteriores
    return [
        {"id": 101, "fecha": "2026-05-01", "perfilFinanciero": "RIESGOSO", "gastoTotal": 2400.0, "endeudamiento": 58.0},
        {"id": 102, "fecha": "2026-06-01", "perfilFinanciero": "EN_OBSERVACION", "gastoTotal": 1800.0, "endeudamiento": 42.0},
        {"id": 103, "fecha": "2026-07-01", "perfilFinanciero": "EN_OBSERVACION", "gastoTotal": 1400.0, "endeudamiento": 35.0}
    ]

def obtener_transacciones_detalle(token: str = None):
    """
    Endpoint: GET /api/v1/transactions
    """
    endpoint = f"{API_BASE_URL}/transactions"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(endpoint, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass

    # Mock Data para la tabla de transacciones de Swagger
    return [
        {"id": 1, "monto": 210.0, "tipo": "Gasto", "categoria": "Entretenimiento", "descripcion": "Cine y Snacks", "fecha": "2026-08-04"},
        {"id": 2, "monto": 650.0, "tipo": "Gasto", "categoria": "Alimentación", "descripcion": "Supermercado Walmart", "fecha": "2026-08-03"},
        {"id": 3, "monto": 360.0, "tipo": "Gasto", "categoria": "Transporte", "descripcion": "Combustible / Gasolina", "fecha": "2026-08-02"},
        {"id": 4, "monto": 180.0, "tipo": "Gasto", "categoria": "Servicios", "descripcion": "Pago Servicio Electricidad", "fecha": "2026-08-01"}
    ]