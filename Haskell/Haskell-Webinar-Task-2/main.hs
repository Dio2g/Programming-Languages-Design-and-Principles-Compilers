circPerim :: Float -> Float
circPerim r = 2 * pi * r

circArea :: Float -> Float
circArea r = pi * r ^ 2

squareArea :: Float -> Float 
squareArea a = a^2

squarePerim :: Float -> Float 
squarePerim a = 4*a

rectArea :: (Float,Float) -> Float 
rectArea (l,w) = l*w

rectPerim :: (Float,Float) -> Float 
rectPerim (l,w) = 2*(l+w)

main :: IO()
main = do let radius = 5.0
          print (circArea radius)
          print (circPerim radius)
          print (squareArea(4))
          print (squarePerim(4))
          print (rectArea(3,4))
          print (rectPerim(3,4))


