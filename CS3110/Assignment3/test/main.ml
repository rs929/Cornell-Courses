open OUnit2
open Search

(*****************************************************************)
(* Examples of how to create data structures *)
(*****************************************************************)

module Int = struct
  type t = int

  let compare x y =
    match Stdlib.compare x y with
    | x when x < 0 -> Dictionary.LT
    | 0 -> EQ
    | _ -> GT

  let to_string = string_of_int
end

module String = struct
  type t = string

  let compare x y =
    match Stdlib.compare x y with
    | x when x < 0 -> Dictionary.LT
    | 0 -> EQ
    | _ -> GT

  let to_string x = x
end

module Float = struct
  type t = float

  let compare x y =
    match Stdlib.compare x y with
    | x when x < 0 -> Dictionary.LT
    | 0 -> EQ
    | _ -> GT

  let to_string = string_of_float
end

(* Example: A list dictionary that maps ints to ints. *)
module D1 = ListDictionary.Make (Int) (Int)

(* Example: A set of strings, implemented with list dictionaries. *)
module S1 = DictionarySet.Make (StringKey.String) (ListDictionary.Make)

(* Example: A tree dictionary that maps case-insensitive strings to ints. *)
module D2 = TreeDictionary.Make (StringKey.CaselessString) (Int)

(* Example: A set of strings, implemented with tree dictionaries. *)
module S2 = DictionarySet.Make (StringKey.String) (TreeDictionary.Make)

(*****************************************************************)
(* Examples of how to index a directory *)
(*****************************************************************)

let data_dir_prefix = "data" ^ Filename.dir_sep
let preamble_path = data_dir_prefix ^ "preamble"

let preamble_list_idx =
  try Some (ListEngine.E.index_of_dir preamble_path) with _ -> None

let preamble_tree_idx =
  try Some (TreeEngine.E.index_of_dir preamble_path) with _ -> None

(*****************************************************************)
(* Test suite *)
(*****************************************************************)
let remove_test = false

