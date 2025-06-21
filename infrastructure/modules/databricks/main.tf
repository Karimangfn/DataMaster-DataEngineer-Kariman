resource "databricks_repo" "repo" {
  count = var.enable ? 1 : 0

  provider = databricks.this

  url    = var.git_repo_url
  path   = "/Repos/dtMaster/service"
  branch = var.git_repo_branch
}

resource "databricks_service_principal" "sp" {
  application_id = var.client_id
  display_name   = "dtMasterSPN"
  allow_cluster_create = true
}
