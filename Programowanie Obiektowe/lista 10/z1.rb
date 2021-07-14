
class Kolekcja

    def initialize(arr)
        @arr = arr
    end

    def swap(i, j)
        @arr[i], @arr[j] = @arr[j], @arr[i]
    end

    def get(i)
        return @arr[i]
    end

    def set(i, val)
        @arr[i] = val
    end

    def length()
        return @arr.length
    end

    def to_s
        return @arr.to_s
    end

end


class Sortowanie
    def initialize
    end

    def sort1(kolekcja)
        n = kolekcja.length()
        for i in 0..(n-1)
            for j in 0..(n-i-2)
                if kolekcja.get(j) > kolekcja.get(j+1)
                    kolekcja.swap(j, j+1)
                end
            end
        end
    end

    def sort2(kolekcja)
        for i in 1..kolekcja.length()-1 
  
            key = kolekcja.get(i)

            j = i-1
            while j >= 0 && key < kolekcja.get(j)
                    kolekcja.set(j+1, kolekcja.get(j))
                    j -= 1
            end
            kolekcja.set(j+1, key)
        end
    end
end

def timeit(&p)
    t1 = Time.now
    p.call()
    t2 = Time.now
    return t2 - t1
end




k1 = Kolekcja.new([5, 3, 1, 0, 5, 3, 1, 1, -10])
k2 = Kolekcja.new([5, 3, 1, 0, 5, 3, 1, 1, -10])


sortowanie = Sortowanie.new()
puts timeit{sortowanie.sort1(k1)}
puts k1

puts timeit{sortowanie.sort2(k2)}
puts k2