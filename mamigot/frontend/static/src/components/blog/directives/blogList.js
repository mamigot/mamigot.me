angular.module('blog')

  /*
  Retrieves a list of the posts in the blog through the template below. Though
  the retrieval is up to the controller called in the template, this directive
  sets a 'limit' variable on the template's scope that the controller can use
  to set a limit for the number of posts it retrieves.

  EXAMPLE:
    No limit:
      <blog-list></blog-list>

    Set a limit to 3:
      <blog-list limit=3></blog-list>
  */
  .directive('blogList', function(){

    return {
      restrict: 'E',
      templateUrl: 'static/src/partials/_blog-list.html',

      controller: function($scope, $attrs){
        /*
        Set 'limit' on the template's scope according to the attribute
        on the directive. This only affects the template's scope.
        */
        $scope.limit = $attrs.limit;
      }
    };

  });
