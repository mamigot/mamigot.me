var app = angular.module('blog', [
  'ngRoute',
]);


app.config(['$routeProvider', '$locationProvider',

  function($routeProvider, $locationProvider){
    $routeProvider

    .when('/blog', {
      templateUrl: 'static/app/partials/blog-archive.html',
      // pass controller here
    })

    .when('/blog/:year/:month/:day/:slug', {
      templateUrl: 'static/app/partials/blog-archive.html',
    })

  }]);
