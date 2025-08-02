output "databricks_job_id" {
  description = "ID of the Databricks job for data processing"
  value       = databricks_job.data_process.id
}

output "databricks_job_name" {
  description = "Name of the Databricks job for data processing"
  value       = databricks_job.data_process.name
}
