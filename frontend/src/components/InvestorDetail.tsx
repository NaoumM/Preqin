import React, { useEffect, useState } from "react"
import { useLocation, useParams, useNavigate } from "react-router-dom"
import type { Investor, Commitment } from "../types"
import { getCommitments } from "../services/api"
import AssetClassFilter from "./AssetClassFilter"
import CommitmentTable from "./CommitmentTable"

const InvestorDetail: React.FC = () => {
  const { name } = useParams()
  const location = useLocation()
  const navigate = useNavigate()

  const investor = location.state as Investor | null
  const [commitments, setCommitments] = useState<Commitment[]>([])
  const [assetClass, setAssetClass] = useState<string | null>(null)

  useEffect(() => {
    if (name) {
      getCommitments(name, assetClass).then(setCommitments)
    }
  }, [name, assetClass])

  if (!investor) {
    return (
      <div className="p-4">
        <p>Investor not found.</p>
        <button
          className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
          onClick={() => navigate("/")}
        >
          ← Back
        </button>
      </div>
    )
  }

  return (
    <div className="p-6">
      <button
        className="mb-4 px-4 py-2 bg-blue-500 text-white rounded"
        onClick={() => navigate("/")}
      >
        ← Back
      </button>

      <h2 className="text-2xl font-bold mb-2">{investor.name} Commitments</h2>
      <AssetClassFilter
        value={assetClass}
        onChange={setAssetClass}
        commitments={commitments}
      />
      <CommitmentTable commitments={commitments} />
    </div>
  )
}

export default InvestorDetail
