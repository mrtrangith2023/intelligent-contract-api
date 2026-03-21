import React, { useState } from "react";
import client from "../genlayerClient";

export default function ContractForm() {
  const [user, setUser] = useState("");
  const [action, setAction] = useState("");
  const [data, setData] = useState("{}");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    try {
      const parsedData = JSON.parse(data);
      const response = await client.submit({ user, action, data: parsedData });
      setResult(response);
    } catch (err) {
      setResult({ status: "error", message: err.message });
    }
  };

  return (
    <div>
      <h2>Submit Contract</h2>
      <input placeholder="User" value={user} onChange={e => setUser(e.target.value)} />
      <input placeholder="Action" value={action} onChange={e => setAction(e.target.value)} />
      <textarea placeholder="Data JSON" value={data} onChange={e => setData(e.target.value)} />
      <button onClick={handleSubmit}>Submit</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}