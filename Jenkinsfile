pipeline {
  agent any
  stages {
    stage('test') {
      agent any
      steps {
        sh 'pytest code/add2.py'
      }
    }

  }
}
