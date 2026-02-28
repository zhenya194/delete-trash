## Delete not essential files of Python and several Python libraries
clean_python_unix:
	find . -name "**/*.pyc" -delete 
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -r {} +
	rm -f .coverage coverage.xml
	rm -rf htmlcov/ .mypy_cache .pytest_cache .ruff_cache
	rm -rf *.egg-info
clean_python_win:
	Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
	Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force
	Remove-Item .pytest_cache -Recurse -Force
	Remove-Item *.egg-info -Recurse -Force

## Delete not essential files of Kotlin and several Kotlin libraries
clean_kotlin_unix:
	rm -rf .gradle out .kotlin
	rm -rf target
clean_kotlin_win:
	Remove-Item -Recurse -Force .gradle, .kotlin, out
	Remove-Item -Recurse -Force target