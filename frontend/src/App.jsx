import React, { useState } from "react";
import Login from "./Login";
import Tasks from "./Tasks";

export default function App() {
  // Check if a token exists in localStorage to decide if user is authenticated
  const [auth, setAuth] = useState(localStorage.getItem("token") ? true : false);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Intern Assignment App</h1>
      {auth ? (
        <Tasks />
      ) : (
        <Login setAuth={setAuth} />
      )}
    </div>
  );
}