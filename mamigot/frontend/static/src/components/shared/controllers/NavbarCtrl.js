angular.module('shared')

  .controller('NavbarCtrl', function(){

    this.activePage = undefined;

    this.selectPage = function(page){
      this.activePage = page;
    };

    this.isSelected = function(page){
      return this.activePage == page;
    };

  });
