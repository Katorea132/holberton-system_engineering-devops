include stdlib

file_line {'phpp':
  ensure => present,
  path   => '/var/www/html/wp-settings.php',
  line   => 'php',
  match  => 'phpp'
}
