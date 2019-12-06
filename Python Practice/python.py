#!usr/bin/python

#mib_bits = "111001110011000111110010"
mib_bits=raw_input("enter the bit string:")
if len(mib_bits)==24:
	dl_rb_bits=mib_bits[0:3]
	phich_duration_bits=mib_bits[3]
	phich_resource_bits=mib_bits[4:6]
	sfn_bits=mib_bits[6:14]
	spare_bits=mib_bits[14:]



	dl_rb={'000':'n6','001':'n15','010':'n25',\
		'011':'n50','100':'n75','101':'n100'}
	
	phich_Resource={'00':'oneSixth','01':'one',\
			 '10':'half','11':'two'}

	sfn_number=int(sfn_bits,2)


	if dl_rb_bits in dl_rb.keys():
		print "dl_bandwidth\t",dl_rb[dl_rb_bits]
	else:
		print "error in mib bits string- dl_rb_bits "

	if phich_duration_bits=='0':
  	    print "phich-duration\t","normal"
	elif phich_duration_bits=='1':
            print "phich-duration\t","Extended"
       	else:
            print " error in mib bit string - phich bits "

	if phich_resource_bits in phich_Resource.keys():
	     print "phich-Resource\t",phich_Resource[phich_resource_bits]
       	else:
	     print " error in mib bit string - phich bits "

	print "systemFrameNumber\t",sfn_number

else:	
	print(" length of the MIB should contain 24 bits only ")

