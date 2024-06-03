object PizzeriaApp extends App {
  import pizzeria.Pizza
  import orders.Order
  
  val pizza1 = Pizza("Margarita", "regular", "thin")
  val pizza2 = Pizza("Pepperoni", "large", "thick", extraMeat = Some("salami"))
  val pizza3 = Pizza("Funghi", "small", "thin", extraTopping = Some("garlic"))
  
  val order = new Order(
    name = "John Doe",
    address = "123 Scala Street",
    phone = "123-456-7890",
    pizzas = List(pizza1, pizza2, pizza3),
    drinks = List("lemonade", "lemonade"),
    discount = Some("student"),
    specialInfo = Some("Ring doesn't work, please knock")
  )
  
  println(order)
}
