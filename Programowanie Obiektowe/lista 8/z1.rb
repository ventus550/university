
class Integer
    def czynniki
        tmp = self
        k = 2
        arr = [1]
        while tmp > 1
            x = 1
            if tmp % k == 0
                tmp /= k
                if not arr.include?(k)
                    arr << k
                end
            else
                k += 1
            end
        end
        arr
    end

    def ack(y)
        def Ack(n, m)
            if n == 0
                m + 1
            elsif m == 0
                Ack(n-1, 1)
            else
                Ack(n - 1, Ack(n, m - 1))
            end
        end

        Ack(self, y)
    end

    def doskonala
        if self.czynniki.inject(:+) == self and self != 1
            true
        else
            false
        end
    end

    def slowna
        assoc = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec"]
        res = ""

        for i in 0..self.to_s.length-1
            res += assoc[self.to_s[i].to_i] + " "
        end

        res


    end
end


