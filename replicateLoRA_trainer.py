import os
from dotenv import load_dotenv
import replicate

# Load environment variables from .env file
load_dotenv()

# Get the API token from the environment variable
api_token = os.getenv("REPLICATE_API_TOKEN")

# Configure the Replicate client with the API token
replicate.Client(api_token=api_token)

# Now you can use the replicate object to interact with the API
training = replicate.trainings.create(
    version="ostris/flux-dev-lora-trainer:4ffd32160efd92e956d39c5338a9b8fbafca58e03f791f6d8011f3e20e8ea6fa",
    input={
        "input_images": open("/Users/spartan/Downloads/Archive_AmeyaPics.zip", "rb"),
        "steps": 1000,
    },
    destination="ameya690/fluxtrainer2"
)

print(f"Training started: {training.status}")
print(f"Training URL: https://replicate.com/p/{training.id}")

print(f"Training status now: {training.status}")

# import replicate

# training = replicate.trainings.create(
#   # You need to create a model on Replicate that will be the destination for the trained version.
#   destination="ameya690/fluxtrainer1",
#   version="ostris/flux-dev-lora-trainer:6029be968faad5bcc6d44e827af89eee22d61c35f3b5d0950751815506a9db04",
#   input={
#     "steps": 1000,
#     "lora_rank": 16,
#     "optimizer": "adamw8bit",
#     "batch_size": 1,
#     "resolution": "512,768,1024",
#     "autocaption": True,
#     "input_images": "https://ibb.co/fCjv7gh", "https://ibb.co/QMG3GXr", "https://ibb.co/kJb2RPF",
#     "trigger_word": "TOK",
#     "learning_rate": 0.0004,
#     "wandb_project": "flux_train_replicate",
#     "wandb_save_interval": 100,
#     "caption_dropout_rate": 0.05,
#     "cache_latents_to_disk": False,
#     "wandb_sample_interval": 100
#   },
# )

