(function(){

  var app = angular.module('blog', ['ngRoute']);

  app.config(['$routeProvider', '$locationProvider',

    function($routeProvider, $locationProvider){
      $routeProvider

      .when('/blog', {
        templateUrl: 'static/app/partials/blog.html',
        controller: 'BlogListCtrl',
      })

      .when('/blog/:slug', {
        templateUrl: 'static/app/partials/blog.html',
        controller: 'BlogDetailCtrl',
      })

    }]);

})();