module TestDictionary (Dict : Dictionary.DictionaryMaker) = struct
  module D1 = Dict (Int) (Int)
  module D2 = Dict (String) (Int)
  module D3 = Dict (String) (String)
  module D4 = Dict (Int) (String)

  let test_is_empty =
    [
      ( "(int : int) Test is_empty: empty dict" >:: fun _ ->
        assert_equal true D1.(empty |> is_empty) );
      ( "(int : int) Test is_empty: non-empty dict" >:: fun _ ->
        assert_equal false D1.(empty |> insert 1 1 |> is_empty) );
      ( "(string : int) Test is_empty: empty dict" >:: fun _ ->
        assert_equal true D2.(empty |> is_empty) );
      ( "(string : int) Test is_empty: non-empty dict" >:: fun _ ->
        assert_equal false D2.(empty |> insert "One" 1 |> is_empty) );
      ( "(string : string) Test is_empty: empty dict" >:: fun _ ->
        assert_equal true D3.(empty |> is_empty) );
      ( "(string : string) Test is_empty: non-empty dict" >:: fun _ ->
        assert_equal false D3.(empty |> insert "One" "OCaml" |> is_empty) );
    ]

  let emptydict = "{}"
  let dict1 = [ "{1 : 2}"; "{1 : 2, 3 : 4}"; "{1 : 12}"; "{0 : 4, 1 : 2}" ]
  let dict2 = [ "{Apples : 3}"; "{Apples : 3, Oranges : 5}" ]
  let dict3 = [ "{Name : Richie}"; "{Name : Richie, NetID : rs929}" ]
  let dict4 = "{1 : 2, 3 : 4, 5 : 6, 7 : 8, 9 : 10, 11 : 12, 13 : 14, 15 : 16}"

  let test_size =
    [
      ( "(int : int) Test size: empty dict" >:: fun _ ->
        assert_equal 0 D1.(empty |> size) );
      ( "(int : int) Test size: {1 : 2, 4 : 5}" >:: fun _ ->
        assert_equal 2 D1.(empty |> insert 1 2 |> insert 4 5 |> size) );
      ( "(string : int) Test size: empty dict" >:: fun _ ->
        assert_equal 0 D2.(empty |> size) );
      ( "(string : int) Test size: {Help : 2, Me : 5}" >:: fun _ ->
        assert_equal 2 D2.(empty |> insert "Help" 2 |> insert "Me" 5 |> size) );
      ( "(string : string) Test size: empty dict" >:: fun _ ->
        assert_equal 0 D3.(empty |> size) );
      ( "(string : string) Test size: {Help : Me, Please : Help}" >:: fun _ ->
        assert_equal 2
          D3.(empty |> insert "Help" "Me" |> insert "Please" "Help" |> size) );
    ]

  let test_insert =
    [
      ( "Test insert: (1, 2) to empty)" >:: fun _ ->
        assert_equal (List.nth dict1 0) D1.(empty |> insert 1 2 |> to_string) );
      ( "Test insert: (3, 4) to {1 : 2})" >:: fun _ ->
        assert_equal (List.nth dict1 1)
          D1.(empty |> insert 1 2 |> insert 3 4 |> to_string) );
      ( "Test insert: (1, 12) to {1 : 2})" >:: fun _ ->
        assert_equal (List.nth dict1 2)
          D1.(empty |> insert 1 2 |> insert 1 12 |> to_string) );
      ( "Test insert: (0, 4) to {1 : 2})" >:: fun _ ->
        assert_equal (List.nth dict1 3)
          D1.(empty |> insert 1 2 |> insert 0 4 |> to_string) );
      ( "Test insert: (Apples, 3) to empty)" >:: fun _ ->
        assert_equal (List.nth dict2 0)
          D2.(empty |> insert "Apples" 3 |> to_string) );
      ( "Test insert: (Oranges, 5) to {Apples : 3})" >:: fun _ ->
        assert_equal (List.nth dict2 1)
          D2.(empty |> insert "Apples" 3 |> insert "Oranges" 5 |> to_string) );
      ( "Test insert: (Name, Richie) to empty)" >:: fun _ ->
        assert_equal (List.nth dict3 0)
          D3.(empty |> insert "Name" "Richie" |> to_string) );
      ( "Test insert: (NetID, rs929) to {Name : Richie})" >:: fun _ ->
        assert_equal (List.nth dict3 1)
          D3.(
            empty |> insert "Name" "Richie" |> insert "NetID" "rs929"
            |> to_string) );
      ( "Test insert: A lot of numbers into {})" >:: fun _ ->
        assert_equal dict4
          D1.(
            empty |> insert 11 12 |> insert 3 4 |> insert 5 6 |> insert 7 8
            |> insert 9 10 |> insert 1 2 |> insert 13 14 |> insert 15 16
            |> to_string) );
    ]

  let test_member =
    [
      ( "Test member: 1 in empty" >:: fun _ ->
        assert_equal false D1.(empty |> member 1) );
      ( "Test member: 1 in {1 : 2}" >:: fun _ ->
        assert_equal true D1.(empty |> insert 1 2 |> member 1) );
      ( "Test member: 2 in {1 : 2}" >:: fun _ ->
        assert_equal false D1.(empty |> insert 1 2 |> member 2) );
    ]

  let test_find =
    [
      ( "Test find: 1 in empty" >:: fun _ ->
        assert_equal None D1.(empty |> find 1) );
      ( "Test find: 2 in {1 : 2}" >:: fun _ ->
        assert_equal None D1.(empty |> insert 1 2 |> find 2) );
      ( "Test find: 1 in {1 : 2}" >:: fun _ ->
        assert_equal (Some 2) D1.(empty |> insert 1 2 |> find 1) );
      ( "Test find: 1 in {1 : zxcasdfs2}" >:: fun _ ->
        assert_equal (Some "2")
          (let _ =
             print_endline
               (match
                  D4.(
                    empty |> insert 1 "1" |> insert 2 "2" |> insert 1 "1"
                    |> insert 2 "2" |> insert 1 "1" |> insert 2 "2"
                    |> insert 1 "1" |> insert 1 "1" |> insert 2 "2"
                    |> insert 2 "2" |> find 1)
                with
               | Some a -> a
               | None -> "")
           in
           D4.(
             empty |> insert 1 "1" |> insert 2 "2" |> insert 1 "1"
             |> insert 2 "2" |> insert 1 "1" |> insert 2 "2" |> insert 1 "1"
             |> insert 1 "1" |> insert 2 "2" |> insert 2 "2" |> find 2)) );
    ]

  let add_values k v init = init + v
  let add_keys k v init = init + k
  let add_key_values k v init = init + k + v
  let concat_keys k v init = k ^ " " ^ init

  let test_fold =
    [
      ( "Test fold: add values in {}" >:: fun _ ->
        assert_equal 0 D1.(empty |> fold add_values 0) );
      ( "Test fold: add values in {1 : 2, 3 : 4}" >:: fun _ ->
        assert_equal 6
          D1.(empty |> insert 1 2 |> insert 3 4 |> fold add_values 0) );
      ( "Test fold: add keys in {1 : 2, 3 : 4}" >:: fun _ ->
        assert_equal 4 D1.(empty |> insert 1 2 |> insert 3 4 |> fold add_keys 0)
      );
      ( "Test fold: add keys and values in {1 : 2, 3 : 4}" >:: fun _ ->
        assert_equal 10
          D1.(empty |> insert 1 2 |> insert 3 4 |> fold add_key_values 0) );
      ( "Test fold: add keys and values in {1 : 2, 3 : 4, 5 : 6, 7 : 10}"
      >:: fun _ ->
        assert_equal 38
          D1.(
            empty |> insert 1 2 |> insert 3 4 |> insert 5 6 |> insert 7 10
            |> fold add_key_values 0) );
      ( "Test fold: concat keys in {My : 3, Brain Cells : 1}" >:: fun _ ->
        assert_equal "My Brain Cells "
          D2.(
            empty |> insert "My" 3 |> insert "Brain Cells" 1
            |> fold concat_keys "") );
    ]

  let assoc_empty = []
  let assoclist1 = [ (1, 2) ]
  let assoclist2 = [ (1, 2); (3, 4); (5, 6) ]

  let test_to_list =
    [
      ( "Test to_list: empty" >:: fun _ ->
        assert_equal assoc_empty D1.(empty |> to_list) );
      ( "Test to_list: {1 : 2}" >:: fun _ ->
        assert_equal assoclist1 D1.(empty |> insert 1 2 |> to_list) );
      ( "Test to_list: {1 : 2}" >:: fun _ ->
        assert_equal assoclist2
          D1.(empty |> insert 1 2 |> insert 3 4 |> insert 5 6 |> to_list) );
      ( "Test to_list: {1 : 2}" >:: fun _ ->
        assert_equal assoclist2
          D1.(empty |> insert 3 4 |> insert 5 6 |> insert 1 2 |> to_list) );
    ]

  let tests =
    "test dictionary"
    >::: List.flatten
           [
             test_is_empty;
             test_size;
             test_insert;
             test_member;
             test_find;
             test_fold;
             test_to_list;
           ]
