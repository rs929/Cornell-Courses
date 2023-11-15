.PHONY: test

build:
	dune build

code:
	-dune build
	code .
	! dune build --watch	

test:
	OCAMLRUNPARAM=b dune exec test/main.exe

bisect:
	rm -f *.coverage
	-dune exec --instrument-with bisect_ppx test/main.exe
	bisect-ppx-report html

clean:
	rm -rf *.coverage _coverage
	dune clean