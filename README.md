#  Gatling Genie

**Gatling Genie** is a CLI tool that uses OpenAI's GPT models to generate Gatling (Java) performance test simulations from OpenAPI specifications. It simplifies the creation of realistic load testing scripts by interpreting your API spec and generating ready-to-use Gatling code.

---

## Features

- Parse OpenAPI YAML specs
- Automatically generate Gatling Java simulations
- Choose between Open and Closed workload models based on the endpoint
- Powered by GPT (supports `gpt-3.5-turbo` and `gpt-4`)

---

## Installation

1. Clone the repository:
2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python3 gatling_genie.py example.yaml --openai-api-key YOUR_OPENAI_API_KEY --model gpt-3.5-turbo
```

### Arguments

| Argument               | Description                          |
|------------------------|--------------------------------------|
| `example.yaml`         | Path to your OpenAPI spec (YAML)     |
| `--openai-api-key`     | Your OpenAI API key                  |
| `--model` _(optional)_ | LLM model to use (`gpt-3.5-turbo`, `gpt-4`) |

---

##  Output

- Generated simulation code will be printed in the terminal.
- You can redirect it to a file like:

```bash
python3 gatling_genie.py example.yaml --openai-api-key sk-... > CustomerApiSimulation.java
```

---

## Example OpenAPI YAML

```yaml
paths:
  /customers:
    post:
      summary: Create a new customer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                email:
                  type: string
      responses:
        '201':
          description: Created
```

---

## Powered by OpenAI

This tool uses the [OpenAI Python SDK](https://github.com/openai/openai-python) under the hood.
