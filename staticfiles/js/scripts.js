// map.js

function initMap(latitude, longitude) {
  var map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: latitude, lng: longitude },
    zoom: 12,
  });

  var marker = new google.maps.Marker({
    position: { lat: latitude, lng: longitude },
    map: map,
    title: "Farm Location",
  });
}

const rate = (rating, product_id) => {
  fetch(`/rate/${product_id}/${rating}/`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  }).then((rest) => {
    window.location.reload();
  });
};
