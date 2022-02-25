
// [] są podobne do false i 0
console.assert([] == false && [] !== false)

// ! rzutuje [] na typ boolean i nadaje mu wartość false
console.assert(![] === false)

// + jest zdefiniowany dla wartości boolowskich
console.assert(false + false === 0)

// + użyty jako operator unarny wykonuje rzutowanie na number
console.assert(+[] !== false && +[] === 0)

// + binarny jest zefiniowany dla [] jako konkatenacja stringów (poprzez rzutowanie obu operandów)
console.assert([1, 3] + [2] === '1,32')

// odwołanie do nieistnijącej składowej zwraca undefined
console.assert([][0] === undefined)

// operacje arytmetyczne na undefined zwracają NaN
console.assert(isNaN(undefined + 1))

//! zadanie właściwe

// najpierw ![]+[] oblicza się do 'false', a następnie jako, że wynik jest strigiem to możemy wykonać do niego dostęp za pomocą []
console.assert( (![]+[])[+[]] === 'f') 

// 'false'[1]
console.assert( (![]+[])[+!+[]] === 'a') 

// wykonujemy dostęp do stringa pod kluczem '10', więc otrzymujemy 10-tą literę
console.assert(([![]]+[][[]]) === 'falseundefined')
console.assert(+!+[]+[+[]] === '10')
console.assert( 'falseundefined'['10'] === ([![]]+[][[]])[+!+[]+[+[]]] && ([![]]+[][[]])[+!+[]+[+[]]] === 'i' )

// 'false'[2]
console.assert((![]+[])[!+[]+!+[]] === 'l')


// na koniec sklajmy te litery + i otrzymujemy
console.log( (![]+[])[+[]]+(![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]] );