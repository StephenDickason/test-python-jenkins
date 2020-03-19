pipeline {
  agent any
  stages {
    stage('test') {
      agent {
        docker { dockerfile true }

      }
      steps {
        sh 'pytest code/add2.py'
      }
    }

  }
}
