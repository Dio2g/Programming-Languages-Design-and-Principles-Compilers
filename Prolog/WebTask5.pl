countA([],0).
countA([H|T],X) :-
    H = 'a',
    countA(T,Y),
    X is Y + 1.

countA([H|T],X) :-
    H \= 'a',
    countA(T,Y),
    X is Y.

countChar(Y,X) :-
    string_chars(Y,Str),
    countA(Str,X).

rev([X],[X]).
rev([H|T],X) :- rev(T,R),
    append(R,[H],X).

myReverse(X,Y) :- string_chars(X,Str),
    rev(Str,R_Str),
    string_chars(Y,R_Str).
    
