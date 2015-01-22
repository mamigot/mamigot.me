angular.module('projects')

  .controller('ProjectsPanelCtrl',
    ['ProjectsPanelSvce', function(ProjectsPanelSvce){

      this.projects = ProjectsPanelSvce;


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

  }]);
