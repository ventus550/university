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
    def find21(cards: List[Card], target: Int, path: List[Card], result: List[List[Card]]): List[List[Card]] = {
      if (target == 0) result :+ path
      else if (target < 0 || cards.isEmpty) result
      else {
        find21(cards.tail, target, path, result) ++ find21(cards.tail, target - calculatePoints(cards.head), path :+ cards.head, result)
      }
    }

    find21(deck.cards, 21, List(), List())
  }

  def first21(): Unit = {
    all21.headOption match {
      case Some(cards) =>
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
