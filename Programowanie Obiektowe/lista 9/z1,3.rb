sleep(1)


class Funkcja
    @equation

    def initialize(eq_block)
        @equation = eq_block
    end

    def value(x)
        @equation.call(x)
    end

    def zerowe(a, b, e)
        arr = []

        recSearch = -> a, b {
            if b-a <= e
                if value(a)*value(b) < 0
                    arr.push((a+b)/2.0)
                end

            else
                recSearch.(a, (a+b)/2.0)
                recSearch.((a+b)/2.0, b)
            end
        }

        recSearch.(a, b)
        return arr
    end

    def pole(a, b)
        n = (b - a) / 1000.0
        pole = 0;
        (1..1000).each{|i| pole += value(a + i*n)*n}
        return pole
    end

    def poch(x)
        n = 0.00001
        return (value(x + n) - value(x)) / n
    end

    def draw(a, b)
        n = (b-a) / 100.0

        values = []
        (1..100).each{|i| values.push(value(a + i*n))}

        mx = values.max
        mn = values.min
        prec = (mx-mn)/30.0

        values = values.map{|v| (v / prec).floor()}
        values = values.map{|v| v + values.min.abs}

        for i in ( values.min..values.max ) do
            line = ""

            values.each{|v| v == values.max - i ? line += "*" : line += " "}
            puts line
        end

        return values
    end


end

=begin

lin = Funkcja.new(Proc.new{|x| x})
lin.draw(0, 1)


polynomial = Funkcja.new(Proc.new {|x| x*x*x - x*x + 0.1})
polynomial.draw(-0.5, 1)



parab = Funkcja.new(Proc.new{|x| (x-5)*(x-5) - 10})
parab.draw(0, 10)

=end