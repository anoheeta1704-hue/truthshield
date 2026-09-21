import { create } from 'zustand'

/**
 * TruthShield Global State Store
 *
 * Manages application state using Zustand.
 * Slices will be expanded as features are implemented.
 */
const useStore = create((set) => ({
  // ── Analysis State ──
  analysisResult: null,
  isAnalyzing: false,
  analysisError: null,

  // ── Session History State (Milestone 9) ──
  sessions: [],
  isLoadingSessions: false,

  // ── Live Recording State (Milestone 10) ──
  isRecording: false,
  liveSessionId: null,

  // ── Actions ──
  setAnalysisResult: (result) => set({ analysisResult: result, analysisError: null }),
  setIsAnalyzing: (isAnalyzing) => set({ isAnalyzing }),
  setAnalysisError: (error) => set({ analysisError: error, isAnalyzing: false }),
  resetAnalysis: () => set({
    analysisResult: null,
    isAnalyzing: false,
    analysisError: null,
  }),

  setSessions: (sessions) => set({ sessions }),
  setIsLoadingSessions: (isLoadingSessions) => set({ isLoadingSessions }),

  setIsRecording: (isRecording) => set({ isRecording }),
  setLiveSessionId: (liveSessionId) => set({ liveSessionId }),
}))

export default useStore
