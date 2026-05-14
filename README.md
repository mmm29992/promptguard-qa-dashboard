# PromptGuard QA Dashboard

PromptGuard is an AI-centric QA automation dashboard for testing prompts, tracking pass/fail results, logging defects, and validating API/database workflows.

## Project Overview

This project is designed to simulate a QA workflow for AI-powered SaaS products. Users can submit prompts, define expected behavior, store prompt test cases, and track QA results through REST API endpoints.

The goal of this project is to demonstrate experience with backend development, REST APIs, SQL/database workflows, automated testing, CI/CD, cloud deployment, and QA automation concepts.

## Tech Stack

- Backend: Python, FastAPI
- Database: SQL
- Testing: Pytest
- CI/CD: GitHub Actions
- Frontend: React, TypeScript, Tailwind CSS
- Deployment: Vercel + Render/Railway

## Current Features

- FastAPI backend setup
- Health-check endpoint
- Create prompt test cases
- View all prompt test cases
- Search prompt test cases by ID
- Interactive API documentation through FastAPI Swagger UI

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Root API welcome message |
| GET | `/health` | Health-check endpoint |
| GET | `/prompts` | Returns all prompt test cases |
| POST | `/prompts` | Creates a new prompt test case |
| GET | `/prompts/{prompt_id}` | Returns one prompt test case by ID |

## Sample Prompt Test Case

```json
{
  "title": "Insurance Quote Prompt Test",
  "prompt_text": "Can I get car insurance if I do not currently have an active policy?",
  "expected_behavior": "The response should clearly explain general insurance requirements without making false guarantees or giving legal advice.",
  "category": "Insurance"
}