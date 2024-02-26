/*
	Zmienne zadeklarowane za pomocą var są widoczne w zakresie najbliższej funkcji, a nie bloku kodu { ... }.
	Z tego powodu licznik pętli `i` jest widoczny w całej funkcji `createFs`, więc gdy skończymy się pętlić `i`
	będzie miało wartość 10 dla wszystkich funkcji w tablicy.
*/

function createFs(n) {
	var fs = [];

	var _loop = function _loop(i) {
		fs[i] = function () {
			return i;
		};
	};

	for (var i = 0; i < n; i++) {
		_loop(i);
	};
	return fs;
}

