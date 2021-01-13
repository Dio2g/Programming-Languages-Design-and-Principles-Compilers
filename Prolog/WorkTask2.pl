factorial(1,1) :- !.
factorial(X,Y) :- I is X - 1,
                  factorial(I,J),
                  Y is X * J.
    			