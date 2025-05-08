export const getSentence = async (id: number) => {
  try {
    const response = await fetch(`/api/v1/sentence/${id}`)
    if (!response.ok) {
      const errorMessage = `${response.status} (${response.statusText})`
      const error = new Error(errorMessage)
      throw error
    }
  } catch (error) {
    if (error instanceof Error) {
      console.error(`Error in Fetch: ${error.message}`)
    } else {
      console.error(`Error in Fetch: ${String(error)}`)
    }
    throw error
  }
}
