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
    stage('node-test') {
      agent { dockerfile { 
        filename 'Dockerfile-js'
        }
      }
      environment {
        HOME = '.'
      }
      steps {
        sh 'sleep 1m'
      }
    }
    stage('python-test') {
      agent { dockerfile true }
      steps {
        sh 'pwd'
        sh 'ls'
        sh 'pytest python/add2.py'
      }
    }
    stage('python-run') {
      agent { dockerfile true }
      steps {
        sh 'pwd'
        sh 'ls'
        sh 'python python/add2.py'
      }
    }
    stage('node-publish') {
      agent { dockerfile { 
        filename 'Dockerfile-js'
        }
      }
      environment {
        HOME = '.'
      }
      steps {
        sh 'cd node/ && ng serve'
      }
    }
  }
}