end

module TestSet (DM : Dictionary.DictionaryMaker) = struct
  module S1 = DictionarySet.Make (Int) (DM)
  module S2 = DictionarySet.Make (String) (DM)
  module S3 = DictionarySet.Make (Float) (DM)

  let test_is_empty =
    [
      ( "Int Set Test is_empty: empty set" >:: fun _ ->
        assert_equal true S1.(empty |> is_empty) );
      ( "Int Set Test is_empty: non-empty set" >:: fun _ ->
        assert_equal false S1.(empty |> insert 1 |> is_empty) );
      ( "String Set Test is_empty: empty set" >:: fun _ ->
        assert_equal true S2.(empty |> is_empty) );
      ( "String Set Test is_empty: non-empty set" >:: fun _ ->
        assert_equal false S2.(empty |> insert "Hello" |> is_empty) );
      ( "Float Set Test is_empty: empty set" >:: fun _ ->
        assert_equal true S3.(empty |> is_empty) );
      ( "Float Set Test is_empty: non-empty set" >:: fun _ ->
        assert_equal false S3.(empty |> insert 3.33 |> is_empty) );
    ]

  let test_size =
    [
      ( "Int Set Test size: empty set" >:: fun _ ->
        assert_equal 0 S1.(empty |> size) );
      ( "Int Set  Test size: {1 : 2, 4 : 5}" >:: fun _ ->
        assert_equal 2 S1.(empty |> insert 1 |> insert 4 |> size) );
      ( "String Set Test size: empty set" >:: fun _ ->
        assert_equal 0 S2.(empty |> size) );
      ( "String Set Test size: {Help : 2, Me : 5}" >:: fun _ ->
        assert_equal 2 S2.(empty |> insert "Help" |> insert "Me" |> size) );
      ( "Float Set Test size: empty dict" >:: fun _ ->
        assert_equal 0 S3.(empty |> size) );
      ( "Float Set Test size: {Help : Me, Please : Help}" >:: fun _ ->
        assert_equal 2 S3.(empty |> insert 1.1 |> insert 2.2 |> size) );
    ]

  let set1 = [ "{1}"; "{1, 2}"; "{1, 2, 5}" ]
  let set2 = [ "{hello}"; "{hello, world}"; "{hello, my, world}" ]

  let test_insert =
    [
      ( "Int Set Test insert: 1 to empty " >:: fun _ ->
        assert_equal (List.nth set1 0) S1.(empty |> insert 1 |> to_string) );
      ( "Int Set Test insert: 1 to {1} " >:: fun _ ->
        assert_equal (List.nth set1 0)
          S1.(empty |> insert 1 |> insert 1 |> to_string) );
      ( "Int Set Test insert: 2 to {1} " >:: fun _ ->
        assert_equal (List.nth set1 1)
          S1.(empty |> insert 1 |> insert 2 |> to_string) );
      ( "Int Set Test insert: 2 to {1, 5} " >:: fun _ ->
        assert_equal (List.nth set1 2)
          S1.(empty |> insert 1 |> insert 5 |> insert 2 |> to_string) );
      ( "String Set Test insert: hello to empty " >:: fun _ ->
        assert_equal (List.nth set2 0) S2.(empty |> insert "hello" |> to_string)
      );
      ( "String Set Test insert: hello to {hello} " >:: fun _ ->
        assert_equal (List.nth set2 0)
          S2.(empty |> insert "hello" |> insert "hello" |> to_string) );
      ( "String Set Test insert: world to {hello} " >:: fun _ ->
        assert_equal (List.nth set2 1)
          S2.(empty |> insert "hello" |> insert "world" |> to_string) );
      ( "String Set Test insert: my to {hello, world} " >:: fun _ ->
        assert_equal (List.nth set2 2)
          S2.(
            empty |> insert "hello" |> insert "world" |> insert "my"
            |> to_string) );
    ]

  let test_member =
    [
      ( "Int Set Test member: 1 in empty" >:: fun _ ->
        assert_equal false S1.(empty |> member 1) );
      ( "Int Set Test member: 1 in {1}" >:: fun _ ->
        assert_equal true S1.(empty |> insert 1 |> member 1) );
      ( "Int Set Test member: 2 in {1}" >:: fun _ ->
        assert_equal false S1.(empty |> insert 1 |> member 2) );
      ( "String Set Test member: hello in empty" >:: fun _ ->
        assert_equal false S2.(empty |> member "hello") );
      ( "String Set Test member: hello in {hell}" >:: fun _ ->
        assert_equal true S2.(empty |> insert "hello" |> member "hello") );
      ( "String Set Test member: HELLO in {hello}" >:: fun _ ->
        assert_equal false S2.(empty |> insert "hello" |> member "HELLO") );
    ]

  let test_fold =
    [
      ( "Int Set Test fold: add values in {}" >:: fun _ ->
        assert_equal 0 S1.(empty |> fold ( + ) 0) );
      ( "Int Set Test fold: add values in {1, 3}" >:: fun _ ->
        assert_equal 4 S1.(empty |> insert 1 |> insert 3 |> fold ( + ) 0) );
      ( "Int Set Test fold: subtract keys in {1, 3, 4}" >:: fun _ ->
        assert_equal 2
          S1.(empty |> insert 1 |> insert 3 |> insert 4 |> fold ( - ) 0) );
      ( "String Set Test fold: concat values in {}" >:: fun _ ->
        assert_equal "" S2.(empty |> fold ( ^ ) "") );
      ( "String Set Test fold: concat values in {hello, world}" >:: fun _ ->
        assert_equal "worldhello"
          S2.(empty |> insert "hello" |> insert "world" |> fold ( ^ ) "") );
    ]

  let s1 = S1.(empty |> insert 1 |> insert 2 |> insert 3)
  let s2 = S1.(empty |> insert 4 |> insert 5 |> insert 6)
  let s3 = S1.(empty |> insert 3)
  let s4 = S1.(empty |> insert 1 |> insert 3 |> insert 4)
  let s1_4 = S1.(empty |> insert 2)
  let s1n4 = S1.(empty |> insert 1 |> insert 3)

  let s1u2 =
    S1.(
      empty |> insert 1 |> insert 2 |> insert 3 |> insert 4 |> insert 5
      |> insert 6)

  let test_union =
    [
      ( "Int Set Test union: union {} {}" >:: fun _ ->
        assert_equal S1.empty S1.(union empty empty) );
      ( "Int Set Test union: union {} {1, 2, 5}" >:: fun _ ->
        assert_equal s1
          S1.(empty |> insert 1 |> insert 2 |> insert 3 |> union empty) );
      ( "Int Set Test union: union {4, 5, 6} {1, 2, 3}" >:: fun _ ->
        assert_equal s1u2 S1.(union s2 s1) );
      ( "Int Set Test union: union {1, 2, 3} {1, 2, 3}" >:: fun _ ->
        assert_equal s1 S1.(union s1 s1) );
      ( "Int Set Test union: union {1, 2, 3, 12} {1, 2, 3}" >:: fun _ ->
        assert_equal (s1 |> S1.insert 12) S1.(union (s1 |> insert 12) s1) );
    ]

  let test_intersect =
    [
      ( "Int Set Test intersect: intersect {} {}" >:: fun _ ->
        assert_equal S1.empty S1.(intersect empty empty) );
      ( "Int Set Test intersect: intersect {1, 2, 3} {1, 2, 3}" >:: fun _ ->
        assert_equal s1 S1.(intersect s1 s1) );
      ( "Int Set Test intersect: intersect {1, 2, 3} {3}" >:: fun _ ->
        assert_equal s3 S1.(intersect s1 s3) );
      ( "Int Set Test intersect: intersect {1, 2, 3} {1, 3, 4}" >:: fun _ ->
        assert_equal s1n4 S1.(intersect s1 s4) );
      ( "Int Set Test intersect: intersect {1, 2, 3} {4, 5, 6}" >:: fun _ ->
        assert_equal S1.empty S1.(intersect s1 s2) );
    ]

  let test_difference =
    [
      ( "Int Set Test difference: difference {} {}" >:: fun _ ->
        assert_equal S1.empty S1.(difference empty empty) );
      ( "Int Set Test difference: difference {1, 2, 3} {1, 2, 3}" >:: fun _ ->
        assert_equal S1.empty S1.(difference s1 s1) );
      ( "Int Set Test difference: difference {1, 2, 3} {1, 2, 3}" >:: fun _ ->
        assert_equal S1.empty S1.(difference s1 s1) );
      ( "Int Set Test difference: difference {1, 2, 3} {4, 5, 6}" >:: fun _ ->
        assert_equal s1 S1.(difference s1 s2) );
      ( "Int Set Test difference: difference {1, 2, 3} {1, 3, 4}" >:: fun _ ->
        assert_equal s1_4 S1.(difference s1 s4) );
      ( "Int Set Test difference: difference {1, 2, 3} {2}" >:: fun _ ->
        assert_equal s1n4 S1.(difference s1 s1_4) );
    ]

  let tests =
    "test set"
    >::: List.flatten
           [
             test_is_empty;
             test_size;
             test_insert;
             test_member;
             test_fold;
             test_union;
             test_intersect;
             test_difference;
           ]
