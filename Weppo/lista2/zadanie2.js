

// [] pozwala odwoływać się do składowych obiektu dynamicznie przy użyciu stringu, . wymaga posidania zdefiniowanego symbolu w kodzie.
let obj = {prop: 1}
console.assert(obj.prop)
console.assert(obj["prop"])

// nie moglibyśmy odwołać się do obj[rand] za pomocą . jako, że nie mamy jego symbolu
const rand = Math.random()
obj[rand] = 2
console.assert(obj[rand]) 

/* -------------------------------------------------------------------------------------------- */

obj = {}

// liczby są rzutowane na string przy dostępie i zapisie z obj
obj[1] = 1
console.assert(obj[1] == obj['1'])

// wszystkie obiekty dostają ten sam klucz
const objA = {"A": null}, objB = {"B": null, "C": 123}
obj[objA] = "1"
console.assert(objA !== objB)
console.assert(obj[objA] === obj[objB])

// jeśli domyślne zachowanie nam nie odpowiada możemy zdefiniować funkcję tworzącą unikalne stringi dla
// interesujących nas obiektów i używa ich do adresowania składowych obiektu

/* -------------------------------------------------------------------------------------------- */

let arr = new Array(10)

// ogólnie prototypem Array jest Object. Użycie operatora [] na typie innym niż number
// oznacza po prostu podpięcie pod obiekt nowej składowej, która zachowuje się tak jak w zwykłych obiektach
// dla wartości typu number mamy przedział indeksów, dla których miejsce w Array jest zarezerwowane

arr["a"] = "a"
arr[0] = 0
arr[obj] = 1
arr.length = 100
console.assert(arr["0"] == arr[0])
console.log(arr)
arr.length = 0 // zmniejszamy przedział liczbowy do 0 i wyrzucamy wszystkie jego wartości
console.log(arr)



