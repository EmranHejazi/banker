export async function searchCustomers(params: any) {
  const res = await fetch("http://localhost:8000/api/search/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
  });

  return await res.json();
}
