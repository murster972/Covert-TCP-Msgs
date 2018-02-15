See defcon25 talk on covert TCP communication - https://www.youtube.com/watch?v=IIrzbzzNFjw

:TODO: CURRENTLY ONLY WORKS WITH ASCII MSGS,
       allow binary files to be sent

Sending and recieve covert TCP msgs with methods discussed in defcon25 talk linked
above.

METHODS
1. Use IP identification field
2. Use inital TCP SYN no.
3. Use intial TCP SYN no. and set IP SRC as recv IP and dest IP as random
   server, server will send response to recv and msg will be in
   ACK no.

 :PROBLEM NOTE: if sending ascii msgs const cannot exceed 127 (2**7), as
                ascii uses 7 bits to represent char.

:TODO: Indicate different msg types - init, ascii, binary - with different flag combinations,

-------BASIC IDEA-------
SENDER: user inputs msg, method and options (private key, dest ip, src ip, src port, dest port, etc.)

        program splits msg into segement, then encodes/encrypts
        OR
        encodes/encrypts then segments msg, would be more secure but
        would leave entire msg unreadable should any segements be lost

        ENCODING/SEGMENTS:
            msg will be split converted to bits
            segemented into blocks of bit length L
            multiplied by a constant

            :NOTE: It's essentially a Polyalphabetic cipher
                   it is not intended to be stong scheme, but
                   instead hide the contents. The point becomes
                   moot if the person breaks the cipher as the whole
                   point is for it to be covert, and finding the cipher
                   would break that constraint

            :NOTE: the constant will come from a list of constants,
                   the same for both sender and reciever.

                   The list of constants will be continually cycled
                   through when encoding segments.

        reciever couldnt read any of msg if any segements lost

        sends indication msg to reciever to show about to send segements

        :NOTE: Possibly use TCP Flags to indicate msg start and end
               e.g. intial packet can have all tcp flags Set
                    and have the no of segments being sent as
                    the inital msg(id, seq no. etc.)

        using their choosen method sends each segement to reciever
        listens to reply from reciever, either to request lost segs or to finish

RECEIVER: selects the method to recieve msg from sender
          inputs options - port, private key, etc.

          binds socket to port(dest or src based depends on method) to ensure
          no other program uses it to send or recieve traffic.

          listens for segements from user using choosen method/options

          :NOTE: Find way to diff between msgs sent by sender and normal traffic.
                 maybe the source port?

          sends msg to sender either stating they recieved all or requesting any
          lost segments

          decodes/decrypts each segement and ressabembles
          OR
          reassemble then decode/decrypts the reassembled msg
