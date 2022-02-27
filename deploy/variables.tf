variable "prefix" {}

variable "project" {
  default = "web-portal"
}

variable "contact" {
  default = "adriel_tolentino@outlook.com"
}

variable "db_username" {
  description = "Username for the RDS postgres instance"
}

variable "db_password" {
  description = "Password for the RDS postgress instance"
}

variable "bastion_key_name" {
  default = "web_portal_bastion_secret_key"
}
