resource "aws_ecs_cluster" "main" {
  name = "${local.prefix}-cluster"

  tags = local.common_tags
}

resource "aws_iam_policy" "task_execution_role_policy" {
  name        = "${local.prefix}-task-exec-role-policy"
  path        = "/"
  description = "Allow retrieving of images/files and adding to logs"
  policy      = file("./templates/ecs/task-exec-role.json")
}

resource "aws_iam_role" "task_execution_role" {
  name               = "${local.prefix}-task-exec-role"
  assume_role_policy = file("./templates/ecs/assume-role-policy.json")
}

resource "aws_iam_role_policy_attachment" "task_execution_role" {
  role       = aws_iam_role.task_execution_role.name
  policy_arn = aws_iam_policy.task_execution_role_policy.arn
}


resource "aws_iam_role" "app_iam_role" {
  name               = "${local.prefix}-api-task"
  assume_role_policy = file("./templates/ecs/assume-role-policy.json")

  tags = local.common_tags
}

resource "aws_cloudwatch_log_group" "ecs_task_logs" {
  name = "${local.prefix}-api"

  tags = local.common_tags
}

data "template_file" "webapp_container_definitions" {
  template = file("./templates/ecs/container-definitions.json.tpl")

  vars = {
    app_image         = var.docker_webportal_image
    proxy_image       = var.docker_proxy_image
    django_secret_key = var.django_secret_key
    db_host           = aws_db_instance.webportal_database.address
    db_name           = aws_db_instance.webportal_database.name
    db_user           = aws_db_instance.webportal_database.username
    db_pass           = aws_db_instance.webportal_database.password
    log_group_name    = aws_cloudwatch_log_group.ecs_task_logs.name
    log_group_region  = data.aws_region.current.name
    allowed_hosts     = "*" //URGENT: Using wildcard for now. Needs to be updated 
  }
}

resource "aws_ecs_task_definition" "webapp" {
  family                   = "${local.prefix}-webapp"
  container_definitions    = data.template_file.webapp_container_definitions.rendered
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = 256
  memory                   = 512
  execution_role_arn       = aws_iam_role.task_execution_role.arn
  task_role_arn            = aws_iam_role.app_iam_role.arn
  volume {
    name = "static"
  }

  tags = local.common_tags
}
