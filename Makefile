all: marker/ansilib

marker/ansilib: submodules/ansi/ansi/
	mkdir -p $@
	cp -vr $</* $@
