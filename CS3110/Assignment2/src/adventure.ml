(* Note: You may introduce new code anywhere in this file. *)
open Yojson.Basic.Util

exception UnknownRoom of string
exception UnknownExit of string

type exit = {
  name : string;
  room_id : string;
}

type room = {
  id : string;
  description : string;
  exits : exit list;
}

type t = {
  rooms : room list;
  start_room : string;
}

(* Helper functions defined below: *)
(* ######################################################### *)
let exit_of_json j =
  {
    name = j |> member "name" |> to_string;
    room_id = j |> member "room id" |> to_string;
  }

let room_of_json j =
  {
    id = j |> member "id" |> to_string;
    description = j |> member "description" |> to_string;
    exits = j |> member "exits" |> to_list |> List.map exit_of_json;
  }

let rec get_room_ids (lst : room list) =
  match lst with
  | [] -> []
  | h :: t -> h.id :: get_room_ids t

let compare_struct x y = if x = y then 0 else 1

let get_room_by_id (rooms : room list) (id : string) =
  let lst = List.filter (fun room -> room.id = id) rooms in
  match lst with
  | [] -> raise (UnknownRoom (id ^ " is not an existing room"))
  | h :: _ -> h

let get_exit_by_name (name : string) (exits : exit list) =
  let ex = List.filter (fun exit -> exit.name = name) exits in
  match ex with
  | [] -> raise (UnknownExit (name ^ " is not an existing exit"))
  | h :: _ -> h

let rec get_reachable_rooms (exits : exit list) =
  match exits with
  | [] -> []
  | h :: t -> h.room_id :: get_reachable_rooms t
(* ######################################################### *)
(* End of defined helper functions *)

let from_json json =
  {
    rooms = json |> member "rooms" |> to_list |> List.map room_of_json;
    start_room = json |> member "start room" |> to_string;
  }

let start_room adv =
  match adv with
  | { rooms; start_room } -> start_room

let room_ids adv =
  match adv with
  | { rooms; start_room } -> List.sort_uniq compare_struct (get_room_ids rooms)

let description adv room = (get_room_by_id adv.rooms room).description

let exits adv room =
  (get_room_by_id adv.rooms room).exits
  |> List.map (fun exit -> exit.name)
  |> List.sort_uniq compare_struct

let next_room adv room ex =
  ((get_room_by_id adv.rooms room).exits |> get_exit_by_name ex).room_id

let next_rooms adv room =
  (get_room_by_id adv.rooms room).exits |> get_reachable_rooms
  |> List.sort_uniq compare_struct
