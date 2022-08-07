pipeline{
    parameters{
        string(name: 'branch', defaultValue: 'dev', description: 'Enter the Name of branch')
    }
    agent any
    stages{
        stage('clone the git repo'){
            steps{
                dir('source-code'){
                    git branch: branch,
                    url: 'git@github.com:hamzamaan/Delta_kubernetes.git'


                }
            }
        }
    }
}