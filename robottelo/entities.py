from robottelo import orm

class Operatingsystems(orm.Entity):
    # validator: Must match regular expression /\A(\S+)\Z/.
    name = orm.StringField(required=True, null=False)
    # validator: String
    major = orm.StringField(required=True, null=False)
    # validator: String
    minor = orm.StringField(required=False, null=True)
    # validator: String
    description = orm.StringField(required=False, null=True)
    # validator: String
    family = orm.StringField(required=False, null=True)
    # validator: String
    release_name = orm.StringField(required=False, null=True)


class Organizations(orm.Entity):
    # description: name
    # validator: String
    name = orm.StringField(required=True, null=False)
    # description: unique label
    # validator: String
    label = orm.StringField(required=False, null=False)
    # description: description
    # validator: String
    description = orm.StringField(required=False, null=False)

    class Meta:
        api_path="/katello/api/v2/organizations"


class Architectures(orm.Entity):
    # validator: String
    name = orm.StringField(required=True, null=False)
    # description: Operatingsystem ID's
    # validator: Array
    operatingsystem = orm.OneToManyField(Operatingsystems, required=False, null=True)


class AuthSourceLdaps(orm.Entity):
    # validator: String
    name = orm.StringField(required=True, null=False)
    # validator: String
    host = orm.StringField(required=True, null=False)
    # description: defaults to 389
    # validator: number.
    port = orm.StringField(required=False, null=True)
    # validator: String
    account = orm.StringField(required=False, null=True)
    # validator: String
    base_dn = orm.StringField(required=False, null=True)
    # description: required if onthefly_register is true
    # validator: String
    account_password = orm.StringField(required=False, null=True)
    # description: required if onthefly_register is true
    # validator: String
    attr_login = orm.StringField(required=False, null=True)
    # description: required if onthefly_register is true
    # validator: String
    attr_firstname = orm.StringField(required=False, null=True)
    # description: required if onthefly_register is true
    # validator: String
    attr_lastname = orm.StringField(required=False, null=True)
    # description: required if onthefly_register is true
    # validator: String
    attr_mail = orm.StringField(required=False, null=True)
    # validator: String
    attr_photo = orm.StringField(required=False, null=True)
    # validator: boolean
    onthefly_register = orm.StringField(required=False, null=True)
    # validator: boolean
    tls = orm.StringField(required=False, null=True)


class Bookmarks(orm.Entity):
    # validator: String
    name = orm.StringField(required=True, null=False)
    # validator: String
    controller = orm.StringField(required=True, null=False)
    # validator: String
    query = orm.StringField(required=True, null=False)
    # validator: boolean
    public = orm.StringField(required=False, null=True)


class CommonParameters(orm.Entity):
    # validator: String
    name = orm.StringField(required=True, null=False)
    # validator: String
    value = orm.StringField(required=True, null=False)


class ComputeProfiles(orm.Entity):
    # validator: String
    name = orm.StringField(required=True, null=False)


class ComputeResources(orm.Entity):
    # validator: String
    name = orm.StringField(required=False, null=True)
    # description: Providers include Libvirt, Ovirt, EC2, Vmware, Openstack,
    # Rackspace, GCE
    # validator: String
    provider = orm.StringField(required=False, null=True)
    # description: URL for Libvirt, RHEV, and Openstack
    # validator: String
    url = orm.StringField(required=True, null=False)
    # validator: String
    description = orm.StringField(required=False, null=True)
    # description: Username for RHEV, EC2, Vmware, Openstack. Access Key for
    # EC2.
    # validator: String
    user = orm.StringField(required=False, null=True)
    # description: Password for RHEV, EC2, Vmware, Openstack. Secret key for
    # EC2
    # validator: String
    password = orm.StringField(required=False, null=True)
    # description: for RHEV, Vmware Datacenter
    # validator: String
    uuid = orm.StringField(required=False, null=True)
    # description: for EC2 only
    # validator: String
    region = orm.StringField(required=False, null=True)
    # description: for Openstack only
    # validator: String
    tenant = orm.StringField(required=False, null=True)
    # description: for Vmware
    # validator: String
    server = orm.StringField(required=False, null=True)


