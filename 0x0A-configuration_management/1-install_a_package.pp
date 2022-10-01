# Using Puppet, install flask from pip3
framework {'flask': ensure => '2.1.0', provider => 'pip3',}
