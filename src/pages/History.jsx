import { Clock } from 'lucide-react'

function History() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">Session History</h1>
        <p className="text-muted-foreground">
          View previous analysis sessions and results
        </p>
      </div>

      <div className="rounded-xl border border-dashed border-border p-12 text-center">
        <Clock className="mx-auto h-10 w-10 text-muted-foreground" />
        <p className="mt-4 text-sm text-muted-foreground">
          SessionHistory component will be implemented in Milestone 9
        </p>
      </div>
    </div>
  )
}

export default History