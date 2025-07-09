import React from "react"
import type { Investor } from "../types"
import { useNavigate } from "react-router-dom"

interface Props {
  investors: Investor[]
  selected: Investor | null
  onSelect: (investor: Investor) => void
}

const InvestorList: React.FC<Props> = ({ investors, selected, onSelect }) => {
  const navigate = useNavigate()

  const handleClick = (inv: Investor) => {
    onSelect(inv)
    navigate(`/investor/${inv.name}`, { state: inv })
  }

  return (
    <table className="w-full text-sm border border-gray-300">
      <thead className="bg-gray-100">
        <tr>
          <th className="text-left px-4 py-2 border border-gray-300">ID</th>
          <th className="text-left px-4 py-2 border border-gray-300">Name</th>
          <th className="text-left px-4 py-2 border border-gray-300">Type</th>
          <th className="text-left px-4 py-2 border border-gray-300">Date Added</th>
          <th className="text-left px-4 py-2 border border-gray-300">Address</th>
          <th className="text-left px-4 py-2 border border-gray-300">Total Commitment</th>
        </tr>
      </thead>
      <tbody>
        {investors.map((inv) => (
          <tr
            key={inv.id}
            className={`cursor-pointer hover:bg-gray-50 ${
              selected?.id === inv.id ? "bg-blue-100 font-semibold" : ""
            }`}
            onClick={() => handleClick(inv)}
          >
            <td className="px-4 py-2 border border-gray-300">{inv.id}</td>
            <td className="px-4 py-2 border border-gray-300">{inv.name}</td>
            <td className="px-4 py-2 border border-gray-300">{inv.type}</td>
            <td className="px-4 py-2 border border-gray-300">{inv.date_added}</td>
            <td className="px-4 py-2 border border-gray-300">{inv.address}</td>
            <td className="px-4 py-2 border border-gray-300">${inv.total_commitment}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}

export default InvestorList
