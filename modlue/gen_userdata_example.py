# This use to config ubuntu20.04 and centOS7.
# it not work for any case, it depend on your computer, os, defult config.

def gen_userdata(os,defaultpassword,ComputerName,CustomIPa4,CustomNetPrefix,CustomDF4GW):
    userdata = []
    # Add cloud init declare
    userdata.append("#cloud-config")
    # User config
    userdata.append(f"""
users:
  - name: rootadmin
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    lock-passwd: false
    plain_text_passwd: {defaultpassword}
""")
    # ComputerName config
    if os in ["ubuntu20.04"]:
        userdata.append(f"hostname: {ComputerName}")
    else:
        userdata.append(f"fqdn: {ComputerName}")
    # allocate writefile and runcmd
    writefile = []
    runcmd = []

    # Network Config
    # if has network
    if CustomIPa4!="-":
        # netplan eth0
        if os in ["ubuntu20.04"]:
            writefile.append({"path":"/etc/netplan/00-installer-config.yaml","content":f"""
network:
  ethernets:
    eth0:
      addresses: [{CustomIPa4}/{CustomNetPrefix}]
      gateway4: {CustomDF4GW}
      nameservers:
        addresses: [8.8.8.8]
  version: 2
"""})
            runcmd.append("netplan apply")

    # eject config iso
    runcmd.append("eject sr0")

    # add writefile to userdata
    if writefile:
        userdata.append("write_files:")
    for file in writefile:
        userdata.append(f"""
  - path: {file["path"]}
    content: {file["content"]}"
""")
    # add run cmd to userdata
    if runcmd:
        userdata.append("runcmd:")
    for cmd in runcmd:
        userdata.append(f"  - {cmd}")
    
    # final masage
    userdata.append("final_message: Computer setup successfully!")

    return '\n'.join(userdata)