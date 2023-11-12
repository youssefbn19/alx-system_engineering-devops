# web stack debugging by fixing a line in configuration file
exec {'config file':
path     => ['/usr/bin', '/bin'],
command  => "sudo sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
provider => 'shell',
}
