# increase number of open fd
exec {'fd':
path     => ['/usr/bin', '/bin'],
command  => "sudo sed -i 's/15/2000/g' /etc/default/nginx; sudo service nginx restart",
provider => 'shell',
}