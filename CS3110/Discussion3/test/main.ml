open Brb 
open OUnit2
let tests = "brb test suite" >::: [("zero balance" >:: fun _ -> assert_equal 0 (make |> balance));
("deposit 100c" >:: fun _ -> assert_equal 100 (make |> deposit 100 |> balance));
("deposit 12500c" >:: fun _ -> assert_equal 12500 (make |> deposit 12500 |> balance));
("deposit 1000c pay 100c" >:: fun _ -> assert_equal 900 (make |> deposit 1000 |> pay 100 |> balance));
("audit fails" >:: fun _ ->
  assert_raises AuditFailure (fun () ->
    make |> record_in_ledger 10 |> audit));]
let _ = run_test_tt_main tests