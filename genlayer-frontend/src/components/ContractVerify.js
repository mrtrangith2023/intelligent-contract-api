import React, { useState } from "react";
import BASE_URL from "../config";

export default function ContractVerify() {
  const [contractId, setContractId] = useState("");

  const verifyContract = async () => {
    try {
      const res = await fetch(`${BASE_URL}/api/verify`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          contract_id: contractId
        })
      });

      const data = await res.json();
      alert("Result: " + data.result);

    } catch (err) {
      console.error("Verify error:", err);
    }
  };

  return (
    <div>
      <h2>Verify Contract</h2>
      <input
        type="text"
        placeholder="Enter Contract ID"
        value={contractId}
        onChange={(e) => setContractId(e.target.value)}
      />
      <button onClick={verifyContract}>Verify</button>
    </div>
  );
}