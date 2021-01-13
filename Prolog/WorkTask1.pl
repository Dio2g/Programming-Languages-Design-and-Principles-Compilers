fizzbuzz(X) :- 0 is X mod 15,
    			 writeln('FizzBuzz').
fizzbuzz(X) :- 0 is X mod 3,
    			 writeln('Fizz').
fizzbuzz(X) :- 0 is X mod 5,
    			 writeln('Buzz').
fizzbuzz(X) :- writeln(X).

fizzBuzzCount(X,Y) :- X =< Y,
    				  fizzbuzz(X),
                      !,
    				  Z is X + 1,
                      fizzBuzzCount(Z,Y).
    
    					
