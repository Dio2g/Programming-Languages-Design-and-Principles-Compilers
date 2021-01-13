countChar(_Char,[],0).
countChar(Char,[H|T],Result) :- H = Char,
 countChar(Char,T,TailResult),
Result is TailResult + 1.

countChar(Char,[H|T],Result) :- H \= Char,
 countChar(Char,T,TailResult),
Result is TailResult.

getAlphabet(X) :- string_chars("abcdefghijklmnopqrstuvwxyz",
X).

myWrite(_Char, 0) :- !.
myWrite(Char, Frequency) :- write(Char),
 write('='),
writeln(Frequency).

countAlphabet([],_Str).
countAlphabet([H|T],Str) :- countChar(H,Str,Result),
 myWrite(H,Result),
 countAlphabet(T,Str).

countLetters(String) :- string_chars(String,Str_List),
 getAlphabet(X),
countAlphabet(X,Str_List).