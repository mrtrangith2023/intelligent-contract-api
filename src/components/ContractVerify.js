import React, { useState } from "react";
import client from "../genlayerClient";

export default function ContractVerify() {
  const [submissionId, setSubmissionId] = useState("");
  const [result, setResult] = useState(null);

  const handleVerify = async () => {
    try {
      const response = await client.verify(submissionId);
      setResult(response);
    } catch (err) {
      setResult({ status: "error", message: err.message });
    }
  };

  return (
    <div>
      <h2>Verify Contract</h2>
      <input placeholder="Submission ID" value={submissionId} onChange={e => setSubmissionId(e.target.value)} />
      <button onClick={handleVerify}>Verify</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}