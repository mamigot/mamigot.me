angular.module('projects')

  .controller('ProjectsPanelCtrl',
    ['ProjectsOverviewSvce', function(ProjectsOverviewSvce){

      // List of all projects (all projects are on the same level)
      // TODO: modify the service to return a promise
      var rawProjects = ProjectsOverviewSvce;
      var numProjects = rawProjects.length;

      // Convert list to a list of lists (one list per row)
      this.projects = [];

      var numProjsPerRow = 3;
      var curr; var i = ctr = 0;
      for(i = 0; i < numProjects; i++){
        curr = rawProjects[i];
        curr.id = i;

        if(ctr == 0){
          this.projects.push( [curr] );

        } else if(ctr < numProjsPerRow){
          this.projects[this.projects.length - 1].push( curr );
        }

        ctr++;
        if(ctr == numProjsPerRow){ ctr = 0; } // New list
      }

      this.defaultProject = this.projects[0][1];
      this.activeProject = this.defaultProject;

      this.selectProject = function(projectID){
        var i, j = 0;
        for(i = 0; i < this.projects.length; i++){

          for(j = 0; j < this.projects[i].length; j++){

            if(projectID == this.projects[i][j].id){

              this.activeProject = this.projects[i][j];
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



  }]);
