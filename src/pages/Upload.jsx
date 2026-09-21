import { Upload as UploadIcon } from 'lucide-react'

function Upload() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">Upload Audio</h1>
        <p className="text-muted-foreground">
          Upload an audio file for AI-assisted deception analysis
        </p>
      </div>

      <div className="rounded-xl border border-dashed border-border p-12 text-center">
        <UploadIcon className="mx-auto h-10 w-10 text-muted-foreground" />
        <p className="mt-4 text-sm text-muted-foreground">
          MediaUploader component will be implemented in Milestone 4
        </p>
      </div>
    </div>
  )
}

export default Upload