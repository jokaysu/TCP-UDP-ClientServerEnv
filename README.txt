*********************************************************************

TCP and UDP socket programming in a client-server environment

Negotiation using TCP sockets & Transaction using UDP sockets

*********************************************************************

Instruction for running the program

1.	Run the server program on the server machine with <req_code>
	
		$./server.sh <req_code>

2. 	Run the client program on teh client machine with 
	<server_address>, <n_port>, which is given by the server program,
	<req_code>, must be the same as the one given to server program,
	or the program would exit, and <msg> you wanna be reversed.

		$./client.sh <server_address> <n_port> <req_code> <msg>

3.	After you client program returns and print the reversed message,
	you can repeat step 2 as many times as you want.

*********************************************************************

Testing Information

1. 	I ran the server program on @ubuntu1604-006 and the client
	program and ran the client program on @ubuntu1604-002.
	It works perfectly.

2.	I ran both the server and the client on @ubuntu1604-002.
	It works fine.

3.	The compiler that I am using is Python 2.7.12
	