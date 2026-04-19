export default function SearchResults({ results }: any) {
  if (!results || results.length === 0)
    return <p className="text-gray-400 mt-6">No results found.</p>;

  return (
    <div className="mt-8 grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
      {results.map((item: any) => (
        <div key={item.id} className="card">
          <h2 className="text-lg font-semibold text-red-300">
            {item.full_name || "Unknown"}
          </h2>

          <div className="mt-4 space-y-2 text-sm text-gray-300">
            <p><strong>National Code:</strong> {item.national_code}</p>
            <p><strong>Mobile:</strong> {item.mobile}</p>
            <p><strong>Age:</strong> {item.age}</p>
            <p><strong>City:</strong> {item.city_name}</p>
            <p><strong>Province:</strong> {item.province_name}</p>
            <p><strong>Birth City:</strong> {item.birth_city}</p>
            <p><strong>Birth Province:</strong> {item.birth_province}</p>
            <p><strong>Gender:</strong> {item.gender}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
