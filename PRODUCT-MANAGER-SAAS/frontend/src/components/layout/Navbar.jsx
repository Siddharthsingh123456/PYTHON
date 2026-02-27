import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="nav">
      <Link to="/">Dashboard</Link>
      <Link to="/pricing">Pricing</Link>
      <Link to="/analytics">Analytics</Link>
    </nav>
  );
}
