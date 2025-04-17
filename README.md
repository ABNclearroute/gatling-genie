# 🧞‍♂️ gatling-genie

**gatling-genie** is a Python-based CLI tool that uses LLMs (like GPT-4) to generate Java-based Gatling simulations from OpenAPI (Swagger) specifications. It intelligently chooses between Open Model (arrival rate) and Closed Model (concurrent users) based on the endpoint logic.

---

## Features

- Parse OpenAPI/Swagger JSON specs
- Use LLMs to auto-generate Gatling simulations (Java DSL)
- Automatically decide workload model (Open or Closed)
- Add realistic checks, feeders, and structure
- Does *not* run simulations or generate Maven projects — just clean simulation code

---
