$(function(){
  $(document).on('click',function(e) {
     if(!$(e.target).closest('#select_create_session_type_container').length && $(e.target).closest('#select_create_session_type_container_bg').length) {
       $('#select_create_session_type_container_bg').fadeOut(300)
     }
  });

  $('#create_session_anchor').click(function(){
    $('#select_create_session_type_container_bg').fadeIn(300);
  });
})
