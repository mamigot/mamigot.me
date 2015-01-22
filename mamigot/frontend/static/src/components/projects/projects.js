(function(){

  var app = angular.module('projects', ['ngRoute']);

  app.config(['$routeProvider', '$locationProvider',

  function($routeProvider, $locationProvider){
    $routeProvider

      .when('/projects', {
        templateUrl: 'static/src/partials/projects.html',
      })

      .when('/projects/:slug', {
        templateUrl: 'static/src/partials/projects.html',
      })

  }]);

})();
