"use client";
import { useEffect, useState } from "react";

export default function Home() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;
    if (!apiUrl) {
      setLoading(false);
      return;
    }
    fetch(apiUrl + "/api/v1/dashboard/macro")
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div style={{ padding: 50, fontFamily: "Arial", textAlign: "center" }}>
        ⏳ Chargement des données économiques...
      </div>
    );
  }

  return (
    <div style={{ padding: 20, fontFamily: "Arial", maxWidth: 800, margin: "0 auto" }}>
      <h1>📊 CEMAC Economic Intelligence Platform</h1>
      <p style={{ color: "#555" }}>
        Données récupérées depuis le backend (toutes les sources API)
      </p>
      <pre style={{ background: "#f4f4f4", padding: 20, borderRadius: 8, overflowX: "auto" }}>
        {JSON.stringify(data, null, 2)}
      </pre>
      <p>
        💡 <strong>Prochaine étape :</strong> lancer le pipeline ETL pour collecter les vraies données.
      </p>
      <p>
        Utilisez l'endpoint <code>POST /api/v1/etl/run</code> (via Swagger à l'adresse{" "}
        <code>{process.env.NEXT_PUBLIC_API_URL}/docs</code>).
      </p>
    </div>
  );
}