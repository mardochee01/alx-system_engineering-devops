# Using Puppet, install flask from pip3

framework {'flask':
command => '/usr/bin/pip3 install flask -v 2.1.0',
}
