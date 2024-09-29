import sys
from pyp2p.net import Net

def send_message(message):
    # Create the P2P connection
    net = Net(passive_bind="0.0.0.0", passive_port=44445, node_type="passive", debug=1)
    net.start()

    # Connect to the server (P2P listener)
    con = net.bootstrap([{"addr": "receiver_ip_here", "port": 44444}])

    # Send the message
    con.send(message)

    # Close connection
    con.shutdown()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python send_message.py <message>")
    else:
        message = sys.argv[1]
        send_message(message)
