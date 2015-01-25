(function(){

  var app = angular.module('blog', ['ngRoute']);

  app.config(['$routeProvider', '$locationProvider',

    function($routeProvider, $locationProvider){
      $routeProvider

      .when('/blog', {
        templateUrl: 'static/src/partials/_blog-list.html',
      })

      .when('/blog/:slug', {
        templateUrl: 'static/src/partials/_blog-detail.html',
      })

    }]);

})();
