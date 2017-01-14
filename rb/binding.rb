def return_binding
  foo = 100
  binding
end

puts return_binding.class
puts return_binding.eval('foo')

puts foo