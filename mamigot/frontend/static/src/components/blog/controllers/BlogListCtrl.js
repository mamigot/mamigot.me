angular.module('blog')

  .controller('BlogListCtrl', ['$http', '$scope', function($http, $scope){

      var c = this;
      c.posts = {};

      var limitParam = $scope.limit ? "&limit=" + $scope.limit : "";

      $http.get('/api/blog/posts?fields=title,created_at' + limitParam)
        .success(function(data){

          c.posts = data;

        });

  }]);
