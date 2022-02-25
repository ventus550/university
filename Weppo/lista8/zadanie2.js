var pg = require('pg');

var pool = new pg.Pool({
	host: 'localhost',
	database: 'pgdb',
	user: 'pg',
	password: 'pg'
});


(async function select() {
	var result = await pool.query('select * from OSOBA');
	result.rows.forEach(r => {
		console.log(`${r.id} ${r.name}`);
	});
})();


(async function insert() {
	var result = await pool.query(`
		INSERT INTO OSOBA
			(name, surname, sex, age)
		VALUES
			('Maksymilian', 'Debeściak', '0', 22)
		RETURNING id;
	`);
	console.log(`Returned ${result.rows[0].id}`);
})();