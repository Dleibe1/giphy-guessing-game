import React from 'react'
import { Routes, Route } from 'react-router'
import GiphyList from './components/GiphyList'
import HomePage from './components/HomePage'
import './App.css'

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/giphy-sentence-creator/:sentenceId" element={<GiphyList />} />
    </Routes>
  )
}

export default App
