numOfElements :: [a] -> Int
numOfElements [] = 0
numOfElements (x:xs) = numOfElements xs + 1