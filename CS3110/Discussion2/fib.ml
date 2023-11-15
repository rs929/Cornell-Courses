let rec fib n =
  if n == 0 then 0 else (if n == 1 then 1 else fib (n-1) + fib (n-2));;

let rec step (a, b) = 
  (b, a+b)

let rec fib_loop n (x, y)= 
  if n == 0 then (x, y) else fib_loop (n-1) (step(x, y));;