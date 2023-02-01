# CPSC/ECE 3220, Spring 2023
#
# Python program for simple client/server using MPI
#
# The general structure of this program follows Figure 3.11 in
#   the textbook. The details differ because we are using
#   blocking sends and receives to the MPI world communicator
#   in Python rather than reads and writes to individual UNIX
#   pipes in C. We are also adding completion notices and ending
#   the server once all the clients have completed rather than
#   staying in a forever loop.
#
# Six calls to sends and receives have been removed from the
#   code below, and you must add back the appropriate sends and
#   receives with the appropriate arguments at sites marked by:
#
#	# MISSING IPC CALL <with optional comment>
#
#   At each site, a call to an MPI send or receive function is
#   needed with two aruments, the first being the message array
#   object that is being sent or received and the second being
#   a specification of the communicating partner:
#
#	comm.Send( ____, dest=____ )
#
#   or
#
#	comm.Recv( ____, source=____ )
#
#   Note that the server must be able to receive from any client.
#   This is an example of the "select" functionality described in
#   section 3.4.2. The ability for a server to select a message
#   from any client is easy to code with MPI in Python. See
#   https://nyu-cds.github.io/python-mpi/02-messagepassing/ for
#   a tutorial on MPI blocking sends and receives in Python.
#
# Example command line to run this program:
#
#	mpiexec -n 3 python mpi3.py
#
#   (the number of processes given by -n should be 2 or more)
#
# The server process has rank 0. It maintains a sum variable,
#   which it updates based on requests from clients. The server
#   will also receive completion messages from clients and will
#   terminate when all the clients have completed.
#
# The client processes have ranks 1 and above, which are used as
#   the client numbers. A client process sends an update request
#   and then waits on an acknowledgement reply from the server.
#   After a given number of update requests, each client sends a
#   completion message to the server and then waits on an
#   acknowledgement reply from the server.
#
# The update message format from a client to the server is:
#
#	[ <client number> <value> ]
#
#   (where <value> == 0 is used as a sentinel value for completion)
#
# All requests are acknowledged by the server in a reply message.
#   The reply message format from the server is:
#
#	[ 0 1 ]
#
# Note that all messages start with the rank of the process that
#   is sending the message. This message protocol allows the
#   server process to know the identity of the requesting client
#   when a request is selected by the server's call to the MPI
#   receive function. The server can then reply to that client.
#
# numpy is used for more efficient numeric arrays.

import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
num_clients = comm.Get_size() - 1

if num_clients <= 0:

	print( 'command line argument does not allow clients' )
	raise SystemExit


# client code

if rank != 0:

	request = numpy.zeros( 2, dtype='i' )
	reply = numpy.zeros( 2, dtype='i' )

	for i in range( 1, 3 ):

		request[0] = rank
		request[1] = i * rank

		# MISSING IPC CALL  # to server with update request
		comm.Send(request, dest=0)


		# MISSING IPC CALL  # from server for reply
		comm.Recv(reply, source=0)

		print( 'client '+ str(rank) + ' received acknowledgement' )

	request[0] = rank
	request[1] = 0

	# MISSING IPC CALL  # to server with completion notice
	comm.Send(request, request[0])

	# MISSING IPC CALL  # from server for reply
	comm.Recv(reply, rank)

	print( 'client ' + str(rank) + ' done' )


# server code

else:

	print( 'simple server with ' + str(num_clients) + ' clients' )
	sum = 0
	print( 'server starts with a sum value of ' + str(sum) )

	service_request = numpy.zeros( 2, dtype='i' )
	acknowledgement = numpy.zeros( 2, dtype='i' )
	acknowledgement[0] = 0
	acknowledgement[1] = 1

	while num_clients > 0:

		# MISSING IPC CALL  # from any client
		comm.Recv(service_request,source=MPI.ANY_SOURCE)


		if service_request[1] != 0:

			print( 'server received update from client ' + \
			 str(service_request[0]) )
			sum += service_request[1]
			print( 'server added ' + str(service_request[1]) + \
			 ' and sum is now ' + str(sum) )

		else:

			print( 'server receives completion notice ' + \
			 'from client ' + str(service_request[0]) )
			num_clients -= 1

		# MISSING IPC CALL  # reply back to that client
	comm.Send(acknowledgement, dest=1)

	print( 'server done with final sum of ' + str(sum) )
