from pathlib import Path
from extract import extract_weather_data
import yaml

if __name__ == "__main__":
    # Load configurations and secrets
    configs = Path("configs/task_extract/base.yaml").read_text()
    secrets = Path("secrets/task_extract/base.yaml").read_text()
    configs = yaml.safe_load(configs)
    secrets = yaml.safe_load(secrets)

    # Extract weather data
    data = extract_weather_data(configs, secrets)
    if (data != None):
        print(data)