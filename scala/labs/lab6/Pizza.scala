package pizzeria {
  case class Pizza(
    pizzaType: String,
    size: String,
    crust: String,
    extraMeat: Option[String] = None,
    extraTopping: Option[String] = None
  ) {
    
    override def toString(): String = {
      s"Pizza(type: $pizzaType, size: $size, crust: $crust, extraMeat: ${extraMeat.getOrElse("None")}, extraTopping: ${extraTopping.getOrElse("None")})"
    }
    
    // Calculate price of the pizza
    val price: Double = {
      val basePrice = pizzaType match {
        case "Margarita" => 5.0
        case "Pepperoni" => 6.5
        case "Funghi"    => 7.0
      }
      
      val sizeMultiplier = size match {
        case "small"  => 0.9
        case "regular" => 1.0
        case "large"  => 1.5
      }
      
      val meatPrice = if (extraMeat.isDefined) 1.0 else 0.0
      val toppingPrice = extraTopping match {
        case Some("ketchup") => 0.5
        case Some("garlic") => 0.5
        case _ => 0.0
      }
      
      basePrice * sizeMultiplier + meatPrice + toppingPrice
    }
  }
}
