# manifest that kills a process named killmenow.

Exec { 'killmenow_process':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
