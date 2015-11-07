# -*- mode: ruby -*-
# vi: set ft=ruby :

# Set our default provider for this Vagrantfile to 'vmware_appcatalyst'
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'vmware_appcatalyst'

nodes = [
  { hostname: 'gantry-test-1', box: 'hashicorp/precise64' },
  { hostname: 'gantry-test-2', box: 'hashicorp/precise64' }
]

Vagrant.configure('2') do |config|

  # Configure our boxes with 1 CPU and 384MB of RAM
  config.vm.provider 'vmware_appcatalyst' do |v|
    v.cpus = '1'
    v.memory = '384'
  end

  # Go through nodes and configure each of them.
  nodes.each do |node|
    config.vm.define node[:hostname] do |node_config|
      node_config.vm.box = node[:box]
      node_config.vm.hostname = node[:hostname]
      node_config.vm.synced_folder('sources/', '/home/vagrant/RadioController')
    end
  end
end
