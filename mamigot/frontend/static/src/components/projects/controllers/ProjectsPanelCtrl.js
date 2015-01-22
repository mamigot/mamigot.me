angular.module('projects')

  .controller('ProjectsPanelCtrl', function(){

    /* TODO: build this structure via the API; have a service return this */
    this.projects = [
      [
        {
          id : 1,
          title : 'Software Development at About.com',
          slug : '',
          logo : 'static/img/logos/about.png',
        },
        {
          id : 2,
          title : 'Education Technology at IBL Studios Education',
          slug : '',
          logo : 'static/img/logos/iblstudios.png',
        },
        {
          id : 3,
          title : 'Online Courses and MOOCs',
          slug : '',
          logo : 'static/img/logos/edx.png',
        },
      ],
      [
        {
          id : 4,
          title : 'Web Application Development',
          slug : '',
          logo : 'static/img/logos/flask.png',
        },
        {
          id : 5,
          title : 'Coursework at NYU',
          slug : '',
          logo : 'static/img/logos/nyu.png',
        },
        {
          id : 6,
          title : 'Additional Projects',
          slug : '',
          logo : 'static/img/logos/xilinx.png',
        },
      ]
    ];

    this.defaultProject = this.projects[0][1];
    this.activeProject = this.defaultProject;

    this.selectProject = function(projectID){
      /* TODO: improve the performance of this method */
      var numRows = this.getNumRows();
      var numPerRow = this.projects[0].length;

      for(var i = 0; i < numRows; i++){

        var currRow = this.projects[i];
        for(var j = 0; j < numPerRow; j++){

          if(currRow[j].id == projectID){
            this.activeProject = currRow[j];
            return;
          }
        }
      }
    };

    this.isSelected = function(projectID){
      return this.activeProject.id == projectID;
    };

    this.getSelected = function(){
      return this.activeProject;
    }

    this.getNumRows = function(){
      return this.projects.length;
    }

    this.getRow = function(rowNumber){
      /* rowNumber starts at 1 */
      if(rowNumber <= 0 || rowNumber > this.projects.length){
        return undefined;
      }

      return this.projects[rowNumber - 1];
    }

  });
