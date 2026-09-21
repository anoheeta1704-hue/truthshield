import { BarChart3 } from 'lucide-react'

function Dashboard() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">Analysis Dashboard</h1>
        <p className="text-muted-foreground">
          View detailed analysis results and score breakdowns
        </p>
      </div>

      <div className="rounded-xl border border-dashed border-border p-12 text-center">
        <BarChart3 className="mx-auto h-10 w-10 text-muted-foreground" />
        <p className="mt-4 text-sm text-muted-foreground">
          Dashboard components (TruthMeterGauge, BreakdownPanel, FraudAlertBanner)
          will be implemented in Milestone 8
        </p>
      </div>
    </div>
  )
}

export default Dashboard
