# Gantt Platform

This folder contains a prototype for a web platform that tracks project progress from an Excel file. The backend is built with Django REST Framework, the frontend uses React, and Streamlit provides a quick admin view.

## Running locally

1. Install Python dependencies (requires internet access):
   ```bash
   pip install -r backend/requirements.txt
   ```
2. Install Node dependencies for the frontend:
   ```bash
   cd frontend
   npm install
   ```
3. Start the Django server:
   ```bash
   python backend/manage.py runserver
   ```
4. In another terminal, start the React dev server:
   ```bash
   cd frontend
   npm start
   ```

## Excel file

The application expects a file named `progress.xlsx` inside the `data` directory. If it does not exist, run:

```bash
python backend/setup_excel.py
```

This script creates a sample workbook with the required sheets:
- `avance_programado`
- `avance_real`
- `avance_registrado`

## Streamlit

For a quick visual overview, run:

```bash
streamlit run streamlit_app.py
```

## Authentication

The sample code includes a very simple header-based user identification. Replace it with proper authentication for production use.
