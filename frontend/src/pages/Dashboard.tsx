import React, { useState, useEffect } from "react"
import { getInvestors, getCommitments } from "../services/api"
import type { Investor, Commitment } from "../types"
import InvestorList from "../components/InvestorList"
import CommitmentTable from "../components/CommitmentTable"
import AssetClassFilter from "../components/AssetClassFilter"

const Dashboard: React.FC = () => {
  const [investors, setInvestors] = useState<Investor[]>([])
  const [selectedInvestor, setSelectedInvestor] = useState<Investor | null>(null)
  const [commitments, setCommitments] = useState<Commitment[]>([])
  const [assetClass, setAssetClass] = useState<string | null>(null)

  useEffect(() => {
    getInvestors().then(setInvestors)
  }, [])

  useEffect(() => {
    if (selectedInvestor) {
      getCommitments(selectedInvestor.name, assetClass).then(setCommitments)
    }
  }, [selectedInvestor, assetClass])

  return (
    <div className="flex h-screen bg-gray-50">
      <div className="w-1/3 bg-white border-r shadow p-4 overflow-y-auto">
        <h1 className="text-2xl font-bold mb-4">Investors</h1>
        <InvestorList
          investors={investors}
          selected={selectedInvestor}
          onSelect={setSelectedInvestor}
        />
      </div>
      <div className="w-2/3 p-6">
        {selectedInvestor ? (
          <>
            <h2 className="text-xl font-semibold mb-4">
              {selectedInvestor.name} Commitments
            </h2>
            <AssetClassFilter
              value={assetClass}
              onChange={setAssetClass}
              commitments={commitments}
            />
            <CommitmentTable commitments={commitments} />
          </>
        ) : (
          <p className="text-gray-600">Select an investor to view commitments.</p>
        )}
      </div>
    </div>
  )
}

export default Dashboard
