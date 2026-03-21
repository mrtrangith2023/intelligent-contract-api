import React from "react";
import ContractForm from "./components/ContractForm";
import ContractVerify from "./components/ContractVerify";
import ContractHistory from "./components/ContractHistory";

function App() {
  return (
    <div style={{ padding: 20 }}>
      <h1>🚀 Intelligent Contract Demo</h1>

      <ContractForm />
      <hr />

      <ContractVerify />
      <hr />

      <ContractHistory />
    </div>
  );
}

export default App;