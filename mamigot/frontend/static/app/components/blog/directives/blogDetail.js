angular.module('blog')

  .directive('blogDetail', function(){

    return {
      restrict: 'E',
      templateUrl: 'static/app/partials/_post-detail.html',
    };

  });
