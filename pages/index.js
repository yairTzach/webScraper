import { useState } from 'react';

export default function Home() {
  const [productName, setProductName] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const apiUrl = `http://localhost:8000/search/${encodeURIComponent(productName)}`;
    console.log(`Making request to ${apiUrl}`);
    try {
      const response = await fetch(apiUrl);
      console.log('Response status:', response.status);

      if (response.ok) {
        const data = await response.json();
        console.log('Response data:', data);
        setResults(data);
      } else {
        console.error('Failed to fetch data:', response.status);
        const errorData = await response.text();
        console.error('Error details:', errorData);
      }
    } catch (error) {
      console.error('Failed to fetch data:', error);
    }
  };

  return (
    <div className="container">
      <h1>From Idea To Zap</h1>
      <form>
        <input
          type="text"
          value={productName}
          onChange={(e) => setProductName(e.target.value)}
          placeholder="Enter product name"
          id="productNameInput"
          name="productName"
          className="inputField"
        />
        <button type="button" onClick={handleSearch}>Search</button>
      </form>
      {results.length > 0 && (
        <table className="resultsTable">
          <thead>
            <tr>
              <th>Site</th>
              <th>Item Title</th>
              <th>Price</th>
            </tr>
          </thead>
          <tbody>
            {results.map((item, index) => (
              <tr key={index}>
                <td>{item.Site}</td>
                <td><a href={item['Item title name']} target="_blank" rel="noopener noreferrer">{item['Item title name']}</a></td>
                <td>{item['Price(USD)']}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      <style jsx>{`
        .container {
          min-height: 100vh;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          text-align: center;
          padding: 2rem;
        }

        .inputField {
          width: 70%;
          height: 100px;
          font-size: 100px;
          margin: 20px 0;
          padding: 20px;
          border-radius: 20px;
          border: 5px solid #04AA6D;
        }

        .resultsTable {
          width: 60%;
          border-collapse: collapse;
          box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
          border-radius: 400px;
          margin-top: 30px;
          font-size: 60px;
        }

        .resultsTable th, .resultsTable td {
          border: 1px solid #ddd;
          padding: 20px;
          text-align: left;
        }

        .resultsTable th {
          background-color: #04AA6D;
          color: white;
          font-size: 100px;
        }

        .resultsTable td {
          background-color: #f9f9f9;
        }

        .resultsTable th:first-child,
        .resultsTable td:first-child {
          border-top-left-radius: 10px;
          border-bottom-left-radius: 10px;
        }

        .resultsTable th:last-child,
        .resultsTable td:last-child {
          border-top-right-radius: 10px;
          border-bottom-right-radius: 10px;
        }

        button {
          margin-left: 15px;
          padding: 15px 40px;
          border: none;
          background-color: #04AA6D;
          color: white;
          font-size: 100px;
          cursor: pointer;
          border-radius: 10px;
          transition: background-color 0.3s ease;
        }

        button:hover {
          background-color: #218c5e;
        }

        h1 {
          font-size: 200px;
          font-weight: bold;
          color: #04AA6D;
          margin-bottom: 100px;
          text-align: center;
          text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
        }
      `}</style>
    </div>
  );
}
