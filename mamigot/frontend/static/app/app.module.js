var app = angular.module('main', ['ngRoute', 'blog', 'shared']);


app.config(['$routeProvider', '$locationProvider',

  function($routeProvider, $locationProvider){
    $routeProvider

    .when('/', {
      templateUrl: 'static/app/partials/home.html',
    })

    .otherwise({
      templateUrl: 'static/app/partials/errors/404.html',
    });

    // https://docs.angularjs.org/error/$location/nobase
    $locationProvider.html5Mode({
      enabled: true
    });
    // https://github.com/angular/angular.js/issues/5519
    $locationProvider.hashPrefix('!');

  }]);
