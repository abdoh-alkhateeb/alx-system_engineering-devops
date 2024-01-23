# Kill a process named killmenow

exec { 'kill killmenow':
  command  => 'pkill -f killmenow',
  provider => 'shell'
}
