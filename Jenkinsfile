pipeline {
  agent any
  stages {
    stage('test') {
      agent { dockerfile true }
      steps {
        sh 'pytest code/add2.py'
      }
    }
  }
}
