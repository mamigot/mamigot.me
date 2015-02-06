angular.module('projects')

  .controller('GithubReposCtrl', ['$http', '$scope', function($http, $scope){

    var c = this;
    c.repos = {};

    var numRepos = 4;
    var limitParam = "limit=" + numRepos;

    $http.get('/api/github/repos?' + limitParam)
      .success(function(data){

        c.repos = data.content;

      });


  }]);
