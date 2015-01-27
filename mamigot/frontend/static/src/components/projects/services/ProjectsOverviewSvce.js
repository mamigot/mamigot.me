angular.module('projects')

  .factory('ProjectsOverviewSvce', function(){

    /* TODO: fetch this via an API and return all in single list */
    this.projects = [
      {
        title : 'Software Development at About.com',
        slug : '',
        logo : 'static/img/logos/about.png',
      },
      {
        title : 'Education Technology at IBL Studios Education',
        slug : '',
        logo : 'static/img/logos/iblstudios.png',
      },
      {
        title : 'Online Courses and MOOCs',
        slug : '',
        logo : 'static/img/logos/edx.png',
      },
      {
        title : 'Web Application Development',
        slug : '',
        logo : 'static/img/logos/flask.png',
      },
      {
        title : 'Coursework at NYU',
        slug : '',
        logo : 'static/img/logos/nyu.png',
      },
      {
        title : 'Additional Projects',
        slug : '',
        logo : 'static/img/logos/xilinx.png',
      }
    ];


    return this.projects;

  });
