import React from 'react'
import { Routes, Route } from 'react-router'
import TestComponent from './components/TestComponent'
import './App.css'

function App() {
  return (
    <Routes>
      <Route path="/" element={<TestComponent />} />
    </Routes>
  )
}

export default App
