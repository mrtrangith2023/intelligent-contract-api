import React, { useState } from "react";
import axios from "axios";

export default function ContractVerify() {
  const [result, setResult] = useState(null);

  const handleVerify = async () => {
    const res = await axios.post("http://127.0.0.1:8000/api/verify?submission_id=0");
    setResult(res.data);
  };

  return (
    <div>
      <h2>Verify Contract</h2>
      <button onClick={handleVerify}>Verify ID 0</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}