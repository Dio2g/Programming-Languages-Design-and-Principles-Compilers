element_at(X,[X|T],1).
element_at(X,[H|T],N) :-
  N1 is N - 1,
  element_at(X,T,N1).