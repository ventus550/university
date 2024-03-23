// Package plugins with abstractions for text manipulations
package plugins

// Traits for text manipulations
trait Reverting {
  def revert(text: String): String
}

trait LowerCasing {
  def lowerCase(text: String): String
}

trait SingleSpacing {
  def singleSpace(text: String): String
}

trait NoSpacing {
  def noSpace(text: String): String
}

trait DuplicateRemoval {
  def removeDuplicates(text: String): String
}

trait Rotating {
  def rotate(text: String): String
}

trait Doubling {
  def double(text: String): String
}

trait Shortening {
  def shorten(text: String): String
}

// Object Actions with abstractions for several actions using combinations of plugins
object Actions {
  // Pluginable trait for composing plugins
  trait Pluginable {
    def plugin(text: String): String
  }

  // Implementations of Pluginable actions
  val actionA: Pluginable = new Pluginable {
    override def plugin(text: String): String =
      SingleSpacingImpl.singleSpace(DoublingImpl.double(ShorteningImpl.shorten(text)))
  }

  val actionB: Pluginable = new Pluginable {
    override def plugin(text: String): String =
      NoSpacingImpl.noSpace(ShorteningImpl.shorten(DoublingImpl.double(text)))
  }

  val actionC: Pluginable = new Pluginable {
    override def plugin(text: String): String =
      DoublingImpl.double(LowerCasingImpl.lowerCase(text))
  }

  val actionD: Pluginable = new Pluginable {
    override def plugin(text: String): String =
      RotatingImpl.rotate(DuplicateRemovalImpl.removeDuplicates(text))
  }

  val actionE: Pluginable = new Pluginable {
    override def plugin(text: String): String =
      RevertingImpl.revert(DoublingImpl.double(ShorteningImpl.shorten(NoSpacingImpl.noSpace(text))))
  }

  val actionF: Pluginable = new Pluginable {
    override def plugin(text: String): String = {
      var rotatedText = text
      for (_ <- 1 to 5) {
        rotatedText = RotatingImpl.rotate(rotatedText)
      }
      rotatedText
    }
  }

  val actionG: Pluginable = new Pluginable {
    override def plugin(text: String): String =
      actionB.plugin(actionA.plugin(text))
  }
}

// Implementations of the traits
object RevertingImpl extends Reverting {
  override def revert(text: String): String = text.reverse
}

object LowerCasingImpl extends LowerCasing {
  override def lowerCase(text: String): String = text.toLowerCase
}

object SingleSpacingImpl extends SingleSpacing {
  override def singleSpace(text: String): String = text.replaceAll("\\s+", " ")
}

object NoSpacingImpl extends NoSpacing {
  override def noSpace(text: String): String = text.replaceAll("\\s", "")
}

object DuplicateRemovalImpl extends DuplicateRemoval {
  override def removeDuplicates(text: String): String = text.distinct
}

object RotatingImpl extends Rotating {
  override def rotate(text: String): String = text.tail + text.head
}

object DoublingImpl extends Doubling {
  override def double(text: String): String = text.flatMap(c => c.toString * 2)
}

object ShorteningImpl extends Shortening {
  override def shorten(text: String): String = text.zipWithIndex.filter(_._2 % 2 == 0).map(_._1).mkString
}
