pipeline {
    agent any

    tools {
		jdk "JDK"
        maven "3.6.0" 
    }

    stages {
        stage("Build") {
            steps {
                sh "mvn clean install"
            }
        }
		stage("Check Container") {
            steps {
                sh "apt-get install python"
                sh "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"
                sh "python get-pip.py"
                sh "python -m pip install -U pip"
                sh "python -m pip --version"
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