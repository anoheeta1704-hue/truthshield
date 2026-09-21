# TruthShield

TruthShield is an AI-based audio deception analysis system. It analyzes audio conversations using multiple AI/ML signals (Voice Stress, NLP Inconsistency, Voice Clone Detection) and combines them into a unified analysis result.

## Development

The project consists of a React (Vite) frontend and a FastAPI backend.

### Frontend Setup

```bash
npm install
npm run dev
```

### Backend Setup (Milestone 2+)

```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Unix: source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

*Note: Models and datasets will be required for later milestones. See the respective service documentation in `backend/app/services/` for details.*
