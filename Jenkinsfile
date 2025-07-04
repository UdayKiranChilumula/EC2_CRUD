pipeline {
    agent any

    parameters {
        choice(name: 'OPERATION', choices: ['create', 'start', 'stop', 'terminate'], description: 'Choose the EC2 operation')
    }

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/your-username/aws-ec2-launcher.git', branch: 'main'
            }
        }

        stage('Execute EC2 Operation') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-credentials']]) {
                    sh 'python3 ec2_manager.py ${OPERATION}'
                }
            }
        }
    }
}
