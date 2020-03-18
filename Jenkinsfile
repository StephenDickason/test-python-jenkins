pipeline {
  agent any
  stages {
    stage('test') {
      agent any
      steps {
        sh 'pytest code/python/add2.py'
      }
    }

  }
}
