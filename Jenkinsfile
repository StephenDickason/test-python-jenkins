pipeline {
  agent any
  stages {
    stage('test') {
      agent { dockerfile true }
      steps {
        sh 'pwd'
        sh 'ls'
        sh 'pytest add2.py'
      }
    }
  }
}
