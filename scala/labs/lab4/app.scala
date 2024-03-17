object Main extends App {
  import games._

  // Test the implementation
  val blackjack = Blackjack(1)


  println("\nDrawing 5 cards:")
  blackjack.play(5)

  println("\nFinding the first combination that sums up to 21:")
  blackjack.first21()
}