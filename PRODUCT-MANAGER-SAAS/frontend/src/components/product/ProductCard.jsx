export default function ProductCard({ product }) {
  return (
    <article className="card">
      <h4>{product.name}</h4>
      <p>SKU: {product.sku}</p>
      <p>${product.current_price}</p>
    </article>
  );
}
