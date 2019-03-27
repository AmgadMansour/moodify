  var video = document.getElementById("videoElement");
  var canvas = document.getElementById('canvas');
  var context=canvas.getContext('2d');

  var cars = "car A";


if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({video: true})
  .then(function(stream) {
    video.srcObject = stream;
  })
  .catch(function(err0r) {
    console.log("Something went wrong!");
  });
}

function snap() {
    //window.alert("snap called");
    context.fillRect(0,0,320,240);
    context.drawImage(video,0,0,320,240);
    var image = canvas.toDataURL("image/png");  // base64-encoded image using canvas.toDataURL
    var arr = image.split(",",2); // remove metadata
    var img64 = arr[1];
    //tmp = "amgad";
    //window.alert("pre ajax");
    $.ajax({
            contentType: 'application/json;charset=UTF-8',
            url: '/test',
            type: 'POST',
            data: JSON.stringify({img64}),
            success: function (result) {
               // alert(result);
            },
            error: function (result) {
                //alert("error!");
            }
        });   //end ajax
    //window.alert("post ajax");
    //window.location.href = '/test/'+image; // directly redirect to url with paramter given
  }

function myFunction() {
  var x = document.getElementById("mood");
  if (x.style.display === "none") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

