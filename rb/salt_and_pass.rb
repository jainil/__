require 'BCrypt'

plain = ARGV[0]
 
p "Plain: #{plain}"

salt = BCrypt::Engine.generate_salt
pass = BCrypt::Engine.hash_secret(plain, salt)

p "Salt: #{salt}"
p "Password: #{pass}"