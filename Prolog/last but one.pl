lastButOne(X,[X,Y]).
lastButOne(X, [_|T]) :- lastButOne(X,T).