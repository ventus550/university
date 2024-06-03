package orders {
  import pizzeria.Pizza
  import scala.util.matching.Regex
  
  class Order(
    val name: String,
    val address: String,
    val phone: String,
    val pizzas: List[Pizza],
    val drinks: List[String],
    val discount: Option[String] = None,
    val specialInfo: Option[String] = None
  ) {
    require(isValidPhoneNumber(phone), s"Invalid phone number: $phone")

    private def isValidPhoneNumber(phone: String): Boolean = {
      val phonePattern: Regex = """^\d{3}-\d{3}-\d{4}$""".r
      phonePattern.matches(phone)
    }

    def extraMeatPrice: Option[Double] = {
        val totalExtraMeatPrice = pizzas.flatMap(_.extraMeat).length * 1.0
        if (totalExtraMeatPrice > 0) Some(totalExtraMeatPrice) else None
      }

    def pizzasPrice: Option[Double] = {
      val totalPizzasPrice = pizzas.map(_.price).sum
      if (totalPizzasPrice > 0) Some(totalPizzasPrice) else None
    }

    def drinksPrice: Option[Double] = {
      val totalDrinksPrice = drinks.length * 2.0
      if (totalDrinksPrice > 0) Some(totalDrinksPrice) else None
    }

    def priceByType(pizzaType: String): Option[Double] = {
      val totalPriceByType = pizzas.filter(_.pizzaType == pizzaType).map(_.price).sum
      if (totalPriceByType > 0) Some(totalPriceByType) else None
    }

    val price: Double = {
      val totalPrice = pizzasPrice.getOrElse(0.0) + drinksPrice.getOrElse(0.0)
      
      discount match {
        case Some("student") => totalPrice * 0.95
        case Some("senior") => totalPrice * 0.93
        case _ => totalPrice
      }
    }
    
    override def toString(): String = {
      s"Order(name: $name, address: $address, phone: $phone, pizzas: ${pizzas.mkString(", ")}, drinks: ${drinks.mkString(", ")}, discount: ${discount.getOrElse("None")}, specialInfo: ${specialInfo.getOrElse("None")}, total price: $price)"
    }
  }
}
