pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git(url: 'https://github.com/AnjaliPPrajapati/crud-application', branch: 'main')
                script{
                        env.COMMIT_SHA = bat (
                                returnStdout: true,
                                script: 'Git rev-parse HEAD'
                        ).trim()
                    }
                    echo "111111111111111111111 ${COMMIT_SHA}"
            }
            
        }
        stage('Test') {
            steps {
                echo 'Testing..........!'
                bat 'pip install -r requirements.txt'
                bat 'python manage.py test'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat "docker build -t jenkinslearn ."
            }
        }
        stage('Login to docker hub'){
            steps{
                script{
                    withCredentials([string(credentialsId: 'jenkins_dockerhub', variable: 'jenkins_dockerhub')]) {
                        bat "docker login -u anjalipprajapati -p ${jenkins_dockerhub}"
                    }
                }
            }
        }
        stage('Publish Image')
        {
            steps{
                bat "docker tag jenkinslearn anjalipprajapati/jenkinslearning:jenkinslearn-${BUILD_NUMBER}"
                bat "docker push anjalipprajapati/jenkinslearning:jenkinslearn-${BUILD_NUMBER}"
            }
        }
    }
    post{
        always{
            bat 'docker logout'
        }
        
    }
}
