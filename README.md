server.py has function waitformsg()
waitformsg just opens a socket at the local address at socket 7539 and waits for a connection
when it receives a connection, it opens a stream and sends any data it receives until the connection is closed or it receives data of NULL value

client.py has funciton sendmsg(mess)
sendmsg sends a string (mess) to local address, socket 7539
it prints any data it gets back from the connection

the lettuce test assumes the server connection is up and running.