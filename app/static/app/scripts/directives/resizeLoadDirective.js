pageApp.directive('resizeLoad', function ($window) {
    return function (scope, element, attrs) {
        var w = angular.element($window);
        element.css('height', '500px');

        w.bind('resize load', function () {
            var divHeight = "" + $window.innerHeight + "px";
            element.css('height', divHeight);
        });
    };
});
