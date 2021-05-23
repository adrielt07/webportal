variable "prefix" {}

variable "project" {
  default = "ctrl-layer-web-portal"
}

variable "contact" {
  default = "atolentino@ctrl-layer.com"
}

variable "db_username" {
  description = "Username for the RDS postgres instance"
}

variable "db_password" {
  description = "Password for the RDS postgress instance"
}