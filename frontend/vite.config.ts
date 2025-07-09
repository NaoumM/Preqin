import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import { fileURLToPath } from "url"
import { dirname, resolve } from "path"

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: resolve(__dirname, "../backend/app/static"),
    emptyOutDir: true,
  },
  server: {
    watch: {
      ignored: ["**/.venv/**", "**/db/**", "**/__pycache__/**"],
    },
  },
})
