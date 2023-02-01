Problem Statement

You are to implement a simple client/server program using the Python programming language and MPI blocking sends and receives. Skeleton code is provided in mpics.py Download mpics.py. You will run your program using the mpiexec library and the Python interpreter installed on one of the joey servers for the School of Computing (e.g., joey1, joey2, ...).

 

Discussion

The server is very simple and merely maintains a sum variable that is updated by client requests. Please read and follow all the comments within the skeleton program, and please read https://nyu-cds.github.io/python-mpi/02-messagepassing/ Links to an external site.to see how a server can receive a request from any client in a pool of clients. The comments and web page will guide you to the solution, which is merely to add six calls to MPI send and receive with the appropriate parameters. You do not need to add extra Python statements beyond those, so you don't need prior experience in programming in Python.

Please turn in a completed source file, named "mpics.py", using handin.cs.clemson.edu Links to an external site.. Do not submit a compressed source file, and do not submit any other source files. Your code must run on the School of Computing servers (e.g., the joeys) to be graded.

 

Pedagogical Rationale

This assignment illustrates that individual processes are separate protection domains, that they do not share variables, and that you must take explicit actions to communicate between different processes. See the Python program mpi1.py Download mpi1.pyfor an example of different copies of the variable x in different processes created from a single Python source program (similar to question 9 at the end of Chapter 3), and see the Python program mpi2.py Download mpi2.pyfor an example of a simple MPI send and receive.

This assignment illustrates the client/server design pattern and the execution-time message select functionality that a server must have to receive messages from a pool of client processes.
 

Guidelines

The code should be written totally by yourself.

You may discuss the project requirements and the concepts with me, the TA, or with anyone in the class.

However, you should not send code to anyone or receive code from anyone, whether by email, printed listings, photos, visual display on a computer/laptop/cell-phone/etc. screen, or any other method of communication.

Do not post the assignment, or a request for help, or your code on any web sites.

The key idea is that you shouldn't short-circuit the learning process for others once you know the answer. (And you shouldn't burden anyone else with inappropriate requests for code or "answers" and thus short-circuit your own learning process.)

 

Example Expected Output

For the command line "mpiexec -n 3 python mpics.py", on one run you might see:

simple server with 2 clients
server starts with a sum value of 0
server received update from client 2
server added 2 and sum is now 2
server received update from client 1
server added 1 and sum is now 3
client 2 received acknowledgement
server received update from client 2
client 1 received acknowledgement
server added 4 and sum is now 7
client 2 received acknowledgement
server received update from client 1
server added 2 and sum is now 9
client 1 received acknowledgement
server receives completion notice from client 2
client 2 done
server receives completion notice from client 1
client 1 done
server done with final sum of 9

The sequencing of the output statements will depend on the scheduling of process execution. At the end or near the end of the output you will see a statement of the form "server done with final sum of __". When your code is working correctly, look for these final values based on the -n command line parameter: