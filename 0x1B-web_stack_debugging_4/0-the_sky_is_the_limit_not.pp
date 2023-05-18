# It allows you to simulate HTTP requests to a web server. 
# In this case, 
# I will make 2000 requests to my server with 100 requests at a time.

file_line{'ulimit_option':
    pathi => '/etc/default/nginx',
    line  => 'ULIMIT="-n 2049"',
    match => '^ULIMIT='
}
