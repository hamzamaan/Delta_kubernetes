pipeline{
    parameters{
        string(name: 'branch', defaultValue: 'dev', description: 'Enter the Name of branch')
    }
    agent any
    stages{
        stage('clone the source-code git repo'){
            steps{
                dir('source-code'){
                    git branch: branch,
                    credentialsId: 'hamza.sajjad',
                    url: 'git@github.com:hamzamaan/Delta_kubernetes.git'


                }
            }
        }

        stage('clone the kubernetes-app git repo '){
            steps{
                dir('kubernetes-app'){
                    git branch: branch
                    credentialsId: 'hamza.sajjad'
                    url: 'git@github.com:hamzamaan/Kubernetes_app.git'
                }
            }

        }
    }
}