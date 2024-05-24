# from raw EC2 machine or other fresh installation

## TODO: adapt this into a dockerfile and prove runs

sudo apt install gh
sudo apt install make
sudo apt install pip
sudo apt update
sudo apt install -y curl git imagemagick jq unzip vim zsh tree
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
sudo apt-get update; sudo apt-get install direnv
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc

echo -e "<ssh_key_fingerprint> github.com" >> ~/.ssh/known_hosts
# >> appends

- this is overkill detail, especially line by line echoes:
    echo -e "Host github.com" > ~/.ssh/config
      HostName github.com" >> ~/.ssh/config
    echo -e "  User git" >> ~/.ssh/config
    echo -e "  IdentityFile '~/.ssh/ec2_240518'" >> ~/.ssh/config

- better:
echo -e "Host github.com
    Hostname github.com                            
    User git                  
    IdentityFile '~/.ssh/some_key'" > ~/temp_config_example.txt

    ssh -T git@github.com
    Hi hughharford! You've successfully authenticated, but GitHub does not provide shell access.

- Make sure an SSH key is setup with Github on this instance, then:
mkdir code; cd code
git clone git@github.com:hughharford/atp.git


### dotfiles
export GITHUB_USERNAME=`gh api user | jq -r '.login'`
echo $GITHUB_USERNAME
cd ~/code; git clone git@github.com:hughharford/dotfiles.git
cd ~/code/dotfiles && zsh install.sh
cd ~/code/dotfiles && zsh git_setup.sh

# TODO: HERE ___ SKIP FOR NOW
<!-- vim ~/.zshrc and add ssh-agent to the end of the plugins= list
save and exit -->

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
exec zsh

### install python:
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
python3-dev

### reboot or re-source to get this to work: 
- exec zsh
pyenv install 3.10.6

### set virtual environment
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
exec zsh
pyenv virtualenv 3.10.6 hsth_data_sci
pyenv global hsth_data_sci

### install python packages
pip install --upgrade pip

### install many Python packages for data science
- Wary of what is needed, and how much space is required
-- BEFORE RUNNING COMMAND:
    ➜  code df -H                                                       [🐍 hsth_data_sci]
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/root        31G  3.8G   27G  13% /
    tmpfs           502M     0  502M   0% /dev/shm
    tmpfs           201M  877k  200M   1% /run
    tmpfs           5.3M     0  5.3M   0% /run/lock
    /dev/xvda16     924M   79M  780M  10% /boot
    /dev/xvda15     110M  6.4M  104M   6% /boot/efi
    tmpfs           101M   13k  101M   1% /run/user/1000

-- COMMAND: (NB LONG LIST - started at 0952)
pip install -r https://raw.githubusercontent.com/lewagon/data-setup/master/specs/releases/linux.txt

-- AFTER RUNNING COMMAND:
@@@@@@@@@@@@ on HSTH machine, which might have lots already installed...
/dev/nvme0n1p5  113G   69G   39G  64% /
/dev/nvme0n1p5  113G   71G   37G  66% / 
- On HSTH machine requirements makes 6Gb
- Could well be more on EC2 Volume, given low starting point of installed code
- EC2 had 30GB - say 20GB is needed to allow for Swapfile etc
- RESTART did it, back up:

  ➜  code df -H                                                        [🐍 hsth_data_sci]
  Filesystem      Size  Used Avail Use% Mounted on
  /dev/root        31G  5.1G   26G  17% /
  tmpfs           502M     0  502M   0% /dev/shm
  tmpfs           201M  877k  200M   1% /run
  tmpfs           5.3M     0  5.3M   0% /run/lock
  /dev/xvda16     924M   79M  780M  10% /boot
  /dev/xvda15     110M  6.4M  104M   6% /boot/efi
  tmpfs           101M   13k  101M   1% /run/user/1000

- Seems only <2G was installed
- But ho, Jupyter not yet installed. odd.

- Line by line install from list above using pip
pip install jupyter-contrib-core==0.4.0;
pip install jupyter-contrib-nbextensions==0.5.1;
pip install jupyter-highlight-selected-word==0.2.0;
pip install jupyter-latex-envs==1.4.6;
pip install jupyter-nbextensions-configurator==0.5.0;
pip install jupyter-resource-usage==0.6.3;
pip install jupyter-server==1.21.0;
pip install jupyter_client==7.4.3;
pip install jupyter_core==4.11.2;
pip install jupyterlab==3.4.8;
pip install jupyterlab-pygments==0.2.2;
pip install jupyterlab-widgets==1.1.1;
pip install jupyterlab_server==2.16.1;


# JUPYTER NOTEBOOK
*** JUPYTER NOTEBOOK
### install nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable toc2/main
jupyter nbextension enable collapsible_headings/main
jupyter nbextension enable spellchecker/main
jupyter nbextension enable code_prettify/code_prettify

# RUNNING JUPYTER NOTEBOOK
- run:
  --jupyter notebook from the command line within VS Code
- then:
  -- click the link to open in your browser - needs a little authorisation
  -- works fine, without difficulty
