object Main extends App {
  import games._

  // Test the implementation
  val deck = Deck()
  val blackjack = new Blackjack(deck)

  println("Standard Deck:")
  println(deck.cards)

  println("\nDrawing 5 cards:")
  blackjack.play(5)

  println("\nFinding all combinations that sum up to 21:")
  blackjack.all21.foreach(println)

  println("\nFinding the first combination that sums up to 21:")
  blackjack.first21()
}