pipeline {
  agent any
  stages {
    stage('node-build') {
      agent { dockerfile { 
        filename 'Dockerfile-js'
        }
      }
      environment {
        HOME = '.'
      }
      steps {
        sh 'cd node/ && npm install'
      }
    }
    stage('test') {
      agent { dockerfile true }
      steps {
        sh 'pwd'
        sh 'ls'
        sh 'pytest python/add2.py'
      }
    }
  }
}
