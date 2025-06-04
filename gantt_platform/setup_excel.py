"""Create sample Excel workbook for development."""
import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
path = os.path.join(BASE_DIR, 'data', 'progress.xlsx')
os.makedirs(os.path.join(BASE_DIR, 'data'), exist_ok=True)
programado = pd.DataFrame({
    'ID': [1, 2],
    'Tareas': ['Plan', 'Execute'],
    'avance': [0, 0],
    'Responsable': ['Alice', 'Bob'],
})
real = programado.copy()
registrado = pd.DataFrame(columns=['ID', 'Tareas', 'avance', 'Responsable', 'fecha', 'hora'])
with pd.ExcelWriter(path) as writer:
    programado.to_excel(writer, sheet_name='avance_programado', index=False)
    real.to_excel(writer, sheet_name='avance_real', index=False)
    registrado.to_excel(writer, sheet_name='avance_registrado', index=False)
print('Excel workbook created at', path)
