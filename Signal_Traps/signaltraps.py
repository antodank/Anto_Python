import signal 
import sys
def interrupt_signal_handler(signal, frame):
        print("You pressed Ctrl+C!")
        sys.exit(0)

def break_signal_handler(signal, frame):
        print("You pressed Ctrl+Break!")
        sys.exit(0)
        
def ternimal_signal_handler(signal, frame):
        print("Termination signal received. Exiting gracefully...")
        sys.exit(0)

signal.signal(signal.SIGINT, interrupt_signal_handler)
signal.signal(signal.SIGBREAK, break_signal_handler)
signal.signal(signal.SIGTERM, ternimal_signal_handler)

while 1:
        continue