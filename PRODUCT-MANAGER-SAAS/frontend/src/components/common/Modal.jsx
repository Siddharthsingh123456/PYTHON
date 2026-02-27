export default function Modal({ title, children, onClose }) {
  return (
    <div className="modal-overlay">
      <div className="modal">
        <h3>{title}</h3>
        <div>{children}</div>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}
