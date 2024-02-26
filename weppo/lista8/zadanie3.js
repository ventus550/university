var pg = require('pg');

var pool = new pg.Pool({
	host: 'localhost',
	database: 'pgdb',
	user: 'pg',
	password: 'pg'
});


(async function main() {
	try {
		await pool.query('DROP TABLE OSOBA;')
	} catch {}
	
	await pool.query(`
		CREATE TABLE OSOBA (
			ID SERIAL PRIMARY KEY,
			name varchar(100) NULL,
			surname varchar(100) NULL,
			sex bit(1) NULL,
			age smallint NULL);


		INSERT INTO OSOBA
			(name, surname, sex, age)
		VALUES
			('Jakub', 'Skalski', '0', 22),
			('Alicja', 'Jagoda', '1', 21);
	`);

	await pool.query(`
		UPDATE OSOBA
		SET name = 'updated'
		WHERE id = 1; 
	`);

	await pool.query(`
		DELETE FROM OSOBA
		WHERE name = 'Alicja'; 
	`);

	var result = await pool.query('select * from OSOBA');
	result.rows.forEach(r => {
		console.log(`${r.id} ${r.name}`);
	});

})();
