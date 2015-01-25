angular.module('blog')

.controller('BlogListCtrl', ['$http',
  function($http){

    var c = this;
    c.posts = {};

    $http.get('/api/blog/posts?fields=title,created_at')
      .success(function(data){

        c.posts = data;

      });

}]);
