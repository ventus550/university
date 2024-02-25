//Print names of all .scala files which are in filesHere & are non-empty
val filesHere = new java.io.File(".").listFiles

def printNonEmptyUgly(pattern: String): Unit = {
  var i = 0
  do {
    if (filesHere(i).getName.endsWith(".scala")) {
      if (filesHere(i).length > 0) {
        println(filesHere(i).getName)
      }
    }
    i += 1
  } while (i < filesHere.length)
}

def printNonEmpty(pattern: String): Unit = {
  for {
    file <- filesHere
    if file.getName.endsWith(".scala") && file.length > 0
  } println(file.getName)
}

// Test the functions
println("Non-Empty Scala Files Ugly:")
printNonEmptyUgly(".scala")

println("Non-Empty Scala Files:")
printNonEmpty(".scala")
