pipeline {
    agent any
    stages {
        stage('Configuring') {
            steps {
                deleteDir()
                
                sh 'echo "$JOB_NAME | Cloning Repository..."'
                sh "git clone https://github.com/DaniloSouzza/caesar_cipher.git"
                
                echo 'Configuring environment...'
                sh 'pip3 install -r $(find . -name "requirements.txt" | xargs realpath)'
            
                echo 'Requirements Installed Successfully!'
            }
        }
        stage('Testing') {
            steps {
                sh 'echo "$JOB_NAME | Running Tests..."'
                sh 'python3 -m pip install pytest'
                sh 'python3 -m pytest -p no:cacheprovider -v'
        
                echo 'Tests proccessed!'
            }
        }
        stage('Deploying') {
            steps {
                dir("caesar_cipher") {
                sh 'echo "$JOB_NAME | Deploying Application..."'

                // sh 'docker stop $(docker ps -q)'
                // sh 'docker container prune || true'

                sh 'docker build -t $JOB_NAME -f $(find . -name "*.dockerfile" | xargs realpath) .'
                sh 'docker run -d -p 80:80 $JOB_NAME'

                echo 'Application Up!'
                }
            }
        }
    }
}
