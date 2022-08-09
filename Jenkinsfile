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
                    credentialsId: 'ssh_git',
                    url: 'git@github.com:hamzamaan/Delta_kubernetes.git'


                }
            }
        }

        stage('clone the kubernetes-app git repo '){
            steps{
                dir('kubernetes-app'){
                    git branch: branch,
                    credentialsId: 'ssh_git',
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

            stage('DockerFile Liniting - HADOLINT ') {
            steps {
                sh '''
                cd code && docker run --rm -i -v ${PWD}/.hadolint.yml:/.hadolint.yaml hadolint/hadolint hadolint  -f json - < Dockerfile > hadolint.json
                
                #Create engagment
                #curl -X POST   "http://18.216.55.201:8080/api/v2/engagements/" -H "Authorization: Token 494d5bcaf4cbadcb1f09df5f76f0a4389aaf5ad7"  -F "name=saelor-microservices-lint-eg" -F "product=3" -F "target_start=2022-06-14" -F "target_end=2022-06-14"

                curl -X POST "http://18.216.55.201:8080/api/v2/reimport-scan/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -H  "Authorization: Token 494d5bcaf4cbadcb1f09df5f76f0a4389aaf5ad7"  -F "minimum_severity=Info" -F "active=true" -F "verified=true" -F "scan_type=Hadolint Dockerfile check" -F "push_to_jira=false" -F "close_old_findings=true" -F "file=@/home/new_home/workspace/AWS-EKS-Microservices-Test/code/hadolint.json" -F "product_name=saelor" -F "product=3" -F "scan_date=2022-06-14" -F "engagement_name=saelor-microservices-lint-eg -F "engagement=8"
                '''
                // curl --location --request POST 'http://3.144.3.241:8080/api/v2/import-scan/' --header 'Authorization: Token d654dc00c584932942be6c064923543b996201fe' --form 'scan_type="Hadolint Dockerfile check"' --form 'engagement="2"' --form 'file=@/home/new_home/workspace/AWS-EKS-Microservice/code/hadolint.json'

            }
        }
    }
}