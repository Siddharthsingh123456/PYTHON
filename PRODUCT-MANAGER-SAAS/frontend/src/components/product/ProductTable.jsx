export default function ProductTable({ products = [] }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>SKU</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        {products.map((p) => (
          <tr key={p.id || p.sku}>
            <td>{p.name}</td>
            <td>{p.sku}</td>
            <td>{p.current_price}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
