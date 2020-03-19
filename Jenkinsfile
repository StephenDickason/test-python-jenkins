pipeline {
  agent any
  stages {
    stage('node-build') {
      agent { dockerfile { 
        filename 'Dockerfile-js'
        }
      }
      steps {
        sh 'cd node/simple-node-js-react-npm-app-master/'
        sh 'ls'
        sh 'pwd'
        sh 'cd node/simple-node-js-react-npm-app-master/'
        sh 'ls'
        sh 'npm install'
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
