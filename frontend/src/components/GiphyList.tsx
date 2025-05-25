import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router'
import { Sentence } from '../types'
import { getSentence, upsertSentence } from '../services/ApiService'
/*  If it's a new sentence:
      check the database for the highest ID
      redirect to /translate-to-gif/:sentenceId"

  When user is finished: 
    Delete the sentence or save it in "my sentences"
*/
function GiphyList() {
  const { sentenceId } = useParams()
  const [errors, setErrors] = useState({})
  const [sentence, setSentence] = useState<Sentence>({
    id: sentenceId!,
    text: 'hello',
    words: [],
  })
  useEffect(() => {
    getSentence(sentenceId!)
      .then((sentenceData: Sentence) => {
        if (sentenceData.id === sentenceId) {
          setSentence(sentenceData)
          setErrors({ wrongURLError: 'Wrong URL for this sentence' })
        } else {
          console.log('no errors')
        }
      })
      .catch((error) => {
        console.log(error)
      })
  }, [sentenceId])
  console.log(sentence)
  const sentenceText = 'hello'

  useEffect(() => {
    upsertSentence({ ...sentence, text: sentenceText }).then((sentenceData) => {
      setSentence(sentenceData)
    })
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const hasErrors = Object.keys(errors).length > 0

  if (hasErrors) {
    console.log('Errors exist:', errors)
  }
  return <div>{sentence.text}</div>
}

export default GiphyList
