import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from functions.functions import available_functions
from functions.call_function import call_function


def main():
    load_dotenv()
    args = sys.argv[0:]
    verbose = "--verbose" in sys.argv

    if len(args) < 2:
        print("Usage: agent [PROMPT}")
        print("    -- verbose return all the context messages")
        sys.exit(1)

    prompt = args[1]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    resp = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt, tools=[available_functions]
        ),
    )

    metadata = resp.usage_metadata
    if verbose and metadata:
        print(f"User prompt: {prompt}")
        print("Response tokens:", metadata.candidates_token_count)
        print("Prompt tokens:", metadata.prompt_token_count)

    print(f"Response: {resp.text}")
    function_responses = []
    if resp.function_calls:
        for function_call in resp.function_calls:
            result = call_function(function_call, verbose)
            if not result.parts or not result.parts[0].function_response:
                raise Exception("empty function call result")

            if verbose:
                print(f"-> {result.parts[0].function_response.response}")
            function_responses.append(result.parts[0])
        if not function_responses:
            raise Exception("no function responses generated, exiting.")


if __name__ == "__main__":
    main()
