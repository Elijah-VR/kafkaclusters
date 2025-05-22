variable "vpc-00a22d417f36b6e7e" {}
variable "subnet_ids" {
  type = ["subnet-0ffad71c47bf57506", "subnet-08453128f96f409c0", "subnet-0841fd9b8af9c910e"])
}
variable "instance_type" {
  default = "t3.small"
}
