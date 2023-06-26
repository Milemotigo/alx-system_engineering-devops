#server config
file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'ssh_config_1':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'IdentityFile ~/.ssh/school',
  match    => '^#?IdentityFile',
}

file_line { 'ssh_config_2':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'PasswordAuthentication no',
  match    => '^#?PasswordAuthentication',
}
