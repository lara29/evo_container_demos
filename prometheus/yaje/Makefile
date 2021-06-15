install:
	echo "Installing junos_exporter";
	python3 setup.py install;


develop:
	echo "";
	echo "Develop junos_exporter";
	python3 setup.py develop

build:
	echo "Creating folder packages";
	mkdir -p packages;

	python3 setup.py bdist_wheel;
	cp -R dist/*-py3-none-any.whl packages;

	echo "Creating docker image for junos_exporter";
	docker build -t lara/junos_exporter .;

clean:
	echo "Cleaning junos_exporter";
	rm -rf dist/;
	rm -rf build;
	python3 setup.py clean;

	rm -rf packages;
