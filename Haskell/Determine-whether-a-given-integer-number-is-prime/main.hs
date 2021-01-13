isPrime :: Int -> Bool
isPrime k = if k > 1 then null [x | x <- [2..k-1], k `mod` x == 0] else False 