angular.module('blog')

.controller('BlogListCtrl', ['$scope', '$http',
  function($scope, $http){

    $http.get('/api/blog/posts?fields=title,created_at')
      .success(function(data){

        $scope.posts = data;

      });

}]);
