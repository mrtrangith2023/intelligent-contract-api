import React, { useEffect, useState } from "react";
import BASE_URL from "../config";

export default function ContractHistory() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetch(`${BASE_URL}/api/history`)
      .then(res => res.json())
      .then(data => setHistory(data))
      .catch(err => console.error("History error:", err));
  }, []);

  return (
    <div>
      <h2>History</h2>
      <pre>{JSON.stringify(history, null, 2)}</pre>
    </div>
  );
}