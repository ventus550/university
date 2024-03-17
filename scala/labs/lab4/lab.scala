import scala.util.Random

sealed trait Suit
case object Clubs extends Suit
case object Diamonds extends Suit
case object Hearts extends Suit
case object Spades extends Suit

sealed trait Face
case object Jack extends Face
case object Queen extends Face
case object King extends Face

case class Card(suit: Suit, value: Either[Int, Face])

object Card {
  def apply(suit: Suit, value: Int): Card = Card(suit, Left(value))
  def apply(suit: Suit, face: Face): Card = Card(suit, Right(face))
}

class Deck(cards: List[Card]) {
  // Creates new deck without the first card
  def pull(): Deck = new Deck(cards.tail)

  // Creates new deck with given card pushed on top
  def push(c: Card): Deck = new Deck(c :: cards)
  def push(suit: Suit, value: Int): Deck = push(Card(suit, value))
  def push(suit: Suit, face: Face): Deck = push(Card(suit, face))

  // Checks if deck is a standard deck
  val isStandard: Boolean = cards.length == 52

  // Amount of duplicates of the given card in the deck
  def duplicatesOfCard(card: Card): Int = cards.count(_ == card)
  
  // Amount of cards in the deck for the given color
  def amountOfColor(color: Suit): Int = cards.count(_.suit == color)
  
  // Amount of cards in the deck for given numerical card (2, 3, 4, 5, 6, 7, 8, 9, 10)
  def amountOfNumerical(numerical: Int): Int = cards.collect { case Card(_, Left(`numerical`)) => true }.size
  
  // Amount of all numerical cards in the deck (2, 3, 4, 5, 6, 7, 8, 9, 10)
  val amountWithNumerical: Int = cards.count(_.value.isLeft)
  
  // Amount of cards in the deck for the given face (Jack, Queen & King)
  def amountOfFace(face: Face): Int = cards.collect { case Card(_, Right(`face`)) => true }.size
  
  // Amount of all cards in the deck with faces (Jack, Queen & King)
  val amountWithFace: Int = cards.count(_.value.isRight)
}

object Deck {
  def apply(): Deck = {
    val suits = List(Clubs, Diamonds, Hearts, Spades)
    val values = (2 to 10) ++ List(Jack, Queen, King)
    val cards = for {
      suit <- suits
      value <- values
    } yield Card(suit, value)
    new Deck(Random.shuffle(cards))
  }
}

class Blackjack(deck: Deck) {
  private def calculatePoints(card: Card): Int = card.value match {
    case Left(value) => value
    case Right(face) => face match {
      case Jack | Queen | King => 10
    }
  }

  def play(n: Int): Unit = {
    val (drawnCards, remainingDeck) = deck.cards.splitAt(n)
    val points = drawnCards.map(calculatePoints).sum
    println("Drawn Cards:")
    drawnCards.foreach(println)
    println(s"Total Points: $points")
  }

  lazy val all21: List[List[Card]] = {
    def find21(cards: List[Card], target: Int): List[List[Card]] = {
      if (target == 0) List(Nil)
      else if (target < 0 || cards.isEmpty) Nil
      else {
        find21(cards.tail, target) ++
          find21(cards.tail, target - calculatePoints(cards.head)).map(cards.head ::)
      }
    }

    find21(deck.cards, 21)
  }

  def first21(): Unit = {
    all21.headOption match {
      case Some(cards) =>
        println("First combination of cards that sum up to 21:")
        cards.foreach(println)
      case None =>
        println("No combination of cards sum up to 21.")
    }
  }
}

object Blackjack {
  def apply(numOfDecks: Int): Blackjack = {
    val decks = List.fill(numOfDecks)(Deck())
    val combinedDeck = new Deck(decks.flatMap(_.cards))
    new Blackjack(combinedDeck)
  }
}

object Main extends App {
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
