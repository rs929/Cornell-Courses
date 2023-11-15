open Dictionary

module Make =
functor
  (K : KeySig)
  (V : ValueSig)
  ->
  struct
    module Key = K
    module Value = V

    type key = K.t
    type value = V.t

    (** AF: The tree (v, l, r) represents the dictionary
      {a1 : b1, ..., an : bn}, where v is the pair (a, b) and the sub trees
      are of the same formata1...an is the sorted set of keys and b1...bn 
      is the set of values, where bk is the value associated to the ak for all 
      + integers k. The empty tree Leaf represents the empty dictionary {}
      RI: None*)
    type color =
      | Red
      | Black

    type t =
      | Leaf
      | Node of (color * (key * value) * t * t)

    (*Begin Helper Functions***************************************************)
    let rec size_helper d =
      match d with
      | Leaf -> 0
      | Node (c, v, l, r) -> 1 + size_helper l + size_helper r

    let rec mem_helper k d =
      match d with
      | Leaf -> false
      | Node (c, v, l, r) ->
          let a, _ = v in
          (match Key.compare a k with
          | LT -> false
          | EQ -> true
          | GT -> false)
          || mem_helper k l || mem_helper k r

    let rec find_helper k d =
      match d with
      | Leaf -> None
      | Node (c, v, l, r) -> (
          let a, b = v in
          match Key.compare a k with
          | LT -> find_helper k r
          | EQ -> Some b
          | GT -> find_helper k l)

    let balance = function
      | Black, z, Node (Red, y, Node (Red, x, a, b), c), d
      | Black, z, Node (Red, x, a, Node (Red, y, b, c)), d
      | Black, x, a, Node (Red, z, Node (Red, y, b, c), d)
      | Black, x, a, Node (Red, y, b, Node (Red, z, c, d)) ->
          Node (Red, y, Node (Black, x, a, b), Node (Black, z, c, d))
      | a, b, c, d -> Node (a, b, c, d)

    let rec insert_helper k v d =
      match d with
      | Leaf -> Node (Red, (k, v), Leaf, Leaf)
      | Node (c, x, l, r) -> (
          let a, b = x in
          match Key.compare a k with
          | LT -> balance (c, (a, b), l, insert_helper k v r)
          | GT -> balance (c, (a, b), insert_helper k v l, r)
          | EQ -> balance (c, (k, v), l, r))

    let rec fold_helper f acc d =
      match d with
      | Leaf -> acc
      | Node (c, v, l, r) ->
          let a, b = v in
          fold_helper f (f a b (fold_helper f acc l)) r

    (*End Helper Functions*****************************************************)
    let rep_ok d = d [@@coverage off]
    let empty = Leaf
    let is_empty d = d = empty
    let size d = size_helper d
    let member k d = mem_helper k d

    let insert k v d =
      match insert_helper k v d with
      | Node (_, (y, z), a, b) -> Node (Black, (y, z), a, b)
      | Leaf ->
          (* guaranteed to be nonempty *)
          failwith "RBT insert failed with ins returning leaf"

    let remove k d = d
    let find k d = find_helper k d

    let rec tree_to_list d =
      match d with
      | Leaf -> []
      | Node (c, x, l, r) ->
          let k, v = x in
          tree_to_list l @ [ (k, v) ] @ tree_to_list r

    let to_list d = tree_to_list d
    let fold f acc d = fold_helper f acc d

    let rec internal lst =
      lst |> rep_ok
      |> List.map (fun (a, b) -> K.to_string a ^ " : " ^ V.to_string b)
      |> String.concat ", "

    let to_string d = "{" ^ internal (to_list d) ^ "}"
  end
