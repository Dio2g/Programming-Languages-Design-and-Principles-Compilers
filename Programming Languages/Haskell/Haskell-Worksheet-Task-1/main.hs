fizzbuzz :: Int -> String
fizzbuzz x
  | mod x 15 == 0 = "FizzBuzz"
  | mod x 3 == 0 = "Fizz"
  | mod x 5 == 0 = "Buzz"
  | otherwise = show x

fizzbuzzRecursive :: [Int] -> [String]
fizzbuzzRecursive [] = []
fizzbuzzRecursive (x:xs) = [fizzbuzz x] ++ fizzbuzzRecursive xs

main :: IO()
main = do 
print(fizzbuzzRecursive [1..100])
       
