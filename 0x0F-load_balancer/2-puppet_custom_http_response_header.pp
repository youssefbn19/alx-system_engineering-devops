# Creating a custom HTTP header response.
exec { 'apt-get update':
    command => '/usr/bin/apt-get update'
}

package { 'nginx':
    ensure => "installed"
    require => Exec['apt-get update']
}

service { 'nginx':
   ensure => running,
   enable => true
}

exec { 'ufw allow':
    command => '/usr/bin/sudo /usr/sbin/ufw allow "Nginx HTTP"'
    require => Package['nginx']
}
exec { 'sed header':
    command => "/usr/bin/sudo /usr/bin/sed -i '/^\tlocation \/ {/ a\\n\t\tadd_header X-Served-By $hostname;' /etc/nginx/sites-enabled/default"
    require => Package['nginx']
}

