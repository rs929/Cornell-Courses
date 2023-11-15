
type data = String of string | Float of float | Null;;
type series = string * data list;;
type frame = series list;;

let rec count ser =
  match ser with
  | (a, b) -> List.length b

let rec count1 (_,lst) = List.length lst

let rec sum (_, lst) =
  match lst with
  | [] -> 0
  | (a : float) :: b -> a + 