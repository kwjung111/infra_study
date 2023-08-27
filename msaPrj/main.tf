resource "aws_db_instance" "msa_RDS"{
  allocated_storage = 8
  engine = "mysql"
  engine_version = "8.0.33"
  identifier = "mds-db"
  db_name ="mds-db"
  instance_class = "db.t2.micro"
  password = "password"
  skip_final_snapshot = true
  storage_encrypted = false
  publicly_accessible = true
  username = "admin"
  apply_immediately = true
  port = 5000
}