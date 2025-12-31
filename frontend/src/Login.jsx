import React, { useState } from "react";
import API from "./api"; // axios instance

export default function Login({ setAuth }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await API.post("/login", {
        email,
        password,
      });
      localStorage.setItem("token", response.data.access_token);
      setAuth(true);
    } catch (error) {
      alert("Login failed. Please check your credentials.");
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await API.post("/register", {
        email,
        password,
      });
      alert("Registration successful! You can now log in.");
    } catch (error) {
      alert("Registration failed. Try again.");
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "auto", padding: "20px" }}>
      <h2>Login / Register</h2>
      <form>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{ display: "block", marginBottom: "10px", width: "100%" }}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{ display: "block", marginBottom: "10px", width: "100%" }}
        />
        <button onClick={handleLogin} style={{ marginRight: "10px" }}>
          Login
        </button>
        <button onClick={handleRegister}>Register</button>
      </form>
    </div>
  );
}