#!/bin/bash

SSHKEY=""
USERNAME="ansible"
PASSWORD="12345678"

apt-get update
apt-get install -y mc htop wget curl python3 ssh

# создать пользователя
useradd -m -s /bin/bash $USERNAME
usermod -aG sudo $USERNAME

# установить пароль
echo "$USERNAME:$PASSWORD" | chpasswd

# создать ssh ключи
mkdir -p /home/$USERNAME/.ssh
echo "$SSHKEY" > /home/$USERNAME/.ssh/authorized_keys

# права
chown -R $USERNAME:$USERNAME /home/$USERNAME/.ssh
chmod 700 /home/$USERNAME/.ssh
chmod 600 /home/$USERNAME/.ssh/authorized_keys

echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME