import { Radio } from 'lucide-react'

function Live() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">Live Recording</h1>
        <p className="text-muted-foreground">
          Record audio live for real-time AI-assisted analysis
        </p>
      </div>

      <div className="rounded-xl border border-dashed border-border p-12 text-center">
        <Radio className="mx-auto h-10 w-10 text-muted-foreground" />
        <p className="mt-4 text-sm text-muted-foreground">
          LiveRecord component will be implemented in Milestone 10
        </p>
      </div>
    </div>
  )
}

export default Live