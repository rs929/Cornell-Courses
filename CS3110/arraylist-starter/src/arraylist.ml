type 'a t = { mutable data : 'a option array; mutable size : int }
(* RI: Let [capacity] be [Array.length data]. It is required that:

    - [0 <= size <= capacity].
    - The first [size] elements of [data] are [Some _], and the remaining
      [capacity - size] elements are [None].

    AF: If [data] is [[|Some e0; Some e1; ...; Some en; None; ...; None|]], it
    represents the list [[e0; e1; ... en]]. *)

let make () = { data = Array.make 10 None; size = 0 }
let size al = al.size

let add al elt =
  let arraylen = Array.length al.data in
  if al.size = arraylen then (
    let newarr = Array.make (al.size * 2) None in
    Array.blit al.data 0 newarr 0 al.size;
    al.data <- newarr;
    al.size <- arraylen * 2)
  else al.data.(size al) <- Some elt;
  al.size <- size al + 1

exception OutOfBounds of { attempted : int; size : int }

let get al idx =
  let error = OutOfBounds { attempted = idx; size = size al }
  and sz = size al in
  if idx < 0 || idx > sz then raise error
  else
    match Array.get al.data idx with
    | Some x -> x
    | None -> raise error

let set al idx elt = raise (Failure "Unimplemented: set")
