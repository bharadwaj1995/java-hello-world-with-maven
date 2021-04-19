pipeline {
    agent any

    tools {
		jdk "JDK"
        maven "3.6.0" 
    }

    stages {
        stage("Build") {
            steps {
                sh "mvn -version"
                sh "mvn clean install"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}