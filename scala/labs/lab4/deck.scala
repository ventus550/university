package deck

import scala.util.Random
import cards._

class Deck(val cards: List[Card]) {
  // Creates new deck without the first card
  def pull(): Deck = new Deck(cards.tail)

  // Creates new deck with given card pushed on top
  def push(c: Card): Deck = new Deck(c :: cards)
  def push(suit: Suit, value: Int): Deck = push(Card(suit, value))
  def push(suit: Suit, face: Face): Deck = push(Card(suit, face))

  // val cards: List[Card] = cards

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
    val numericalValues = (2 to 10)
    val faceValues = List(Jack, Queen, King)
    val numericalCards = for {
      suit <- suits
      value <- numericalValues
    } yield Card(suit, value)
    val faceCards = for {
      suit <- suits
      face <- faceValues
    } yield Card(suit, face)
    new Deck(Random.shuffle(numericalCards ++ faceCards))
  }
}
