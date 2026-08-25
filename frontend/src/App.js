import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import './App.css';

// Pages
const LoginPage = () => <div className='p-4'><h1>Login Page</h1><p>Coming soon...</p></div>;
const DashboardPage = () => <div className='p-4'><h1>Dashboard</h1><p>Coming soon...</p></div>;
const TicketsPage = () => <div className='p-4'><h1>Tickets</h1><p>Coming soon...</p></div>;
const CreateTicketPage = () => <div className='p-4'><h1>Create Ticket</h1><p>Coming soon...</p></div>;
const NotFoundPage = () => <div className='p-4'><h1>404 - Page Not Found</h1></div>;

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Check if user is logged in
    const token = localStorage.getItem('access_token');
    setIsAuthenticated(!!token);
  }, []);

  return (
    <Router basename="/support-ticket-hub">
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/dashboard" element={isAuthenticated ? <DashboardPage /> : <Navigate to="/login" />} />
        <Route path="/tickets" element={isAuthenticated ? <TicketsPage /> : <Navigate to="/login" />} />
        <Route path="/tickets/new" element={isAuthenticated ? <CreateTicketPage /> : <Navigate to="/login" />} />
        <Route path="/" element={isAuthenticated ? <Navigate to="/dashboard" /> : <Navigate to="/login" />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </Router>
  );
}

export default App;
