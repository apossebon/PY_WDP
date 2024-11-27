from pathlib import Path
from task_extract.extract import extract_weather_data
import json

if __name__ == "__main__":
    # Load configurations and secrets
    configs = Path("configs/configs.json").read_text()
    secrets = Path("secrets/secrets.json").read_text()
    configs = json.loads(configs)
    secrets = json.loads(secrets)

    # Extract weather data
    data = extract_weather_data(configs, secrets)
    print(data)