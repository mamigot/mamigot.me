angular.module('shared').

  /*
  Converts a path for a partial from relative to absolute.

  EXAMPLE:
    Without the filter:
      <div ng-include="'/static/app/partials/_navbar.html'"></div>

    With the filter:
      <div ng-include=" '_navbar.html' | partial "></div>
  */
  filter('partial', function(){

    return function(relative) {
      return "/static/app/partials/" + relative;
    };

  });
