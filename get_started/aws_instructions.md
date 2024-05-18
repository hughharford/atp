# AWS setup
- Get an EC2 instance configured and running.
- Follow something like this: https://medium.com/@christyjacob4/using-vscode-remotely-on-an-ec2-instance-7822c4032cff
- Once the EC2 is up and SSH connection established, follow instructions below
- NOTE: These instructions work for this AMI:
--        ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-20240423

# Set the AWS traffic rules to accept on port 22, from your IP address.
- Consider making your IP static so that you can specify just from your IP
    https://www.freecodecamp.org/news/setting-a-static-ip-in-ubuntu-linux-ip-address-tutorial/
    if you get errors, remember permissions:
    https://jason19970210.medium.com/proper-way-to-setup-netplan-yaml-file-permission-867da8eb026a

# Set ssh <ec2_ip_may_vary_of_course>:
- config file for ssh. /home/hughharford/.ssh/config
  Host aws-ec2
    HostName ec2-54-159-48-6.compute-1.amazonaws.com
    IdentityFile /home/hughharford/.ssh/240517_aws2.pem
    User ubuntu

    # connect with:
    # ssh -i /home/hughharford/.ssh/240517_aws.pub ubuntu@ec2-54-159-48-6.compute-1.amazonaws.com
    # permissions set with 
    #                   chmod 700 /home/hughharford/.ssh/240517_aws2.pem

# ONCE ON THE INSTANCE:

# SSH command line to get started
- Use the following commands, copy and paste as needed:  
mkdir code; cd code

- Make sure an SSH key is setup with Github on this instance, then:
git clone git@github.com:hughharford/atp.git

ssh -T git@github.com
