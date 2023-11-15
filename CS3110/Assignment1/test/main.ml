open OUnit2
open Enigma

(** [index_test name input expected_output] constructs an OUnit test named
    [name] that asserts the quality of [expected_output] with [index input]. *)
let index_test (name : string) (input : char) (expected_output : int) : test =
  name >:: fun _ ->
  (* the [printer] tells OUnit how to convert the output to a string *)
  assert_equal expected_output (index input) ~printer:string_of_int

(* You will find it helpful to write functions like [index_test] for each of the
   other functions you are testing. They will keep your lists of tests below
   very readable, and will also help you to avoid repeating code. You will also
   find it helpful to create [~printer] functions for the data types in use. *)

let map_rl_test (name : string)
(wire_spec : string) (top : char) (input : int) (expected_output : int) : test =
  name >:: fun _ ->
  assert_equal expected_output (map_r_to_l wire_spec top input)
  ~printer:string_of_int

let map_lr_test (name : string)
(wire_spec : string) (top : char) (input : int) (expected_output : int) : test =
  name >:: fun _ ->
  assert_equal expected_output (map_l_to_r wire_spec top input)
  ~printer:string_of_int

let map_refl_test (name : string)
(wire_spec : string) (input : int) (expected_output : int) : test =
  name >:: fun _ ->
  assert_equal expected_output (map_refl wire_spec input)

let map_plug_test (name : string)
(plugs : (char * char) list) (c : char) (expected_output : char) : test = 
  name >:: fun _ ->
  assert_equal expected_output (map_plug plugs c)

let cipher_char_test (name : string)
(conf : config) (c : char) (expected_output : char) : test =
  name >:: fun _ ->
  assert_equal expected_output (cipher_char conf c)

let step_test (name : string) (conf : config) (expected_output : config) =
  name >:: fun _ ->
  assert_equal expected_output (step conf)

let cipher_test (name : string)
(conf : config) (str : string) (expected_output : string) =
  name >:: fun _ ->
  assert_equal expected_output (cipher conf str)
      
 
let index_tests =
  [index_test "index of A is 0" 'A' 0;
  index_test "index of Z is 25" 'Z' 25;
  index_test "index of C is 2" 'C' 2;
  index_test "index of K is 10" 'K' 10;
  index_test "index of S is 18" 'S' 18;
  index_test "index of L is 11" 'L' 11;
  index_test "index of B is 1" 'B' 1;
  index_test "index of Y is 24" 'Y' 24;
  index_test "index of W is 22" 'W' 22]

let rotorI = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
let rotorII = "XJAGZHEIONVTFKDBWMCLRYQUSP"
let rotorIII = "BJMXAYSUVCGFTZQLNRKHPOIWDE"
let rotorIV = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
let rotorV = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
let reflectorB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
let reflectorC = "FVPJIAOYEDRZXWGCTKUQSBNMHL"
let map_rl_tests = 
  [map_rl_test "map_rl of 0 is 0" rotorI 'A' 0 0;
  map_rl_test "map_rl of 0 is 23" rotorII 'A' 0 23;
  map_rl_test "map_rl of 1 is 3" rotorI 'C' 1 3;
  map_rl_test "map_rl of 2 is 9" rotorII 'Z' 2 9;
  map_rl_test "map_rl of 25 is 1" rotorIII 'B' 25 1; 
  map_rl_test "map_rl of 23 is 9" rotorIV 'E' 23 9;
  map_rl_test "map_rl of 20 is 11" rotorIV 'Q' 20 11;
  map_rl_test "map_rl of 25 is 16" rotorV 'Z' 25 16]
let map_lr_tests = 
  [map_lr_test "map_lr of 0 is 0" rotorI 'A' 0 0;
  map_lr_test "map_lr of 23 is 0" rotorII 'A' 23 0;
  map_lr_test "map_lr of 3 is 1" rotorI 'C' 3 1;
  map_lr_test "map_lr of 9 is 2" rotorII 'Z' 9 2;
  map_lr_test "map_lr of 1 is 25" rotorIII 'B' 1 25;
  map_lr_test "map_lr of 9 is 23" rotorIV 'E' 9 23;
  map_lr_test "map_lr of 11 is 20" rotorIV 'Q' 11 20;
  map_lr_test "map_lr of 16 is 25" rotorV 'Z' 16 25]
let map_refl_tests = 
  [map_refl_test "map_ref of 0 is 0" rotorI 0 0;
  map_refl_test "map_ref of 5 is 5" rotorI 5 5;
  map_refl_test "map_ref of 3 is 7" reflectorB 3 7;
  map_refl_test "map_ref of 7 is 3" reflectorB 7 3;
  map_refl_test "map_ref of 5 is 0" reflectorC 5 0;
  map_refl_test "map_ref of 0 is 0" reflectorC 0 5;
  map_refl_test "map_ref of 24 is 7" reflectorC 24 7;
  map_refl_test "map_ref of 7 is 24" reflectorC 7 24]

  let plugI = [('A', 'Z'); ('X', 'Y')]
  let plugII = [('E', 'Z'); ('W', 'I'); ('N', 'S')]
  let plugIII = [('A', 'B'); ('C', 'D'); ('E', 'F'); ('G', 'H')]
