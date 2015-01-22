angular.module('projects')

  .directive('projectsPanel', function(){

    return {
      restrict: 'E',
      templateUrl: 'static/src/partials/_projects-panel.html',
    };

  });
