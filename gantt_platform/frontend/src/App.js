import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null);
  const [avance, setAvance] = useState('');
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    fetch('/api/tasks/')
      .then(r => r.json())
      .then(setData);
  }, []);

  const submit = () => {
    if (!selected) return;
    fetch('/api/report/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-User': 'demo'
      },
      body: JSON.stringify({ ID: selected.ID, Tareas: selected.Tareas, avance })
    }).then(() => window.location.reload());
  };

  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <h1>Avance Programado</h1>
      <ul>
        {data.programado.map(t => (
          <li key={t.ID} onClick={() => setSelected(t)}>
            {t.Tareas}: {t.avance}%
          </li>
        ))}
      </ul>
      {selected && (
        <div>
          <h2>Reportar avance para {selected.Tareas}</h2>
          <input value={avance} onChange={e => setAvance(e.target.value)} />
          <button onClick={submit}>Enviar</button>
        </div>
      )}
    </div>
  );
}
export default App;
