resource "openstack_networking_secgroup_v2" "secgroup1" {
  name = "secgroup1"
  description = "Security Group 1"
}

resource "openstack_networking_secgroup_rule_v2" "allow_https" {
  direction = "ingress"
  ethertype = "IPv4"
  protocol = "tcp"
  port_range_max = 443
  port_range_min = 443
  remote_ip_prefix = "0.0.0.0/0"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup1.id}"
}
resource "openstack_networking_secgroup_rule_v2" "allow_ftp_pasv" {
  direction = "ingress"
  ethertype = "IPv4"
  protocol = "tcp"
  port_range_max = 64050
  port_range_min = 64000
  remote_ip_prefix = "192.10.2.0/24"
  security_group_id = "${openstack_networking_secgroup_v2.secgroup1.id}"
}
