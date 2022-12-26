# Create Cloud init ISO file for config Linux Computer

## Overall
- Create iso file for config Linux Computer by cloud-init.

## Usage
- Create function gen_userdata in modlue/gen_userdata.py this function is create config for computer as string. Ex. [user-data example](https://cloudinit.readthedocs.io/en/latest/topics/examples.html), 
- run python main.py any parameter you need for config the computer. Ex. python main.py ubuntu20.04 password computer_name 192.168.1.2 24 192.169.1.1 1

## Resource
- [about cloud-init.](https://cloudinit.readthedocs.io/en/latest/index.html)
- [makeiso for cloud-init reference.](https://github.com/clalancette/pycdlib/issues/7)
