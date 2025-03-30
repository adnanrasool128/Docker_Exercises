{
  "variables": {
    "aws_region": "us-east-1"
  },
  "builders": [
    {
      "type": "amazon-ebs",
      "region": "{{user `aws_region`}}",
      "source_ami": "ami-04b4f1a9cf54c11d0",
      "instance_type": "t2.micro",
      "ssh_username": "ubuntu",
      "ami_name": "python3.9-only-ami-{{timestamp}}",
      "associate_public_ip_address": true
    }
  ],

  provisioner "shell" {
  inline = [
    "curl https://pyenv.run | bash",
    "export PATH=$HOME/.pyenv/bin:$PATH",
    "eval \"$(pyenv init --path)\"",
    "pyenv install 3.9.0",
    "pyenv global 3.9.0",
    "python3.9 --version"
  ]
}
}
