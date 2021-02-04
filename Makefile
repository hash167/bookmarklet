ACTIVATE := . ../env/social/bin/activate &&

venv: requirements.txt
	@python3 -m venv ../env/social
	$(ACTIVATE) pip install -r requirements.txt

run: venv
	export SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=$(SOCIAL_AUTH_GOOGLE_OAUTH2_KEY)
	export SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=$(SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET)
	$(ACTIVATE) python manage.py runserver_plus --cert-file cert.crt