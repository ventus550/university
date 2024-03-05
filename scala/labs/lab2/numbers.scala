package numbers

class Rational private (val numer: Int, val denom: Int) {
  require(denom != 0, "Denominator must be non-zero")

  private def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
  private val gcdValue: Int = gcd(numer.abs, denom.abs)
  val numerator: Int = numer / gcdValue
  val denominator: Int = denom / gcdValue

  def +(other: Rational): Rational =
    Rational(numerator * other.denominator + other.numerator * denominator,
             denominator * other.denominator)

  def -(other: Rational): Rational =
    Rational(numerator * other.denominator - other.numerator * denominator,
             denominator * other.denominator)

  def *(other: Rational): Rational =
    Rational(numerator * other.numerator, denominator * other.denominator)

  def /(other: Rational): Rational =
    Rational(numerator * other.denominator, denominator * other.numerator)

  override def toString: String =
    if (denominator == 1) s"$numerator"
    else if (numerator.abs > denominator.abs)
      s"${numerator / denominator} ${numerator % denominator}/${denominator}"
    else s"$numerator/$denominator"
}

object Rational {
  def apply(numer: Int, denom: Int = 1): Rational = new Rational(numer, denom)
  def apply(numer: Int): Rational = new Rational(numer, 1)
  val zero: Rational = Rational(0)
  val one: Rational = Rational(1)
}
