package figures

import numbers.Rational

case class Point(x: Rational, y: Rational)

abstract class Shape {
  def area: Double
  val description: String
}

class Triangle(a: Point, b: Point, c: Point) extends Shape {
  def area: Double = {
    val ab = Math.sqrt(Math.pow(a.x.numerator - b.x.numerator, 2) + Math.pow(a.y.numerator - b.y.numerator, 2))
    val bc = Math.sqrt(Math.pow(b.x.numerator - c.x.numerator, 2) + Math.pow(b.y.numerator - c.y.numerator, 2))
    val ca = Math.sqrt(Math.pow(c.x.numerator - a.x.numerator, 2) + Math.pow(c.y.numerator - a.y.numerator, 2))

    val semiPerimeter = (ab + bc + ca) / 2
    Math.sqrt(semiPerimeter * (semiPerimeter - ab) * (semiPerimeter - bc) * (semiPerimeter - ca))
  }
  val description: String = "Triangle"
}

class Rectangle(a: Point, b: Point, c: Point, d: Point) extends Shape {
  def area: Double = {
    val side1 = Math.sqrt(Math.pow(a.x.numerator - b.x.numerator, 2) + Math.pow(a.y.numerator - b.y.numerator, 2))
    val side2 = Math.sqrt(Math.pow(b.x.numerator - c.x.numerator, 2) + Math.pow(b.y.numerator - c.y.numerator, 2))
    side1 * side2
  }
  val description: String = "Rectangle"
}

class Square(a: Point, b: Point, c: Point, d: Point) extends Shape {
  def area: Double = {
    val side = Math.sqrt(Math.pow(a.x.numerator - b.x.numerator, 2) + Math.pow(a.y.numerator - b.y.numerator, 2))
    side * side
  }
  val description: String = "Square"
}

object Triangle {
  def apply(a: Point, b: Point, c: Point): Triangle = new Triangle(a, b, c)
}

object Rectangle {
  def apply(a: Point, b: Point, c: Point, d: Point): Rectangle = new Rectangle(a, b, c, d)
}

object Square {
  def apply(a: Point, b: Point, c: Point, d: Point): Square = new Square(a, b, c, d)
}

object Geometry {
  def areaSum(figures: List[Shape]): Double = ???
  
  def printAll(figures: List[Shape]): Unit = {
    figures.foreach(f => println(f.description))
  }
}
