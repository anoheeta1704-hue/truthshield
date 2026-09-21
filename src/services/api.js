/**
 * TruthShield API Client
 *
 * Handles communication between the React frontend and FastAPI backend.
 *
 * Configuration:
 *   Set VITE_API_URL in .env to point to the backend server.
 *   Default: http://localhost:8000
 *
 * Endpoint implementations will be connected in their respective milestones.
 */

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

/**
 * Base fetch wrapper with error handling.
 */
async function apiFetch(endpoint, options = {}) {
  const url = `${API_BASE_URL}${endpoint}`

  try {
    const response = await fetch(url, {
      ...options,
      headers: {
        ...options.headers,
      },
    })

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: response.statusText }))
      throw new Error(error.detail || `API error: ${response.status}`)
    }

    return await response.json()
  } catch (error) {
    if (error.name === 'TypeError' && error.message === 'Failed to fetch') {
      throw new Error('Unable to connect to the TruthShield backend. Is the server running?')
    }
    throw error
  }
}

/**
 * GET /health — Health check
 */
export async function checkHealth() {
  return apiFetch('/health')
}

/**
 * POST /analyze/full — Upload audio for full analysis
 * Implementation: Milestone 4
 */
export async function analyzeAudio(file) {
  const formData = new FormData()
  formData.append('file', file)

  return apiFetch('/analyze/full', {
    method: 'POST',
    body: formData,
  })
}

/**
 * GET /sessions — Get session history
 * Implementation: Milestone 9
 */
export async function getSessions() {
  return apiFetch('/sessions')
}

/**
 * POST /stream/chunk — Send audio chunk for live analysis
 * Implementation: Milestone 10
 */
export async function sendStreamChunk(chunk, sessionId) {
  const formData = new FormData()
  formData.append('chunk', chunk)
  if (sessionId) formData.append('session_id', sessionId)

  return apiFetch('/stream/chunk', {
    method: 'POST',
    body: formData,
  })
}

export { API_BASE_URL }
