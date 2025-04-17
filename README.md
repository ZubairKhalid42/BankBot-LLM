BankBot-LLM/
├── data/                  # Contains raw and cleaned banking documents
├── src/
│   ├── ingest/            # Scripts for reading, sanitizing, and preprocessing documents
│   ├── embedding/         # Code for generating and indexing vector embeddings
│   ├── llm/               # Model loading, fine-tuning, and inference logic
│   ├── ui/                # Frontend interface for user interaction
│   ├── guardrails/        # Guardrails and safety checks to protect LLM responses
│   └── utils/             # Helper functions and shared utilities
├── requirements.txt       # Python dependencies
