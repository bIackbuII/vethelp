ymaps.ready(init);

function init () {
    var clinic_map = new ymaps.Map('clinic_map', {
        center: [55.76, 37.64],
        zoom: 9,
        controls: ['routeButtonControl']
    }, {
        searchControlProvider: 'yandex#search'
    });

    var control = clinic_map.controls.get('routeButtonControl');
    control.routePanel.geolocate('from');

    clinic_clusterer = new ymaps.Clusterer({
        clusterDisableClickZoom: false,
        preset: 'islands#darkblueClusterIcons'
    })

    for (let i = 0; i < clinics_points.length; i++) {
        var point = clinics_points[i];
        var ClinicMark = new ymaps.Placemark(
            [point.y, point.x],
            {
                balloonContent: point.name,
                balloonContentFooter: ''
            },
            {
                preset: 'islands#greenMedicalIcon',
                openEmptyBalloon: 'true'
            });
        clinic_clusterer.add(ClinicMark)
    }
    clinic_map.geoObjects.add(clinic_clusterer);

    document.querySelector("#submit").onclick = function(){
        alert("Вы нажали на кнопку");
    }
}