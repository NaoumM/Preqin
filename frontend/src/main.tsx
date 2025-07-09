import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import App from './App.tsx'
import InvestorDetail from './components/InvestorDetail.tsx'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/investor/:name" element={<InvestorDetail />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
)
