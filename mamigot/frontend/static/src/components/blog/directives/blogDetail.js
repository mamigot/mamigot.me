angular.module('blog')

  .directive('blogDetail', function(){

    return {
      restrict: 'E',
      templateUrl: 'static/src/partials/_blog-detail.html',
    };

  });
