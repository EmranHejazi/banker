export default function Navbar() {
  return (
    <nav className="border-b border-[#2a2a31] bg-[#121216]/80 backdrop-blur-xl">
      <div className="container mx-auto px-6 py-4 flex items-center justify-between">
        <h1 className="text-2xl font-bold tracking-wide text-red-400">
          Banker Dashboard
        </h1>
        <span className="text-gray-400 text-sm">v1.0.0</span>
      </div>
    </nav>
  );
}
