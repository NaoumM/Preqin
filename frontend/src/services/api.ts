import axios from "axios"
import type { Investor, Commitment } from "../types"

const BASE_URL = "http://127.0.0.1:8000/api"

export async function getInvestors(): Promise<Investor[]> {
  const response = await axios.get(`${BASE_URL}/investors`)
  return response.data
}

export async function getCommitments(investorName: string, assetClass: string | null): Promise<Commitment[]> {
  const params = assetClass ? { asset_class: assetClass } : {}
  const response = await axios.get(
    `${BASE_URL}/investors/${encodeURIComponent(investorName)}/commitments`,
    { params }
  )
  return response.data
}
