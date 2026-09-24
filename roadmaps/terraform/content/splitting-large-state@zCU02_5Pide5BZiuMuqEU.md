# Splitting Large State

Large state files slow down plans and increase the risk of conflicts. Splitting infrastructure into smaller, independently managed configurations with their own state files reduces plan times and limits the impact of a failed apply. Resources in different state files communicate through remote state data sources or variable passing.