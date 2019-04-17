import java.util.Random

/*
 * Class to create Attribute objects which
 * contain the attributes name, min, and max values
 */
class Attribute {
    var name: String
    var min: Double
    var max: Double

    constructor(name: String, min: Double, max: Double) {
        this.name = name
        this.min = min
        this.max = max
    }
}

/*
 * Generates a random number within the bounds, adds to the row,
 * prints out the row 'n' number of times (default=1)
 * TODO: Do I need the 'help' and 'metavar' values like his Python?
 */
fun main(args: Array<String>) {
    var seed = 1 // 1 by default
    var numRepeats = 1 // 1 by default

    // Assign the values of -s and -n if they are included
    for (arg in args) {
        if (arg.contains("-s=")) {
            seed = arg.substring(3, arg.length).toInt()
        }
        if (arg.contains("-n=")) {
            numRepeats = arg.substring(3, arg.length).toInt()
        }
    }

    // Generate the values
    val attr = listOf(
        Attribute("pomposity", 0.0, 1.0),
        Attribute("learning_curve", 1.0, 100.0),
        Attribute("optimism", 0.1, 10.0),
        Attribute("atleast", 0.0, 100.0),
        Attribute("done_percent", 0.0, 100.0),
        Attribute("sDR_param1", 0.0, 1.0),
        Attribute("sDR_param2", 1.0, 10.0),
        Attribute("d", 0.0, 90.0),
        Attribute("ep", 1.0, 30.0),
        Attribute("nprod", 0.1, 1.0),
        Attribute("np", 1.0, 30.0),
        Attribute("ts", 1.0, 10.0),
        Attribute("to", 1.0, 100.0),
        Attribute("r", 100.0, 1000.0)
        )

    // Generates a random number within the bounds, adds to the row
    // prints out the row 'n' number of times (default=1)
    val row = mutableMapOf<String, Double>();
    val rand = Random(seed.toLong()) // Seed - val rand = Random(seed)
    for (run in 1..numRepeats) {
        for (item in attr) {
            val value:Double = item.min + (item.max - item.min) * rand.nextDouble()
            val rounded:Double = String.format("%.2f", value).toDouble()
            row[item.name] = rounded
        }
        println(row)
    }

}