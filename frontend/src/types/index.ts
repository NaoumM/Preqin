export interface Investor {
  id: number
  name: string
  type: string
  date_added: string
  address: string
  total_commitment: string
}

export interface Commitment {
  id: number
  asset_class: string
  currency: string
  amount: string
}
