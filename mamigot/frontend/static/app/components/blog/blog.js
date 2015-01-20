(function(){

  var app = angular.module('blog', ['ngRoute']);

  app.config(['$routeProvider', '$locationProvider',

    function($routeProvider, $locationProvider){
      $routeProvider

      .when('/blog', {
        templateUrl: 'static/app/partials/blog-archive.html',
      })

      .when('/blog/:slug', {
        templateUrl: 'static/app/partials/_post-detail.html',
        controller: 'PostDetailController',
      })

    }]);

})();
