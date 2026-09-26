install:
	python -m pip install -r requirements.txt
run:
	python scripts/generate_data.py && python quality/checks.py && python scripts/run_pipeline.py
test:
	pytest -q
