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
