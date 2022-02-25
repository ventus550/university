

/*
	Pokazać jak zdefiniować nowy obiekt zawierający co najmniej jedno pole,
	jedną metodę oraz właściwości z akcesorami get i set
*/

const testObj = {

	_field: null,

	set field(val) {
		this._field = val
	},

	get field() {
		return this._field
	}
}

console.assert(testObj.field === null)
testObj.field = 10
console.assert(testObj.field === 10)


/*
	Pokazać jak do istniejącego obiektu dodać nowe pole,
	nową metodę i nową właściwość z akcesorami get i set
*/

let foo = 0;
Object.defineProperty(testObj, 'foo', {
	get() { return foo; },
	set(newValue) { foo = newValue + 1; }
});

console.assert(testObj.foo === 0)
testObj.foo += 1
console.assert(testObj.foo === 2)


/*
	Z powyższych tylko get i set nie mogą być dodane
*/

testObj.method = (x) => x + 1
testObj.property = 123



