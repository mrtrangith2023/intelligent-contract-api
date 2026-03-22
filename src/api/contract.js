const API_URL = process.env.REACT_APP_API_URL;

// ✅ Submit
export async function submitContract(data) {
  const res = await fetch(`${API_URL}/api/submit`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return res.json();
}

// ✅ Verify
export async function verifyContract(id) {
  const res = await fetch(`${API_URL}/api/verify?submission_id=${id}`, {
    method: "POST",
  });

  return res.json();
}

// ✅ History
export async function getHistory() {
  const res = await fetch(`${API_URL}/api/history`);
  return res.json();
}