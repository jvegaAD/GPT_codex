import pandas as pd
import streamlit as st
from pathlib import Path

DATA_FILE = Path(__file__).parent / 'data' / 'progress.xlsx'

def load_data():
    sheets = pd.read_excel(DATA_FILE, sheet_name=None)
    return sheets['avance_programado'], sheets['avance_real'], sheets['avance_registrado']

st.title('Gantt Progress Overview')
if DATA_FILE.exists():
    programado, real, registrado = load_data()
    st.subheader('Avance Programado')
    st.dataframe(programado)
    st.subheader('Avance Real')
    st.dataframe(real)
    st.subheader('Reportes Registrados')
    st.dataframe(registrado)
else:
    st.warning('Excel file not found. Run setup_excel.py first.')
