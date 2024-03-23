import plugins._

// Entry-point object with example tests
object Main extends App {
  // Example usage
  val text = "ala ma   kota"

  println("Original Text: " + text)
  println("Action A: " + Actions.actionA.plugin(text))
  println("Action B: " + Actions.actionB.plugin(text))
  println("Action C: " + Actions.actionC.plugin(text))
  println("Action D: " + Actions.actionD.plugin(text))
  println("Action E: " + Actions.actionE.plugin(text))
  println("Action F: " + Actions.actionF.plugin(text))
  println("Action G: " + Actions.actionG.plugin(text))
}
