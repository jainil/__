# proc returns from the current context
def call_proc
  puts "Before proc"
  my_proc = Proc.new{ return 2 }
  my_proc.call
  puts "after proc"
end

p call_proc