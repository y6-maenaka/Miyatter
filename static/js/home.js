$(function(){

  var connect_count = 1;
  var prev_session;

  if(!($('.new_event_card').length)){
    console.log('empty');
  }

  let homeSocket = new WebSocket(
    'ws://'
    +window.location.hostname
    +':8080/ws_home/');

  homeSocket.onclose = function(e){
    console.error('Session Socket Closed');
  };

  homeSocket.onmessage = function(e){
    const data = JSON.parse(e.data);


    if(data.notification_type == 'comment'){

      var new_event = "<div class='comment_card new_event_card notification_comment'>"
      +"<a href='/session/"+data.session_id+"/top/'>"
      +"<p class='comment_content'>"+data.content+"</p>"
      +"<p class='comment_session_anchor'>"+data.session_name+"</p>"
      +"</a></div>"
    }else if(data.notification_type == 'user_connect'){

      if(prev_session == data.session_id){
        connect_count += 1;
        var new_event = "<div class='new_event_card notification_connect'>"
        +"<a href='/session/"+data.session_id+"/top/'>"+data.session_name
        +"  :  ユーザが参加しました("+connect_count+")</a></div>";
      }else{
        var new_event = "<div class='new_event_card notification_connect'>"
        +"<a href='/session/"+data.session_id+"/top/'>"+data.session_name
        +"  :  ユーザが参加しました</a></div>";
        connect_count = 0;
      };

      prev_session = data.session_id;
    }
    $('#main_flow_container').prepend(new_event).trigger('create');
  };

})
