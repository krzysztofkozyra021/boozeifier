.PHONY: help install run fix lint clean freeze

help:
	@echo "----------------------------------------------------------------"
	@echo "PROJECT MANAGEMENT - ORBITAL SIMULATOR"
	@echo "----------------------------------------------------------------"
	@echo "make install  - Install dependencies from requirements.txt"
	@echo "make freeze   - Save installed packages to requirements.txt"
	@echo "make run      - Start the development server (FastAPI)"
	@echo "make fix   - Format code and fix imports (Ruff)"
	@echo "make lint     - Check code for errors (Ruff)"
	@echo "make clean    - Remove cache files (__pycache__)"
	@echo "----------------------------------------------------------------"

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txtsubheader

run:
	uvicorn main:app --reload

fix:
	ruff format .
	ruff check . --fix

lint:
	ruff check .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .ruff_cache
