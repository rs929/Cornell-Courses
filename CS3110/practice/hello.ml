let _ = print_endline "Hello World"
let _ = print_endline "Goodbye World"
let _ = print_endline "Goodbye Cruel World"
let _ = print_endline "AHHHHHHHH"

let rec factorial x = if x < 2 then 1 else x * factorial (x - 1);;
let rec power x n = if x = 0 then 1 else x * power x (n-1);;
let rec power2 x n = if n = 0 then 1 else (if n mod 2 = 0 then x * x * power2 x (n/2) else x * power2 x (n/2));;

let _ = print_endline 