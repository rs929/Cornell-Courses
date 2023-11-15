open OUnit2
open Interval

(** [string_of_float_pair] converts a pair of floats to a string representation.
    Example: [string_of_float_pair (1., 1.)] is ["(1., 1.)"]. *)
let string_of_float_pair (f1, f2) =
  "(" ^ string_of_float f1 ^ ", " ^ string_of_float f2 ^ ")"

(** [assert_pair_equal] is a helper function for constructing tests on
    intervals. The [expected] argument is a pair of floats representing the
    expected lower and upper bounds of an interval. The function asserts that
    [Interval.lo] and [Interval.hi], when applied to the [intv] argument,
    produce the expected bounds. *)
let assert_pair_equal expected intv =
  assert_equal expected (lo intv, hi intv) ~printer:string_of_float_pair

let tests =
  [
    ("contains" >:: fun _ -> assert_equal true (make 0. 1. |> contains 0.));
    ("make" >:: fun _ -> assert_pair_equal (0., 1.) (make 0. 1.));
    ( "addition" >:: fun _ ->
      assert_pair_equal (4., 8.) (make 2. 6. + make 2. 2.) );
    ( "subtract" >:: fun _ ->
      assert_pair_equal (~-.4.0, 7.0) (make 4.0 9.0 - make 2.0 8.0) );
    ( "subtract" >:: fun _ ->
      assert_pair_equal (~-.3., 3.0) (make 5.0 9.0 - make 6.0 8.0) );
    ( "multiply" >:: fun _ ->
      assert_pair_equal (8.0, 15.0) (make 2.0 3.0 * make 4.0 5.0) );
  ]

let test_suite = "interval test suite" >::: tests
let _ = run_test_tt_main test_suite
