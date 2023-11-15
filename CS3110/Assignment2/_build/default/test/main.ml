open OUnit2
open Game
open Adventure
open Command
open State

(********************************************************************
   Here are some helper functions for your testing of set-like lists.
 ********************************************************************)

(** [cmp_set_like_lists lst1 lst2] compares two lists to see whether they are
    equivalent set-like lists. That means checking two things. First, they must
    both be "set-like", meaning that they do not contain any duplicates. Second,
    they must contain the same elements, though not necessarily in the same
    order. *)
let cmp_set_like_lists lst1 lst2 =
  let uniq1 = List.sort_uniq compare lst1 in
  let uniq2 = List.sort_uniq compare lst2 in
  List.length lst1 = List.length uniq1
  && List.length lst2 = List.length uniq2
  && uniq1 = uniq2

(** [pp_string s] pretty-prints string [s]. *)
let pp_string s = "\"" ^ s ^ "\""

(** [pp_list pp_elt lst] pretty-prints list [lst], using [pp_elt] to
    pretty-print each element of [lst]. *)
let pp_list pp_elt lst =
  let pp_elts lst =
    let rec loop n acc = function
      | [] -> acc
      | [ h ] -> acc ^ pp_elt h
      | h1 :: (h2 :: t as t') ->
          if n = 100 then acc ^ "..." (* stop printing long list *)
          else loop (n + 1) (acc ^ pp_elt h1 ^ "; ") t'
    in
    loop 0 "" lst
  in
  "[" ^ pp_elts lst ^ "]"

(* These tests demonstrate how to use [cmp_set_like_lists] and [pp_list] to get
   helpful output from OUnit. *)
let cmp_demo =
  [
    ( "order is irrelevant" >:: fun _ ->
      assert_equal ~cmp:cmp_set_like_lists ~printer:(pp_list pp_string)
        [ "foo"; "bar" ] [ "bar"; "foo" ] )
    (* Uncomment this test to see what happens when a test case fails.
       "duplicates not allowed" >:: (fun _ -> assert_equal
       ~cmp:cmp_set_like_lists ~printer:(pp_list pp_string) ["foo"; "foo"]
       ["foo"]); *);
  ]

(********************************************************************
   End helper functions.
 ********************************************************************)

(* You are welcome to add strings containing JSON here, and use them as the
   basis for unit tests. You can also use the JSON files in the data directory
   as tests. And you can add JSON files in this directory and use them, too. *)

(* Here is an example of how to load files from the data directory: *)
let data_dir_prefix = "data" ^ Filename.dir_sep
let lonely = Yojson.Basic.from_file (data_dir_prefix ^ "lonely_room.json")
let ho = Yojson.Basic.from_file (data_dir_prefix ^ "ho_plaza.json")
let house = Yojson.Basic.from_file (data_dir_prefix ^ "my_house.json")
let repeat_rooms = Yojson.Basic.from_file (data_dir_prefix ^ "repeat_rooms.json")
let repeat_exits = Yojson.Basic.from_file (data_dir_prefix ^ "repeat_exits.json")

(* You should not be testing any helper functions here. Test only the functions
   exposed in the [.mli] files. Do not expose your helper functions. See the
   handout for an explanation. *)

let test_start_room (name : string) (adv : Adventure.t)
    (expected_output : string) : test =
  name >:: fun _ ->
  assert_equal expected_output (start_room adv) ~printer:pp_string

let test_room_ids (name : string) (adv : Adventure.t)
    (expected_output : string list) : test =
  name >:: fun _ ->
  assert_equal ~cmp:cmp_set_like_lists ~printer:(pp_list pp_string)
    expected_output (room_ids adv)

let test_description (name : string) (adv : Adventure.t) (room : string)
    (expected_output : string) : test =
  name >:: fun _ ->
  assert_equal expected_output (description adv room) ~printer:pp_string

let test_description_exn (name : string) (adv : Adventure.t) (room : string) :
    test =
  name >:: fun _ ->
  assert_raises
    (UnknownRoom (room ^ " is not an existing room"))
    (fun () -> description adv room)

let test_exits (name : string) (adv : Adventure.t) (room : string)
    (expected_output : string list) : test =
  name >:: fun _ ->
  assert_equal ~cmp:cmp_set_like_lists ~printer:(pp_list pp_string)
    expected_output (exits adv room)

let test_exits_exn (name : string) (adv : Adventure.t) (room : string) : test =
  name >:: fun _ ->
  assert_raises
    (UnknownRoom (room ^ " is not an existing room"))
    (fun () -> exits adv room)

let test_next_room (name : string) (adv : Adventure.t) (room : string)
    (ex : string) (expected_output : string) : test =
  name >:: fun _ ->
  assert_equal expected_output (next_room adv room ex) ~printer:pp_string

let test_next_room_exn (name : string) (adv : Adventure.t) (room : string)
    (ex : string) : test =
  name >:: fun _ ->
  assert_raises
    (if name = "roomError" then UnknownRoom (room ^ " is not an existing room")
    else UnknownExit (ex ^ " is not an existing exit"))
    (fun () -> next_room adv room ex)

let test_next_rooms (name : string) (adv : Adventure.t) (room : string)
    (expected_output : string list) : test =
  name >:: fun _ ->
  assert_equal ~cmp:cmp_set_like_lists ~printer:(pp_list pp_string)
    expected_output (next_rooms adv room)

let test_next_rooms_exn (name : string) (adv : Adventure.t) (room : string) :
    test =
  name >:: fun _ ->
  assert_raises
    (UnknownRoom (room ^ " is not an existing room"))
    (fun () -> next_rooms adv room)

let adventure_tests =
  [
    test_start_room "Lonely" (from_json lonely) "the room";
    test_start_room "Ho Plaza" (from_json ho) "ho plaza";
    test_start_room "My House" (from_json house) "my room";
    test_room_ids "Lonely rooms" (from_json lonely) [ "the room" ];
    test_room_ids "Ho Plaza rooms" (from_json ho)
      [ "ho plaza"; "health"; "tower"; "nirvana" ];
    test_room_ids "Repeated Rooms" (from_json repeat_rooms)
      [ "the cool room"; "the room"; "the room2" ];
    test_description "Lonely room description" (from_json lonely) "the room"
      "A very lonely room.";
    test_description "Repeated Rooms description" (from_json repeat_rooms)
      "the room" "A very lonely room.";
    test_description "Nirvana room description" (from_json ho) "nirvana"
      "You have reached a higher level of existence.  There are no more words.";
    test_description "The bathroom room description" (from_json house)
      "the bathroom" "A very clean bathroom.";
    test_description_exn "Invalid Lonely room description" (from_json lonely)
      "the cool room";
    test_description_exn "Invalid House room description" (from_json house)
      "the dirty bathroom";
    test_exits "Lonely room empty exits" (from_json lonely) "the room" [];
    test_exits "Ho Plaza room exits" (from_json ho) "ho plaza"
      [
        "southwest";
        "south west";
        "Cornell Health";
        "Gannett";
        "chimes";
        "concert";
        "clock tower";
      ];
    test_exits "Repeated Exits room" (from_json repeat_exits) "the cool room"
      [ "exit1"; "exit2" ];
    test_description_exn "Invalid Lonely room exit" (from_json lonely)
      "the cool room";
    test_description_exn "Invalid House room exit" (from_json house)
      "the dirty bathroom";
    test_next_room "House Kitchen south" (from_json house) "the kitchen" "north"
      "the living room";
    test_next_room "Ho Plaza southwest" (from_json ho) "ho plaza" "southwest"
      "health";
    test_next_room "Repeat exits the cool room" (from_json repeat_exits)
      "the cool room" "exit1" "tower";
    test_next_room_exn "roomError" (from_json lonely) "the cool room" "exit";
    test_next_room_exn "exitError" (from_json ho) "ho plaza" "exit";
    test_next_rooms "Ho plaza next rooms" (from_json ho) "ho plaza"
      [ "health"; "tower" ];
    test_next_rooms "Lonely empty next rooms" (from_json lonely) "the room" [];
    test_next_rooms "Repeated Exits next rooms" (from_json repeat_exits)
      "the cool room" [ "tower"; "tower2" ];
    test_next_rooms_exn "Invalid Lonely next rooms" (from_json lonely)
      "the coolest room";
    test_next_rooms_exn "Invalid House next rooms" (from_json house)
      "the pool room";
  ]

let valid_strings =
  [
    "go clock tower";
    "    go     clock    tower";
    "   go   please   go   home";
    "quit";
    "    quit   ";
    "  go   go go PowerRangers";
  ]

let invalid_strings =
  [
    "";
    "     ";
    "   go  ";
    "GO clock tower";
    "QuIt";
    "quit please";
    "AHHHHHHHH";
    "I like camels";
  ]

let test_parse (name : string) (str : string) (expected_output : command) : test
    =
  name >:: fun _ -> assert_equal expected_output (parse str)

let test_parse_exn (name : string) (is_empty : bool) (str : string) : test =
  name >:: fun _ ->
  assert_raises (if is_empty then Empty else Malformed) (fun () -> parse str)

let command_tests =
  [
    test_parse "Single Space Between" (List.nth valid_strings 0)
      (Go [ "clock"; "tower" ]);
    test_parse "Multi Space Between" (List.nth valid_strings 1)
      (Go [ "clock"; "tower" ]);
    test_parse "Mulit Space Multi Object" (List.nth valid_strings 2)
      (Go [ "please"; "go"; "home" ]);
    test_parse "Valid quit no space" (List.nth valid_strings 3) Quit;
    test_parse "Valid quit with space" (List.nth valid_strings 4) Quit;
    test_parse "GO GO POWERRANGERS" (List.nth valid_strings 5)
      (Go [ "go"; "go"; "PowerRangers" ]);
    test_parse_exn "Empty String" true (List.nth invalid_strings 0);
    test_parse_exn "Only Spaces" true (List.nth invalid_strings 1);
    test_parse_exn "Only go" false (List.nth invalid_strings 2);
    test_parse_exn "GO capitalized" false (List.nth invalid_strings 3);
    test_parse_exn "QuIt Wrong Caps" false (List.nth invalid_strings 4);
    test_parse_exn "quit with object" false (List.nth invalid_strings 5);
    test_parse_exn "Test AHHHHHHHH" false (List.nth invalid_strings 6);
    test_parse_exn "Test I like camels" false (List.nth invalid_strings 7);
  ]

let lonely_init = init_state (from_json lonely)
let house_init = init_state (from_json house)
let ho_init = init_state (from_json ho)

let process_result adv res =
  match res with
  | Illegal -> init_state adv
  | Legal s -> s

let house_living =
  init_state (from_json house)
  |> go "south" (from_json house)
  |> process_result (from_json house)

let house_kitchen =
  house_living
  |> go "south" (from_json house)
  |> process_result (from_json house)

let test_go_curr (name : string) (ex : string) (adv : Adventure.t)
    (state : State.t) (expected_curr : string) : test =
  name >:: fun _ ->
  assert_equal expected_curr
    (current_room_id (process_result adv (go ex adv state)))
    ~printer:pp_string

let test_go_visited (name : string) (ex : string) (adv : Adventure.t)
    (state : State.t) (expected_visited : string list) : test =
  name >:: fun _ ->
  assert_equal ~cmp:cmp_set_like_lists ~printer:(pp_list pp_string)
    expected_visited
    (visited (process_result adv (go ex adv state)))

let state_tests =
  [
    test_go_curr "Ho Plaza init to health" "south west" (from_json ho) ho_init
      "health";
    test_go_visited "Ho Plaza init to health" "south west" (from_json ho)
      ho_init [ "ho plaza"; "health" ];
    test_go_curr "Ho Plaza init to tower" "chimes" (from_json ho) ho_init
      "tower";
    test_go_visited "Ho Plaza init to tower" "chimes" (from_json ho) ho_init
      [ "ho plaza"; "tower" ];
    test_go_curr "House init to the living room" "south" (from_json house)
      house_init "the living room";
    test_go_visited "House init to the living room" "south" (from_json house)
      house_init
      [ "my room"; "the living room" ];
    test_go_curr "Lonely init to Illegal" "exit" (from_json lonely) lonely_init
      "the room";
    test_go_visited "Lonely init to Illegal" "exit" (from_json lonely)
      lonely_init [ "the room" ];
    test_go_curr "House init to Illegal" "Narnia" (from_json house) house_init
      "my room";
    test_go_visited "House init to Illegal" "Narnia" (from_json house)
      house_init [ "my room" ];
    test_go_curr "House living to garage" "east" (from_json house) house_living
      "the garage";
    test_go_visited "House living to garage" "east" (from_json house)
      house_living
      [ "my room"; "the living room"; "the garage" ];
    test_go_curr "House living to kitchen" "south" (from_json house)
      house_living "the kitchen";
    test_go_visited "House living to kitchen" "south" (from_json house)
      house_living
      [ "my room"; "the living room"; "the kitchen" ];
    test_go_curr "House kitchen back to the living room" "north"
      (from_json house) house_kitchen "the living room";
    test_go_visited "House kitchen back to the living room" "north"
      (from_json house) house_kitchen
      [ "my room"; "the living room"; "the kitchen" ];
  ]

let suite =
  "test suite for A2"
  >::: List.flatten [ cmp_demo; adventure_tests; command_tests; state_tests ]

let _ = run_test_tt_main suite
