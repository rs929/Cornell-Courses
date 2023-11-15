(* Note: You may introduce new code anywhere in this file. *)

type object_phrase = string list

type command =
  | Go of object_phrase
  | Quit

exception Empty
exception Malformed

(* Helper functions defined below: *)
(* ######################################################### *)
let rec remove_empty (lst : string list) =
  match lst with
  | [] -> []
  | h :: t -> if h = "" then remove_empty t else h :: remove_empty t

let valid_command (verb : string) (obj : string list) =
  if verb <> "go" && verb <> "quit" then raise Malformed
  else if verb = "go" then
    match obj with
    | [] -> raise Malformed
    | verb_obj -> Go verb_obj
  else if verb = "quit" && obj = [] then Quit
  else raise Malformed

(* ######################################################### *)
(* End of defined helper functions *)
let parse str =
  let lst = str |> String.split_on_char ' ' |> remove_empty in
  match lst with
  | [] -> raise Empty
  | h :: t -> valid_command h t
