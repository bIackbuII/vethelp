ymaps.ready(init);

function init () {
    var clinic_map = new ymaps.Map('clinic_map', {
            center: [55.76, 37.64],
            zoom: 9
        }, {
            searchControlProvider: 'yandex#search'
        });
    clinic_clusterer = new ymaps.Clusterer({clusterDisableClickZoom: false})

    for (let i = 0; i < clinics_points.length; i++) {
        var point = clinics_points[i];
        var ClinicMark = new ymaps.Placemark([point.y, point.x]);
        clinic_clusterer.add(ClinicMark)
    }
    clinic_map.geoObjects.add(clinic_clusterer);
}