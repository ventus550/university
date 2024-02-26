
class Item
    attr_accessor :next
    attr_accessor :prev
    attr_accessor :value
    attr_reader   :value

    def initialize(value, prv, nxt)
        
        @value = value
        @next = nxt
        @prev = prv

        if @prev
            @prev.next = self
        end

        if @next
            @next.prev = self
        end 
    end

    def to_s
        "Item with value: #{@value}"
    end
end

class Kolekcja
    attr_accessor :len

    def initialize
        @head = nil
        @len = 0
    end

    def insert(value)
        @len += 1
        if @head
            if @head.value >= value
               @head = Item.new(value, nil, @head)
               return
            end

            p = @head
            while (p.next && p.next.value <= value)
                p = p.next
            end

            Item.new(value, p, p.next)
        else
            @head = Item.new(value, nil, nil)
        end
    end

    def [](i)
        p = @head
        i.times {p = p.next}
        return p.value
    end

    def []=(i, value)
        p = @head
        i.times {p = p.next}
        p.value = value
    end

    def print
        node = @head
        puts node
        while (node = node.next)
            puts node
        end
    end
end


class Wyszukiwanie
    def initialize
    end

    def bsearch(k, val)

        def search(k, val, a, b)

            if a > b
                return -1
            end

            n = (a + b - 1) / 2

            if k[n] == val
                return n
            end
            
            if k[n] > val
                return search(k, val, a, n - 1)
            else
                return search(k, val, n + 1, b)
            end
        end

        return search(k, val, 0, k.len)
    end



    def isearch(k, val)

        def search(k, val, lo, hi) 

            if lo <= hi && val >= k[lo] && val <= k[hi]   

                pos = lo + (((hi - lo).to_f / (k[hi] - k[lo])) * (val - k[lo])).round; 
                
                if k[pos] == val
                    return pos;
                end

                if k[pos] < val
                    return search(k, val, pos+1, hi);
                end
                    
                if k[pos] > val
                    return search(k, val, lo, pos-1);
                end
            end
            
            return -1; 
        end

        search(k, val, 0, k.len - 1)
    end
  

end





LL = Kolekcja.new()
LL.insert(10)
LL.insert(5)
LL.insert(1)
LL.insert(5)
LL.insert(5)
LL.insert(15)
LL.insert(3)
LL.insert(1)
LL.print

wyszukiwanie = Wyszukiwanie.new()
puts wyszukiwanie.isearch(LL, 0)
puts wyszukiwanie.isearch(LL, 0)

puts wyszukiwanie.isearch(LL, 10)
puts wyszukiwanie.isearch(LL, 10)