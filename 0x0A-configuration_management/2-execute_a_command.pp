#execute a command
exec { 'kill_process':
     command => 'pkill -f killmenow',
     onlyif  => 'pgrep -f killmenow',
}
    