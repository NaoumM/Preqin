import React from "react"
import type { Commitment } from "../types"

interface Props {
  commitments: Commitment[]
}

const CommitmentTable: React.FC<Props> = ({ commitments }) => {
  return (
    <table className="w-full table-auto border-collapse border border-gray-300">
      <thead className="bg-gray-100">
        <tr>
          <th className="px-4 py-2 border border-gray-300 text-left">Id</th>
          <th className="px-4 py-2 border border-gray-300 text-left">Asset Class</th>
          <th className="px-4 py-2 border border-gray-300 text-left">Currency</th>
          <th className="px-4 py-2 border border-gray-300 text-left">Amount</th>
        </tr>
      </thead>
      <tbody>
        {commitments.map((c) => (
          <tr key={c.id} className="hover:bg-gray-50">
            <td className="px-4 py-2 border border-gray-300">{c.id}</td>
            <td className="px-4 py-2 border border-gray-300">{c.asset_class}</td>
            <td className="px-4 py-2 border border-gray-300">{c.currency}</td>
            <td className="px-4 py-2 border border-gray-300">£{c.amount}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}

export default CommitmentTable
