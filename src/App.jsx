import { Routes, Route, Navigate } from 'react-router-dom'
import Layout from './components/Layout'
import Upload from './pages/Upload'
import Live from './pages/Live'
import History from './pages/History'
import Dashboard from './pages/Dashboard'

function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route index element={<Navigate to="/upload" replace />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/live" element={<Live />} />
        <Route path="/history" element={<History />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Route>
    </Routes>
  )
}

export default App
