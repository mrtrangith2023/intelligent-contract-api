import React from "react";
import BASE_URL from "../config";

export default function ContractForm() {
  const submitContract = async () => {
    try {
      const res = await fetch(`${BASE_URL}/api/submit`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          content: "This is a test contract"
        })
      });

      const data = await res.json();
      alert("Submitted: " + data.contract_id);

    } catch (err) {
      console.error("Submit error:", err);
    }
  };

  return (
    <div>
      <h2>Submit Contract</h2>
      <button onClick={submitContract}>Submit Contract</button>
    </div>
  );
}