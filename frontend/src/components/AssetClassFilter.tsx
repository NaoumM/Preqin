import React from "react"
import type { Commitment } from "../types"

interface Props {
  value: string | null
  onChange: (val: string | null) => void
  commitments: Commitment[]
}

const AssetClassFilter: React.FC<Props> = ({ value, onChange, commitments }) => {
  const assetClasses = Array.from(
    new Set(commitments.map((c) => c.asset_class))
  )

  return (
    <div className="mb-4">
      <label className="block text-sm mb-1">Filter by Asset Class:</label>
      <select
        className="border px-3 py-2 rounded"
        value={value ?? ""}
        onChange={(e) => onChange(e.target.value || null)}
      >
        <option value="">All</option>
        {assetClasses.map((ac) => (
          <option key={ac} value={ac}>
            {ac}
          </option>
        ))}
      </select>
    </div>
  )
}

export default AssetClassFilter
