factorial :: Int -> Int
factorial 1 = 1
factorial x = x * factorial (x - 1)
