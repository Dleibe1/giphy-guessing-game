import { Sentence } from '../types'

export const getHighestSentenceId = async () => {
  try {
    const response = await fetch(`/api/v1/highest-sentence-id`)
    if (!response.ok) {
      const errorMessage = `${response.status} (${response.statusText})`
      throw new Error(errorMessage)
    }
    return await response.json()
  } catch (error) {
    if (error instanceof Error) {
      console.error(`Error in Fetch: ${error.message}`)
    } else {
      console.error(`Error in Fetch: ${error}`)
    }
    throw error
  }
}

export const createSentence = async (sentenceData: Sentence) => {
  try {
    const requestBody = sentenceData
    const response = await fetch(`/api/v1/sentence/`, {
      method: 'POST',
      headers: new Headers({
        'Content-Type': 'application/json',
      }),
      body: JSON.stringify(requestBody),
    })
    if (!response.ok) {
      const errorMessage = `${response.status} (${response.statusText})`
      throw new Error(errorMessage)
    }
    return await response.json()
  } catch (error) {
    if (error instanceof Error) {
      console.error(`Error in Fetch: ${error.message}`)
    } else {
      console.error(`Error in Fetch: ${error}`)
    }
    throw error
  }
}

export const updateSentence = async (sentenceData: Sentence) => {
  try {
    const requestBody = sentenceData
    const response = await fetch(`/api/v1/sentence/`, {
      method: 'POST',
      headers: new Headers({
        'Content-Type': 'application/json',
      }),
      body: JSON.stringify(requestBody),
    })
    if (!response.ok) {
      const errorMessage = `${response.status} (${response.statusText})`
      throw new Error(errorMessage)
    }
    return await response.json()
  } catch (error) {
    if (error instanceof Error) {
      console.error(`Error in Fetch: ${error.message}`)
    } else {
      console.error(`Error in Fetch: ${error}`)
    }
    throw error
  }
}

export const getSentence = async (id: string) => {
  try {
    const response = await fetch(`/api/v1/sentence/${id}`)
    if (!response.ok) {
      const errorMessage = `${response.status} (${response.statusText})`
      throw new Error(errorMessage)
    }
    return await response.json()
  } catch (error) {
    if (error instanceof Error) {
      console.error(`Error in Fetch: ${error.message}`)
    } else {
      console.error(`Error in Fetch: ${error}`)
    }
    throw error
  }
}

export const getGiphy = async (searchTerm: string) => {
  try {
    const response = await fetch(`/api/v1/giphy-proxy/${searchTerm}`, {
      method: 'POST',
      headers: new Headers({
        'Content-Type': 'application/json',
      }),
      body: JSON.stringify({ searchTerm }),
    })
    if (!response.ok) {
      const errorMessage = `${response.status} (${response.statusText})`
      throw new Error(errorMessage)
    }
    return await response.json()
  } catch (error) {
    if (error instanceof Error) {
      console.error(`Error in Fetch: ${error.message}`)
    } else {
      console.error(`Error in Fetch: ${error}`)
    }
    throw error
  }
}
