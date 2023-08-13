# 0-strace_is_your_friend.pp
exec { 'restart-apache':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
}

file { '/etc/apache2/apache2.conf':
  ensure => file,
  source => 'puppet:///modules/<your_module_name>/apache2.conf'
  notify => Exec['restart-apache'],
}
