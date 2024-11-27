import pytest
from unittest.mock import patch, Mock
import requests
from src.task_extract.extract import extract_weather_data


def test_extract_weather_data_success():
    configs = {"api": {"url": "http://api.openweathermap.org/data/2.5/weather", "query": "Curitiba"}}
    secrets = {"api": {"appid": "fake_appid"}}
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"weather": "sunny"}

    with patch('requests.get', return_value=mock_response):
        data = extract_weather_data(configs, secrets)
        assert data == {"weather": "sunny"}

def test_extract_weather_data_request_exception():
    configs = {"api": {"url": "http://api.openweathermap.org/data/2.5/weather", "query": "Curitiba"}}
    secrets = {"api": {"appid": "fake_appid"}}

    with patch('requests.get', side_effect=requests.exceptions.RequestException):
        data = extract_weather_data(configs, secrets)
        assert data is None

def test_extract_weather_data_http_error():
    configs = {"api": {"url": "http://api.openweathermap.org/data/2.5/weather", "query": "Curitiba"}}
    secrets = {"api": {"appid": "fake_appid"}}

    with patch('requests.get', side_effect=requests.exceptions.HTTPError):
        data = extract_weather_data(configs, secrets)
        assert data is None

def test_extract_weather_data_connection_error():
    configs = {"api": {"url": "http://api.openweathermap.org/data/2.5/weather", "query": "Curitiba"}}
    secrets = {"api": {"appid": "fake_appid"}}

    with patch('requests.get', side_effect=requests.exceptions.ConnectionError):
        data = extract_weather_data(configs, secrets)
        assert data is None

def test_extract_weather_data_timeout_error():
    configs = {"api": {"url": "http://api.openweathermap.org/data/2.5/weather", "query": "Curitiba"}}
    secrets = {"api": {"appid": "fake_appid"}}

    with patch('requests.get', side_effect=requests.exceptions.Timeout):
        data = extract_weather_data(configs, secrets)
        assert data is None

def test_extract_weather_data_value_error():
    configs = {"api": {"url": "http://api.openweathermap.org/data/2.5/weather", "query": "Curitiba"}}
    secrets = {"api": {"appid": "fake_appid"}}
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.side_effect = ValueError

    with patch('requests.get', return_value=mock_response):
        data = extract_weather_data(configs, secrets)
        assert data is None

def test_extract_weather_data_unexpected_error():
    configs = {"api": {"url": "http://api.openweathermap.org/data/2.5/weather", "query": "Curitiba"}}
    secrets = {"api": {"appid": "fake_appid"}}

    with patch('requests.get', side_effect=Exception):
        data = extract_weather_data(configs, secrets)
        assert data is None