

  var video = document.getElementById("videoElement");
  var canvas = document.getElementById('canvas');
  var context=canvas.getContext('2d');


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
    context.fillRect(0,0,320,240);
    context.drawImage(video,0,0,320,240);
  }

