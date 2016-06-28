pageApp.directive('divImg', function () {
    return function (scope, element, attrs) {
        attrs.$observe('divImg', function (value) {
            element.css({
                'background-image': 'url(' + value + ')'
            })
        });
    };
});