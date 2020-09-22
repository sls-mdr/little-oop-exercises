#author: Silas Mederer
#Version:: v0.1

def readNumber()
  var = " "
  while(true)

    puts()
    puts("Bitte geben Sie eine Zahl ein!")
    var = gets.chomp

    if(false if Float(var) rescue true)
      puts "Das war keine Zahl!"
    elsif(false if Float(var) rescue true)
      puts "Das war keine Zahl!"
    else
      puts("Die eingegebene Zahl ist: #{var}")
    end
  end

end

readNumber()
