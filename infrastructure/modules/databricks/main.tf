data "databricks_group" "admins" {
  display_name = "admins"
}

resource "databricks_service_principal" "sp" {
  application_id = var.client_id
  display_name   = "dtMasterSPN"
  allow_cluster_create = true
}

resource "databricks_group_member" "admin" {
  group_id  = data.databricks_group.admins.id
  member_id = databricks_service_principal.sp.id
}

resource "databricks_directory" "folder" {
  provider = databricks.this
  path     = "/Repos/dtMaster"
}

resource "databricks_repo" "repo" {
  count = var.enable ? 1 : 0

  provider = databricks.this

  url    = var.git_repo_url
  path   = "/Repos/dtMaster/service"
  branch = var.git_repo_branch

  depends_on = [databricks_directory.dtmaster_folder]
}
