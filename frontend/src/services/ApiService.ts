export const getSentence = async (id: number) => {
  try {
    const response = await fetch(`/api/v1/sentence/${id}/`)
    if (!response.ok) {
      const errorMessage = `${response.status} (${response.statusText})`
      throw new Error(errorMessage)
    }
    return await response.json()
  } catch (error) {
    if (error instanceof Error) {
      console.error(`Error in Fetch: ${error.message}`)
    } else {
      console.error(`Error in Fetch: ${String(error)}`)
    }
    throw error
  }
}

// export const upsertSentence = async (id: number, text: string) => {
//   try {
//     const response = await fetch(`/api/v1/sentence/${id}`, {
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({ text }),
//     })
//   } catch (error) {}
// }
