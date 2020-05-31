// function initMap(id){
//        alert("in initmap");
//        if (navigator.geolocation){
//            alert('in if condition');
//            navigator.geolocation.getCurrentPosition(function(position){
//                alert("in geocurrentpostion");
//                var latitude = position.coords.latitude;
//                var longitude = position.coords.longitude;
//                var accuracy = position.coords.accuracy;
//                var time = position.timestamp;
//                document.getElementById("latitude").setAttribute("value", latitude);
//                document.getElementById("longitude").setAttribute("value", longitude);
//                var a = document.getElementsByClassName("emoji");
//                document.getElementById("emoji_id").setAttribute("value", a[id-1].value);
//                alert('location done')
//                function error(msg){
//                    alert("please enable your GPS postion feature.");
//                }
//            },
//                {maximumAge: 10000, timeout: 5000, enableHighAccuracy: true});
//        }
//     }