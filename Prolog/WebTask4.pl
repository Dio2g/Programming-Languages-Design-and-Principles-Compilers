lastElement(X,[X]).
lastElement(X,[_|L]) :- lastElement(X,L).
