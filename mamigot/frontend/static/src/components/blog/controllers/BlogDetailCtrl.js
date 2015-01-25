angular.module('blog')

  .controller('BlogDetailCtrl', ['$routeParams', '$http',
    function($routeParams, $http){

      var c = this;
      c.post = {};

      var slug = $routeParams.slug;


      $http.get('/api/blog/posts/' + slug).success(function(data){
        // Body HTML is automatically sanitized using ng-sanitize
        // https://docs.angularjs.org/api/ngSanitize/service/$sanitize

        c.post = data[0];

      });

  }]);
