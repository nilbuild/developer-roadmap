# Creation / Destroy Time

Provisioners run either at creation time, after the resource is created, or at destroy time, before the resource is deleted. Creation-time provisioners bootstrap resources, while destroy-time provisioners handle cleanup tasks. If a creation-time provisioner fails, the resource is marked as tainted and will be destroyed and recreated on the next apply.

Visit the following resources to learn more:

- [@official@Creation Time Provisioners](https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax#creation-time-provisioners)
- [@official@Destroy Time Provisioners](https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax#destroy-time-provisioners)
- [@official@How to: Terraform destroy time provisioners](https://support.hashicorp.com/hc/en-us/articles/11119084989587-How-to-Terraform-Destroy-time-Provisioners)