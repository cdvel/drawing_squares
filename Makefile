tests:
	nosetests 
	
dev_test:
	when-changed test 'clear && make tests'
