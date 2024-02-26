var pg = require('pg');

var pool = new pg.Pool({
	host: 'localhost',
	database: 'pgdb',
	user: 'pg',
	password: 'pg'
});


(async function main() {
	try { await pool.query('DROP TABLE PRACA_OSOBA;') } catch { }
	try { await pool.query('DROP TABLE OSOBA;') } catch { }
	try { await pool.query('DROP TABLE MIEJSCE_PRACY;') } catch { }

	await pool.query(`
		CREATE TABLE MIEJSCE_PRACY (
			ID SERIAL PRIMARY KEY,
			work varchar(100) NULL);

		CREATE TABLE OSOBA (
			ID SERIAL PRIMARY KEY,
			name varchar(100) NULL);

		CREATE TABLE PRACA_OSOBA (
			work_id integer references MIEJSCE_PRACY(ID),
			person_id integer references OSOBA(ID),
			CONSTRAINT work_person_key PRIMARY KEY(work_id, person_id));
	`);

	var wrows = (await pool.query(`
		INSERT INTO MIEJSCE_PRACY
			(work)
		VALUES
			('A'),
			('B')
		RETURNING id;
	`)).rows;

	var prows = (await pool.query(`
		INSERT INTO OSOBA
			(name)
		VALUES
			('Adam'),
			('Beata')
		RETURNING id;
	`)).rows;

	await pool.query(`
		INSERT INTO PRACA_OSOBA
			(work_id, person_id)
		VALUES
			(${wrows[0].id}, ${prows[0].id}),
			(${wrows[1].id}, ${prows[0].id}),
			(${wrows[1].id}, ${prows[1].id}),
			(${wrows[0].id}, ${prows[1].id});
	`);
	
	var result = await pool.query('select * from MIEJSCE_PRACY');
	console.log("Miejsca pracy")
	result.rows.forEach(r => {
		console.log(`${r.id}\t${r.work}`);
	});

	var result = await pool.query('select * from OSOBA');
	console.log("\nOsoby")
	result.rows.forEach(r => {
		console.log(`${r.id}\t${r.name}`);
	});

	var result = await pool.query('select * from PRACA_OSOBA');
	console.log("\nMiejsca pracy x Osoby")
	result.rows.forEach(r => {
		console.log(`${r.work_id}\t${r.person_id}`);
	});

	pool.end()

})();
