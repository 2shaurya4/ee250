# Lab 2

## Team Members
 - Shaurya Goel (Github handle: @2shaurya4)

## Lab Question Answers
Answer for Question 1A:
Q1A: UDP lost multiple packets, some to the point where the numbers wouldn't even appear on the screen. This happened because UDP doesn't gurantee reliabiity. It has no acknowledgement mechanisms to make sure that packets get to the other side. 

Answer for Question 2A:
Q2A: Under a simulated 50% packet loss, TCP was just as reliable with packet loss as it was without packet loss. This occoured because TCP is acknowledgement mechanisms that recognize when a packet doesn't make it through intact and resends it. 

Answer for Question 3A:
Q3A: Under a simulated 50% packet loss, TCP's speed drop massively. This happened because in an attempt to get the packet from one place to another intact, it would try to resend it again and again. In some unlucky cases, TCP would need to send the packets multiple times which caused the drop in speed. 

Answer for Question 4A:
Q4A: An LLM (ChatGPT) was used to assist me with this lab. The only work done by ChatGPT was to troubleshoot my UDP transmission problems. My client was sending packets to IPv6, whereas my server was listening to IPv4. Given that I've had no prior experince in networking and that this lab was complpeted by me on a weekend (I couldn't recieve help from any of the TAs over the weekend), my hand was forced to use AI. All code submitted by me for this lab was written by me.

Answer for Question 1C: 
Q1C: argc is the number of command‑line arguments passed to the program (including the program name as argv[0]). argv: is the array of pointers to null‑terminated C strings holding each argument, where argv[0] = program name, argv[1]..argv[argc-1] = user arguments, argv[argc] = NULL (by convention)

Answer for Question 2C: 
Q2C: A UNIX is a non negative integer that identifies a I/O resource in a process. A file descriptor table is an array indexable by file descriptors containting etnries pointing to kernel open file descriptions

Answer for Question 3C:
Q3C: A struct is a definable variable type in C that groups together related variables under one name. sockaddr_in models an IPv4 endpoint. Typical defintion consists of:
struct sockaddr_in {
    sa_family_t    sin_family; // Address family (AF_INET)
    in_port_t      sin_port;   // Port number (network byte order via htons)
    struct in_addr sin_addr;   // IPv4 address (e.g. INADDR_ANY)
    unsigned char  sin_zero[8];// Padding (unused, set to 0)
};

Answer for Question 4C:
Q4C: Inputs: Domain (AF_INET), Type (Socket Type), Protocol (0 for default)

     Return value: non-negative file descriptor for the socket on success, -1 and error on error

Answer for Question 5C:
Q5C: Bind input paramters: sockfd(socket file descriptor (that's what socket() returns)), addr(pointer to the address str), addrlen(size in bytes of the structure addr points to)

     Listen parameters: sockfd(socket file descriptor (that's what socket() returns)), backlog(length of the pending connection queue)

Answer for Question 6C:
Q6C: while(1) is used to loop forever so the server keeps listening to the client after the first message is sent. This, however, prohibits the server and allows it to only handle one client when it could possible handle multiple. 

Answer for Question 7C:
Q7C: Fork() is usued to create a new child process by duplicating and calling the parent process. After accept, fork can be used so each connection is handeled in its own child process and the parent can go back to accepting more clients. 

Answer for Question 8C:
Q8C: A system call is a call used by a program as an entry point into the kernel from a user space to ask for a service. 
