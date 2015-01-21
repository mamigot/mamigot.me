angular.module('blog')

  .controller('BlogDetailCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http){

      var slug = $routeParams.slug;


      $http.get('/api/blog/posts/' + slug).success(function(data){
        // Body HTML is automatically sanitized using ng-sanitize
        // https://docs.angularjs.org/api/ngSanitize/service/$sanitize

        $scope.post = data[0];

      });

  }]);
