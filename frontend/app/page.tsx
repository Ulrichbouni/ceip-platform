"use client";
import { useEffect, useState } from "react";

export default function Home() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(process.env.NEXT_PUBLIC_API_URL + "/api/v1/dashboard/macro")
      .then(res => res.json())
      .then(json => {
        setData(json);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <div style={{padding:50, fontFamily:'Arial'}}>Chargement des données économiques...</div>;

  return (
    <div style={{padding:20, fontFamily:'Arial'}}>
      <h1>📊 CEMAC Economic Intelligence Platform</h1>
      <p>Données récupérées depuis le backend (toutes les sources API)</p>
      <pre style={{background:'#f4f4f4', padding:20, borderRadius:8}}>
        {JSON.stringify(data, null, 2)}
      </pre>
      <p>Les données réelles apparaîtront après l'exécution du pipeline ETL.</p>
      <p>Pour lancer la collecte, utilisez le endpoint <code>POST /api/v1/etl/run</code> (via Swagger).</p>
    </div>
  );
}