clear-posts:
	py -m cli post clear

post:
	py -m cli post --id $(id)

carousel:
	py -m cli template --type carousel --title MyFirstPost
	
single:
	py -m cli template --type single --title MyFirstPost