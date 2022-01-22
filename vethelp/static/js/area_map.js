ymaps.ready(init);

function init () {
    var area_map = new ymaps.Map('area_map', {
        center: [55.76, 37.64],
        zoom: 9
        }, {
            searchControlProvider: 'yandex#search'
        });
    area_clusterer = new ymaps.Clusterer({
        clusterDisableClickZoom: true,
        preset: 'islands#darkblueClusterIcons'
    })

    for (let i = 0; i < areas_points.length; i++) {
        var point = areas_points[i];
        var AreaMark = new ymaps.Placemark(
        [point.y, point.x],
        {
            balloonContentHeader: 'Площадка № ' + (i+1),
            balloonContent: "<b>Оборудование:</b><br/>" + point.elements + '<br/>' + "<b>Освещение:</b><br/>" + point.lighting + '<br/>' + "<b>Ограждение:</b><br/>" + point.fencing,
            clusterCaption:'Площадка № ' + (i+1)
        },
        {
            preset: 'islands#blueDogIcon'
        });
        area_clusterer.add(AreaMark)
    }
    area_map.geoObjects.add(area_clusterer);
}