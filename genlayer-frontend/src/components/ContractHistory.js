import React, { useEffect, useState } from "react";
import axios from "axios";

export default function ContractHistory() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/history")
      .then(res => setHistory(res.data));
  }, []);

  return (
    <div>
      <h2>History</h2>
      <pre>{JSON.stringify(history, null, 2)}</pre>
    </div>
  );
}