# Dashboard_FinanceAI

## 🚀 Guía de Inicio Rápido: Dashboard FinanceAI

1. Clonar el repositorio
Abre tu terminal y ejecuta el siguiente comando:
```bash
git clone https://github.com/Basurero2/Dashboard_FinanceAI.git
```

2. Entrar a la carpeta del proyecto
```
cd Dashboard_FinanceAI
```

3. Crear e iniciar el entorno virtual:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

- Si PowerShell bloquea la ejecución de scripts, habilítala temporalmente con:
```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

4. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

5. actualizar archivo **.env.exmaple**
   - renombarlo a .env
   - llenar el campo ```API_BACKEND_URL=```  con la API del backend o usar ```http://localhost:8000/api``` para usar la prueba de manera local

6. Ejecutar la aplicación:
```powershell
streamlit run app.py
```

7. Abrir en el navegador: http://localhost:8501



## Estructura

```
financeai-dashboard/
├── .env.example          <-- 1. PLANTILLA DE CONFIGURACÓN DE RED
├── requirements.txt      <-- 2. GESTIÓN DE DEPENDENCIAS
├── app.py                <-- 3. CAPA DE PRESENTACIÓN (UI)
└── src/
    ├── services/         <-- 4. CAPA DE COMUNICACIÓN CON EL BACKEND
    │   └── api_client.py
    └── components/       <-- 5. COMPONENTES VISUALES REUTILIZABLES (Futuro)
```

