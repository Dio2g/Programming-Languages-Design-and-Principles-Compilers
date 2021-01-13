lastElement :: [a] -> a
lastElement [] = error "No end for empty lists!"
lastElement [x] = x
lastElement (x:xs) = lastElement(xs)