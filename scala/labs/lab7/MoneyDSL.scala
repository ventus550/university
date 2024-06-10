object MoneyDSL {
  trait Currency
  case object USD extends Currency
  case object EUR extends Currency
  case object PLN extends Currency
  
  case class Money(amount: BigDecimal, currency: Currency)(implicit val currencyConverter: CurrencyConverter) {
    def +(other: Money): Money = Money(convertTo(currency, other.currency, other.amount) + amount, currency)
    def -(other: Money): Money = Money(amount - convertTo(currency, other.currency, other.amount), currency)
    def *(value: BigDecimal): Money = Money(amount * value, currency)
    def as(newCurrency: Currency): Money = {
      val convertedAmount = convertTo(currency, newCurrency, amount)
      Money(convertedAmount, newCurrency)
    }
    def >(other: Money): Boolean = amount > convertTo(currency, other.currency, other.amount)
    def <(other: Money): Boolean = amount < convertTo(currency, other.currency, other.amount)

    private def convertTo(from: Currency, to: Currency, amount: BigDecimal): BigDecimal = {
      if (from == to) amount
      else currencyConverter.convert(from, to) * amount
    }
  }

  case class CurrencyConverter(conversion: Map[(Currency, Currency), BigDecimal]) {
    def convert(from: Currency, to: Currency): BigDecimal = {
      conversion.getOrElse((from, to), throw new IllegalArgumentException(s"No conversion rate found from $from to $to"))
    }
  }

  object MoneyPackage {
    val conversionRates: Map[(Currency, Currency), BigDecimal] = Map(
      (USD, EUR) -> 0.89,
      (USD, PLN) -> 3.77,
      (EUR, USD) -> 1.12,
      (EUR, PLN) -> 4.23,
      (PLN, USD) -> 0.27,
      (PLN, EUR) -> 0.24
    )
    implicit val currencyConverter = CurrencyConverter(conversionRates)
	
	implicit class MoneySyntax(amount: Double) {
		def apply(currency: Currency): Money = Money(amount, currency)
	}

  }

  def main(args: Array[String]): Unit = {
    import MoneyPackage._

    val sum1: Money = 100.01(USD) + 200(EUR)
    println(s"Sum 1: $sum1")

    val sum2: Money = 100.01(PLN) + 200(USD)
    println(s"Sum 2: $sum2")

    val sum3: Money = 5(PLN) + 3(PLN) + 20.5(USD)
    println(s"Sum 3: $sum3")

    val sub: Money = 300.01(USD) - 200(EUR)
    println(s"Subtraction: $sub")

    val mult1: Money = 30(PLN) * 20
    println(s"Multiplication 1: $mult1")

    val mult2: Money = 20(USD) * 11
    println(s"Multiplication 2: $mult2")

    val conv1: Money = 150.01(USD) as PLN
    println(s"Conversion 1: $conv1")

    val conv2: Money = 120.01(USD) as EUR
    println(s"Conversion 2: $conv2")

    val compare1: Boolean = 300.30(USD) > 200(EUR)
    println(s"Comparison 1: $compare1")

    val compare2: Boolean = 300.30(USD) < 200(EUR)
    println(s"Comparison 2: $compare2")
  }
}
