(** The abstract syntax tree type. *)

(******************************************************************************
   These types (id, handle, uop, bop) are used by the parser and type-checker.
   You do not want to change them.
 ******************************************************************************)

type id = string
type handle = int

type bop =
  | Add
  | Sub
  | Mul
  | Div
  | Mod
  | And
  | Or
  | Lt
  | Le
  | Gt
  | Ge
  | Eq
  | Ne
  | Cat
  | Pipe
  | Cons
  | Assign
  | Bind

and uop =
  | Neg
  | Not
  | Ref
  | Deref

(******************************************************************************
   [pat] is the type of the AST for patterns. You may implement
   this type however you wish. Look at the formal semantics and think about other
   AST types we have worked with for inspiration.
 ******************************************************************************)

type pat =
  | PVar of string
  | Empty
  | PBool of bool
  | PInt of int
  | PString of string
  | PPair of pat * pat
  | PUnit of unit
  | PCons of pat * pat
  | WildCard

(******************************************************************************
   [expr] is the type of the AST for expressions. You may implement
   this type however you wish.  Use the example interpreters seen in
   the textbook as inspiration.
 ******************************************************************************)

type expr =
  | Unit of unit
  | Int of int
  | Bool of bool
  | String of string
  | Binop of bop * expr * expr
  | Unop of uop * expr
  | Let of pat * expr * expr
  | Var of string
  | If of expr * expr * expr
  | Fun of pat * expr
  | App of expr * expr
  | Pair of expr * expr
  | List of expr * expr
  | EList of pat
  | Seq of expr * expr
  | Match of expr * (pat * expr) list

(******************************************************************************
   [defn] is the type of the AST for definitions. You may implement this type
   however you wish.  There are only two kinds of definition---the let
   definition and the let [rec] definition---so this type can be quite simple.
 ******************************************************************************)
and defn = Def of pat * expr

(******************************************************************************
   [prog] is the type of the AST for an RML program. You should 
   not need to change it.
 ******************************************************************************)

type prog = defn list
