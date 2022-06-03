pipeline {
    agent any
    stages {
        stage('analisis-codigo') {
            steps {
                sh 'echo "Ejecuta comandos para análisis de estándar código"'
                sh 'echo "Ejecuta SonaQube"'
            }
        }
        stage('test') {
            steps {
                sh 'echo "Pruebas unitarias"'
            }
            
        }
        stage('build') {
            steps {
                sh 'Cosas de construcción'
                sh 'python manage.py collectstatic --noinput'
            }
        }
        stage('despliegue-pre') {
            steps {
                sh 'echo "Despliegue a pre-producción"'
                sh 'chmod +x deploy.sh'
                sh './deploy.sh'
            }
        }

        stage('Revisión por QA') {
            steps {
                input "Desplegar en producción?"
            }
        }
        stage('despliegue-pro') {
            steps {
                sh 'echo "Despliegue a producción"'
            }
        }
    }
    post {
        always {
            deleteDir() /* clean up our workspace */
        }
    }

}
chuckNorris()

