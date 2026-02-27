import { useEffect, useState } from "react";
import api from "../../api/axiosConfig";
import ProductTable from "../../components/product/ProductTable";

export default function Dashboard() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get("/products/").then((res) => setProducts(res.data.products || [])).catch(() => setProducts([]));
  }, []);

  return (
    <section>
      <h1>Dashboard</h1>
      <ProductTable products={products} />
    </section>
  );
}
