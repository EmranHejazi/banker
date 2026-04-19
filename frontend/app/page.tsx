"use client";

import { useState } from "react";
import SearchForm from "./components/SearchForm";
import SearchResults from "./components/SearchResults";

export default function Page() {
  const [results, setResults] = useState([]);

  return (
    <div className="space-y-10">
      <SearchForm onResults={setResults} />
      <SearchResults results={results} />
    </div>
  );
}
