install:
	pip install -r requirements.txt

lint:
	flake8 . --ignore=E501,W503

format:
	black .

test:
	pytest tests/

run-api:
	uvicorn app.api:app --reload

run-ui:
	python gradio_ui/interface.py

build:
	docker build -t llama-agent .

