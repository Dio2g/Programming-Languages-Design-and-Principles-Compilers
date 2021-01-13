sumList :: [Int] -> Int
sumList [] = 0
sumList (x:xs) = x + sumList xs

myReverse :: [Char] -> [Char]
myReverse [] = []
myReverse (x:xs) = myReverse xs ++ [x]

mulList :: [Int] -> Int
mulList [] = 1
mulList (x:xs) = x * mulList xs

main :: IO()
main = do print (sumList [1,2,3,4,5])
          print (myReverse "hello world")
          print (mulList [1,2,3])


