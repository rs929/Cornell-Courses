open Game.Adventure
open Game.Command
open Game.State
open Printf

(** [play_game f] starts the adventure in file [f]. *)

(* Helper functions defined below: *)
(* ######################################################### *)
let print_message str = ANSITerminal.print_string [ ANSITerminal.green ] str
let print_exits str = ANSITerminal.print_string [ ANSITerminal.cyan ] str

let print_error str =
  ANSITerminal.print_string [ ANSITerminal.red ] str;
  print_endline "\n--------------------------------------------------------"

let print_warning str =
  ANSITerminal.print_string [ ANSITerminal.yellow ] str;
  print_endline "\n--------------------------------------------------------"

let print_output adv state =
  ANSITerminal.print_string [ ANSITerminal.green ]
    ("Room: " ^ current_room_id state ^ "\n");
  print_endline (description adv (current_room_id state));
  print_exits "Exits: \n";
  List.iter print_exits
    (List.map (fun s -> s ^ " | ") (exits adv (current_room_id state)));
  print_endline "\n--------------------------------------------------------"

let process_input command adv state =
  match command with
  | exception Empty ->
      print_endline "Invalid Input; Please Try again\n";
      state
  | Quit -> state
  | Go g -> (
      try
        match go (List.nth g 0) adv state with
        | Legal l ->
            print_output adv l;
            l
        | Illegal ->
            print_warning "Not a valid exit; Please Try again\n";
            state
      with _ ->
        print_warning "Invalid Input; Please Try again\n";
        state)

let rec make_choices adv state =
  match read_line () with
  | exception End_of_file -> ()
  | com -> (
      try
        match parse com with
        | command ->
            if command = Quit then print_endline "Quitting Game..."
            else make_choices adv (process_input command adv state)
      with
      | Empty ->
          print_error "No Input received; Please Try again\n";
          make_choices adv state
      | Malformed ->
          print_error
            "Not a Valid Command; Please try either\n\
             1. go <exit name>\n\
             2. quit \n";
          make_choices adv state)
(* ######################################################### *)
(* End of defined helper functions *)

let play_game f =
  let adv = f |> Yojson.Basic.from_file |> from_json
  and state = f |> Yojson.Basic.from_file |> from_json |> init_state in
  print_output adv state;
  make_choices adv state

let data_dir_prefix = "data" ^ Filename.dir_sep

(** [main ()] prompts for the game to play, then starts it. *)
let main () =
  ANSITerminal.print_string [ ANSITerminal.red ]
    "\n\nWelcome to the 3110 Text Adventure Game engine.\n";
  print_endline "Please enter the name of the game file you want to load.\n";
  print_string "> ";
  match read_line () with
  | exception End_of_file -> ()
  | file_name -> play_game (data_dir_prefix ^ file_name ^ ".json")

(* Execute the game engine. *)
let () = main ()
