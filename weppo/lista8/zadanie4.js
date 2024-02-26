var pg = require('pg');

var pool = new pg.Pool({
	host: 'localhost',
	database: 'pgdb',
	user: 'pg',
	password: 'pg'
});


(async function main() {
	try { await pool.query('DROP TABLE OSOBA;') } catch { }
	try { await pool.query('DROP TABLE MIEJSCE_PRACY;') } catch { }

	await pool.query(`
		CREATE TABLE MIEJSCE_PRACY (
			ID SERIAL PRIMARY KEY,
			work varchar(100) NULL);


		INSERT INTO MIEJSCE_PRACY
			(work)
		VALUES
			('A'),
			('B');


		CREATE TABLE OSOBA (
			ID SERIAL PRIMARY KEY,
			name varchar(100) NULL,
			surname varchar(100) NULL,
			sex bit(1) NULL,
			age smallint NULL,
			work_id integer not null references MIEJSCE_PRACY(ID));


		INSERT INTO OSOBA
			(name, surname, sex, age, work_id)
		VALUES
			('Jakub', 'Skalski', '0', 22, 1),
			('Alicja', 'Jagoda', '1', 21, 2);
	`);

	var id = (await pool.query(`
		INSERT INTO MIEJSCE_PRACY
			(work)
		VALUES
			('C')
		RETURNING id;
	`)).rows[0].id;

	await pool.query(`
		INSERT INTO OSOBA
			(name, surname, sex, age, work_id)
		VALUES
			('Marek', 'Niemiec', '0', 30, ${id}),
			('Król', 'Artur', '1', 30, ${id});
	`);
	
	var result = await pool.query('select * from MIEJSCE_PRACY');
	console.log("Miejsca pracy")
	result.rows.forEach(r => {
		console.log(`${r.id}\t${r.work}`);
	});

	var result = await pool.query('select * from OSOBA');
	console.log("\nOsoby")
	result.rows.forEach(r => {
		console.log(`${r.id}\t${r.name}\t${r.surname}\t${r.work_id}`);
	});

	pool.end()

})();
