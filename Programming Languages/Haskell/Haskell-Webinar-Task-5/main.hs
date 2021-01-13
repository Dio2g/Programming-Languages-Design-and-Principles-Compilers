describeLetterIf :: Char -> String
describeLetterIf c =
    if c >= 'a' && c <= 'z'
        then "Lower case"
        else if c >= 'A' && c <= 'Z'
            then "Upper case"
            else "Not an ASCII letter"

describeLetterGuard :: Char -> String
describeLetterGuard c
   | c >= 'a' && c <= 'z' = "Lower case"
   | c >= 'A' && c <= 'Z' = "Upper case"
   | otherwise            = "Not an ASCII letter"

amountOfLowerCase :: [Char] -> Int
amountOfLowerCase [] = 0
amountOfLowerCase (x:xs)
   | x >= 'a' && x <= 'z' = 1 + amountOfLowerCase xs
   | otherwise            = 0 + amountOfLowerCase xs


amountOfLowerCase2 :: [Char] -> Int
amountOfLowerCase2 [] = 0
amountOfLowerCase2 (x:xs) =
   if x >= 'a' && x <= 'z'
        then 1 + amountOfLowerCase2 xs
          else 0 + amountOfLowerCase2 xs

main :: IO()
main = do print (describeLetterIf 'a')
          print (describeLetterGuard 'X')
          print (amountOfLowerCase ['a','b','c','D','E','f'])
          print (amountOfLowerCase2 ['a','b','c','D','E','f'])

