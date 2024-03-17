package cards

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