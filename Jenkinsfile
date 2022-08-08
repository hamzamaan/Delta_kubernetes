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
                    git branch: branch,
                    credentialsId: 'hamza.sajjad',
                    url: 'git@github.com:hamzamaan/Kubernetes_app.git'
                }
            }

        }

           stage('Code Analysis - sonarqube-saelor') {
            steps {
                script{
                    env.sonarHome= tool name: 'sonarqube-saelor', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                }
                withSonarQubeEnv('sonarqube-saelor') {
                    sh """
                      ${sonarHome}/bin/sonar-scanner \
                      -Dsonar.projectKey=saelor-project  \
                      -Dsonar.sources=. \
                    """
                }
            }
        }
    }
}