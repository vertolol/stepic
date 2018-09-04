bind = "127.0.0.1:8080"
# или через сокет
# bind = "unix:/home/proft/projects/blog/run/blog.socket"
workers = 5
user = "vertol"
group = "vertol"
logfile = "/home/vertol/PycharmProjects/untitled/stepic/my_stepic_project/gunicorn.log"
loglevel = "info"
proc_name = "blog"
#pidfile = "/home/proft/projects/blog/gunicorn.pid"