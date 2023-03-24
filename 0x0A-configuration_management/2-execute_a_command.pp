# A Manifest to kill a process killmenow
exec {'killing a process killmenow on all puppet-agent':
  command  => 'pkill -9 killmenow',
  path     => '/bin:/usr/bin',
  onlyif   => 'pgrep killmenow',
  provider => shell
}
