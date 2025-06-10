import React from 'react'
import { useNavigate } from 'react-router'
import { createSentence } from '../services/ApiService'
import { Sentence } from '../types'

function HomePage() {
  const testSentenceToCreate = {
    text: 'This is a sentence',
    words: [
      { word_text: 'This', order: 1 },
      { word_text: 'is', order: 2 },
      { word_text: 'a', order: 3 },
      { word_text: 'sentence', order: 4 },
    ],
  }

  const navigate = useNavigate()
  const createNewSentence = () => {
    createSentence(testSentenceToCreate)
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
