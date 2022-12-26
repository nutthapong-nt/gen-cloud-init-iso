import pycdlib
from io import BytesIO

def make_iso(automatenumber:int,userdata:str, metadata:str):
    # Create a PyCdlib object.
    iso = pycdlib.PyCdlib()
    # Define iso config.
    iso.new(interchange_level=3,
            joliet=True,
            sys_ident='LINUX',
            rock_ridge='1.09',
            vol_ident='cidata')
    # Add meta-data file in iso.
    metadata_file = BytesIO(metadata.encode())
    metadata_file.seek(0)
    iso.add_fp(metadata_file,
               len(metadata),
               '/METADATA.;1',
               rr_name="meta-data",
               joliet_path='/meta-data',
               )
    # Add user-data file in iso.
    userdata_file = BytesIO(userdata.encode())
    iso.add_fp(userdata_file,
               len(userdata),
               '/USERDATA.;1',
               rr_name="user-data",
               joliet_path='/user-data',
               )
    # Write the iso file.
    iso.write(f"./CloudInitIso/Automate{str(automatenumber)}.iso")
    # Close PyCdlib Object.
    iso.close()
    userdata_file.close()
    metadata_file.close()
    return {"name":"create iso file","status":"success"}
