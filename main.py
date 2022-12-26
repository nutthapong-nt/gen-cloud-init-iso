from modlue.gen_userdata import gen_userdata
from modlue.makeiso import make_iso
from sys import argv

if __name__=="__main__":
    # Extract parameter
    _, osname, defaultpassword,ComputerName,CustomIPa4,CustomNetPrefix,CustomDF4GW,automatenumber = argv
    # Gen userdata
    userdata = gen_userdata(
        os=osname,
        defaultpassword=defaultpassword,
        ComputerName=ComputerName,
        CustomIPa4=CustomIPa4,
        CustomNetPrefix=CustomNetPrefix,
        CustomDF4GW=CustomDF4GW)
    # Gen metadata
    metadata = """instance-id: iid-local01\nlocal-hostname: localhost"""
    # Create iso file
    make_iso(automatenumber,userdata, metadata)
    