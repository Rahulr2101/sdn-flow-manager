from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

class SimpleTopo(Topo):
    def build(self):
        # Create switches and hosts
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        
        # Add links with predefined ports
        self.addLink(host1, switch1)
        self.addLink(switch1, host3)
        self.addLink(switch1, switch2)
        self.addLink(host2, switch2)
        self.addLink(switch2, host3)

def run():
    topo = SimpleTopo()
    net = Mininet(topo=topo, controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6653))
    net.start()
    
    # Start CLI for testing
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
