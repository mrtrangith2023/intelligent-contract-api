import React, { useState } from "react";
import axios from "axios";

export default function ContractForm() {
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const res = await axios.post("http://127.0.0.1:8000/api/submit", {
      user: "TAM",
      action: "mint",
      data: { amount: 100 }
    });
    setResult(res.data);
  };

  return (
    <div>
      <h2>Submit Contract</h2>
      <button onClick={handleSubmit}>Submit</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}