(* Note: You may introduce new code anywhere in this file. *)

type t = {
  current_room : string;
  visited_rooms : string list;
}

let compare_struct x y = if x = y then 0 else 1

let init_state adv =
  {
    current_room = Adventure.start_room adv;
    visited_rooms = [ Adventure.start_room adv ];
  }

let current_room_id st = st.current_room
let visited st = st.visited_rooms

type result =
  | Legal of t
  | Illegal

let go ex adv st =
  let room = st |> current_room_id in
  try
    match Adventure.next_room adv room ex with
    | (room : string) ->
        Legal
          {
            current_room = room;
            visited_rooms =
              List.sort_uniq compare_struct (room :: st.visited_rooms);
          }
  with _ -> Illegal
