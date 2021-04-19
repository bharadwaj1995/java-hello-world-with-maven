pipeline {
    agent any

    tools {
		jdk "JDK"
        maven "3.6.0" // You need to add a maven with name "3.6.0" in the Global Tools Configuration page
		java "JDK"
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