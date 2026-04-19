"use client";

import { useState } from "react";
import { searchCustomers } from "../lib/api";
import InputGroup from "./InputGroup";

export default function SearchForm({ onResults }: any) {
  const [search, setSearch] = useState("");

  const [filters, setFilters] = useState({
    age: "",
    city_name: "",
    province_name: "",
    birth_city: "",
    birth_province: "",
    gender: "",
  });

  const updateFilters = (e: any) => {
    setFilters({ ...filters, [e.target.name]: e.target.value });
  };

  const submit = async (e: any) => {
    e.preventDefault();
    const res = await searchCustomers({ search, filters });
    onResults(res);
  };

  return (
    <form onSubmit={submit} className="card grid grid-cols-1 lg:grid-cols-3 gap-6">

      {/* MAIN SEARCH BOX */}
      <div className="lg:col-span-3">
        <InputGroup
          label="Search (Code / Name / Mobile)"
          name="search"
          value={search}
          onChange={(e: any) => setSearch(e.target.value)}
        />
      </div>

      {/* FILTERS BELOW */}
      <InputGroup label="Age" name="age" value={filters.age} onChange={updateFilters} />
      <InputGroup label="City" name="city_name" value={filters.city_name} onChange={updateFilters} />
      <InputGroup label="Province" name="province_name" value={filters.province_name} onChange={updateFilters} />
      <InputGroup label="Birth City" name="birth_city" value={filters.birth_city} onChange={updateFilters} />
      <InputGroup label="Birth Province" name="birth_province" value={filters.birth_province} onChange={updateFilters} />
      <InputGroup label="Gender" name="gender" value={filters.gender} onChange={updateFilters} />

      <div className="lg:col-span-3 flex justify-end pt-4">
        <button type="submit" className="btn-primary">
          Search
        </button>
      </div>
    </form>
  );
}
