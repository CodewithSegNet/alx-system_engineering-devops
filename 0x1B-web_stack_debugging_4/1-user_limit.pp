# A puppet manifest that change the user limit
file { '/etc/security/limits.conf':
  ensure => file,
  require => Exec['change_value_to_50'],
}

exec { 'change_value_to_50':
  command     => "/bin/sed -i 's/5/50/g' /etc/security/limits.conf",
  refreshonly => true,
}

exec { 'change_value_to_40':
  command     => "/bin/sed -i 's/4/40/g' /etc/security/limits.conf",
  refreshonly => true,
}
