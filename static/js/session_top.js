$(function(){

  let selecting_session_menu = location.pathname;
  selecting_session_menu = selecting_session_menu.split('/')[3];

  switch(selecting_session_menu){
    case "top":
      $('.session_menu_'+selecting_session_menu).addClass("selecting_session_menu");
  }

  $(document).on('input','.post_comment_textarea',function(e){
    comment_count_meter();
  })

  let session_id = location.pathname.substr(9,36);
  let sessionSocket = new WebSocket(
    'ws://'
    +window.location.hostname
    +':8080/ws_session/'
    +session_id
    +'/');

  sessionSocket.onmessage = function(e){
    const data = JSON.parse(e.data);


    const now = new Date();
    var year = now.getFullYear();
    var month = now.getMonth() + 1;
    var day = now.getDate();
    var hour = now.getHours();
    var minutes = now.getMinutes();

    if(data.type == 'user_connect'){
      var new_event = "<div class='notification_connect'>ユーザが参加しました</div>";
    }else{
      var new_event = "<div class='comment_card'><p class='comment_content'>"
      +data.comment
      +"</p><p class='comment_session_anchor'>"
      +data.post_user_information.nick_name
      +"@"+year+"年"+month+"月"+day+'日'+hour+'時'+minutes+"分"
      +"@(new)"
      +"</p></div>"
    }

    $('#comment_line_container').prepend(new_event).trigger('create');
  };

  sessionSocket.onclose = function(e){
    console.error('Session Socket Closed');
  };

  $('.post_comment_button').click(function(e){
    var comment = $('.post_comment_textarea').val();
    sessionSocket.send(JSON.stringify({
        'comment':comment,
    }))
    $('.post_comment_textarea').val('');
    comment_count_meter();
  })

  $.ajax({
    type: "GET",
    url:'/session/api/session_comment',
    data:{
      'session_id':session_id,
    },
    success:function(response){
      for(var key in response){
        let postDate = new Date(response[key]['created_at']);

        var year = postDate.getFullYear();
        var month = postDate.getMonth() + 1;
        var day = postDate.getDate();
        var hour = postDate.getHours();
        var minutes = postDate.getMinutes();

        var past_comment = "<div class='comment_card'><p class='comment_content'>"
        +response[key]['comment']
        +"</p><p class='comment_session_anchor'>"
        +response[key]['created_by_nick_name']
        +"@"+year+"年"+month+"月"+day+'日'+hour+'時'+minutes+"分"
        +"@("+key+")</p></div>";

        $('#comment_line_container').prepend(past_comment).trigger('create');
      }
    },
    error:function(response){
      console.log('error')
    }
  })

  function comment_count_meter(){
    $('.post_comment_textarea').val($('.post_comment_textarea').val());
    $(".comment_words_counter").val($('.post_comment_textarea').val().length);
  }

  $('.session_registration_button').click(function(e){
    $.ajax({
      type: "POST",
      url:'/session/api/registration_session/',
      data:{
        'session_id':session_id,
        'user_id':$('input[type=hidden]'),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success:function(response){
        console.log('success');
      },
      error:function(response){
        console.log('error');
      }
    })
  })

})
