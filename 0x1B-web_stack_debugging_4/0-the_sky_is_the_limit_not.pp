# Sky is the limit, let's bring that limit higher
exec { 'find-n-replace':
  command => "sed -i 's/ULIMIT = -n 15/ULIMIT = -n 5000/g' /etc/nginx/nginx.conf; sudo service nginx restart",
  path    => $::path
}
