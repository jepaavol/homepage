﻿pageApp.filter('removeSpacesLower', [function () {
    return function (string) {
        if (!angular.isString(string)) {
            return string;
        }
        return string.replace(/[\s]/g, '').toLowerCase();
    };
}]);