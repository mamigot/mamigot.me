angular.module('projects')

  .directive('githubRepos', function(){

    return {
      restrict: 'E',
      templateUrl: 'static/src/partials/_github-repos.html',
    };

  });