let map_plug_tests = 
  [map_plug_test "map_plug of A is Z" [] 'A' 'A';
  map_plug_test "map_plug of A is Z" plugI 'A' 'Z';
  map_plug_test "map_plug of Z is A" plugI 'Z' 'A';
  map_plug_test "map_plug of Y is X" plugI 'D' 'D';
  map_plug_test "map_plug of E is Z" plugII 'E' 'Z';
  map_plug_test "map_plug of Z is E" plugII 'Z' 'E';
  map_plug_test "map_plug of I is W" plugII 'T' 'T';
  map_plug_test "map_plug of D is C" plugIII 'D' 'C';
  map_plug_test "map_plug of C is D" plugIII 'C' 'D']

  let rotorsI = {wiring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; turnover = 'A'}
  let rotorsII = {wiring = "XJAGZHEIONVTFKDBWMCLRYQUSP"; turnover = 'A'}
  let rotorsIII = {wiring = "BJMXAYSUVCGFTZQLNRKHPOIWDE"; turnover = 'A'}

  let o_rotorsI_A = {rotor = rotorsI; top_letter = 'A'}
  let o_rotorsII_A = {rotor = rotorsII; top_letter = 'A'}
  let o_rotorsIII_A = {rotor = rotorsIII; top_letter = 'A'}
  let o_rotorsI_M = {rotor = rotorsI; top_letter = 'M'}
  let o_rotorsII_M = {rotor = rotorsII; top_letter = 'M'}
  let o_rotorsIII_M = {rotor = rotorsIII; top_letter = 'M'}
  
  let configI = {refl = reflectorB;
  plugboard = plugI; rotors = [o_rotorsI_A]}
  let configII = {refl = reflectorB;
  plugboard = plugI; rotors = [o_rotorsI_A; o_rotorsII_A; o_rotorsIII_A]}
  let configIII = {refl = reflectorC;
  plugboard = plugIII; rotors = [o_rotorsI_M; o_rotorsII_M; o_rotorsIII_M]}
  let configIV = {refl = reflectorC;
  plugboard = plugIII; rotors = [o_rotorsIII_M]}
  let configV = {refl = rotorI;
  plugboard = []; rotors = []}

  let cipher_char_tests = 
    [cipher_char_test "cipher A to A" configV 'A' 'A';
    cipher_char_test "cipher A to T" configI 'A' 'T';
    cipher_char_test "cipher Z to X" configI 'Z' 'X';
    cipher_char_test "cipher R to B" configI 'R' 'B';
    cipher_char_test "cipher A to R" configII 'A' 'R';
    cipher_char_test "cipher R to K" configII 'R' 'K';
    cipher_char_test "cipher X to A" configII 'X' 'A';
    cipher_char_test "cipher A to B" configIII 'A' 'B';
    cipher_char_test "cipher Y to X" configIII 'Y' 'X';
    cipher_char_test "cipher E to M" configIII 'E' 'M';
    cipher_char_test "cipher A to C" configIV 'A' 'C';
    cipher_char_test "cipher X to I" configIV 'X' 'I';
    cipher_char_test "cipher M to P" configIV 'M' 'P';]

let step_test2_rotors = [{rotor = rotorsI; top_letter = 'B'}]
let step_test3_rotors = [{rotor = rotorsIII; top_letter = 'N'}]
let step_test4_rotors = [{rotor = rotorsI; top_letter = 'B'};
{rotor = rotorsII; top_letter = 'B'}; {rotor = rotorsIII; top_letter = 'B'}]
let step_test5_rotors = [{rotor = rotorsI; top_letter = 'N'};
{rotor = rotorsII; top_letter = 'N'}; {rotor = rotorsIII; top_letter = 'N'}]

let step_tests =
  [step_test "No Step" configV configV;
  step_test "Step rotorI from A to B" configI
  {refl = reflectorB; plugboard = plugI; rotors = step_test2_rotors};
  step_test "Step rotorI from M to N" configIV
  {refl = reflectorC; plugboard = plugII; rotors = step_test3_rotors};
  step_test "Step rotorI, II, III from A to B" configII
  {refl = reflectorB; plugboard = plugI; rotors = step_test4_rotors};
  step_test "Step rotorI, II, III from M to N" configIII
  {refl = reflectorC; plugboard = plugII; rotors = step_test5_rotors};]

let wwii_rotor =
[{rotor={wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ";turnover='A'};top_letter='A'};
{rotor={wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE";turnover='A'};top_letter='A'};
{rotor={wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ";turnover='A'};top_letter='A'}]
let wwii_enigma = {refl = reflectorB; plugboard = []; rotors = wwii_rotor}
let cipher_tests =
  [cipher_test "cipher HELLO to ILBDA" wwii_enigma "HELLO" "ILBDA";
  cipher_test "cipher WORLD to KIXDI" wwii_enigma "WORLD" "KIXDI";
  cipher_test "cipher blank" wwii_enigma "" "";
  cipher_test "cipher RICHIE to VOEKDN" wwii_enigma "RICHIE" "VOEKDN";
  cipher_test "cipher OCAML to " wwii_enigma "OCAML" "TRZOU"]

let tests =
  "test suite for A1"
  >::: List.flatten
         [
           index_tests;
           map_rl_tests;
           map_lr_tests;
           map_refl_tests;
           map_plug_tests;
           cipher_char_tests;
           step_tests;
           cipher_tests;
         ]

let _ = run_test_tt_main tests
