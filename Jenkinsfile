pipeline {
  agent any
  stages {
    stage('test') {
      agent { dockerfile true }
      steps {
        sh 'pytest add2.py'
      }
    }
  }
}
