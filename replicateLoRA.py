import os
from dotenv import load_dotenv
import replicate

# Load environment variables from .env file
load_dotenv()

# Get the API token from the environment variable
api_token = os.getenv("REPLICATE_API_TOKEN")

# Configure the Replicate client with the API token
replicate.Client(api_token=api_token)

output = replicate.run(
    "ameya690/fluxtrainer1",
    input={
        "prompt": "A portrait photo behind a space station, bad 70s food",
        "num_inference_steps": 28,
        "guidance_scale": 7.5,
        "model": "dev",
    }
)

print(f"Generated image URL: {output}")

