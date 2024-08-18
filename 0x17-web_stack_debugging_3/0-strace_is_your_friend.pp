#Some php setting not right in wp-settings.php.... we stream edit it
exec { 'replace':
  command => "sed -i -e 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/'
}
