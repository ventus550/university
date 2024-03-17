package games

import deck.Deck
import cards._

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
