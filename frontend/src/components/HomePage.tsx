import React from 'react'
import { useNavigate } from 'react-router'
import { upsertSentence } from '../services/ApiService'
import { Sentence } from '../types'

function HomePage() {
  const navigate = useNavigate()
  const createNewSentence = () => {
    upsertSentence(null)
      .then((sentenceData: Sentence) => {
        navigate(`/giphy-sentence-creator/${sentenceData.id}`)
      })
      .catch((error) => {
        console.log(error)
      })
  }
  return (
    <button onClick={createNewSentence} type="button">
      New Sentence
    </button>
  )
}

export default HomePage
