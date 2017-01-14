import thread

def thread_(stuff):
    print "I'm a real boy!"
    print stuff

thread.start_new_thread(thread_,('Argument'))

