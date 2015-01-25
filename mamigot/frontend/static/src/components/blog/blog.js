(function(){

  var app = angular.module('blog', ['ngRoute']);

  app.config(['$routeProvider', '$locationProvider',

    function($routeProvider, $locationProvider){
      $routeProvider

      .when('/blog', {
        templateUrl: 'static/src/partials/blog.html',
      })

      .when('/blog/:slug', {
        templateUrl: 'static/src/partials/blog.html',
        controller: function($scope, $routeParams){
          $scope.slug = $routeParams.slug;
        }
      })

    }]);

})();
