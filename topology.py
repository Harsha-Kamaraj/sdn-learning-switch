# Mininet Topology for SDN Learning Switch Demo
# Creates: 3 hosts connected to 1 OpenFlow switch

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI


class SimpleTopo(Topo):
    """Simple topology: 3 hosts connected to 1 switch"""

    def build(self):
        # Add switch
        s1 = self.addSwitch('s1')

        # Add 3 hosts with specific IPs
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')

        # Connect each host to the switch
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)


def run():
    topo = SimpleTopo()

    # Connect to Ryu controller running on localhost port 6633
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6633)
    )

    net.start()
    print("\n=== Network Started ===")
    print("Hosts: h1(10.0.0.1), h2(10.0.0.2), h3(10.0.0.3)")
    print("Type 'exit' or Ctrl+D to stop\n")

    CLI(net)  # Opens interactive Mininet CLI
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
