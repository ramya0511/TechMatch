import React from "react";

function ResultCard({ title, content }) {
  return (
    <div className="card">
      <h2>{title}</h2>
      <pre>{content}</pre>
    </div>
  );
}

export default ResultCard;