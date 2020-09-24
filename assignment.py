import argparse
import openstack

conn = openstack.connect(cloud_name='openstack')
def create(conn):
    ''' Create a set of Openstack resources '''
	openstack network create --internal \kyleal1\-net
	openstack subnet create --network \kyleal1\-net --subnet-range 192.168.50.0/24 \kyleal1\-net
	
	openstack router create \kyleal1\-rtr
	openstack router add subnet \kyleal1\-rtr \kyleal1-subnet
	openstack router set --external-gateway public-net \kyleal1\-rtr
	
	openstack floating ip create public-net
	
	openstack server create --image ubuntu-minimal-16.04-x86_64 \
	--security-group assignment2 \ 
	--flavour c1.c1r1 \
	--network \kyleal1\-net \
	\kyleal1\-web
	
		openstack server create --image ubuntu-minimal-16.04-x86_64 \
	--security-group assignment2 \ 
	--flavour c1.c1r1 \
	--network \kyleal1\-net \
	\kyleal1\-app
	
		openstack server create --image ubuntu-minimal-16.04-x86_64 \
	--security-group assignment2 \ 
	--flavour c1.c1r1 \
	--network \kyleal1\-net \
	\kyleal1\-db
    pass

	
	'''*create*: Create the following resources in OpenStack
  - A network named "\<username\>-net" with a subnet, 192.168.50.0/24
  - A router named "\<username\>-rtr" with interfaces joining the network
    above with public-net
  - A floating IP address
  - Three servers
     - image: ubuntu-minimal-16.04-x86_64
     - flavour: c1.c1r1
     - names: \<username\>-web, \<username\>-app, \<username\>-db
     - security-group: assignment2 (You may need to create this)
  Assign the floating IP to the web server.
  If any of the resources above already exisit when the script is run, then they 
  should not be recreated.'''
  
  
  
def run():
    ''' Start  a set of Openstack virtual machines
    if they are not already running.
    '''
    pass

def stop():
    ''' Stop  a set of Openstack virtual machines
    if they are running.
    '''
    pass

def destroy():
    ''' Tear down the set of Openstack resources 
    produced by the create action
    '''
	openstack server delete \kyleal1\-web
	openstack server delete \kyleal1\-app
	openstack server delete \kyleal1\-db
	openstack floating ip delete <io address>
	openstack router remove subnet \kyleal1\-rtr \kyleal1-subnet
	openstack router delete \kyleal1\-rtr
	openstack subnet delete \kyleal1-subnet
	openstack network delete \kyleal1\-net

    pass

def status():
    ''' Print a status report on the OpenStack
    virtual machines created by the create action.
    '''
	openstack server show \kyleal1\-web
	openstack server show \kyleal1\-app
	openstack server show \kyleal1\-db
    pass


### You should not modify anything below this line ###
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('operation',
                        help='One of "create", "run", "stop", "destroy", or "status"')
    args = parser.parse_args()
    operation = args.operation

    operations = {
        'create'  : create,
        'run'     : run,
        'stop'    : stop,
        'destroy' : destroy,
        'status'  : status
        }

    action = operations.get(operation, lambda: print('{}: no such operation'.format(operation)))
    action()
