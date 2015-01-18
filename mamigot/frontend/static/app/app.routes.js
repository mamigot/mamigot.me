angular.module('main').config(['$routeProvider', '$locationProvider',

    function($routeProvider, $locationProvider){
      $routeProvider

        .when('/', {
          templateUrl: 'static/app/partials/home.html',
        })

        .when('/blog', {
          templateUrl: 'static/app/partials/blog.html',
        });

        // https://docs.angularjs.org/error/$location/nobase
        $locationProvider.html5Mode({
          enabled: true
        });

    }]);
