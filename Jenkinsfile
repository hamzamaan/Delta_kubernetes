pipeline{
    parameters{
        string(name: 'branch', defaultValue: 'dev', description: 'Enter the Name of branch')
        string(name: 'registry', defaultValue: '191124798140.dkr.ecr.us-east-2.amazonaws.com', description: 'Enter the ARN of the registry')
        string(name: 'registry_name', defaultValue: 'saelor-application', description: 'Enter the Name of the registry')
        string(name: 'dockerImage', defaultValue: '191124798140.dkr.ecr.us-east-2.amazonaws.com', description: 'Enter the Name of the Docker Image')
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
                
                
                curl -X POST "http://18.216.55.201:8080/api/v2/reimport-scan/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data"  -H "Authorization: Token 494d5bcaf4cbadcb1f09df5f76f0a4389aaf5ad7" -F "active=true" -F "verified=true" -F "minimum_severity=Info" -F "active=true" -F "scan_type=Hadolint Dockerfile check" -F "file=@/home/new_home/workspace/AWS-EKS-Microservice/code/hadolint.json" -F "product_name=saelor" -F "scan_date=2022-06-14" -F "engagement_name=saelor-microservices-lint-eg" -F "engagement=8"
                '''
                // curl --location --request POST 'http://3.144.3.241:8080/api/v2/import-scan/' --header 'Authorization: Token d654dc00c584932942be6c064923543b996201fe' --form 'scan_type="Hadolint Dockerfile check"' --form 'engagement="2"' --form 'file=@/home/new_home/workspace/AWS-EKS-Microservice/code/hadolint.json'
                //Create engagment
                //curl -X POST   "http://18.216.55.201:8080/api/v2/engagements/" -H "Authorization: Token 494d5bcaf4cbadcb1f09df5f76f0a4389aaf5ad7"  -F "name=saelor-microservices-lint-eg" -F "product=3" -F "target_start=2022-06-14" -F "target_end=2022-06-14"

            }
        }

          stage('Building Docker image - DOCKER PLUGIN') { 
            steps {
                script {
                    dockerImage = docker.build (registry + ":$BUILD_NUMBER", "./code") 
                }           
            }
        }

        stage ('Docker Image Vulnerability Scan - TRIVY '){
            steps{
                script{
                    sh '''
                    trivy image -f json -o results.json --exit-code 0 --severity CRITICAL,HIGH  $registry:$BUILD_NUMBER
                    curl -X POST "http://18.216.55.201:8080/api/v2/reimport-scan/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -H  "Authorization: Token 494d5bcaf4cbadcb1f09df5f76f0a4389aaf5ad7" -F "minimum_severity=Info" -F "active=true" -F "verified=true" -F "scan_type=Trivy Scan" -F "push_to_jira=false" -F "close_old_findings=true" -F "file=@/home/new_home/workspace/AWS-EKS-Microservices-Test/code/results.json" -F "product_name=saelor" -F "scan_date=2022-06-14" -F "engagement_name=saelor-microservices-trivy-eg" -F "engagement=9"
                    '''
                    //curl --location --request POST 'http://3.144.3.241:8080/api/v2/import-scan/' --header 'Authorization: Token d654dc00c584932942be6c064923543b996201fe' --form 'scan_type="Trivy Scan"' --form 'engagement="2"' --form 'file=@/home/new_home/workspace/AWS-EKS-Microservice/code/results.json'
                    //Create engagment
                    //curl -X POST   "http://18.216.55.201:8080/api/v2/engagements/" -H "Authorization: Token 494d5bcaf4cbadcb1f09df5f76f0a4389aaf5ad7"  -F "name=saelor-microservices-lint-trivy-eg" -F "product=3" -F "target_start=2022-06-14" -F "target_end=2022-06-14"

                }
            }
        }

        
        stage('Push Docker image to Registry - DOCKERHUB/ECR/ACR') { 
            steps { 
                script { 
                    sh '''#!/bin/bash
                    aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $registry
                    docker tag $registry:$BUILD_NUMBER $registry/$registry_name:$BUILD_NUMBER
                    docker push $registry/$registry_name:$BUILD_NUMBER
                    '''
                } 
            }
        }



    }
}