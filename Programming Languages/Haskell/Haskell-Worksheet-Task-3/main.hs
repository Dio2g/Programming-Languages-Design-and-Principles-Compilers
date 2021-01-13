import Data.Char

countLetter :: [Char] -> Char -> Int
countLetter [] c = 0
countLetter (x:xs) c | c == x = 1 + countLetter xs c
                     | otherwise = countLetter xs c

countAlphabet :: [Char] -> [Int]
countAlphabet str = map (countLetter str) ['a'..'z']

getOutput :: Char -> [Int] -> [String]
getOutput c [] = []
getOutput c (x:xs) | x == 0 = getOutput (chr (ord c + 1)) xs
                   | otherwise = [(show c) ++ " = " ++ (show x)] ++ getOutput (chr (ord c + 1)) xs

callGetOutput :: [Int] -> [String]
callGetOutput frequencies = getOutput 'a' frequencies

main :: IO()
main = do putStrLn "enter your String"
          input <- getLine
          let frequencies = countAlphabet input
          let output = callGetOutput frequencies
          mapM_ putStrLn output