countElements([],0).
countElements([_|T],X) :- countElements(T,X1), X is X1+1.
