docs:
	mkdir -p doc
	pydoc -w ./
	mv *.html doc

tests:
	python3 -uB ./test/tests.py

pep8:
	pycodestyle test/*.py
	pycodestyle tasks/*.py

profile:
	python3 -m cProfile tasks/$(file).py > $(file)-profile.txt

clean:
	pyclean .
	rm -rf doc