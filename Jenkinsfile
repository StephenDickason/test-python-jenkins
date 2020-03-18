pipeline {
  agent any
  stages {
    stage('test') {
      agent {
        docker {
          image 'python:3.6-stretch'
          args '-v code/python:code/'
        }

      }
      steps {
        sh 'pytest python/add2.py'
      }
    }

  }
}