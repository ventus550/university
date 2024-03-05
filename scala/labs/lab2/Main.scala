import numbers._
import figures._

object Main extends App {

  val rational1 = Rational(3, 4)
  val rational2 = Rational(2, 5)
  val rational3 = Rational(1, 3)

  val triangle = Triangle(Point(rational1, rational2), Point(rational1, rational3), Point(rational2, rational3))
  val rectangle = Rectangle(Point(rational1, rational2), Point(rational1, rational3), Point(rational2, rational3), Point(rational2, rational2))
  val square = Square(Point(rational1, rational2), Point(rational1, rational3), Point(rational2, rational3), Point(rational2, rational2))

  val figures = List(triangle, rectangle, square)

  println("Areas:")
  figures.foreach(f => println(f.area))

  println("\nDescriptions:")
  Geometry.printAll(figures)
}
