ACTIVATE := . ../env/social/bin/activate &&

venv: requirements.txt
	@python3 -m venv ../env/social
	$(ACTIVATE) pip install -r requirements.txt

run: venv
	$(ACTIVATE) python manage.py runserver_plus --cert-file cert.crt

shell: venv
	$(ACTIVATE) python manage.py shell