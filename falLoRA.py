from dotenv import load_dotenv
import fal_client

# Load environment variables from .env file
load_dotenv()

handler = fal_client.submit(
    "fal-ai/flux-lora",
    arguments={
        "prompt": "a male model standing behind pyramids",
        "model_name": None,
        "loras": [{
                "path": "https://storage.googleapis.com/fal-flux-lora/c381c8f968954209b8b1af3332dea783_pytorch_lora_weights.safetensors",
                "scale": 1
            }],
        "embeddings": []
    },
)

result = handler.get()
print(result)