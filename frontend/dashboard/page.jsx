import React, { useEffect, useState } from "react";

export default function Dashboard() {
  const [health, setHealth] = useState(null);

  useEffect(() => {
    async function fetchHealth() {
      const res = await fetch("http://localhost:8000/health");
      const data = await res.json();
      setHealth(data);
    }

    fetchHealth();
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>LTD Dashboard</h1>
      <p>Status: {health ? health.status : "Loading..."}</p>

      <div style={{ marginTop: 20 }}>
        <h2>Run Orchestrator</h2>
        <button
          onClick={async () => {
            const res = await fetch("http://localhost:8000/agent/orchestrator", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ task: "Process incoming data" })
            });
            alert(JSON.stringify(await res.json(), null, 2));
          }}
        >
          Execute Task
        </button>
      </div>
    </div>
  );
}
