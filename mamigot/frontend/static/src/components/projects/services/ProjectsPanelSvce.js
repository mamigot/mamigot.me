angular.module('projects')

  .factory('ProjectsPanelSvce', function(){

    /* TODO: fetch this via an API and return all in single list */
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

    return this.projects;

  });
