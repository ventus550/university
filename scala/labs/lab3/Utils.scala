// Define a custom exception for the `unSafe` method
case class MyException(message: String) extends Exception(message)
case class MyDifferentException(message: String) extends Exception(message)

object Utils {
  def isSorted(as: List[Int], ordering: (Int, Int) => Boolean): Boolean = as match {
    case Nil | _ :: Nil => true
    case x :: y :: tail => ordering(x, y) && isSorted(y :: tail, ordering)
  }

  def isAscSorted(as: List[Int]): Boolean = {
    isSorted(as, _ <= _)
  }

  def isDescSorted(as: List[Int]): Boolean = {
    isSorted(as, _ >= _)
  }

  def foldLeft[A, B](l: List[A], z: B)(f: (B, A) => B): B = {
    var acc = z
    for (elem <- l) {
      acc = f(acc, elem)
    }
    acc
  }

  def sum(l: List[Int]): Int = {
    foldLeft(l, 0)(_ + _)
  }

  def length[A](l: List[A]): Int = {
    foldLeft(l, 0)((acc, _) => acc + 1)
  }

  def compose[A, B, C](f: B => C, g: A => B): A => C = {
    x => f(g(x))
  }

  def repeated[A](f: A => A, n: Int): A => A = {
    if (n <= 0) {
      identity[A]
    } else {
      compose(f, repeated(f, n - 1))
    }
  }

  def curry[A, B, C](f: (A, B) => C): A => (B => C) = {
    a => b => f(a, b)
  }

  def uncurry[A, B, C](f: A => B => C): (A, B) => C = {
    (a, b) => f(a)(b)
  }

  def unSafe[T](ex: Exception)(block: => T): T = {
    try {
      block
    } catch {
      case e: Exception =>
        println(s"An error occurred: ${e.getMessage}")
        throw ex
    }
  }
}

object Main extends App {
  import Utils._

  // Example tests
  val sortedList = List(1, 2, 3, 4, 5)
  val unsortedList = List(5, 3, 1, 2, 4)

  println("isAscSorted:")
  println(isAscSorted(sortedList))  // true
  println(isAscSorted(unsortedList))  // false

  println("isDescSorted:")
  println(isDescSorted(sortedList))  // false
  println(isDescSorted(unsortedList))  // true

  println("sum:")
  println(sum(sortedList))  // 15
  println(sum(unsortedList))  // 15

  println("length:")
  println(length(sortedList))  // 5
  println(length(unsortedList))  // 5

  println("repeated:")
  val addOne = (x: Int) => x + 1
  val addFive = repeated(addOne, 5)
  println(addFive(1))  // 6

  println("curry:")
  val add = (a: Int, b: Int) => a + b
  val curriedAdd = curry(add)
  println(curriedAdd(1)(2))  // 3

  println("uncurry:")
  val uncurriedAdd = uncurry(curriedAdd)
  println(uncurriedAdd(1, 2))  // 3

  println("unSafe:")
  unSafe(MyException("Could not run command")) {
    // block of code which could throw any exception
    println("Running some risky operation...")
    throw new IllegalArgumentException("Some illegal argument!")
  }

  unSafe(MyDifferentException("Error while building map")) {
    // block of code which could throw any exception
    println("Building a map...")
    throw new RuntimeException("Map construction failed!")
  }
}
