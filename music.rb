#author: Silas Mederer
#version:: v0.1

class Song
  def initialize(name,kuenstler)
    @name = name
    @kuenstler = kuenstler
  end

  def to_s()
  "|Song:: #{@name} #{@kuenstler}"
  end
end


class Kuenstler

  def initialize(name, gruppe)
    @name = name
    @gruppe = gruppe
  end

  def to_s()
    "|Künstler:: #{@name}" + " |Gruppe:: #{@gruppe}"
  end

end

song = Song.new("Corona", Kuenstler.new("Udo Seuchenberg", "Quarantäne-Quruppe"))
puts(song)