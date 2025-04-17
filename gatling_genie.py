import yaml
import click
from openai import OpenAI

# Analyze OpenAPI spec using OpenAI
def analyze_openapi_spec_with_openai(openapi_spec: str, api_key: str, model: str):
    client = OpenAI(api_key=api_key)

    prompt = f"""
    You are an expert in analyzing OpenAPI specifications. Please review the following OpenAPI specification and provide a detailed breakdown in the following structure:

    1. **Endpoints (Paths)**: List all available API endpoints and their corresponding HTTP methods (GET, POST, PUT, DELETE, etc.).
    2. **Parameters**: For each endpoint, identify the request parameters (query params, path params, headers, and request body).
    3. **Responses**: For each endpoint, describe the expected response status codes and the structure of the response body.
    4. **Authentication Requirements**: Identify any authentication (e.g., OAuth, API keys) that the API requires.

    Specification:
    {openapi_spec}
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert Gatling simulation generator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


def decide_workload_model(openapi_spec: str, api_key: str, model: str):
    client = OpenAI(api_key=api_key)

    prompt = f"""
    You are an expert in performance testing. Based on the provided OpenAPI specification, decide whether an **Open Model** or **Closed Model** is better suited for performance testing. 

    - **Open Model**: Suitable when traffic is expected to be predictable, and the number of requests per second can be controlled.
    - **Closed Model**: Suitable when simulating a fixed number of concurrent users is critical to test system behavior under load.

    OpenAPI specification:
    {openapi_spec}
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert Gatling simulation generator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


def generate_simulation_with_openai(endpoints_summary, model_type, api_key: str, model: str):
    client = OpenAI(api_key=api_key)

    prompt = f"""
    Based on the following OpenAPI endpoints and workload model (either 'Open' or 'Closed'), generate a complete Gatling simulation in Java:
    
    Endpoints:
    {endpoints_summary}
    
    Model type: {model_type}
    
    Please generate Java code for a Gatling simulation where each endpoint is tested with the correct HTTP method and request body if applicable. Use the Open/Closed model as appropriate.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert Gatling simulation generator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


def load_openapi_spec(file_path: str):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


@click.command()
@click.argument('openapi_spec_path', type=click.Path(exists=True))
@click.option('--openai-api-key', required=True, help="Your OpenAI API key")
@click.option('--model', default='gpt-3.5-turbo', help="OpenAI model to use (e.g. gpt-3.5-turbo or gpt-4)")
@click.option('--output-file', default='generated_simulation.java', help="Output file for the generated Gatling simulation")
def generate_gatling_simulation(openapi_spec_path, openai_api_key, model, output_file):
    """
    gatling-genie: A CLI tool to generate Gatling simulations using OpenAPI specs + OpenAI.
    """

    print("Loading OpenAPI spec...")
    openapi_spec = load_openapi_spec(openapi_spec_path)

    print("Analyzing OpenAPI spec with OpenAI...")
    analysis = analyze_openapi_spec_with_openai(openapi_spec, openai_api_key, model)
    print("\nAnalysis:\n", analysis)

    print("\nDeciding workload model (Open/Closed)...")
    model_type = decide_workload_model(openapi_spec, openai_api_key, model)
    print("\nChosen Workload Model:", model_type)

    print("\n💻 Generating Gatling simulation code...")
    simulation_code = generate_simulation_with_openai(analysis, model_type, openai_api_key, model)
    print("\nGenerated Simulation Code:\n", simulation_code)

    print(f"\nWriting simulation to file: {output_file}")
    with open(output_file, 'w') as file:
        file.write(simulation_code)

    print("\nDone! Your Gatling simulation has been generated.")


if __name__ == '__main__':
    generate_gatling_simulation()
