#Create a file
#Creates a file in /tmp/school with specific ownership configurations and 
#with particular content
file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data'
  group   => 'www-data',
  }
	  
