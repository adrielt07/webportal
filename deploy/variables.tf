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

variable "docker_webportal_image" {
  description = "Webportal docker image"
}

variable "docker_proxy_image" {
  description = "Proxy's docker image"
}

variable "django_secret_key" {
  description = "Secret key for Django key"
}