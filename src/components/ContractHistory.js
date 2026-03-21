import React, { useEffect, useState } from "react";
import axios from "axios";

export default function ContractHistory() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const fetchHistory = async () => {
      const res = await axios.get("http://192.168.56.1:8000/api/history");
      setHistory(res.data);
    };
    fetchHistory();
  }, []);

  return (
    <div>
      <h2>Contract History</h2>
      <pre>{JSON.stringify(history, null, 2)}</pre>
    </div>
  );
}