end

module TestDictionaryRemove (DM : Dictionary.DictionaryMaker) = struct
  let dict1 = [ "{1 : 2}"; "{1 : 2, 3 : 4}"; "{1 : 12}"; "{0 : 4, 1 : 2}" ]

  let test_remove =
    [
      ( "Test remove: 1 from empty" >:: fun _ ->
        assert_equal D1.empty D1.(empty |> remove 1) );
      ( "Test remove: 1 from {1 : 2}" >:: fun _ ->
        assert_equal D1.empty D1.(empty |> insert 1 2 |> remove 1) );
      ( "Test remove: 3 from {1 : 2, 3 : 4}" >:: fun _ ->
        assert_equal (List.nth dict1 0)
          D1.(empty |> insert 1 2 |> insert 3 4 |> remove 3 |> to_string) );
      ( "Test remove: 2 from {1 : 2}" >:: fun _ ->
        assert_equal (List.nth dict1 0)
          D1.(empty |> insert 1 2 |> remove 2 |> to_string) );
    ]

  let tests = "test dict remove" >::: test_remove
end

module TestSetRemove (DM : Dictionary.DictionaryMaker) = struct
  module S1 = DictionarySet.Make (Int) (DM)
  module S2 = DictionarySet.Make (String) (DM)

  let set1 = [ "{1}"; "{1, 2}"; "{1, 2, 5}" ]
  let set2 = [ "{hello}"; "{hello, world}"; "{hello, my, world}" ]

  let test_remove =
    [
      ( "Int Set Test remove: 1 from empty" >:: fun _ ->
        assert_equal S1.empty S1.(empty |> remove 1) );
      ( "Int Set Test remove: 1 from {1}" >:: fun _ ->
        assert_equal S1.empty S1.(empty |> insert 1 |> remove 1) );
      ( "Int Set Test remove: 2 from {1, 2}" >:: fun _ ->
        assert_equal (List.nth set1 0)
          S1.(empty |> insert 1 |> insert 2 |> remove 2 |> to_string) );
      ( "Int Set Test remove: 2 from {1}" >:: fun _ ->
        assert_equal (List.nth set1 0)
          S1.(empty |> insert 1 |> remove 2 |> to_string) );
      ( "Int Set Test remove: 5 from {1, 2, 5}" >:: fun _ ->
        assert_equal (List.nth set1 1)
          S1.(
            empty |> insert 1 |> insert 5 |> insert 2 |> remove 5 |> to_string)
      );
      ( "String Set Test remove: hello from empty" >:: fun _ ->
        assert_equal S2.empty S2.(empty |> remove "hello") );
      ( "String Set Test remove: hello from {hello}" >:: fun _ ->
        assert_equal S2.empty S2.(empty |> insert "hello" |> remove "hello") );
      ( "String Set Test remove: world from {hello, world}" >:: fun _ ->
        assert_equal (List.nth set2 0)
          S2.(
            empty |> insert "hello" |> insert "world" |> remove "world"
            |> to_string) );
      ( "String Set Test remove: world from {hello}" >:: fun _ ->
        assert_equal (List.nth set2 0)
          S2.(empty |> insert "hello" |> remove "world" |> to_string) );
      ( "String Set Test remove: my from {hello, my, world}" >:: fun _ ->
        assert_equal (List.nth set2 1)
          S2.(
            empty |> insert "hello" |> insert "my" |> insert "world"
            |> remove "my" |> to_string) );
    ]

  let tests = "test set remove" >::: test_remove
end

module TestListDictionary = TestDictionary (ListDictionary.Make)
module TestListDicionaryRemove = TestDictionaryRemove (ListDictionary.Make)
module TestDictionarySetRemove = TestSetRemove (ListDictionary.Make)
module TestDictionarySet = TestSet (ListDictionary.Make)
module TestDictionarySet2 = TestSet (TreeDictionary.Make)
module TestTreeDictionary = TestDictionary (TreeDictionary.Make)

let suite =
  "search test suite"
  >::: [
         TestListDictionary.tests;
         TestListDicionaryRemove.tests;
         TestDictionarySet.tests;
         TestDictionarySetRemove.tests;
         TestDictionarySet2.tests;
         TestTreeDictionary.tests;
       ]

let _ = run_test_tt_main suite
