$(function(){
  let menu_name = 'global_menu_'
  let selecting_menu = location.pathname;
  selecting_menu = selecting_menu.split('/')[1];
  
  switch(selecting_menu){
    case "home":
      $('.'+menu_name+selecting_menu).addClass("selecting_menu");
    case "session":
      $('.'+menu_name+selecting_menu).addClass("selecting_menu");
  }
})
