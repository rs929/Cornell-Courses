let name = if Array.length Sys.argv = 1 then "unknown OCaml programmer!" else Sys.argv.(1);;
let result = "Hello " ^ name;;
let _ = print_endline result;;