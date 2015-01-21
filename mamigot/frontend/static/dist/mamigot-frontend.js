(function(){

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

})();
;(function(){

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
;angular.module('blog')

  .controller('BlogDetailCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http){

      var slug = $routeParams.slug;


      $http.get('/api/blog/posts/' + slug).success(function(data){
        // Body HTML is automatically sanitized using ng-sanitize
        // https://docs.angularjs.org/api/ngSanitize/service/$sanitize

        $scope.post = data[0];

      });

  }]);
;angular.module('blog')

.controller('BlogListCtrl', ['$scope', '$http',
  function($scope, $http){

    $http.get('/api/blog/posts/').success(function(data){

      $scope.posts = data;

    });

}]);
;angular.module('blog')

  .directive('blogDetail', function(){

    return {
      restrict: 'E',
      templateUrl: 'static/src/partials/_post-detail.html',
    };

  });
;angular.module('blog')

  .directive('blogList', function(){

      return {
        restrict: 'E',
        templateUrl: 'static/src/partials/_posts-list.html',
      };

    });
;angular.module('shared')

  /*
  Sets the header photo with a title, if provided.

  EXAMPLE:
    Photo renders without a title:
      <header-photo></header-photo>

    Photo renders with "PROJECTS" written in the middle:
      <header-photo data-page-title="Projects"></header-photo>
  */
  .directive('headerPhoto', function(){

    function link(scope, element, attrs){
      attrs.$observe('headerTitle', function(value){
        scope.pageTitle = value ? value.toUpperCase() : "";
      })
    }

    return {
      restrict: 'E',
      templateUrl: 'static/src/partials/_header-photo.html',
      link: link,
    };

  });
;angular.module('shared')

  /*
  Converts a path for a partial from relative to absolute.

  EXAMPLE:
    Without the filter:
      <div ng-include="'/static/app/partials/_navbar.html'"></div>

    With the filter:
      <div ng-include=" '_navbar.html' | partial "></div>
  */
  .filter('partial', function(){

    return function(relative) {
      return "/static/src/partials/" + relative;
    };

  });
;(function(){

  var app = angular.module('shared', []);

})();
