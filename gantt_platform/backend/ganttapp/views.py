import os
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'progress.xlsx')

SHEET_PROGRAMADO = 'avance_programado'
SHEET_REAL = 'avance_real'
SHEET_REGISTRADO = 'avance_registrado'


def ensure_file():
    if not os.path.exists(DATA_FILE):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        programado = pd.DataFrame({'ID': [], 'Tareas': [], 'avance': [], 'Responsable': []})
        real = programado.copy()
        registrado = pd.DataFrame(columns=['ID', 'Tareas', 'avance', 'Responsable', 'fecha', 'hora'])
        with pd.ExcelWriter(DATA_FILE) as writer:
            programado.to_excel(writer, sheet_name=SHEET_PROGRAMADO, index=False)
            real.to_excel(writer, sheet_name=SHEET_REAL, index=False)
            registrado.to_excel(writer, sheet_name=SHEET_REGISTRADO, index=False)


def read_sheets():
    ensure_file()
    xl = pd.read_excel(DATA_FILE, sheet_name=[SHEET_PROGRAMADO, SHEET_REAL])
    return xl[SHEET_PROGRAMADO], xl[SHEET_REAL]


def append_progress(row):
    ensure_file()
    df = pd.read_excel(DATA_FILE, sheet_name=SHEET_REGISTRADO)
    key = (row['ID'], row['Responsable'], row['fecha'])
    if not df[df[['ID', 'Responsable', 'fecha']].eq(key).all(1)].empty:
        return False
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    with pd.ExcelWriter(DATA_FILE, mode='a', if_sheet_exists='overlay')  as writer:
        df.to_excel(writer, sheet_name=SHEET_REGISTRADO, index=False)
    return True


class TaskListView(APIView):
    def get(self, request):
        programado, real = read_sheets()
        data = {
            'programado': programado.to_dict(orient='records'),
            'real': real.to_dict(orient='records'),
        }
        return Response(data)


class ReportView(APIView):
    def post(self, request):
        user = request.headers.get('X-User', 'anonymous')
        task_id = request.data.get('ID')
        avance = request.data.get('avance')
        tareas = request.data.get('Tareas')
        if task_id is None or avance is None:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        now = datetime.now()
        row = {
            'ID': task_id,
            'Tareas': tareas,
            'avance': avance,
            'Responsable': user,
            'fecha': now.date().isoformat(),
            'hora': now.strftime('%H:%M:%S'),
        }
        if append_progress(row):
            return Response({'status': 'ok'})
        return Response({'error': 'Already reported today'}, status=status.HTTP_409_CONFLICT)
