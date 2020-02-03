pipeline {
    agent any
    stages{  
        stage('Build-image') {
            steps {
                sh ''' #!/bin/bash
                  cd /var/lib/jenkins/workspace/
                
                  scp -r Test1 ubuntu@172.31.38.102:/home/ubuntu
                  
                  '''  
            }
        }
    }
}  
