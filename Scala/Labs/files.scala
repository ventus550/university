// Create a list with all lines from a given file
val filesHere = new java.io.File(".").listFiles

def fileLinesUgly(file: java.io.File): List[String] = {
  import scala.io.Source
  var lines: List[String] = Nil
  val source = Source.fromFile(file).getLines()
  do {
    lines = lines :+ source.next()
  } while (!source.isEmpty)
  return lines
}

def fileLines(file: java.io.File): List[String] = {
  import scala.io.Source
  return Source.fromFile(file).getLines().toList
}

// Test functions
println(fileLines(filesHere(1)))
println(fileLinesUgly(filesHere(1)))
