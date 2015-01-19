angular.module('main').config(['$routeProvider', '$locationProvider',

    function($routeProvider, $locationProvider){
      $routeProvider

        .when('/', {
          templateUrl: 'static/app/partials/home.html',
        })

        .when('/blog', {
          templateUrl: 'static/app/partials/blog.html',
        })

        .when('/blog/:year/:month/:day/:slug', {
          templateUrl: 'static/app/partials/blog.html',
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
