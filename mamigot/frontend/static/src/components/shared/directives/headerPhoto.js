angular.module('main')

  /*
  Sets the header photo with a title, if provided.

  EXAMPLE:
    Photo renders without a title:
      <header-photo></header-photo>

    Photo renders with "PROJECTS" written in the middle:
      <header-photo data-page-title="Projects"></header-photo>
  */
  .directive('headerPhoto', function(){

    function link(scope, element, attrs){
      attrs.$observe('headerTitle', function(value){
        scope.pageTitle = value ? value.toUpperCase() : "";
      })
    }

    return {
      restrict: 'E',
      templateUrl: 'static/src/partials/_header-photo.html',
      link: link,
    };

  });
