import React, { useState } from "react";
import { createAccount } from "../api/accountApi";

const AccountForm = () => {
  const [accountType, setAccountType] = useState("savings");
  const [initialDeposit, setInitialDeposit] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");
    setError("");

    try {
      const data = await createAccount({
        account_type: accountType,
        initial_deposit: parseFloat(initialDeposit),
      });
      setMessage(`Account Created! Account Number: ${data.account_number}`);
      setInitialDeposit("");
      setAccountType("savings");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "50px auto", textAlign: "center" }}>
      <h2>Create New Account</h2>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: "15px" }}>
          <label>Account Type:</label>
          <select
            value={accountType}
            onChange={(e) => setAccountType(e.target.value)}
          >
            <option value="savings">Savings</option>
            <option value="current">Current</option>
            <option value="fd">Fixed Deposit (FD)</option>
          </select>
        </div>

        <div style={{ marginBottom: "15px" }}>
          <label>Initial Deposit:</label>
          <input
            type="number"
            value={initialDeposit}
            onChange={(e) => setInitialDeposit(e.target.value)}
            placeholder="Enter initial deposit"
            required
          />
        </div>

        <button type="submit">Create Account</button>
      </form>

      {message && <p style={{ color: "green" }}>{message}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default AccountForm;
