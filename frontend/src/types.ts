export interface Word {
  id?: string
  word_text: string
  order: number
  giphyURL?: string
}

export interface Sentence {
  id?: string
  frontend_lookup_id?: string
  text: string
  words: Word[]
}
