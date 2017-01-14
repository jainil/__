class TreeNode
  attr_accessor :left, :right, :value

  def initialize(value, left, right)
    @value = value
    @left, @right = left, right
  end

  def print_inorder
    @left.print_inorder unless @left.nil?
    puts @value
    @right.print_inorder unless @right.nil?
  end

  def inorder(&block)
    @left.inorder(&block) unless @left.nil?
    yield @value
    @right.inorder(&block) unless @right.nil?
  end

   def bst?
    return false if (@left != nil and @value < @left.value)
    return false if (@right != nil and @value > @right.value)
    left_bst = @left == nil ? true : @left.bst? 
    right_bst = @right == nil ? true : @right.bst?
    return (left_bst and right_bst)
  end
end

left_child = TreeNode.new(1, nil, nil)
right_child = TreeNode.new(3, nil, nil)
root = TreeNode.new(2, left_child, right_child)
root.print_inorder

root.inorder do |value|
  puts value
end