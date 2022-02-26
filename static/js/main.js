let map;
var latSelector;
var lngSelector;
var selector = document.getElementById("ip").value;
var selectorArray = selector.split (",");
var counter = 0;



selectorArray.forEach(function(entry){
    if (counter == 0){
        latSelector = parseFloat(entry);
        counter += 1;
    }
    else{
        lngSelector = parseFloat(entry);
        }            
 });

function selectorChange(){
    
    counter = 0;
    selector = document.getElementById("ip").value;
    selectorArray = selector.split (",");
    selectorArray.forEach(function(entry){
        if (counter == 0){
            latSelector = parseFloat(entry);
            counter += 1;
        }
        else{
            lngSelector = parseFloat(entry);
            }            
     });
    initMap();
}


function initMap() {
        map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: latSelector, lng: lngSelector },
            zoom: 8,
        });}



