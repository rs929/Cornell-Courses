open Dictionary

module type ElementSig = sig
  type t

  include Dictionary.KeySig with type t := t
end

module type Set = sig
  module Elt : ElementSig

  type elt = Elt.t
  type t

  val empty : t
  val is_empty : t -> bool
  val size : t -> int
  val insert : elt -> t -> t
  val member : elt -> t -> bool
  val remove : elt -> t -> t
  val union : t -> t -> t
  val intersect : t -> t -> t
  val difference : t -> t -> t
  val fold : (elt -> 'acc -> 'acc) -> 'acc -> t -> 'acc
  val to_list : t -> elt list

  include Stringable with type t := t
end

module Unit = struct
  type t = unit

  let compare x y = EQ
  let to_string t = ""
end

module Make =
functor
  (E : ElementSig)
  (DM : DictionaryMaker)
  ->
  struct
    module Elt = E

    type elt = Elt.t

    module D = DM (Elt) (Unit)

    type t = D.t
    (** AF: The dictionary {a1 : b1, ..., an : bn} represents the set 
      {a1, ..., an}, where a1...an is the sorted set of keys and 
      b1...bn are all the unit value (). The empty dictionary {} represents the 
      empty set {}
      RI: RI of D.t*)

    (*Begin Helper Functions***************************************************)
    let convert_func f k v init = f k init

    let rec set_to_list s =
      match s with
      | [] -> []
      | (a, _) :: t -> a :: set_to_list t

    (*End Helper Functions*****************************************************)

    let rep_ok s = s
    let empty = D.empty
    let is_empty s = D.is_empty s
    let size s = D.size s
    let insert x s = D.insert x () s
    let member x s = D.member x s
    let remove x s = D.remove x s
    let fold f init s = D.fold (convert_func f) init s
    let to_list s = s |> D.to_list |> set_to_list
    let union s1 s2 = fold insert s2 s1
    let intersect_helper s x acc = if member x s then insert x acc else acc
    let intersect s1 s2 = fold (intersect_helper s2) empty s1
    let difference_helper s x acc = if member x s then acc else insert x acc
    let difference s1 s2 = fold (difference_helper s2) empty s1

    let internal s =
      s |> to_list |> List.map (fun a -> Elt.to_string a) |> String.concat ", "

    let to_string s = "{" ^ internal (rep_ok s) ^ "}"
  end
