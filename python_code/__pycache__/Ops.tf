
resource "aws_instance" "virtual_server" {
 ami           = data.aws_ami.My_ubuntu007.id   
  instance_type = var.instance_type
  key_name      = var.key_name        
  vpc_security_group_ids = [aws_security_group.my-sg.id]
  subnet_id           = data.terraform_remote_state.vpc.outputs.public_subnet_ids[0]
  availability_zone   = var.zones
  
  root_block_device {
    volume_size = var.volume_size
  }

  tags = {
    Name = var.server_name
  }

  
  # USING REMOTE-EXEC PROVISIONER TO INSTALL PACKAGES
  provisioner "remote-exec" {
    # ESTABLISHING SSH CONNECTION WITH EC2
    connection {
      type        = "ssh"
      private_key = file("./DevOps-gitOps-key.pem") # replace with your key-name 
      user        = "ubuntu"
      host        = self.public_ip
    }

    inline = [
      # Install Docker
      # Ref: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
      "sudo apt-get update -y",
      "sudo apt-get install -y ca-certificates curl",
      "sudo install -m 0755 -d /etc/apt/keyrings",
      "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.asc",
      "sudo chmod a+r /etc/apt/keyrings/docker.asc",
      "echo \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
      "sudo apt-get update -y",
      "sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin",
      "sudo usermod -aG docker ubuntu",
      "sudo usermod -aG docker jenkins",
      "sudo systemctl start docker",
      "sudo systemctl enable docker",
      "sudo chmod 777 /var/run/docker.sock",
      "docker --version",

      # Install Gitleaks
      "sudo apt install gitleaks -y",

      # Install Minikube
      # Ref: https://minikube.sigs.k8s.io/docs/start/
      "curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64",
      "sudo chmod +x minikube",
      "sudo mv minikube /usr/local/bin/",
      "sudo install minikube /usr/local/bin/",
      "minikube start --driver=docker",
      "minikube version",

      # Install Helm
      # Ref: https://helm.sh/docs/intro/install/
      # Ref (for .tar.gz file): https://github.com/helm/helm/releases
      "wget https://get.helm.sh/helm-v3.16.1-linux-amd64.tar.gz",
      "tar -zxvf helm-v3.16.1-linux-amd64.tar.gz",
      "sudo mv linux-amd64/helm /usr/local/bin/helm",
      "helm version",

      # Install Trivy
      # Ref: https://aquasecurity.github.io/trivy/v0.18.3/installation/
      "sudo apt-get install -y wget apt-transport-https gnupg",
      "wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null",
      "echo 'deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main' | sudo tee -a /etc/apt/sources.list.d/trivy.list",
      "sudo apt-get update -y",
      "sudo apt-get install trivy -y",

      # Install Kubectl
      # Ref: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
      "curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl",
      "sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl",
      "chmod +x kubectl",
      "mkdir -p ~/.local/bin",
      "mv ./kubectl ~/.local/bin/kubectl",
      "export PATH=$PATH:~/.local/bin",
      "alias k=kubectl",
      "k version --client",

      # Install Java 17
      # Ref: https://www.rosehosting.com/blog/how-to-install-java-17-lts-on-ubuntu-20-04/
      "sudo apt update -y",
      "sudo apt install openjdk-17-jdk openjdk-17-jre -y",
      "java -version",

      # Install Jenkins
      # Ref: https://www.jenkins.io/doc/book/installing/linux/#debianubuntu
      "sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key",
      "echo \"deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/\" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null",
      "sudo apt-get update -y",
      "sudo apt-get install -y jenkins",
      "sudo systemctl start jenkins",
      "sudo systemctl enable jenkins",

       
      # Install SonarQube (as a container)
      "docker run -d --name sonar -p 9000:9000 sonarqube:lts-community",

      # Chqnge Jenkins default port to 8081 
      "sudo sed -i -e 's/Environment=\"JENKINS_PORT=[0-9]\\+\"/Environment=\"JENKINS_PORT=8081\"/' /usr/lib/systemd/system/jenkins.service",
      "sudo sed -i -e 's/^\\s*#\\s*AmbientCapabilities=CAP_NET_BIND_SERVICE/AmbientCapabilities=CAP_NET_BIND_SERVICE/' /usr/lib/systemd/system/jenkins.service",
      "sudo systemctl daemon-reload",
      "sudo systemctl restart jenkins",
      "sudo lsof -i -n -P | grep jenkins",

      # install ArgoCD CLI
      # Ref: https://argo-cd.readthedocs.io/en/stable/cli_installation/
      # ArgoCD Listens On Port 8080
      "k create ns argocd",
      "k apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.5.8/manifests/install.yaml",

      # Get Jenkins initial login password
      "ip=$(curl -s ifconfig.me)",
      "pass=$(sudo cat /var/lib/jenkins/secrets/initialAdminPassword)",

      # Output
      "echo \"Access Jenkins Server here --> http://$ip:8081\"",
      "echo \"Jenkins Initial Password: $pass\"",
    ]
  }
}