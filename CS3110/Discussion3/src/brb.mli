type t
(** The type of BRB accounts. *)

val make : t
(** An account with a zero balance. *)

val balance : t -> int
(** [balance acct] is the balance of [acct]. *)

val deposit : int -> t -> t
(** [deposit amt acct] is [acct] with [amt] deposited into it. *)

val pay : int -> t -> t
(** [pay amt acct] is [acct] with [amt] payed out from it. *)

val record_in_ledger : int -> t -> t
(** [record_in_ledger amt] records a transaction of [amt] in the account's ledger. *)

exception AuditFailure

val audit : t -> t
(** [audit t] is simply [t] as long as the account passes an internal
    audit. Raises [AuditFailure] if the account fails the audit. *)
