import React, { useState } from "react";
import "./App.css";
import ResultCard from "./components/ResultCard";

function App() {
  const [domain, setDomain] = useState("");
  const [data, setData] = useState(null);

  const handleAnalyze = async () => {
    try {
      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ domain })
      });

      const result = await response.json();
      setData(result);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const getCategoryColor = (category) => {
    switch (category) {
      case "Hot":
        return "red";
      case "Warm":
        return "yellow";
      case "Cold":
        return "blue";
      default:
        return "gray";
    }
  };

  const getStrategyContent = () => {
  return data?.strategy?.email_body || "No strategy generated.";
};

  return (
    <div className="app">
      <h1 className="title">TechMatch</h1>

      <div className="search-container">
        <input
          type="text"
          placeholder="Enter company domain..."
          value={domain}
          onChange={(e) => setDomain(e.target.value)}
        />
        <button onClick={handleAnalyze}>Analyze</button>
      </div>

      {data && (
        <>
          <div className="cards">
  <ResultCard
  title="Company Analysis"
  content={`
Industry: ${data.company_analysis?.industry || "N/A"}

Summary:
${data.company_analysis?.summary || "N/A"}

Revenue Streams:
${
  data.company_analysis?.business_model?.revenue_streams
    ? "- " + data.company_analysis.business_model.revenue_streams.join("\n- ")
    : "Not available"
}

Target Customers:
${
  data.company_analysis?.target_customers
    ? "- " + data.company_analysis.target_customers.join("\n- ")
    : "Not available"
}
`}
/>
  <ResultCard
    title="Fit Reasoning"
    content={data.fit_analysis.fit_reasoning}
  />
  <ResultCard
  title="Strategy"
  content={data?.strategy?.email_body || "No strategy generated."}
/>
</div>

          <div className="scores">
            <div className="score-box">
              <h3>Overlap Score</h3>
              <p>{data.fit_analysis.overlap_score}</p>
            </div>

            <div className="score-box">
              <h3>Intent Score</h3>
              <p>{data.fit_analysis.intent_score}</p>
            </div>

            <div className="score-box">
              <h3>Lead Score</h3>
              <p>{data.fit_analysis.lead_score}</p>
            </div>

            <div
              className="category-box"
              style={{
                backgroundColor: getCategoryColor(data.fit_analysis.category)
              }}
            >
              {data.fit_analysis.category}
            </div>
          </div>
        </>
      )}
    </div>
  );
  
}

export default App;