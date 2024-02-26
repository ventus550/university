

console.log("Dzień dobry, użytkowniku! Jak się nazywasz? :^) ")
process.stdin.on('data', data => {
	console.log(`Witaj ${data.toString()}`)
	process.stdin.destroy()
})

