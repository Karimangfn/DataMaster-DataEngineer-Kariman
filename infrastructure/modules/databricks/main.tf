resource "databricks_repo" "repo" {
  count = var.enable ? 1 : 0

  provider = databricks.this

  url    = var.git_repo_url
  path   = "/Repos/${basename(var.git_repo_url)}"
  branch = var.git_repo_branch
}
