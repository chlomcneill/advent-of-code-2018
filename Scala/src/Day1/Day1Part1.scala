package Day1

import scala.io.Source

object Day1Part1 {

  def frequency_changes(): Int = {

    val f = Source.fromFile("/Users/mcneillc/Documents/advent-of-code-2018/Scala/src/Day1/Day1input.txt").getLines

    f.toList.map(_.toInt).sum

  }

  def main(args: Array[String]): Unit = {

    println(frequency_changes())

  }

}
