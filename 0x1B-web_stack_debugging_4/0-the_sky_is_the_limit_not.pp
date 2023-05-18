# It allows you to simulate HTTP requests to a web server. 
# I will make 2000 requests to my server with 100 requests at a time.

file{ '/etc/default/nginx':
    ensure  => file,
    content => "ULIMIT='-n 2049'\n"
}
