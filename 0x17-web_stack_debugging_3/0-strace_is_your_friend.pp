# Fixing returning a 500 error in The Apache server
exec {'config file':
path     => ['/usr/bin', '/bin'],
command  => "sudo sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
provider => 'shell',
}
