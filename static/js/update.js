function push(){
  $.ajax({
    url: "/finishPlayer",
    type: "POST",
    dataType: "json",
    success: function(data){
      
    }
  })
}