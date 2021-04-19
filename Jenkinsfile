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
                sh "apt-get -y install python"
                sh "apt-get -y install python3-distutils"
				sh "apt-get -y install python3-apt"
                sh "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"
                sh "python3 get-pip.py"
                sh "python3 -m pip install -U pip"
                sh "python3 -m pip --version"
				sh "pip install docker"
				sh "python create_container_if_not_exists.py"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}