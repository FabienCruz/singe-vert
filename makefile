site:
	source env/bin/activate && \
	python3 build_site.py && \
	git add docs/ && \
	git commit -m "Update site - $(shell date '+%Y-%m-%d %H:%M')" && \
	git push origin main

build:
	source env/bin/activate && python3 build_site.py

install:
	python3 -m venv env
	source env/bin/activate && pip install -r requirements.txt

clean:
	rm -rf docs/*