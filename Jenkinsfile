pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing'
                echo "${BUILD_ID}"
                echo "${Name}"
            }
        }
        stage('Build') {
            steps {
                echo 'Building'
            }
        }
        stage('Deploy') {
            steps {
                echo 'deploying'
            }
        }
    }
}
