type t = {
  balance : int; (* In cents. Invariant: = sum of ledger. *)
  ledger : int list (* Reverse chronological. *)
}

let make = {balance = 0; ledger = []}

let balance (acc : t) = acc.balance
let deposit amt acc = {balance = acc.balance + amt; ledger = amt :: acc.ledger}
let pay amt acc = {balance = acc.balance - amt; ledger = -(amt) :: acc.ledger}

let record_in_ledger amt acct = { acct with ledger = amt :: acct.ledger }

exception AuditFailure

let audit acct =
  let balance_check = List.fold_left ( + ) 0 acct.ledger in
  if acct.balance <> balance_check then raise AuditFailure else acct



