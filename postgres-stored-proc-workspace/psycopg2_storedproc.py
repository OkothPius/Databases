import psycopg2

if __name__ == "__main__":
	conn = psycopg2.connect(database="red30",
		user="redruko",
		password="password",
		host="localhost",
		port="5432")

	conn.autocommit = True

	cur = conn.cursor()

	cur.execute('''CALL return_nondiscounted_item (%s, %s)''', (1105910, 1))

	# How to call a Postgres Function
	# cur.callproc('return_nondiscounted_item', (1105910, 1))

	conn.close()
