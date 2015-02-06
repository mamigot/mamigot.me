angular.module('projects')

  .controller('ProjectsFullCtrl', ['$http', function($http){

    var c = this;
    c.projects = {};

    $http.get('/api/projects/posts?fields=body,title,slug')
      .success(function(data){

        c.projects = data;

      });


  }]);
