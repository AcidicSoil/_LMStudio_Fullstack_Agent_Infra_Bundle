resource "aws_db_instance" "postgres" {
  identifier         = "lmstudio-db"
  allocated_storage  = 20
  engine             = "postgres"
  engine_version     = "15"
  instance_class     = "db.t3.micro"
  name               = "devdb"
  username           = "dev"
  password           = var.db_password
  skip_final_snapshot = true
  publicly_accessible = true
  vpc_security_group_ids = var.security_group_ids
  db_subnet_group_name   = var.db_subnet_group_name
}