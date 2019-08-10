from urllib import request
import sys, os, time
buf_size = 4096



# Program arguments -> show-title, length of show in hours, output path
def main():
    args = get_arguments()
    stream_source = get_stream_source()
    start_time = int(time.time())
    end_time = start_time + (args['show_length'] * 3600)

    record(args, stream_source, end_time)
    
    

def record(args, src, end):
    
    output_path = format_output_path(args['output_path'], args['show_title'])

    stream = open(output_path, "wb")
    conn = request.urlopen(src)
    while int(time.time()) < end:
        stream.write(conn.read(buf_size))
    conn.close()
    sys.exit(0)


def get_arguments():
    if len(sys.argv) != 4:
        print("Missing required arguments ( show-title, length of show )", sys.stderr)
        sys.exit(-1)
    
    return {
        'show_title' : sys.argv[1],
        'show_length' : int(sys.argv[2]),
        'output_path' : sys.argv[3],
    }


def get_stream_source():
    streams = get_streams()
    for stream in streams:
        if request.urlopen(stream).getcode() == 200:
            return stream
    print("All streams are down! Check stream sources", file=sys.stderr)
    sys.exit(-1)



def get_streams():
    return [
        "http://kxlu.streamguys1.com/kxlu-hi"
    ]
    
    
    
def format_output_path(path, title):
    if path[len(path)-1] != '/':
        path = path + '/'
    if not os.path.isdir(path):
        print("Bad output path supplied", file=sys.stderr)
        sys.exit(-1)
    
    tm = time.gmtime()
    y = tm.tm_year ; m = tm.tm_mon ; d = tm.tm_mday
    timestamp = y + '_' + m + '_' + d + '_'

    path = path + timestamp + title
    return path
