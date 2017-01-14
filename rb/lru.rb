class Node
  attr_accessor :value, :next_node, :prev_node

  def initialize(value, prev_node, next_node)
    @value = value
    @prev_node = prev_node
    @next_node = next_node
  end
end

class LRU
  attr_accessor :head, :tail, :num_items, :max_items

  def initialize(max_items)
    @max_items = max_items
    @table = {}
    @head = nil
    @tail = nil
    @num_items = 0
  end

  def set(key, value)
    @num_items += 1
    if @num_items > @max_items
      @head = @head.next_node
    end

    new_node = Node.new value, @tail, nil
    @head = new_node if tail == nil
    @tail.next_node = new_node if @tail != nil
    @tail = new_node
    @table[key] = new_node
  end

  def get(key)
    node = @table[key]
    return node if node.next_node.nil?

    if node.prev_node != nil
      node.prev_node.next_node = node.next_node
      node.next_node.prev_node = node.prev_node
    else
      @head = node.next_node
      @head.prev_node = nil
    end

    @tail.next_node = node
    node.next_node = nil
    node.prev_node = @tail
    @tail = node
  end
end

lru = LRU.new(3)
lru.set('a', 1)
lru.set('b', 2)
lru.set('c', 3)
puts lru.head.value
lru.get('a')
puts lru.head.value
lru.get('b')
puts lru.head.value
lru.get('c')
puts lru.head.value
lru.set('d', 8)
lru.set('e', 9)
puts lru.head.value
