# Creating a custom HTTP header response.
exec { 'apt-update':
    command => '/usr/bin/sudo /usr/bin/apt-get -y update',
}

package { 'nginx':
    ensure  => installed,
}

service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}

exec { 'change_file_owner':
    command => '/usr/bin/sudo /usr/bin/chown -R "$USER":"$USER"  /var/www/html',
    require => Package['nginx'],
}

exec { 'add_custom_header':
    command => '/usr/bin/sudo /usr/bin/sed -i
    "/^\tlocation \/ {/ a\\n\t\tadd_header X-Served-By $hostname;"
    /etc/nginx/sites-enabled/default',
    require => Package['nginx'],
}

exec { 'add_custom_header':
    command => '/usr/bin/sudo /usr/sbin/service nginx restart',
    require => Package['nginx'],
}