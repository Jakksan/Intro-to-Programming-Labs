# This program prints a table of all the ASCII characters.
# The extended set may be slightly different on different laptops.


print( "\nASCII characters\n" )

for number in range( 0, 256, 8 ):
    print( format( number,   "3d"), chr(number  ), " ", end="" )
    print( format( number+1, "3d"), chr(number+1), " ", end="" )
    print( format( number+2, "3d"), chr(number+2), " ", end="" )
    print( format( number+3, "3d"), chr(number+3), " ", end="" )
    print( format( number+4, "3d"), chr(number+4), " ", end="" )
    print( format( number+5, "3d"), chr(number+5), " ", end="" )
    print( format( number+6, "3d"), chr(number+6), " ", end="" )
    print( format( number+7, "3d"), chr(number+7) )

print( "" )

