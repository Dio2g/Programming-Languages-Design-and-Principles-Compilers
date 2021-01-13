circPerim :: Float -> Float
circPerim r = 2 * pi * r

cm2m :: Float -> Float
cm2m d = d * 0.01

circPerimM :: Float -> Float
circPerimM = circPerim . cm2m

o2p :: Float -> Float
o2p x = x/16

p2s :: Float -> Float
p2s x = x/14

s2t :: Float -> Float
s2t x = x/157

o2s :: Float -> Float
o2s = p2s . o2p

o2t :: Float -> Float
o2t = s2t . p2s . o2p

p2t :: Float -> Float 
p2t = s2t . p2s

main :: IO()
main = do let radiusCm = 50.0
          let perimCm = circPerim radiusCm
          let perimM = cm2m perimCm
          print perimCm
          print perimM
          print (circPerimM radiusCm)
          print (o2p(16))
          print (p2s(14))
          print (s2t(157))
          print (o2s(224))
          print (o2t(35274))
          print (p2t(2205))



