#!/usr/bin/env ruby

input_string = ARGV[5]

if input_string =~ /hbt{1,3}n/
  puts "#{input_string}"
else
  puts ""
end