class ConfigGroups(orm.Entity):
    # validator: String
    name = orm.StringField(required=True, null=False)


class Domains(orm.Entity):
    # description: The full DNS Domain name
    # validator: String
    name = orm.StringField(required=True, null=False)
    # description: Full name describing the domain
    # validator: String
    fullname = orm.StringField(required=False, null=True)


class Environments(orm.Entity):
    # validator: String
    name = orm.StringField(required=True, null=False)

    class Meta:
        api_path = "/api/environments/"


class LifecycleEnvironments(orm.Entity):
    # description: name of organization
    # validator: number.
    organization = orm.OneToOneField(Organizations, required=True, null=False)
    # description: name of the environment
    # validator: String
    name = orm.StringField(required=True, null=False)
    # description: description of the environment
    # validator: String
    description = orm.StringField(required=False, null=False)
    # description: Name of an environment that is prior to the new
    # environment in the chain. It has to be either 'Library' or an environment
    # at the end of a chain.
    # validator: String
    prior = orm.DefaultField("1")

    class Meta:
        api_path = "/katello/api/v2/environments/"





class Media(orm.Entity):
    # description: Name of media
    # validator: String
    name = orm.StringField(required=True, null=False)
    # description: The path to the medium, can be a URL or a valid NFS server
    # (exclusive of the architecture).  for example mirror.centos.org/centos/$version/o
    # s/$arch where $arch will be substituted for the host's actual OS
    # architecture and $version, $major and $minor will be substituted for the
    # version of the operating system.  Solaris and Debian media may also
    # use $release.
    # validator: String
    path = orm.StringField(required=True, null=False)
    # description: The family that the operating system belongs to.
    # Available families:  AIX  Archlinux
    #  Debian  Freebsd  Gentoo
    #  Junos  Redhat  Solaris
    #  Suse  Windows
    # validator: String
    os_family = orm.StringField(required=False, null=True)
    # validator: Array
    operatingsystem = orm.OneToManyField(Operatingsystems, required=False, null=True)



class Ptables(orm.Entity):
    # validator: String
    name = orm.StringField(required=True, null=False)
    # validator: String
    layout = orm.StringField(required=True, null=False)
    # validator: String
    os_family = orm.StringField(required=False, null=True)

class SmartProxies(orm.Entity):
    # validator: String
    name = orm.StringField(required=True, null=False)
    # validator: String
    url = orm.StringField(required=True, null=False)



class Hosts(orm.Entity):
    # validator: String
    name = orm.StringField(required=True, null=False)
    # validator: String
    environment = orm.OneToOneField(Environments, required=False, null=True)
    # description: not required if using a subnet with dhcp proxy
    # validator: String
    ip = orm.StringField(required=False, null=True)
    # description: not required if its a virtual machine
    # validator: String
    mac = orm.StringField(required=False, null=True)
    # validator: number.
    architecture = orm.OneToOneField(Architectures, required=False, null=True)
    # validator: number.
    domain = orm.OneToOneField(Domains, required=False, null=True)
    # validator: String
    operatingsystem = orm.OneToOneField(Operatingsystems, required=True, null=True)
    # validator: number.
    medium = orm.OneToOneField(Media, required=True, null=True)
    # validator: number.
    ptable = orm.OneToOneField(Ptables, required=False, null=True)
    # validator: boolean
    build = orm.StringField(required=False, null=True)
    # validator: boolean
    enabled = orm.StringField(required=False, null=True)
    # validator: String
    provision_method = orm.StringField(required=False, null=True)
    # validator: boolean
    managed = orm.StringField(required=False, null=True)
    # description: UUID to track orchestration tasks status, GET
    # /api/orchestration/:UUID/tasks
    # validator: String
    capabilities = orm.StringField(required=False, null=True)


