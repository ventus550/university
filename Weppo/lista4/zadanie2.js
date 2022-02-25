var Person = (function () {

	var nameSymbol = Symbol('name')

	function Person(name) {
		this[nameSymbol] = name
	}

	Person.prototype.getName = function () {
		return this[nameSymbol]
	}

	return Person
}())

var p1 = new Person('jan')
var p2 = new Person('tomasz')
console.log(p1.getName())
console.log(p2.getName())