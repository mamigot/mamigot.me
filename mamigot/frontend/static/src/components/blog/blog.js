(function(){

  var app = angular.module('blog', ['ngRoute']);

  app.config(['$routeProvider', '$locationProvider',

    function($routeProvider, $locationProvider){
      $routeProvider

      .when('/blog', {
        templateUrl: 'static/src/partials/blog.html',
        controller: 'BlogListCtrl',
      })

      .when('/blog/:slug', {
        templateUrl: 'static/src/partials/blog.html',
        controller: 'BlogDetailCtrl',
      })

    }]);

})();
