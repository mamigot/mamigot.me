var app = angular.module('main', ['ngRoute', 'ngSanitize', 'blog', 'shared']);


app.config(['$routeProvider', '$locationProvider',

  function($routeProvider, $locationProvider){
    $routeProvider

    .when('/', {
      templateUrl: 'static/src/partials/home.html',
    })

    .otherwise({
      templateUrl: 'static/src/partials/errors/404.html',
    });

    // https://docs.angularjs.org/error/$location/nobase
    $locationProvider.html5Mode({
      enabled: true
    });
    // https://github.com/angular/angular.js/issues/5519
    $locationProvider.hashPrefix('!');

  }]);
