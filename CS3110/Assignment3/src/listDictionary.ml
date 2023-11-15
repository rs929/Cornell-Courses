open Dictionary

module Make : DictionaryMaker =
functor
  (K : KeySig)
  (V : ValueSig)
  ->
  struct
    module Key = K
    module Value = V

    type key = K.t
    type value = V.t

    type t = (key * value) list
    (** AF: The list [(a1, b1), ..., (an, bn)] represents the dictionary
      {a1 : b1, ..., an : bn}, where a1...an is the sorted set of keys and 
      b1...bn is the set of values, where bk is the value associated to the ak
      for all + integers k. The empty list [] represents the empty dictionary {}
      RI: None*)

    (*Begin Helper Functions***************************************************)

    let dict_sort lst =
      List.sort
        (fun (a, b) (x, y) ->
          match K.compare a x with
          | LT -> -1
          | EQ -> 0
          | GT -> 1)
        lst

    let rec get_value k d =
      match d with
      | [] -> None
      | (a, b) :: t -> if K.compare a k = EQ then Some b else get_value k t

    let rec set_value k v d acc =
      match d with
      | [] -> acc
      | (a, b) :: t ->
          if K.compare a k = EQ then set_value k v t ((a, v) :: acc)
          else set_value k v t ((a, b) :: acc)

    let rec remove_key k d acc =
      match d with
      | [] -> acc
      | (a, b) :: t ->
          if K.compare a k = EQ then remove_key k t acc
          else remove_key k t ((a, b) :: acc)

    let rec fold_acc f init d =
      match d with
      | [] -> init
      | (k, v) :: t -> fold_acc f (f k v init) t

    (*End Helper Functions*****************************************************)

    let rep_ok d = d
    let empty = []
    let is_empty d = d = empty
    let size d = d |> rep_ok |> List.length

    let member k d =
      let result = d |> rep_ok |> get_value k in
      match result with
      | None -> false
      | Some x -> true

    let find k d = d |> rep_ok |> get_value k

    let insert k v d =
      let lst = if member k d then set_value k v d [] else (k, v) :: d in
      lst |> dict_sort |> rep_ok

    let remove k d = remove_key k (rep_ok d) [] |> dict_sort
    let to_list d = d

    let fold f init d =
      let sorted = dict_sort d in
      sorted |> fold_acc f init

    let internal lst =
      lst |> rep_ok
      |> List.map (fun (a, b) -> K.to_string a ^ " : " ^ V.to_string b)
      |> String.concat ", "

    let to_string d =
      (* Hint: use a [Util] helper function. *)
      "{" ^ internal (rep_ok d) ^ "}"
  end
