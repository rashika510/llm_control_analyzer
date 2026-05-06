# LLM Control Analyzer

This repository contains a containerized **FastAPI** service that leverages **LLMs** to automatically map security incidents to relevant risk controls. Designed as a sanitized, enterprise-grade demo, it allows you to test incident-to-control classification logic using synthetic data.

## Features
- **LLM-Powered Matching:** Uses an LLM to analyze incidents and recommend the best-fit risk control.
- **FastAPI Backend:** Provides a clean, high-performance API surface.
- **Dockerized:** Fully containerized for consistent local deployment and testing.
- **Resilient Design:** Includes a mock response fallback mechanism so the API remains functional even without an API key.

## Architecture
The service processes requests by accepting an incident description, processing it against a catalog of synthetic risk controls, and returning a structured JSON response containing the matching control, confidence score, and explanation.

## Local Setup
1. **Clone the repository.**
2. **Install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run the service:**
   ```bash
   uvicorn src.app:app --reload --host 127.0.0.1 --port 8000
   ```
4. **Access the API:** Navigate to `http://127.0.0.1:8000/docs` to interact with the API documentation and test endpoints.

## Docker Deployment
Build and run the service in a containerized environment:

```bash
# Build the container
docker build -t llm-control-analyzer .

# Run the container
docker run --rm -p 8000:8000 llm-control-analyzer
```

## How to Test
Once the service is running, navigate to the Swagger UI at `http://127.0.0.1:8000/docs`. Under the `POST /match` endpoint, try the following test input:

```json
{
  "incident": "An intern was found to have admin-level access to the production database."
}
```

*Note: This is a demonstration project using synthetic data only and is intended for portfolio and testing purposes.*
