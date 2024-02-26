class Code
    def initialize(string)
        @string = string
    end

    def to_s
        @string
    end
end



class Jawna < Code
    def zaszyfruj(klucz)
        szyfr = ""
        @string.each_char { |c|
            szyfr += klucz[c]
        }
        szyfr
    end
end

class Zaszyfrowane < Code
    def odszyfruj(klucz)
        szyfr = ""
        @string.each_char { |c|
            szyfr += klucz.key(c)
        }
        szyfr

    end
end



j = Jawna.new("ruby")
puts j.to_s

hash = {"b" => "r", "r" => "y", "y" => "u", "u" => "a"}
puts j.zaszyfruj(hash)

z = Zaszyfrowane.new(j.zaszyfruj(hash))
puts z.odszyfruj(hash)

sleep(1)