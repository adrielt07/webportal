# Creates an output of resources.

output "db_host" {
  value = aws_db_instance.webportal_database.address
}
