import Data.Char

getBirthYear :: Int -> Int
getBirthYear x = 2020 - x

main :: IO()
main = do 
       putStrLn "Enter your age"
       age <- getLine
       let x = (read age :: Int)
       print (getBirthYear (x))
