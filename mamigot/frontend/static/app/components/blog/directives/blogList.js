angular.module('blog')

  .directive('blogList', function(){

      return {
        restrict: 'E',
        templateUrl: 'static/app/partials/_posts-list.html',
      };

    });
