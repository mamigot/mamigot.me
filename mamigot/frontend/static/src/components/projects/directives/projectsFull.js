angular.module('projects')

  .directive('projectsFull', function(){

    return {
      restrict: 'E',
      templateUrl: 'static/src/partials/_projects-full.html',
    };

  });
