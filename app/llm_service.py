# app/llm_service.py
import subprocess

def query_ollama(prompt: str) -> str:
    """
    Query the locally installed Ollama LLM using CLI.
    
    This function invokes the Ollama CLI (e.g., via `ollama run llama3.2:3b "<prompt>"`)
    and captures the output. Make sure that the Ollama CLI is installed and in the PATH.
    
    Adjust the model name and CLI arguments as needed.
    """
    model_name = "llama3.2:3b"  # load llama3.2:3b model
    try:
        # Construct the command.
        # Example: ollama run llama-3.2 "prompts here"
        command = ["ollama", "run", model_name, prompt]
        # Run the command and capture output.
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        if not output:
            raise ValueError("No output received from Ollama CLI.")
        return output
    except subprocess.CalledProcessError as e:
        # Include stderr in the error message for debugging.
        raise RuntimeError(f"Ollama CLI call failed: {e.stderr}") from e
