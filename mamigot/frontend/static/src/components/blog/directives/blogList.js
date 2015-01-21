angular.module('blog')

  .directive('blogList', function(){

      return {
        restrict: 'E',
        templateUrl: 'static/src/partials/_posts-list.html',
      };

    });
