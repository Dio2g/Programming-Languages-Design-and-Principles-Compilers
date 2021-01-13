pronounce :: Int -> String

pronounce 0 = "zero"
pronounce 1 = "one"
pronounce 2 = "two"
pronounce 3 = "three"
pronounce 4 = "four"
pronounce 5 = "five"
pronounce 6 = "six"
pronounce 7 = "seven"
pronounce 8 = "eight"
pronounce 9 = "nine"

pronounceNum :: [Int] -> [String]
pronounceNum x = map pronounce x 