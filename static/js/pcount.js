// This is to fetch the player count
$(document).ready(()=>{
    const ip = $(".sip").attr("data-ip");
    const port = $(".sip").attr("data-port");
  
    $.get(`https://mcapi.us/server/status?ip=${ip}&port=${port}`, (result)=>{
      if (result.online) {
        $(".sip").html(result.players.now);
      } else {
        $(".playercount").html("Server isn't online!");
      }
    });
  
    setInterval(()=>{
      $.get(`https://mcapi.us/server/status?ip=${ip}&port=${port}`, (result)=>{
        if (result.online) {
          $(".sip").html(result.players.now);
        } else {
          $(".playercount").html("Server isn't online!");
        }
      });
    }, 3000);
  });
  