angular.module('blog')

.controller('BlogListCtrl', ['$scope', '$http',
  function($scope, $http){

    $http.get('/api/blog/posts/').success(function(data){

      $scope.posts = data;

    });

}]);
